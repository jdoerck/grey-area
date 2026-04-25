# Encoding Terminology Glossary

Canonical definitions for this project. Use these terms consistently across all documents. Link to the relevant term the first time it appears in any document.

> **Track:** Encoding system — project-defined terminology for the encoding layer. "Canonical" in this document means "this project's established term," not "directly from Banks." Evidence labels are not applied per-claim. See [`tracks.md`](tracks.md).

---

## Core terms

### 3×3 grid

Geometry only: 9 cells arranged in three rows × three columns. Describes shape — does not imply anything about cell states or number systems.

### binary cell

A single grid cell with exactly two states: filled (1) or empty (0). All Marain cells are binary. Not ternary; not base-9.

### slate

The 3×3 binary glyph — the stable 9-bit core unit. Every glyph in the vocabulary is defined solely by its slate state (index 0–511). The slate is the invariant, transmissible, renderable unit; everything else in the packet is context around it.

### glyph

One specific slate state — a filled/empty pattern in the 3×3 grid. 512 possible glyphs (indices 0–511). "Glyph" and "slate" are often interchangeable; "slate" emphasises the encoding unit, "glyph" emphasises the visual symbol.

### rails

The upper and lower 3×1 rows flanking the slate in the lattice (6 bits total: 3 above, 3 below). Context channels whose semantics are unassigned in M1. Visually they extend the slate into a 5×3 block. Replaces: "upper channel", "lower channel", "upper/lower channels".

### herald

The single preceding bit in the packet (1 bit). Role undecided — candidates include frame/word boundary marker or protocol header bit. Replaces: "preceding bit".

### lattice

The 5×3 visual area formed by the rails and slate together (15 bits: 3 upper rail + 9 slate + 3 lower rail). The geometric shape of the encoding unit, excluding the herald. Used when discussing the visual/structural frame — e.g. a font renders a lattice.

### packet

The full 16-bit encoding word: herald + lattice (2 bytes). The encoded semantic unit — a self-contained glyph + context bundle. Used when discussing the encoded/transmitted unit — e.g. a transmitter sends a packet. Replaces: "16-bit word", "semantic packet".

### nonary Marain

Banks' canonical name for M1 (the standard writing tier). "Nonary" means "based on nine" — referring to the 9-cell count of the grid, not to the states of each cell. See *Excession*: *"Based on nine. Ordinary Marain; the stuff you learned in kindergarten, for goodness' sake; the three-by-three dot grid."*

### base-8 numerals

The number system: 8 digits (0–7, octal), per Banks. Consistent with 2³ = 8 and the binary glyph structure.

### status scale 0–8

The display layer's 9-level state hierarchy: 0 = null/silence, 8 = critical. A mapping applied to glyph indices by the display layer — not an intrinsic property of the encoding.

---

## What terms do NOT mean

| Avoid | Why |
|-------|-----|
| "ternary cells" or "three-state cells" | Cells are binary (two states). Ternary would mean three states per cell — that is not how Marain works. |
| "base-9 encoding" | The encoding is 9-bit binary (2⁹ = 512 states). Base-9 encoding would mean each symbol has 9 possible values — a completely different system. |
| "base-9 grid" (for the encoding unit) | The grid has 9 cells, but each is binary. "9-bit binary slate" is precise; "base-9 grid" conflates cell count with number base. |
| "nonary" (as cell state description) | "Nonary Marain" is fine — it's Banks' term for M1 as a system. Describing cells themselves as "nonary" (9-state) is wrong. |
| "preceding bit" | Use **herald**. |
| "upper channel" / "lower channel" | Use **rails** (or "upper rail" / "lower rail"). |
| "16-bit word" | Use **packet**. |
| "semantic packet" | Use **packet**. |

---

## Common correct usages

```
✓  slate          — the 3×3 glyph (9 bits)
✓  rails          — the upper + lower context rows (6 bits)
✓  herald         — the preceding bit (1 bit)
✓  lattice        — the 5×3 visual area (15 bits: rails + slate)
✓  packet         — the full 16-bit encoded word (2 bytes)
✓  nonary Marain  — Banks' term for M1 as a writing system
✓  base-8         — the number system (octal, per Banks)
✓  status scale 0–8 — the display layer's 9-level hierarchy

✗  preceding bit, upper/lower channel, 16-bit word, semantic packet
✗  ternary cells, three-state cells, base-9 encoding, base-9 grid
```

---

## Why lattice and packet are both kept

`lattice` and `packet` refer to the same 16 bits from different angles:

- **lattice** — the visual/geometric frame (5×3 block). A font renders a lattice.
- **packet** — the encoded/transmitted unit (16-bit word). A transmitter sends a packet.

These are kept as separate terms until the herald and rail bit assignments are decided. At that point the geometric and semantic descriptions may need to be discussed independently — e.g. a font might render only the lattice while a protocol defines the full packet.

---

## Why the binary/nonary confusion arises

Three different "nines" exist in the system:

1. **9 cells** — the grid geometry. This is where "nonary Marain" comes from, and it is correct.
2. **9-bit binary** — the encoding. 9 binary cells = 9 bits = 512 states (not 9 states per cell).
3. **9-level status scale (0–8)** — a display-layer convention, separate from both of the above.

"Nonary Marain" is canonical (Banks used it) but should not be taken to imply cells have 9 states. Banks defined Marain as a binary system (filled/empty cells) — "nonary" refers to the cell count, not the information capacity of each cell.

---

*See also:* [`direction/encoding-density-and-packets.md`](../direction/encoding-density-and-packets.md) — information-density analysis and the byte-alignment rationale for the 16-bit packet.
