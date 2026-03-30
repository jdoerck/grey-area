# Glyph Index — #0 to #511

All claimed Marain M1 glyph assignments. Values without a claim are omitted — 502 of 512 remain unassigned.

**Binary convention:** Banks uses LSB-first — leftmost digit = bit 0 = value 1. Grid reads left→right, top→bottom across positions 0–8.

```
[0][1][2]
[3][4][5]
[6][7][8]
```

Pattern notation: rows separated by `/` · `█` = filled (1) · `░` = empty (0)

---

| # | Name | Pattern | Meaning(s) | Proposed by |
|--:|------|---------|-----------|-------------|
| 0 | Empty | `░░░/░░░/░░░` | Silence · null · word space · zero | marainkit[^1] |
| 1 | — | `█░░/░░░/░░░` | The number one | Banks[^2] (implied)[^3] |
| 16 | Point | `░░░/░█░/░░░` | Singularity · decimal point · minimal signal | marainkit[^1] |
| 121 | *w* | `█░░/███/█░░` | Phoneme /w/ — first letter of the Marain alphabet | Banks[^2] (canonical) |
| 170 | Diamond | `░█░/█░█/░█░` | Danger · hazard · attention boundary | marainkit[^1] |
| 186 | Cross | `░█░/███/░█░` | Alert · stop · clear warning | marainkit[^1] |
| 325 | Corners | `█░█/░░░/█░█` | Boundary · perimeter · limit | marainkit[^1] |
| 341 | Checkerboard | `█░█/░█░/█░█` | Noise · near-maximum intensity · interference | marainkit[^1] |
| 495 | Frame | `███/█░█/███` | Enclosure · bracket · container · structural boundary | marainkit[^1] |
| 511 | Full | `███/███/███` | Full stop · header marker · maximum · critical | marainkit[^1] |

---

## What is missing

**Banks' alphabet** — only *w* (#121) has a confirmed decimal index. The remaining primary phonemes and their rotation/mirror variants (estimated ~30–60 values) are visually documented in the essay's glyph table image but have no published binary indices.

**Base-8 numerals** — Banks states that values beyond the alphabet encode octal digits 0–7, punctuation, units of measurement, physical/mathematical constants, and chemical elements. None have published indices.

**zakalwe2040 abjad** — the 24 Tonal Marain consonants[^4] are published as SVG glyph diagrams but without decimal index values. Their grid positions are not mapped to the M1 3×3 system (Tonal Marain uses a 4×5 lattice).

---

[^1]: marainkit — derived from the mathematical/geometric properties of the 3×3 binary grid. These 8 values (#0, #16, #170, #186, #325, #341, #495, #511) are the only states fully invariant under all rotations and mirrors. See [`invariant-glyphs.md`](invariant-glyphs.md).

[^2]: Iain M. Banks, *"A Few Notes on Marain"*. Full text at [`../../docs/A_Few_Notes_on_Marain.md`](../../docs/A_Few_Notes_on_Marain.md).

[^3]: Banks writes "The number 1 would be shown as in figure 1" — figure 1 is an image not recoverable from plain text. `#1` (top-left cell only) is the most natural reading of a decimal 1 in LSB-first encoding, but is not confirmed.

[^4]: zakalwe2040, *Tonal Marain*, [github.com/zakalwe2040/marain](https://github.com/zakalwe2040/marain).
