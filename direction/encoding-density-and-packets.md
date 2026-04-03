# Encoding Density and the Semantic Packet Model

Two related insights from comparing Marain's 9-bit encoding to ASCII and conventional 8-bit systems.

---

## Information density

Marain Column B glyphs encode phoneme clusters — roughly 2–3 Latin characters' worth of information per symbol. At a conservative 2.5 letters per glyph:

- 9 bits / 2.5 ≈ **3.6 bits per letter**
- Compare: 8-bit ASCII = 8 bits per character

Even accounting for the 7 non-slate context bits in the full 16-bit packet, each 16-bit unit at 2.5 letters per glyph ≈ 6.4 bits per letter — comparable to ASCII, but with embedded context rather than bare characters.

This compression is what justifies the 7-bit "overhead." The phoneme-cluster encoding offsets it.

---

## The semantic packet framing

The 16-bit word defined in `encoding/docs/channels.md` (`[1 preceding] + [3 upper] + [9 slate] + [3 lower]`) can be usefully grouped as:

```
[glyph: 9 bits] + [context: 7 bits]
```

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
