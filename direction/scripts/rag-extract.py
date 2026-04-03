#!/usr/bin/env python3
"""
RAG extraction: find Marain language references across the Culture novels.

Extracts:
  - Every passage mentioning "Marain" with surrounding context
  - Ship names (italicised, title-case)
  - Culture-specific vocabulary (italicised short phrases, not ship names)
  - Chapter/section headings
  - Character names with first appearances

Output: docs/source/novel-references/<slug>.md per book

Usage:  python3 direction/scripts/rag-extract.py
Run from the repo root.
"""

import zipfile
import re
import sys
from pathlib import Path
from bs4 import BeautifulSoup, NavigableString

ROOT = Path(__file__).parent.parent.parent
BOOKS_DIR = ROOT / "books"
OUT_DIR = ROOT / "docs" / "source" / "culture-marain"

BOOKS = [
    ("Iain M Banks - Consider Phlebas.epub",          "Consider Phlebas",          "01"),
    ("Iain M Banks - The Player of Games.epub",        "The Player of Games",        "02"),
    ("Iain M Banks - Use of Weapons.epub",             "Use of Weapons",             "03"),
    ("Iain M Banks - The State of the Art.epub",       "The State of the Art",       "04"),
    ("Iain M Banks - Excession.epub",                  "Excession",                  "05"),
    ("Iain M Banks - Inversions.epub",                 "Inversions",                 "06"),
    ("Iain M Banks - Look to Windward.epub",           "Look to Windward",           "07"),
    ("Iain M Banks - Matter.epub",                     "Matter",                     "08"),
    ("Iain M Banks - Surface Detail.epub",             "Surface Detail",             "09"),
    ("Iain M Banks - The Hydrogen Sonata.epub",        "The Hydrogen Sonata",        "10"),
    ("Iain M Banks - A Few Notes on the Culture.epub", "A Few Notes on the Culture", "11"),
]

# Italicised phrases that are almost certainly ship names (title-case multi-word
# or well-known names) rather than Marain vocabulary
KNOWN_SHIP_PATTERNS = re.compile(
    r"^[A-Z][a-zA-Z''\- ]{2,}$"   # title-case, 3+ chars
)

# Short italicised words more likely to be Marain vocabulary
VOCAB_MAX_WORDS = 4

# Context window around "Marain" keyword hits (chars each side)
CONTEXT_CHARS = 500


# ── HTML parsing ──────────────────────────────────────────────────────────────

def get_html_files(zf: zipfile.ZipFile):
    """Return HTML files in reading order (by filename, then spine order if available)."""
    names = [n for n in zf.namelist() if re.search(r'\.(html|xhtml|htm)$', n, re.I)]
    # Try to read spine order from content.opf / package.opf
    opf_names = [n for n in zf.namelist() if n.endswith('.opf')]
    order = {}
    for opf_name in opf_names:
        try:
            soup = BeautifulSoup(zf.read(opf_name), 'html.parser')
            for i, item in enumerate(soup.find_all('itemref')):
                idref = item.get('idref', '')
                # Match idref to manifest item href
                manifest_item = soup.find('item', {'id': idref})
                if manifest_item:
                    href = manifest_item.get('href', '')
                    # Resolve relative to opf location
                    opf_dir = opf_name.rsplit('/', 1)[0] + '/' if '/' in opf_name else ''
                    full = opf_dir + href
                    # Normalise
                    full = full.replace('//', '/')
                    order[full] = i
                    order[href] = i
        except Exception:
            pass
    if order:
        names.sort(key=lambda n: order.get(n, order.get(n.split('/')[-1], 9999)))
    else:
        names.sort()
    return names


def get_italic_classes(zf: zipfile.ZipFile) -> set:
    """Parse all CSS files in the EPUB to find class names with font-style:italic."""
    italic_cls = set()
    for name in zf.namelist():
        if name.endswith('.css'):
            try:
                css = zf.read(name).decode('utf-8', errors='replace')
                # Match .classname { ... font-style: italic ... }
                for m in re.finditer(r'(\.[a-zA-Z0-9_-]+)\s*\{([^}]*)\}', css, re.DOTALL):
                    cls_name = m.group(1).lstrip('.')
                    body = m.group(2)
                    if re.search(r'font-style\s*:\s*italic', body):
                        italic_cls.add(cls_name)
            except Exception:
                pass
    return italic_cls


