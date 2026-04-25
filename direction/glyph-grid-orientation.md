# Glyph Grid Orientation — 180° Rotation

## The Issue

The original implementation rendered the 3×3 binary glyph grids in a visually inverted orientation relative to Banks' design vision. This affected every glyph's visual representation.

The grid cell layout:
```
0 1 2
3 4 5
6 7 8
```

Was being rendered with cell indices as-is, placing the least-significant bit (LSB) at the bottom-right corner visually. Banks intended the grid rotated 180°, placing the LSB at the top-left corner.

## The Fix

In `direction/scripts/generate-glyph-table.py`, the `generate_svg()` function now applies a rotation transform:

```python
rotated_idx = 8 - cell_idx  # Map each cell through 180° rotation
```

This transformation maps:
- 0 ↔ 8 (opposite corners)
- 1 ↔ 7
- 2 ↔ 6
- 3 ↔ 5
- 4 ↔ 4 (center, invariant under rotation)

The canonical binary data in `encoding/docs/glyph-table.tsv` remains unchanged; only the visual rendering is rotated.

## Why Banks Likely Intended This

Several plausible reasons for the 180° orientation:

### 1. Binary Endianness & Reading Weight
Banks may have conceptualized the 9-bit value as having a natural reading direction. A 180° rotation places the LSB visually at the top-left rather than bottom-right, which could align with how he imagined the glyphs being "read" or how weight should distribute in the visual representation.

### 2. Aesthetic & Symbolic Meaning
In the Culture novels, visual representation carries semantic weight. The rotation could encode status or urgency — for example, making critical states (111111111) look visually "complete" in a specific orientation that felt natural to Banks' eye.

### 3. Physical Manifestation Conventions
If glyphs were imagined as being carved, projected, or displayed in specific contexts (ship displays, fabric weaving, stone inscriptions), the 180° orientation might reflect how they'd naturally appear in those mediums.

### 4. Reading Direction Alignment
Marain might have been conceived with non-standard reading conventions (bottom-up, right-to-left, or rotated viewing). The 180° rotation could align the glyph orientation with those cultural or linguistic conventions within the Culture universe.

## Impact

This affects:
- Visual glyph table display (`docs/index.html` — regenerated post-fix)
- Glyph recognition and memorization
- Any visual documentation or educational materials derived from the glyph table

The binary encoding itself is unaffected — the TSV values are canonical and don't change.

## Design Lesson

This is a reminder that visual representation carries meaning in a constructed language. An inverted grid doesn't change the semantic value, but it *does* change how the symbol is perceived and remembered. When documenting invented systems, ensure the *visual intent* of the original designer is captured, not just the encoding scheme.
