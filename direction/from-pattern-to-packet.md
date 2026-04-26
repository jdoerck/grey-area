# From Pattern to Packet — Understanding Marain Glyphs

Every Marain glyph is **one stable object** with four representations: a visual pattern, a 9-bit binary value, a semantic meaning, and an encoded packet. This document shows how those representations connect.

---

## The Pattern: Visual Form

A Marain glyph is a **3×3 binary grid**. Each cell is either filled (█) or empty (░).

```
█ ░ █
░ █ ░
█ ░ █
```

This visual arrangement is **not** arbitrary. It's a deliberate design that will be rendered, read, and transmitted.

---

## Pattern → Binary: Indexing

Each cell in the 3×3 grid maps to a bit position (0–8), reading left-to-right, top-to-bottom:

```
Grid layout:          Binary positions:
[0][1][2]             [0][1][2]
[3][4][5]      →      [3][4][5]
[6][7][8]             [6][7][8]
```

Our example pattern:
```
█ ░ █
░ █ ░
█ ░ █
```

Maps to filled positions: **0, 2, 4, 6, 8**

As a 9-bit binary string (reading left-to-right):
```
█░█░█░█░█  →  101010101
```

As a decimal integer:
```
101010101 (binary) = 341 (decimal)
```

**So this pattern is glyph #341.**

---

## Binary → Meaning: Lookup

The 9-bit value is not arbitrary — each value has a documented meaning. For example:

| Property | Value |
|----------|-------|
| **Decimal ID** | 341 |
| **Binary** | `101010101` |
| **Marain name** | *Checkerboard* |
| **Category** | Invariant glyph (warning vocabulary) |
| **Meaning** | Noise · interference · maximum intensity |
| **Properties** | Rotationally symmetric — looks identical when rotated 0°, 90°, 180°, 270° |

This is **metadata** — information stored in the glyph table (TSV).

---

## Meaning → Visual Icon: Rendering

When you render glyph #341, the binary pattern generates a visual icon:

![glyph 341 - Checkerboard](/docs/assets/glyphs/341.png)

This icon is:
- **Deterministic** — the same binary value always produces the same image
- **Scale-independent** — it looks the same at 16px or 256px
- **Font-independent** — we can render it with any rendering engine (SVG, TTF, PNG, etc.)

The icon is what users *see and recognize* as Marain. But it's generated from the binary pattern — there's one source of truth.

---

## Visual Icon → Encoded Packet: Transmission

When Marain text is transmitted, stored, or processed as data, a single glyph is packaged into a **16-bit packet**:

```
bit 0       [H]                   Herald (1 bit) — frame/reserved
bits 1–3    [R₁][R₂][R₃]          Upper rail (3 bits) — context
bits 4–12   [ 0][ 1][ 2]          Slate — the 3×3 glyph (9 bits)
            [ 3][ 4][ 5]          ↓ this is glyph #341
            [ 6][ 7][ 8]
bits 13–15  [R₄][R₅][R₆]          Lower rail (3 bits) — context
```

For glyph #341 (Checkerboard):

```
Packet bits:  [H][R₁R₂R₃][SLATE BITS 0–8][R₄R₅R₆]
Example:      [0][000]     [101010101]     [000]
Binary:       0000101010101000
Hex:          0AA8
Decimal:      2728
```

The **slate** (bits 4–12, the 9-bit glyph value) sits in the center. The **rails** (6 bits, 3 above + 3 below) are context channels. The **herald** (1 bit) marks frame boundaries.

### Why a packet?

- **Self-contained**: one 16-bit word = one semantic unit
- **Extensible**: the 6 rail bits are reserved for future context (tone, vowel marking, syntax class, etc.)
- **Byte-aligned**: 16 bits = 2 bytes = one standard machine word
- **Forward-compatible**: a reader that ignores rails still gets the complete glyph; a reader that understands rails gets extra information

---

## The Complete Flow: Example

