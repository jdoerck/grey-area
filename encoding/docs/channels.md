# Channel Architecture

Marain's base encoding unit is **16 bits** — two standard bytes. The structure is a **herald bit** plus a **5×3 lattice**.

```
bit 0      (herald)   1 bit  — frame marker / reserved
bits 1–3   (rails)    3 bits — upper rail
bits 4–12  (slate)    9 bits — 3×3 glyph grid
bits 13–15 (rails)    3 bits — lower rail
```

Visual layout:

```
H  [R₁][R₂][R₃]        ← herald + upper rail
   [ 0][ 1][ 2]         ┐
   [ 3][ 4][ 5]         ├  slate (3×3 — glyph index 0–511)
   [ 6][ 7][ 8]         ┘
   [R₄][R₅][R₆]        ← lower rail
```

## Terminology

*Canonical definitions live in [`docs/glossary.md`](../../notes/glossary.md). Definitions here are a summary.*

| Term | Bits | Description |
|------|------|-------------|
| **[slate](../../notes/glossary.md#slate)** | 9 | The 3×3 binary glyph — the stable core unit. Every glyph is defined solely by its slate state (index 0–511). |
| **[rails](../../notes/glossary.md#rails)** | 6 | The upper and lower 3×1 rows flanking the slate (3 above, 3 below). Context channels — semantics unassigned in M1. |
| **[herald](../../notes/glossary.md#herald)** | 1 | The single preceding bit. Role undecided — candidates: frame/word boundary marker, protocol header bit. |
| **[lattice](../../notes/glossary.md#lattice)** | 15 | The 5×3 visual area: rails + slate. The geometric shape of the encoding unit, excluding the herald. |
| **[packet](../../notes/glossary.md#packet)** | 16 | The full 2-byte word: herald + lattice. The encoded semantic unit — a self-contained glyph + context bundle. |

**Why two terms for 15–16 bits?** `lattice` is the visual/structural frame; `packet` is the encoded unit. These are kept separate until rail semantics are assigned — at that point the lattice geometry and the packet encoding may need to be discussed independently (e.g. a font renders a lattice; a transmitter sends a packet).

The **slate** is the stable unit. The rails and herald are reserved — they carry no meaning in M1 unless explicitly assigned.

---

## Relationship to zakalwe2040's Tonal Marain

zakalwe2040's [Tonal Marain](https://github.com/zakalwe2040/marain#tonal-marain) uses a **4×5 lattice** (portrait):

| Zone | Location | Purpose |
|------|----------|---------|
| Upper diacritic | top row (×4) | vowel encoding |
| Lower diacritic | bottom row (×4) | additional vowel encoding |
| Tonal channel | right column | tonal information |
| Slate | 3×3 centre | graphemes / logograms |

Our layout omits the right tonal column — the 5×3 lattice retains rails and uses the saved space as the herald. This gives a 16-bit (2-byte) aligned structure.

The **rail semantics** from zakalwe2040 are a strong candidate for adoption. The herald's role is unresolved.

---

## Rail semantics (undecided)

Rail content has not been assigned. Open options:

- **Linguistic** — follow zakalwe2040: upper rail = vowel diacritics, lower rail = secondary vowels, herald = word/phrase boundary
- **Contextual** — semantics vary by context type: a code document might use rails for syntax class; a text document for stress/tone; an alert surface for urgency modifier
- **Mixed** — herald as universal frame marker; rails context-assigned

**No rail or herald bit should be assigned until the linguistic layer (`language/`) has enough vocabulary to make the choice with real content.** Premature assignment risks locking the wrong semantics.

---

## Font rendering of rails

Rails are **optional for fonts**. A compliant M1 font may render only the slate. A more capable font may render one or more rails.

Rules:

1. **A font that ignores rails must still be able to receive a full packet** — it simply discards the non-slate bits.
2. **Rail rendering must be visually subordinate to the slate** — rails are diacritics, not equal-weight symbols.
3. **Rail rendering is declared in font metadata** — so a layout engine can choose an appropriate font for the content type.

---

## Open questions

- What does the herald encode? (Start-of-word, start-of-phrase, delimiter, or protocol header bit?)
- Are rail semantics fixed per script level (M1, M2…) or per context type?
- Should we define a right/tonal rail in a future 6×3 + 1 extension, following zakalwe2040 more closely?
- Does the packet map to `uint16` in implementations? (Probably yes — worth making explicit in the encoding spec.)
