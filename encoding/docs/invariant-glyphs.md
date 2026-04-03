# Invariant Glyphs

Of 512 possible 3×3 binary states, only **8** are fully invariant under all rotations (0°, 90°, 180°, 270°) and mirrors. These are mathematically guaranteed to read identically from any orientation.

They divide naturally into two vocabularies.

For rendering implications — how these glyphs behave across display contexts, minimum size requirements, and their role as the highest-salience tier in the font vocabulary — see [`display/fonts/font-spec.md §3.5 and §5.1`](../../display/fonts/font-spec.md).

---

## Warning Vocabulary (4 glyphs)

| Code | Name | Role | Meaning | Pattern |
|------|------|------|---------|---------|
| `#170` | **Diamond** | warning | danger / hazard | `░█░` `█░█` `░█░` |
| `#186` | **Cross** | warning | alert / stop | `░█░` `███` `░█░` |
| `#325` | **Corners** | warning | boundary / perimeter warning | `█░█` `░░░` `█░█` |
| `#341` | **Checkerboard** | warning | noise / maximum intensity | `█░█` `░█░` `█░█` |

## Structural Delimiters (4 glyphs)

| Code | Name | Role | Meaning | Pattern |
|------|------|------|---------|---------|
| `#0` | **Empty** · *nuul* | structural | silence / null / word space | `░░░` `░░░` `░░░` |
| `#16` | **Point** | structural | singularity / decimal point | `░░░` `░█░` `░░░` |
| `#495` | **Frame** | structural | enclosure / bracket / container | `███` `█░█` `███` |
| `#511` | **Full** | structural | full stop / header marker / maximum | `███` `███` `███` |

---

## Key Implications

1. **These glyphs look different from ordinary text at a glance** — exactly as hazard symbols do today. A reader approaching a Marain document from any direction sees warning glyphs before decoding a single word.
2. **The pairs are semantic inverses:** Empty↔Full (silence/maximum), Point↔Frame (one pixel/everything-but-one-pixel)
3. **The safety system emerges from geometry**, not design convention. It requires no enforcement.
4. **Warning content is readable from any orientation by design** — this is not incidental.

---

## Invariant Glyphs as a Radical Vocabulary

Chinese writing uses 214 Kangxi radicals as composable semantic classifiers — a finite set of structural units that appear alongside content characters to signal categorical meaning (the water radical 氵 before a character indicates "water-related"). These are not decorative: they reduce ambiguity and aid reading speed by establishing semantic context before the reader processes the full character.

The 8 invariant glyphs are natural candidates for an equivalent function in Marain's Column B. Proposed roles:

| Invariant glyph | As radical: semantic domain |
|-----------------|----------------------------|
| Empty `#0` · *nuul* | null / silence / separator |
| Point `#16` | singularity / reference / anchor |
| Diamond `#170` | caution / hazard domain |
| Cross `#186` | alert / stop / prohibition |
| Corners `#325` | boundary / scope / container |
| Checkerboard `#341` | maximum intensity / noise |
| Frame `#495` | structural / enclosure |
| Full `#511` | completion / assertion / header |

A preceding invariant glyph would indicate the semantic domain of the following phonemic sequence — functioning exactly as CJK radicals do. This role should be considered when Column B vocabulary is assigned.

See [`display/fonts/cjk-mixed-scripts.md §3.4`](../../display/fonts/cjk-mixed-scripts.md) and [`font-spec.md §3.5`](../../display/fonts/font-spec.md) for the full rationale.

Sanskrit names have been proposed for all 8 invariant glyphs — see [`language/sanskrit-marain-dictionary-research.md` Category 7](../../language/sanskrit-marain-dictionary-research.md#category-7-warning--safety-vocabulary). These are candidates only; adoption requires validation against the D₄ constraint and Hamming distance requirements.

---

## Open Questions

- Should the 8 invariant glyphs be reserved / highlighted in Column A output?
- Map invariant glyphs to state escalation scale: warning vocabulary → levels 6–8?
- Formalise the radical vocabulary role: are invariant glyphs *always* domain markers in Column B, or optionally so?

---

## Connection to State Escalation

The base-9 index in the display layer maps naturally:

| Glyph | Suggested state level |
|-------|-----------------------|
| Empty `#0` · *nuul* | 0 — silence / null |
| Point `#16` | 1–2 — minimal signal |
| Diamond `#170` | 5–6 — attention/warning boundary |
| Cross `#186` | 6–7 — clear warning |
| Corners `#325` | 5 — boundary/perimeter |
| Checkerboard `#341` | 7 — near-maximum intensity |
| Frame `#495` | 3–4 — structural container |
| Full `#511` | 8 — maximum / critical |

This mapping is proposed, not canonical. Finalize when state escalation system is built.
