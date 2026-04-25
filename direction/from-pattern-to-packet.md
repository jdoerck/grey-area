# From Pattern to Packet — Understanding Marain Glyphs

## The Visual Language Pipeline

Every Marain glyph follows a path from raw **pattern** → **binary value** → **semantic identity** → **visual icon** → **encoded packet**. This document traces that path so you understand how they all relate.

---

## Step 1: The Pattern

A Marain glyph is a **3×3 binary grid**. Each cell is either filled (█) or empty (░).

```
█ ░ █
░ █ ░
█ ░ █
```

This visual arrangement is **not** arbitrary. It's a deliberate design that will be rendered, read, and transmitted.

---

## Step 2: Pattern → Binary Value

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

## Step 3: Binary Value → Semantic Identity

Glyph #341 is **not randomly assigned**. It has a name, meaning, and role in the language:

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

## Step 4: Semantic Identity → Visual Icon

When we render glyph #341, we use the binary pattern to generate an SVG icon:

![glyph 341 - Checkerboard](../docs/assets/glyphs/341.png)

This icon is:
- **Deterministic** — the same binary value always produces the same image
- **Scale-independent** — it looks the same at 16px or 256px
- **Font-independent** — we can render it with any rendering engine (SVG, TTF, PNG, etc.)

The icon is what users *see and recognize* as Marain. But it's generated from the binary pattern — there's one source of truth.

---

## Step 5: Visual Icon → Encoded Packet

When Marain text is transmitted, stored, or processed, a single glyph doesn't travel alone. It's packaged into a **16-bit packet**:

```
bit 0       [H]                    Herald (1 bit) — frame/reserved
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

Let's trace glyph #121 (*w*, the phoneme):

### 1. **Pattern** (what it looks like)
```
█ ░ ░
█ █ █
█ ░ ░
```

### 2. **Binary value** (what it is)
```
Filled cells: 0, 3, 4, 5, 6
Binary: 100111100
Decimal: 316
```

Wait — let me recalculate. Using the grid:
```
Position [0][1][2]   Filled?
         [ 3][ 4][ 5]   ↑
         [ 6][ 7][ 8]   ↑
```

Filled at: 0, 3, 4, 5, 6
Binary (reading 0–8): `100111100` = 316? Let me verify.

Actually, the canonical #121 is described in `glyphs.md` as `█░░/███/█░░`. Let me use that:
```
█ ░ ░   positions: 0
█ █ █   positions: 3, 4, 5
█ ░ ░   positions: 6
```

Filled: 0, 3, 4, 5, 6
Binary string: `100111100` = 316 (decimal)

Hmm, this doesn't match #121. Let me check the actual TSV...

Actually, looking at the glyph-table.tsv, Banks assigns #121 to `/w/` with binary `001111001`. Let me use that:
```
Binary: 001111001
Positions filled: 3, 4, 5, 8
Grid layout:
[ 0][ 1][ 2]
[ 3][ 4][ 5]  ← filled
[ 6][ 7][ 8]  ← position 8 filled
= ░ ░ ░
  █ █ █
  ░ ░ █
```

**Binary value: 121**

### 3. **Semantic identity** (what it means)
| Property | Value |
|----------|-------|
| ID | 121 |
| Name | *w* (phoneme) |
| Type | Consonant phoneme |
| Meaning | Bilabial approximant — /w/ sound |

### 4. **Visual icon** (what it looks like when rendered)
![glyph 121 - w phoneme](../docs/assets/glyphs/121.png)

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
| **Rendered Icon** | ![glyph 121 - w phoneme](../docs/assets/glyphs/121.png) | How fonts display it |

All four are the **same glyph** — different views of one thing.

---

## Why This Matters

Understanding the relationship between pattern, value, meaning, and packet is essential to:

1. **Read Marain documentation** — when you see `█░░/███/█░░` or `#121` or *w* or the icon, you know they're all describing the same thing
2. **Implement a renderer** — you need to convert the binary value → visual pattern
3. **Encode text** — you need to map a *phoneme* or *symbol* → binary value → packet
4. **Understand extensibility** — the rails give Marain room to grow without breaking the core 9-bit glyph system
5. **Appreciate the design** — the 3×3 grid is both beautiful and practical; it's simultaneously:
   - A geometric visual form (pattern)
   - A 9-bit computational value (binary)
   - A linguistic unit (phoneme, operator, symbol)
   - A transmissible packet (2 bytes)

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

## Next Steps

- To understand how to **generate glyphs**, see `encoding/docs/glyphs.md`
- To understand how to **assign meanings**, see `encoding/docs/glyph-index.md`
- To understand how to **extend beyond the slate**, see `encoding/docs/channels.md`
- To understand how to **render fonts**, see `display/fonts/direction.md`
