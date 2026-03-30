# Known Marain Glyphs

A catalogue of claimed Marain glyphs, symbols, and phonemes across canonical and community sources. Attribution and canonicity are noted throughout.

For a lookup table of all assigned values by decimal index, see [`glyph-index.md`](glyph-index.md).

---

## Scope and canonicity

No single authoritative glyph table exists. Banks defined the system mathematically in his essay[^1] but published only a partial character list (the image in that essay is the closest thing to a canonical alphabet). Everything else is community interpretation or extension.

| Status | Meaning |
|--------|---------|
| **Canonical** | Directly stated by Banks in his essay |
| **Community** | Non-canonical; community-created, may be widely adopted |
| **marainkit** | Derived by this project from mathematical/geometric properties of the grid |

---

## Banks' canonical system (M1)[^1]

### Grid structure

Each glyph is a 3×3 binary grid — a 9-bit number. 512 possible values (0–511). Each cell is filled (1) or empty (0), rendered as black or white squares.

The value 0 = all cells empty. The value 511 = all cells filled.

### Known canonical values

Banks names only two specific values explicitly:

| Value | Binary | Description |
|-------|--------|-------------|
| 1 | `000000001` | The number 1 (see "figure 1" in essay) |
| 121 | `001111100` | The phoneme "w" — first letter of the Marain alphabet |

### Canonical alphabet properties

- Glyphs are designed to be **rotated and mirrored** without confusion with any other primary alphabetical symbol
- Rotated versions represent phonemes **close to the original** unrotated sound
- Some rotations have **little phonemic relation** to the original — used for different vocalisations
- The system is designed to reproduce **any language capable of being spoken by a humanoid**

### Canonical non-alphabetic values

Beyond the alphabet, Banks states the remaining values (after phonemes) encode:
- Numbers in **base 8** (octal)
- Punctuation
- Common units of measurement
- Physical and mathematical symbols and constants
- Chemical elements

### Byte extensions

| Byte length | Symbol count | Notes |
|------------|-------------|-------|
| 9-bit (standard) | 512 | Core Marain — M1 |
| 10-bit | 1,024 | 512 additional symbols |
| 12-bit | 4,096 | Most common extended form; representable as a grid |
| 16-bit (4×4 grid) | 65,536 | Next square grid — pictograms, alien symbols, diagrams |
| Arbitrary | Unlimited | In principle unbounded; large grids transmit images |

Data transmission appends a **buffer bit** after each 9-bit glyph.

---

## Invariant glyphs (marainkit)[^2]

Of 512 possible 3×3 binary states, exactly **8 are fully invariant** under all rotations (0°, 90°, 180°, 270°) and mirrors. These are mathematically guaranteed to read identically from any orientation. Identified by this project — not claimed by Banks.

### Warning vocabulary

| Code | Name | Pattern | Proposed meaning |
|------|------|---------|-----------------|
| `#0` | **Empty** | `░░░ ░░░ ░░░` | Silence · null · word space |
| `#16` | **Point** | `░░░ ░█░ ░░░` | Singularity · decimal point |
| `#170` | **Diamond** | `░█░ █░█ ░█░` | Danger · hazard |
| `#186` | **Cross** | `░█░ ███ ░█░` | Alert · stop |
| `#325` | **Corners** | `█░█ ░░░ █░█` | Boundary · perimeter warning |
| `#341` | **Checkerboard** | `█░█ ░█░ █░█` | Noise · maximum intensity |
| `#495` | **Frame** | `███ █░█ ███` | Enclosure · bracket · container |
| `#511` | **Full** | `███ ███ ███` | Full stop · header · maximum |

The pairs are semantic inverses: Empty↔Full, Point↔Frame, Diamond↔Checkerboard, Cross↔Corners.

**Proposed state escalation mapping:**

| Glyph | Suggested level (0–8) |
|-------|-----------------------|
| Empty `#0` | 0 — silence / null |
| Point `#16` | 1–2 — minimal signal |
| Frame `#495` | 3–4 — structural container |
| Corners `#325` | 5 — boundary / perimeter |
| Diamond `#170` | 5–6 — attention / warning boundary |
| Cross `#186` | 6–7 — clear warning |
| Checkerboard `#341` | 7 — near-maximum intensity |
| Full `#511` | 8 — maximum / critical |