def parse_html_file(zf: zipfile.ZipFile, name: str, css_italic_classes: set = None):
    """
    Return a list of structured blocks:
      {'type': 'heading'|'para', 'text': str, 'em': [str], 'raw': str}

    Handles multiple italic conventions across different EPUB sources:
      - <em> / <i> tags  (most books)
      - class="italic"   (Excession, some others)
      - class="calibre1" (Look to Windward)
      - inline style font-style:italic
    """
    raw = zf.read(name).decode('utf-8', errors='replace')
    soup = BeautifulSoup(raw, 'html.parser')

    # Remove script/style
    for tag in soup(['script', 'style']):
        tag.decompose()

    # Build a combined set of italic class names from:
    #   1. CSS-parsed classes passed in (e.g. calibre4)
    #   2. Any class literally named "italic" in this HTML file
    #   3. Any element with inline font-style:italic
    italic_classes = set(css_italic_classes or [])
    for el in soup.find_all(True):
        cls = ' '.join(el.get('class', []))
        style = el.get('style', '')
        if 'italic' in cls.lower():
            italic_classes.add(cls.strip())

    def is_italic(el):
        if el.name in ('em', 'i'):
            return True
        cls_list = el.get('class', [])
        style = el.get('style', '')
        if any(c in italic_classes for c in cls_list):
            return True
        if 'font-style:italic' in style.replace(' ', '').lower():
            return True
        return False

    blocks = []
    for el in soup.find_all(['h1', 'h2', 'h3', 'h4', 'p', 'div']):
        text = el.get_text(' ', strip=True)
        if not text or len(text) < 3:
            continue
        tag = el.name
        btype = 'heading' if tag in ('h1', 'h2', 'h3', 'h4') else 'para'

        # Collect italicised spans using all detected conventions
        em_texts = []
        for child in el.find_all(True):
            if is_italic(child):
                et = child.get_text(' ', strip=True)
                if et and len(et) > 1:
                    em_texts.append(et)

        blocks.append({'type': btype, 'text': text, 'em': em_texts, 'raw': raw})

    return blocks


# ── Extraction passes ─────────────────────────────────────────────────────────

def extract_marain_passages(blocks, filename):
    """Find paragraphs that mention 'Marain' and return them with context."""
    results = []
    prev_text = ''
    for i, b in enumerate(blocks):
        if re.search(r'\bMarain\b', b['text'], re.I):
            # Grab prev para as context prefix if short
            context = ''
            if prev_text and len(prev_text) < 200:
                context = prev_text + ' '
            results.append({
                'file': filename,
                'context': (context + b['text']).strip(),
                'heading': None,
            })
        if b['type'] == 'heading':
            prev_text = ''
        else:
            prev_text = b['text']
    return results


def extract_ship_names(blocks):
    """Collect unique italicised title-case phrases — likely ship names."""
    ships = set()
    for b in blocks:
        for em in b['em']:
            # Must be title-case, not sentence-length, no lowercase start
            if (KNOWN_SHIP_PATTERNS.match(em)
                    and 2 <= len(em.split()) <= 6
                    and not em[0].islower()):
                ships.add(em.strip('.,!? '))
    return ships


def extract_vocab(blocks):
    """Collect italicised short phrases that look like vocabulary (not ship names)."""
    vocab = {}  # word → first context sentence
    for b in blocks:
        for em in b['em']:
            words = em.split()
            if not words:
                continue
            # Skip ship-name patterns and very long phrases
            if len(words) > VOCAB_MAX_WORDS:
                continue
            # Skip if it's clearly a title-case ship name
            if KNOWN_SHIP_PATTERNS.match(em) and len(words) >= 2:
                continue
            # Skip pure punctuation / numbers
            if not re.search(r'[a-zA-Z]', em):
                continue
            # Skip common English words used for emphasis
            common = {'the', 'a', 'an', 'of', 'in', 'is', 'are', 'was', 'and',
                      'or', 'not', 'no', 'yes', 'very', 'so', 'but', 'if',
                      'that', 'this', 'it', 'he', 'she', 'they', 'we', 'I',
                      'have', 'had', 'be', 'been', 'do', 'does', 'did', 'will',
                      'would', 'could', 'should', 'may', 'might', 'must', 'can',
                      'all', 'any', 'some', 'more', 'most', 'other', 'only',
                      'also', 'even', 'just', 'then', 'than', 'there', 'here',
                      'now', 'never', 'always', 'still', 'yet', 'already',
                      'up', 'down', 'out', 'over', 'under', 'through', 'into',
                      'from', 'with', 'at', 'by', 'for', 'on', 'as', 'about',
                      'said', 'asked', 'looked', 'seemed', 'felt', 'knew',
                      'seen', 'been', 'done', 'gone', 'come', 'see', 'go'}
            if em.lower().strip('.,') in common:
                continue
            key = em.strip('.,!? ')
            if key and key not in vocab:
                vocab[key] = b['text'][:200]
    return vocab


def extract_headings(blocks):
    """Return all section headings."""
    return [b['text'] for b in blocks if b['type'] == 'heading' and b['text'].strip()]


def extract_character_names(blocks):
    """
    Heuristic: collect proper nouns (capitalised words in prose, not sentence-start)
    that appear multiple times. These are likely character or place names.
    """
    candidates = {}
    for b in blocks:
        if b['type'] != 'para':
            continue
        sentences = re.split(r'(?<=[.!?])\s+', b['text'])
        for sent in sentences:
            words = sent.split()
            # Skip first word of sentence (always capitalised)
            for w in words[1:]:
                # Capitalised, alphabetic, 3+ chars, not all-caps acronym
                clean = w.strip('.,!?;:\'"()[]')
                if (clean and clean[0].isupper() and clean.isalpha()
                        and len(clean) >= 3 and not clean.isupper()):
                    candidates[clean] = candidates.get(clean, 0) + 1

    # Keep only names that appear 3+ times (likely actual names, not sentence-starts)
    return {k: v for k, v in candidates.items() if v >= 3}


