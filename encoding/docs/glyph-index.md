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

### Banks' phoneme alphabet[^5]

32 phonemes from Banks' glyph table. Patterns are read from the source image — all values except *w* are approximate and need verification against a pixel-precise analysis or the original font file. Ordered as they appear in the image.

† = approximate — read from image, unverified. See footnote [^5].

| # | Phoneme | Pattern | Notes |
|--:|---------|---------|-------|
| 121 | *w* | `█░░/███/█░░` | **Confirmed** — Banks states binary `100111100` = 121 |
| 273 † | *uh* | `█░░/░█░/░░█` | Diagonal `\` shape |
| 457 † | *m* | `█░░/█░░/███` | Bottom-left L shape |
| 493 † | *h* | `█░█/█░█/███` | Cup / U shape |
| 480 † | *d* | `░░░/░░█/███` | Bottom-right hook |
| 456 † | *ah* | `░░░/█░░/███` | Bottom-left corner |
| 459 † | *p* | `██░/█░░/███` | Partial box, open right |
| 214 † | *s* | `░██/░█░/██░` | Diagonal S shape |
| 168 † | *t* | `░░░/█░█/░█░` | Splayed base |
| 84 † | *ih* | `░░█/░█░/█░░` | Diagonal `/` shape |
| 484 † | *l* | `░░█/░░█/███` | Reverse-L shape |
| 60 † | *tch* | `░░█/███/░░░` | Top-right hook |
| 312 † | *k* | `░░░/███/░░█` | Middle row + bottom-right tail |
| 170 † | *oh* | `░█░/█░█/░█░` | O shape — **collides with Diamond #170** [^7] |
| 432 † | *b* | `░░░/░██/░██` | Bottom-right block |
| — | *ch* | — | Not readable at image resolution [^6] |
| 56 † | *f* | `░░░/███/░░░` | Middle row only |
| 2 † | *ay* | `░█░/░░░/░░░` | Top-centre cell only |
| — | *v* | — | Not readable at image resolution [^6] |
| — | *ll* | — | Not readable at image resolution [^6] |
| 295 † | *n* | `███/░░█/░░█` | Top row + right column |
| 50 † | *ee* | `░█░/░██/░░░` | Top-centre + centre-right |
| 120 † | *g* | `░░░/███/█░░` | Middle row + bottom-left |
| 16 † | *ng* | `░░░/░█░/░░░` | Centre cell only — **coincides with Point #16** [^7] |
| 384 † | *z* | `░░░/░░░/░██` | Bottom-right pair |
| 32 † | *eh* | `░░░/░░█/░░░` | Centre-right cell only |
| — | *je* | — | Not readable at image resolution [^6] |
| 57 † | *sh* | `█░░/███/░░░` | Top-left + middle row |
| 184 † | *y* | `░░░/███/░█░` | Middle row + bottom-centre |
| 170 † | *oo* | `░█░/█░█/░█░` | **Collides with *oh* (#170)** — one reading is wrong [^7] |
| 292 † | *r* | `░░█/░░█/░░█` | Right column only |
| 186 † | *th* | `░█░/███/░█░` | **Coincides with Cross #186** [^7] |

---

## What is missing

**Banks' alphabet — decimal indices** — all 32 phonemes are documented above from the glyph table image[^5], but only *w* (#121) has a confirmed decimal index (stated explicitly in the essay text). All other pattern readings are approximate visual interpretations from a low-resolution image. A pixel-precise analysis of the source image or the tomdionysus font file[^8] would resolve most of these.

**Base-8 numerals** — Banks states that values beyond the alphabet encode octal digits 0–7, punctuation, units of measurement, physical/mathematical constants, and chemical elements. None have published indices.

**zakalwe2040 abjad** — the 24 Tonal Marain consonants[^4] are published as SVG glyph diagrams but without decimal index values. Their grid positions are not mapped to the M1 3×3 system (Tonal Marain uses a 4×5 lattice).

---

[^1]: marainkit — derived from the mathematical/geometric properties of the 3×3 binary grid. These 8 values (#0, #16, #170, #186, #325, #341, #495, #511) are the only states fully invariant under all rotations and mirrors. See [`invariant-glyphs.md`](invariant-glyphs.md).

[^2]: Iain M. Banks, *"A Few Notes on Marain"*. Full text at [`../../docs/A_Few_Notes_on_Marain.md`](../../docs/A_Few_Notes_on_Marain.md).

[^3]: Banks writes "The number 1 would be shown as in figure 1" — figure 1 is an image not recoverable from plain text. `#1` (top-left cell only) is the most natural reading of a decimal 1 in LSB-first encoding, but is not confirmed.

[^4]: zakalwe2040, *Tonal Marain*, [github.com/zakalwe2040/marain](https://github.com/zakalwe2040/marain).

[^5]: Banks' glyph table image: [`../../docs/assets/marain-example-banks.png`](../../docs/assets/marain-example-banks.png), reproduced in *"A Few Notes on Marain"*. Patterns for all phonemes except *w* are approximate visual readings from this image and should be treated as provisional.

[^6]: Pattern not legible at available image resolution. These phonemes (*ch*, *v*, *ll*, *je*) are confirmed to exist in Banks' alphabet but their grid patterns need to be sourced from a higher-resolution copy of the image or from a font file implementing the Banks alphabet.

[^7]: *oo* and *th* appear visually similar to *Diamond* (#170) and *Cross* (#186) respectively, but are not invariant glyphs — they may be rotated variants of other phoneme glyphs. This needs verification.

[^8]: tomdionysus, [github.com/tomdionysus/marain-font](https://github.com/tomdionysus/marain-font) — a TrueType implementation of Banks' alphabet. Extracting glyph outlines from `Marain.ttf` via fonttools would yield precise binary values for all mapped characters.