This mapping is **proposed, not canonical**. Finalize when state escalation system is built.

---

## Tonal Marain — zakalwe2040[^3]

A significant community extension adding tonal encoding, a 24-character abjad, diacritics, emoting glyphs, numerals, and mathematical notation. Uses a **4×5 dot lattice** rather than the canonical 3×3 grid. Non-canonical but the most developed community implementation.

### Lattice structure

```
┌─────────────────────────┐
│  Upper diacritic (red)  │  ← short vowels
├─────────────────────────┤
│  3×3 Slate (green)      │  ← core glyph
├─────────────────────────┤
│  Lower diacritic (blue) │  ← short vowels
├────────────┬────────────┤
│            │  Tonal     │  ← 5 tones (emotional content)
│            │  channel   │
└────────────┴────────────┘
```

Direction: **right to left** (following Modern Hebrew / Arabic convention).

### The 24-character abjad

Organized by place of articulation, then phoneme frequency. Default vowel on a bare consonant is *a* (overridden by diacritics).

| Place of articulation | Phonemes |
|----------------------|---------|
| Bilabial | *ma* · *wa* · *pa* · *ba* |
| Labio-dental | *fa* · *va* |
| Interdental | *tha* · *dtha* · *cha* · *dja* |
| Alveolar | *ta* · *na* · *sa* · *da* · *la* · *za* |
| Post-alveolar | *ra* · *sha* |
| Palatal | *ya* |
| Velar | *ga* · *ka* · *nga* |
| Glottal | *aa* · *ha* |

### Diacritics (short vowels)

| Diacritic | Position | Vowel | IPA |
|-----------|----------|-------|-----|
| *up* | Bar above letter | *a* | /æ/ |
| *out* | Dot above start | *u* | /ʊ/ |
| *down* | Bar below letter | *i* | /ɪ/ |
| *stop* | Dot above end | (zero vowel) | — |

### Emoting glyphs (22)

Non-verbal communication glyphs organized into four categories. Unicode equivalents given as approximate reference.

**Logical signals**

| Glyph | Unicode approx. | Meaning |
|-------|----------------|---------|
| *shacha* | 🖖 | Greetings · prosperity · peace · hello · bye |
| *samara* | 🤨 | Fascination · logic understood |

**Positive emotional signals**

| Glyph | Unicode approx. | Meaning |
|-------|----------------|---------|
| *hub* | 💛 | Love |
| *zing* | ✨ | Positivity |
| *yam* | 🙏 | Hope |
| *wun* | 💕 | Warmth |
| *shaa* | 🤣 | Laughter |
| *mar* | 😂 | Joy |
| *hoo* | 😊 | Happiness |
| *lang* | 🥰 | Romance |
| *gang* | 😘 | Affection |
| *shii* | 😉 | Synchronicity |
| *shai* | 👍 | Agreement |
| *zang* | 😲 | Surprise |
| *shuu* | 😍 | Infatuation |

**Necessary emotional signals**

| Glyph | Unicode approx. | Meaning |
|-------|----------------|---------|
| *ging* | 🥺 | Sympathy |
| *bay* | 😢 | Sadness |

**Negative emotional signals**

| Glyph | Unicode approx. | Meaning |
|-------|----------------|---------|
| *buz* | 😭 | Overwhelmed |
| *yan* | 🤢 | Disgust |
| *fin* | 😡 | Anger |
| *pil* | 🥱 | Fatigue |
| *paa* | 😨 | Fear |

### Numerals

Decimal (0–9). Names borrowed from **Mandarin Chinese**. Written **right to left**. The subsequent numbering system does not follow Mandarin — only the digit names are used.[^3]

### Mathematical and logical notation

Glyph design follows the principle of **homoiconicity** — glyphs allude to their meaning through form. Symmetry choices are informed by research on cognitive benefits of symbol symmetry alignment with operator commutativity.[^4]

**Arithmetic operators**

