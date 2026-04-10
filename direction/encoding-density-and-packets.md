# Encoding Density and the Semantic Packet Model

Two related insights from comparing Marain's 9-bit encoding to ASCII and conventional 8-bit systems.

---

## Information density

Marain Column B glyphs encode phoneme clusters — roughly 2–3 Latin characters' worth of information per symbol. At a conservative 2.5 letters per glyph:

- 9 bits / 2.5 ≈ **3.6 bits per letter**
- Compare: 8-bit ASCII = 8 bits per character

Even accounting for the 7 non-[slate](../notes/glossary.md#slate) context bits in the full [packet](../notes/glossary.md#packet), each packet at 2.5 letters per glyph ≈ 6.4 bits per letter — comparable to ASCII, but with embedded context rather than bare characters.

This compression is what justifies the 7-bit "overhead." The phoneme-cluster encoding offsets it.

---

## The semantic packet framing

Each Marain encoding unit is a **packet**: 16 bits = 2 bytes. It groups as:

```
[slate: 9 bits] + [rails + herald: 7 bits]
= glyph + context
```

The full structure (see `encoding/docs/channels.md` for the canonical definition):

```
herald  (1 bit)  — role undecided
rails   (3 bits) — upper rail (3×1 row above slate)
slate   (9 bits) — 3×3 glyph
rails   (3 bits) — lower rail (3×1 row below slate)
```

The **[lattice](../notes/glossary.md#lattice)** is the 5×3 visual area formed by the [rails](../notes/glossary.md#rails) and slate together. The packet is the full 16-bit encoded unit including the [herald](../notes/glossary.md#herald).

### Why 16 bits? Why 2 bytes?

A 9-bit slate is one bit too large for a single byte (8 bits). The minimum standard alignment that fits it is **2 bytes = 16 bits**. That leaves 7 bits — not wasted, but structured as rails (6 bits) and herald (1 bit).

The byte boundary is not a design choice — it's an arithmetic consequence of aligning a 9-bit value to standard storage. The 7 remaining bits become embedded context. You don't choose a 2-byte packet because you need 7 context bits; you get 7 context bits because 2 bytes is the minimum that holds a 9-bit slate.

The 7 non-slate bits function collectively as *embedded context* — they travel with the glyph rather than being declared externally. A Marain symbol is not a character; it is a **character + context packet**.

What 7 context bits can encode (128 possible states):
- status / urgency (normal → critical)
- surface type (document, HUD, code, alert)
- certainty or scope modifiers
- vowel/tone diacritics (following zakalwe2040's channel model)
- error detection bit

Channel semantics are still undecided — see `encoding/docs/channels.md`. But the *capacity* — 128 context states — is already defined by the architecture.

---

## Design principles this implies

**Recoverability** — the packet structure should be decodable without prior agreement on vocabulary. Structure must be legible from the bits alone.

**Context embedded, not external** — meaning travels with the symbol. This is the fundamental shift from character encodings like ASCII, where context is application-level.

**Structure over arbitrary mapping** — bit patterns should reveal categories where possible. The invariant glyph property and the sequential numeral fill rule are examples of this already in the design.
