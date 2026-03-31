# Channel Architecture

Marain's base encoding unit is **16 bits** — one preceding bit plus a 5×3 lattice.

```
bit 0  (preceding)   1 bit   — frame marker / reserved
bits 1–3  (upper)    3 bits  — upper channel
bits 4–12 (slate)    9 bits  — 3×3 glyph grid
bits 13–15 (lower)   3 bits  — lower channel
```

Visual layout:

```
P  [U₁][U₂][U₃]        ← preceding bit + upper channel
   [ 0][ 1][ 2]         ┐
   [ 3][ 4][ 5]         ├  slate (3×3 — glyph index 0–511)
   [ 6][ 7][ 8]         ┘
   [L₁][L₂][L₃]        ← lower channel
```

The **slate** is the stable unit. Every glyph in the active vocabulary is defined solely by its 9-bit slate state. The surrounding channels are reserved — they carry no meaning in M1 unless explicitly assigned.

---

## Relationship to zakalwe2040's Tonal Marain

zakalwe2040's [Tonal Marain](https://github.com/zakalwe2040/marain#tonal-marain) uses a **4×5 lattice** (portrait):

| Zone | Location | Purpose |
|------|----------|---------|
| Upper diacritic | top row (×4) | vowel encoding |
| Lower diacritic | bottom row (×4) | additional vowel encoding |
| Tonal channel | right column | tonal information |
| Slate | 3×3 centre | graphemes / logograms |

Our layout omits the right tonal column — the 5×3 lattice retains upper and lower channels and uses the saved space as a preceding bit. This gives a 16-bit (2-byte) aligned structure.

The **upper and lower channel semantics** from zakalwe2040 are a strong candidate for adoption. The preceding bit's role is unresolved.

---

## Channel semantics (undecided)

Channel content has not been assigned. Open options:

- **Linguistic channels** — follow zakalwe2040: upper = vowel diacritics, lower = secondary vowels, preceding = word/phrase boundary
- **Contextual channels** — semantics vary by context type: a code document might use channels for syntax class; a text document for stress/tone; an alert surface for urgency modifier
- **Mixed model** — preceding bit as universal frame marker; upper/lower channels context-assigned

**No channel should be assigned until the linguistic layer (`language/`) has enough vocabulary to make the choice with real content.** Premature assignment risks locking the wrong semantics.

---

## Font rendering of channels

Channels are **optional for fonts**. A compliant M1 font may render only the slate. A more capable font may render one or more channels.

Rules:

1. **A font that ignores channels must still be able to receive a full 16-bit value** — it simply discards the non-slate bits.
2. **Channel rendering must be visually subordinate to the slate** — channels are diacritics, not equal-weight symbols.
3. **Channel rendering is declared in font metadata** — so a layout engine can choose an appropriate font for the content type.

---

## Open questions

- What does the preceding bit encode? (Start-of-word, start-of-phrase, delimiter, or protocol header bit?)
- Are channel semantics fixed per script level (M1, M2…) or per context type?
- Should we define a right/tonal channel in a future 6×3 + 1 extension, following zakalwe2040 more closely?
- Does the 16-bit boundary mean character encoding maps to `uint16`? (Probably yes — worth making explicit in the encoding spec.)