Glyph #121 is the phoneme */w/* — the only consonant explicitly assigned by Banks.

### 1. **Pattern** (what it looks like)
```
░ ░ ░
█ █ █
░ ░ █
```

### 2. **Binary value** (what it is)

Filled cells are at positions **3, 4, 5, 8**.

Read as a 9-bit binary value (position 0 is the MSB):
```
Position: 0 1 2 3 4 5 6 7 8
Filled:   0 0 1 1 1 1 0 0 1
Binary:   001111001₂
Decimal:  121₁₀
```

This is the canonical value from `encoding/docs/glyph-table.tsv`.

### 3. **Semantic identity** (what it means)
| Property | Value |
|----------|-------|
| ID | 121 |
| Name | *w* (phoneme) |
| Type | Consonant phoneme |
| Meaning | Bilabial approximant — /w/ sound |

### 4. **Visual icon** (what it looks like when rendered)
![glyph 121 - w phoneme](/docs/assets/glyphs/121.png)

### 5. **Encoded packet** (how it travels)
```
Herald + Upper Rail + Slate + Lower Rail = 16-bit packet

[H][R₁R₂R₃][░░░█████░░█][R₄R₅R₆]
[0][000]   [001111001]   [000]    (example with empty rails)

Binary: 0000001111001000
Hex: 07C8
Decimal: 1992
```

When transmitted, this packet carries:
- The **glyph itself** (the slate, bits 4–12 = value 121)
- **Context** (empty rails in this example; could carry tone, diacritics, syntax information when assigned)
- **Frame marker** (the herald bit; role TBD)

---

## The Four Representations

Every Marain glyph can be understood in four ways:

| Representation | Example | Purpose |
|---|---|---|
| **Visual Pattern** | `█░░/███/█░░` | How you draw it by hand or read it visually |
| **Binary Value** | `001111001` (decimal 121) | How you compute it, encode it, transmit it |
| **Semantic Name** | *w* (phoneme) | How you discuss it in language |
| **Rendered Icon** | ![glyph 121 - w phoneme](/docs/assets/glyphs/121.png) | How fonts display it |

All four are the **same glyph** — different views of one thing.

---

## Why This Matters

These four representations are interchangeable. When you see:
- `█░░/███/█░░` (pattern)
- `#121` or `001111001` (binary)
- */w/* (semantic name)
- ![glyph 121](../../docs/assets/glyphs/121.png) (rendered icon)

…they all refer to **the same glyph** — different views of one stable unit.

This matters because:
- **Documentation clarity**: references can be pattern, number, or name interchangeably
- **Implementation**: conversion between forms is deterministic and bidirectional
- **Extensibility**: the packet structure allows context layers (rails) without changing the core glyph encoding
- **Longevity**: fonts and media change; the 9-bit value persists

---

## The Glyph as Stable Unit

Here's the key insight: **the glyph (9-bit value) is the canonical, stable unit**.

Everything else flows from it:
- Different **fonts** render the same glyph differently
- Different **contexts** wrap the glyph in different rail semantics
- Different **media** (print, screen, text, transmission) display it differently
- But the **glyph value itself never changes**

Glyph #121 is always *w*, always `001111001`, always renders as that specific 3×3 pattern. This stability is why Marain can survive across centuries, media shifts, and cultural boundaries — the core unit (the glyph) is rock-solid.

---

## References

- **`encoding/docs/glyph-table.tsv`** — canonical lookup table (decimal ID → name, binary, meaning)
- **`encoding/docs/glyphs.md`** — complete catalog with all known assignments, design decisions, and conflicts
- **`encoding/docs/glyph-index.md`** — index sorted by decimal value
- **`encoding/docs/channels.md`** — packet structure and rail semantics
- **`direction/glyph-grid-orientation.md`** — 180° rotation details
- **`notes/source/a-few-notes-on-marain.md`** — Banks' original essay (source material)