| Glyph | Operation |
|-------|-----------|
| (addition) | + |
| (multiplication) | × |
| (subtraction) | − |
| (division) | ÷ |
| (modulo) | mod |

**Logic**

| Glyph | Name | Meaning |
|-------|------|---------|
| *wa* | conjunction | and (also grammatical conjunctive particle) |
| *ow* | disjunction | or |
| *ma* | negation | not |

**Equality and copula**

| Glyph | Name | Meaning |
|-------|------|---------|
| *heeya* | equality | = |
| *kun* | definition | ≔ (define / assign) |
| *iz* | copula | to be (verb) |

**Punctuation**

| Glyph | Name | Meaning |
|-------|------|---------|
| *mahu* | question / lambda | ? · also λ-calculus |
| (3 others) | — | Not yet named in source |

---

## Reddit conlang (u/comradelenin456, u/ratioprosperous)[^5]

Uses Banks' glyph alphabet as its writing system but adds a full synthetic grammar. Non-canonical; widely used in the community including for tattoos.

Features: flexible word order · no tenses · six grammatical cases · fourth-person pronouns · genderless third-person pronoun. No independent glyph extensions beyond Banks' alphabet.

---

## marain-tools.netlify.app[^6]

Live tool implementing romanized Marain → glyphs → 9-bit binary. Uses a 9-bit bitmap encoding. Known example:

> *ra'yuh prenva zawen* → "I ride aboard a spaceship"
> Gloss: `p1sg+NOM spaceship+ACC ride`

Three input modes: romanized Marain · direct Marain font characters · nine-bit binary. Developers note: not all bit strings produce valid character encodings. Compound words, punctuation, and numbers not yet fully supported.

---

## tomdionysus/marain-font[^7]

TrueType implementation of Banks' glyph alphabet. No published glyph table in the repo — the font file itself is the artifact. The author sent the font to Banks via his publishers; no response on record.

---

## Open questions

- What are the remaining ~480 non-alphabetic glyph assignments? Banks specifies categories (base-8 numerals, punctuation, units, constants, elements) but not the actual mappings.
- Should the 8 marainkit invariant glyphs be treated as reserved values in any implementation?
- Do the zakalwe2040 emoting glyphs have binary assignments in the 3×3 grid, or only in the 4×5 lattice?
- Is Banks' "figure 1" (the number 1) the value `#1` (`000000001`) — bottom-right cell only? This is the most natural reading but not stated explicitly.

---

[^1]: Iain M. Banks, *"A Few Notes on Marain"*, published in *Scripta Manent* (date unknown). Full text at [`docs/A_Few_Notes_on_Marain.md`](../../docs/A_Few_Notes_on_Marain.md). Note: the *Scripta Manent* attribution appears across multiple fan sites but no publication date has been confirmed. See footnote in that document.

[^2]: marainkit project, derived geometrically from the 3×3 binary grid. See [`encoding/docs/invariant-glyphs.md`](invariant-glyphs.md). These values are a mathematical property of the grid, not a design decision — they would hold in any conforming implementation.

[^3]: zakalwe2040, *Tonal Marain: Language of the Culture*, [github.com/zakalwe2040/marain](https://github.com/zakalwe2040/marain). All Tonal Marain glyph names, phonemes, emoting glyphs, numerals, and operator definitions in this document are sourced from that repo's README. Community work — not endorsed by the Banks estate.

[^4]: Reference cited by zakalwe2040: Centre for Mathematical Cognition, Loughborough University — research on cognitive advantages of symmetric mathematical symbols. The original paper is linked in the zakalwe2040 README.

[^5]: Reddit users u/comradelenin456 and u/ratioprosperous, via r/TheCulture and r/Marain. Non-canonical synthetic grammar built on Banks' alphabet. No independent glyph extensions.

[^6]: [marain-tools.netlify.app](https://marain-tools.netlify.app) — author unknown. Implements romanization → glyph → binary pipeline. The most complete live implementation of the phoneme-to-glyph mapping currently available.

[^7]: tomdionysus (Tom Cully), [github.com/tomdionysus/marain-font](https://github.com/tomdionysus/marain-font). TrueType font for Banks' Marain alphabet. Font sent to Banks via publishers; no response recorded.
