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

## What we're building

A Marain script font — custom glyphs for the Marain writing system from Iain M. Banks'
Culture novels. Not a transliteration of English. A visual symbol set for the base-9
encoding system in `encoding/`.

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

1. **Cell size and stroke weight** — thicker strokes read better small; thinner strokes
   look more elegant at display size. Need to test both.

2. **Filled vs outlined cells** — filled squares, outlined squares, or dots?
   Reference fonts use dots and solid squares — pick one and stick with it.

3. **Grid padding** — gap between cells within a glyph affects density and legibility.

4. **Character set scope** — start with 9 base digits only, or include separators/punctuation
   from day one?

5. **Composite glyphs** — does a 2-word sequence get a ligature, or always render as two
   separate glyphs?

---

## Next steps

1. Study reference fonts — note grid geometry, stroke weight, cell size
2. Sketch 9 base digit glyphs on paper or in a grid tool (Figma, Illustrator, even graph paper)
3. Encode those decisions as data (which cells are filled per glyph)
4. Write `build.py` to compile data → font file
5. Load the font in a browser and test against the display system
