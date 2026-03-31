# display/fonts/ — Direction

Font design and build tooling for the Marain display system.

---

## Tools installed

Virtual environment at `.venv/` (not tracked in git).

```bash
# activate
source display/fonts/.venv/bin/activate

# what's installed
fonttools   4.62.1   # core font manipulation and compilation
ufoLib2              # UFO font format read/write (source format)
```

To reinstall from scratch:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install fonttools ufoLib2
```

---

## Key documents

- [`font-spec.md`](font-spec.md) — design principles, rendering requirements, glyph space inventory, vocabulary tiers, testing requirements. **Start here before any build work.**
- [`research.md`](research.md) — deep analysis of Atkinson Hyperlegible and Intel One Mono: what makes them exceptional, shared legibility principles, and what transfers to a Marain grid font.

---

## What we're building

A Marain script font — custom glyphs for the Marain writing system from Iain M. Banks'
Culture novels. Not a transliteration of English. A visual symbol set for the base-9
encoding system in `encoding/`.

This is not a traditional .otf/.ttf font. It is a **rendering function** — a module that takes a 9-bit value and a rendering context and produces SVG, Canvas, or CSS output. See `font-spec.md §10` for implementation notes.

The key advantage: **Marain is grid-based**, not organic. Each glyph is a pattern of
filled/empty cells on a fixed grid. This means glyphs can be defined as data and the
font can be compiled programmatically — no traditional type design skills required.

---

## Design approach

### Grid structure

The encoding layer uses a **3×3 block** as the fundamental unit (9 cells = 1 base-9 word).
The font grid maps directly:

```
┌───┬───┬───┐
│ 0 │ 1 │ 2 │
├───┼───┼───┤
│ 3 │ 4 │ 5 │
├───┼───┼───┤
│ 6 │ 7 │ 8 │
└───┴───┴───┘
```

Each cell is either filled (1) or empty (0). 9 cells = 512 possible glyphs (2^9).
A subset of these will be the actual character set.

### Character set (to be decided)

Minimum viable set:
- 9 base digit symbols (0–8)
- Word separator / space
- Sentence boundary markers

Extended:
- Compound/ligature forms for common sequences
- State indicators (maps to display system urgency levels)
- Punctuation equivalents

### Unicode mapping

Use the **Private Use Area (PUA)**: U+E000 onwards.
This is the standard approach for fictional/custom scripts before (or instead of)
Unicode standardisation. Existing Marain fonts also use PUA.

---

## Build pipeline (planned)

```
glyph definitions     →   Python script   →   .ufo source   →   .ttf / .otf
(data: cell patterns)     (fonttools)         (ufoLib2)
```

Steps:
1. Define each glyph as a list of filled cells (e.g. `[0,1,3,6]` = top row + left column)
2. Script converts cell patterns to Bézier outlines (square paths)
3. `ufoLib2` assembles the UFO source (font metrics, glyph set, kerning)
4. `fonttools` compiles UFO → binary font file

The script lives at `display/fonts/build.py` (not yet written).

---

## Font metrics (to be defined)

These will need visual calibration:

| Property       | Notes                                          |
|----------------|------------------------------------------------|
| Units per em   | 1000 (standard)                                |
| Cap height     | ~700                                           |
| Cell size      | ~200 units per cell (3×3 = 600u square glyph) |
| Stroke weight  | To be decided — affects legibility at small sizes |
| Advance width  | Fixed-width (monospaced) — matches encoding grid |

---

## Reference fonts (not in git)

Collected Marain fonts are at `display/fonts/examples/` (gitignored — third-party, various licenses).
Study these for glyph grammar and style conventions before designing new glyphs:

- `marain-font/` — original TTF, sent to Banks by the author
- `marain.otf/` — OTF variant
- `marain-dots.otf/` — dot-matrix variant
- `marain-regular/` — clean regular weight
- `marain-standard/` — extended standard version
- `marain-ancient-font/` — archival/historical variant

---

## Decisions needed before building

The spec (`font-spec.md`) defines constraints and principles. Remaining open decisions:

1. **Cell shape default** — `square` (highest fidelity) or `dot` (braille-resonant, most visually distinctive)? See `font-spec.md §7.1`.
2. **Column B vocabulary** — which ~24–36 glyphs from 512 to assign to phonemes? Must satisfy D₄ equivalence class constraint and salience map. See `font-spec.md §5.3`.
3. **Centre-cell salience** — is the hypothesised low salience of the centre cell empirically valid? Needs testing before Column B assignment. See `font-spec.md §4.3`.
4. **Animation** — should status escalation transitions animate? See `font-spec.md §11`.

---

## Next steps

1. ~~Study reference fonts~~ — **done** (`research.md`)
2. ~~Define design principles and rendering spec~~ — **done** (`font-spec.md`)
3. Resolve cell shape default (square vs. dot)
4. Sketch and encode the 8 invariant glyphs first — these are the highest-confidence assignments
5. Write `build.py` to compile cell patterns → SVG/Canvas output
6. Test at minimum rendering size (11px) before expanding the vocabulary