# ── Formatting ────────────────────────────────────────────────────────────────

def format_passage(p):
    text = p['context']
    # Highlight Marain occurrences
    text = re.sub(r'\b(Marain)\b', r'**\1**', text)
    return text


def write_book_report(title, number, marain_passages, ships, vocab, headings, char_names):
    slug = title.lower().replace(' ', '-').replace("'", '').replace(',', '')
    out_path = OUT_DIR / f"{number}-{slug}.md"

    lines = [
        f"# Marain References — {title}",
        "",
        f"> Extracted from the novel. Focus: Marain language references, Culture vocabulary, character and ship names.",
        "",
        "---",
        "",
    ]

    # ── Marain passages
    lines += [
        "## Direct Marain Mentions",
        "",
        f"_{len(marain_passages)} passage(s) mentioning 'Marain'._",
        "",
    ]
    if marain_passages:
        seen = set()
        for p in marain_passages:
            key = p['context'][:60]
            if key in seen:
                continue
            seen.add(key)
            lines.append(f"> {format_passage(p)}")
            lines.append("")
    else:
        lines += ["> *(none found)*", ""]

    # ── Ship names
    lines += [
        "## Ship Names",
        "",
        "_Italicised title-case phrases — Culture ship and drone names._",
        "",
    ]
    if ships:
        for s in sorted(ships):
            lines.append(f"- *{s}*")
        lines.append("")
    else:
        lines += ["*(none found)*", ""]

    # ── Vocabulary
    lines += [
        "## Culture / Marain Vocabulary",
        "",
        "_Italicised short phrases not matching ship-name patterns — potential Marain words or Culture-specific terms._",
        "",
    ]
    if vocab:
        for word, ctx in sorted(vocab.items()):
            ctx_clean = ctx.replace('\n', ' ').strip()
            lines.append(f"**{word}** — *{ctx_clean[:120]}*")
            lines.append("")
    else:
        lines += ["*(none found)*", ""]

    # ── Headings
    lines += [
        "## Chapter / Section Headings",
        "",
        "_Often ship names, place names, or Marain words._",
        "",
    ]
    for h in headings[:60]:  # cap at 60 to avoid bloat
        h_clean = h.strip()
        if h_clean:
            lines.append(f"- {h_clean}")
    lines.append("")

    # ── Character names
    lines += [
        "## Recurring Proper Nouns",
        "",
        "_Capitalised words appearing 3+ times in prose (likely character, place, or faction names). Frequency in parentheses._",
        "",
    ]
    top_names = sorted(char_names.items(), key=lambda x: -x[1])[:80]
    for name, count in top_names:
        lines.append(f"- {name} ({count})")
    lines.append("")

    out_path.write_text('\n'.join(lines), encoding='utf-8')
    return out_path


# ── Main ──────────────────────────────────────────────────────────────────────

def process_book(epub_filename, title, number):
    epub_path = BOOKS_DIR / epub_filename
    if not epub_path.exists():
        print(f"  SKIP (not found): {epub_filename}")
        return

    marain_passages = []
    all_ships = set()
    all_vocab = {}
    all_headings = []
    all_char_names = {}

    with zipfile.ZipFile(epub_path) as zf:
        css_italic_classes = get_italic_classes(zf)
        html_files = get_html_files(zf)
        for hf in html_files:
            try:
                blocks = parse_html_file(zf, hf, css_italic_classes)
            except Exception as e:
                continue

            marain_passages += extract_marain_passages(blocks, hf)
            all_ships |= extract_ship_names(blocks)
            for k, v in extract_vocab(blocks).items():
                if k not in all_vocab:
                    all_vocab[k] = v
            all_headings += extract_headings(blocks)
            for k, v in extract_character_names(blocks).items():
                all_char_names[k] = all_char_names.get(k, 0) + v

    out = write_book_report(title, number, marain_passages, all_ships,
                            all_vocab, all_headings, all_char_names)
    n_ships = len(all_ships)
    n_vocab = len(all_vocab)
    n_marain = len(set(p['context'][:60] for p in marain_passages))
    print(f"  {out.name}  ({n_marain} Marain passages · {n_ships} ships · {n_vocab} vocab items)")
    return out


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    print(f"Extracting Marain references from {len(BOOKS)} books...\n")
    for epub_filename, title, number in BOOKS:
        print(f"  {title}...")
        process_book(epub_filename, title, number)

    # Normalise line endings (some EPUBs contain CRLF in their HTML source)
    for f in OUT_DIR.glob("*.md"):
        text = f.read_bytes().replace(b'\r\n', b'\n').replace(b'\r', b'\n')
        f.write_bytes(text)

    print(f"\nDone. Output in {OUT_DIR}/")


if __name__ == "__main__":
    main()
