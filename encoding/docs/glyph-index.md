# Glyph Index

Reference table for all 512 possible Marain M1 glyph values (0–511). Only values with known or claimed assignments are listed. See [`glyphs.md`](glyphs.md) for full source descriptions and attribution.

---

## Binary convention

Banks uses **LSB-first** notation — the leftmost digit in the binary string is bit 0 (value 1), rightmost is bit 8 (value 256). This is the opposite of standard binary notation.

Grid cell numbering:

```
[0][1][2]     value = 2^0 + 2^1 + 2^2
[3][4][5]           + 2^3 + 2^4 + 2^5
[6][7][8]           + 2^6 + 2^7 + 2^8
```

Example: Banks states phoneme "w" = binary `100111100` = 121 in base 10.
Cells filled: 0, 3, 4, 5, 6 → 1 + 8 + 16 + 32 + 64 = 121 ✓

---

## Known assignments

10 of 512 values have confirmed or proposed assignments.

| Value | Binary | Grid | Name / Phoneme | Meaning | Attribution | Status |
|------:|--------|------|---------------|---------|-------------|--------|
| 0 | `000000000` | `░░░/░░░/░░░` | **Empty** | Silence · null · word space | marainkit[^1] | Derived |
| 1 | `100000000` | `█░░/░░░/░░░` | **1** | The number one | Banks[^2] | Implied[^3] |
| 16 | `000010000` | `░░░/░█░/░░░` | **Point** | Singularity · decimal point | marainkit[^1] | Derived |
| 121 | `100111100` | `█░░/███/█░░` | **w** | First letter of Marain alphabet; phoneme /w/ | Banks[^2] | Canonical |
| 170 | `010101010` | `░█░/█░█/░█░` | **Diamond** | Danger · hazard | marainkit[^1] | Derived |
| 186 | `010111010` | `░█░/███/░█░` | **Cross** | Alert · stop | marainkit[^1] | Derived |
| 325 | `101000101` | `█░█/░░░/█░█` | **Corners** | Boundary · perimeter warning | marainkit[^1] | Derived |
| 341 | `101010101` | `█░█/░█░/█░█` | **Checkerboard** | Noise · maximum intensity | marainkit[^1] | Derived |
| 495 | `111101111` | `███/█░█/███` | **Frame** | Enclosure · bracket · container | marainkit[^1] | Derived |
| 511 | `111111111` | `███/███/███` | **Full** | Full stop · header · maximum | marainkit[^1] | Derived |

**502 values are unassigned.**

---

## Notes on known gaps

- **Banks' alphabet:** Banks states the alphabet exists and that rotation/mirror variants cover additional phonemes, but only "w" (`#121`) is given an explicit value in the essay text. The remaining ~26–30 primary phonemes and their rotated variants have no published binary index.
- **Base-8 numerals:** Banks states values beyond the alphabet encode base-8 digits (0–7). The specific glyph indices are unspecified.
- **zakalwe2040 abjad:** The 24-character abjad in Tonal Marain[^4] has visual glyph forms (published as SVG) but the corresponding decimal indices are not listed in the source.
- **`#1` as number one:** Banks says "The number 1 would be shown as in figure 1" — figure 1 is an image not recoverable from the plain text. The assignment `#1 = one` is the most natural reading but is not confirmed.

---

[^1]: marainkit project — derived from mathematical/geometric properties of the 3×3 binary grid. These 8 values are the only states fully invariant under all rotations and mirrors. See [`invariant-glyphs.md`](invariant-glyphs.md).

[^2]: Iain M. Banks, *"A Few Notes on Marain"*. See [`../../docs/A_Few_Notes_on_Marain.md`](../../docs/A_Few_Notes_on_Marain.md).

[^3]: `#1` is implied by Banks stating "The number 1 would be shown as in figure 1" — figure 1 is referenced but not recoverable as text. Treated as implied pending a visual source.

[^4]: zakalwe2040, *Tonal Marain*, [github.com/zakalwe2040/marain](https://github.com/zakalwe2040/marain). Glyph forms are published as SVG diagrams; decimal index values are not listed in the source documentation.
