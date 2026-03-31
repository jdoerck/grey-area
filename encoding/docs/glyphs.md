# Known Marain Glyphs

A catalogue of claimed Marain glyphs, symbols, and phonemes across canonical and community sources. Attribution and canonicity are noted throughout.

For a lookup table of all assigned values by decimal index, see [`glyph-index.md`](glyph-index.md).
For the cross-system comparison tables and design discussion, see [`glyph-decisions.md`](glyph-decisions.md).
For the decision backlog and roadmap, see [`roadmap.md`](roadmap.md).
For the 16-bit word structure and channel architecture (upper, lower, preceding bits), see [`channels.md`](channels.md).

---

## Scope and canonicity

No single authoritative glyph table exists. Banks defined the system mathematically in his essay[^1] but published only a partial character list (the image in that essay is the closest thing to a canonical alphabet). Everything else is community interpretation or extension.

| Status | Meaning |
|--------|---------|
| **Canonical** | Directly stated by Banks in his essay |
| **Community** | Non-canonical; community-created, may be widely adopted |
| **marainkit** | Derived by this project from mathematical/geometric properties of the grid |

---

## Banks' canonical system (M1)[^1]

### Grid structure

Each glyph is a 3×3 binary grid — a 9-bit number. 512 possible values (0–511). Each cell is filled (1) or empty (0), rendered as black or white squares.

The value 0 = all cells empty. The value 511 = all cells filled.

### Known canonical values

Banks names only two specific values explicitly:

| Value | Binary | Description |
|-------|--------|-------------|
| 1 | `000000001` | The number 1 (see "figure 1" in essay) |
| 121 | `001111100` | The phoneme "w" — first letter of the Marain alphabet |

### Canonical alphabet properties

- Glyphs are designed to be **rotated and mirrored** without confusion with any other primary alphabetical symbol
- Rotated versions represent phonemes **close to the original** unrotated sound
- Some rotations have **little phonemic relation** to the original — used for different vocalisations
- The system is designed to reproduce **any language capable of being spoken by a humanoid**

### Canonical non-alphabetic values

Beyond the alphabet, Banks states the remaining values (after phonemes) encode:
- Numbers in **base 8** (octal)
- Punctuation
- Common units of measurement
- Physical and mathematical symbols and constants
- Chemical elements

### Byte extensions

| Byte length | Symbol count | Notes |
|------------|-------------|-------|
| 9-bit (standard) | 512 | Core Marain — M1 |
| 10-bit | 1,024 | 512 additional symbols |
| 12-bit | 4,096 | Most common extended form; representable as a grid |
| 16-bit (4×4 grid) | 65,536 | Next square grid — pictograms, alien symbols, diagrams |
| Arbitrary | Unlimited | In principle unbounded; large grids transmit images |

Data transmission appends a **buffer bit** after each 9-bit glyph.

---

## Invariant glyphs (marainkit)[^2]

Of 512 possible 3×3 binary states, exactly **8 are fully invariant** under all rotations (0°, 90°, 180°, 270°) and mirrors. These are mathematically guaranteed to read identically from any orientation. Identified by this project — not claimed by Banks.

### Warning vocabulary

| Code | Name | Pattern | Proposed meaning |
|------|------|---------|-----------------|
| `#0` | **Empty** · *nuul* | `░░░ ░░░ ░░░` | Silence · null · word space |
| `#16` | **Point** | `░░░ ░█░ ░░░` | Singularity · decimal point |
| `#170` | **Diamond** | `░█░ █░█ ░█░` | Danger · hazard |
| `#186` | **Cross** | `░█░ ███ ░█░` | Alert · stop |
| `#325` | **Corners** | `█░█ ░░░ █░█` | Boundary · perimeter warning |
| `#341` | **Checkerboard** | `█░█ ░█░ █░█` | Noise · maximum intensity |
| `#495` | **Frame** | `███ █░█ ███` | Enclosure · bracket · container |
| `#511` | **Full** | `███ ███ ███` | Full stop · header · maximum |

The pairs are semantic inverses: Empty↔Full, Point↔Frame, Diamond↔Checkerboard, Cross↔Corners.

**Proposed state escalation mapping:**

| Glyph | Suggested level (0–8) |
|-------|-----------------------|
| Empty `#0` · *nuul* | 0 — silence / null |
| Point `#16` | 1–2 — minimal signal |
| Frame `#495` | 3–4 — structural container |
| Corners `#325` | 5 — boundary / perimeter |
| Diamond `#170` | 5–6 — attention / warning boundary |
| Cross `#186` | 6–7 — clear warning |
| Checkerboard `#341` | 7 — near-maximum intensity |
| Full `#511` | 8 — maximum / critical |

This mapping is **proposed, not canonical**. Finalize when state escalation system is built.

---

## Tonal Marain — zakalwe2040[^3]

A significant community extension adding tonal encoding, a 24-character abjad, diacritics, emoting glyphs, numerals, and mathematical notation. Uses a **4×5 dot lattice** rather than the canonical 3×3 grid. Non-canonical but the most developed community implementation.

### Lattice structure

```
┌─────────────────────────┐
│  Upper diacritic (red)  │  ← short vowels
├─────────────────────────┤
│  3×3 Slate (green)      │  ← core glyph
├─────────────────────────┤
│  Lower diacritic (blue) │  ← short vowels
├────────────┬────────────┤
│            │  Tonal     │  ← 5 tones (emotional content)
│            │  channel   │
└────────────┴────────────┘
```

Direction: **right to left** (following Modern Hebrew / Arabic convention).

### The 24-character abjad

Organized by place of articulation, then phoneme frequency. Default vowel on a bare consonant is *a* (overridden by diacritics).

| Place of articulation | Phonemes |
|----------------------|---------|
| Bilabial | *ma* · *wa* · *pa* · *ba* |
| Labio-dental | *fa* · *va* |
| Interdental | *tha* · *dtha* · *cha* · *dja* |
| Alveolar | *ta* · *na* · *sa* · *da* · *la* · *za* |
| Post-alveolar | *ra* · *sha* |
| Palatal | *ya* |
| Velar | *ga* · *ka* · *nga* |
| Glottal | *aa* · *ha* |

### Abjad compatibility with Banks and marainkit

Patterns for all 24 abjad consonants were extracted programmatically from `docs/abjad.svg` in the zakalwe2040 repo (same method as emoting glyphs). Results compared against Banks' approximate phoneme assignments from the glyph table image and marainkit invariants.

**Pattern comparison — zakalwe2040 abjad vs Banks M1**

| Phoneme | Z# | Z-Pattern | B# | B-Pattern | Match |
|---------|----|-----------|----|-----------|-------|
| *ma* | 457 | `█░░/█░░/███` | 457 | `█░░/█░░/███` | ✓ |
| *wa* | 511 | `███/███/███` | 121 | `█░░/███/█░░` | ✗ |
| *pa* | 79 | `███/█░░/█░░` | 459 | `██░/█░░/███` | ✗ |
| *ba* | 295 | `███/░░█/░░█` | 432 | `░░░/░██/░██` | ✗ |
| *fa* | 173 | `█░█/█░█/░█░` | 56 | `░░░/███/░░░` | ✗ |
| *va* | 362 | `░█░/█░█/█░█` | — | — | — |
| *tha* | 133 | `█░█/░░░/░█░` | — | — | — |
| *dtha* | 319 | `███/███/░░█` | — | — | — |
| *cha* | 127 | `███/███/█░░` | — | — | — |
| *dja* | 465 | `█░░/░█░/███` | — | — | — |
| *ta* | 307 | `██░/░██/░░█` | 168 | `░░░/█░█/░█░` | ✗ |
| *na* | 493 | `█░█/█░█/███` | 295 | `███/░░█/░░█` | ✗ |
| *sa* | 367 | `███/█░█/█░█` | 214 | `░██/░█░/██░` | ✗ |
| *da* | 87 | `███/░█░/█░░` | 480 | `░░░/░░█/███` | ✗ |
| *la* | 484 | `░░█/░░█/███` | 484 | `░░█/░░█/███` | ✓ |
| *za* | 469 | `█░█/░█░/███` | 384 | `░░░/░░░/░██` | ✗ |
| *ra* | 189 | `█░█/███/░█░` | 292 | `░░█/░░█/░░█` | ✗ |
| *sha* | 383 | `███/███/█░█` | 57 | `█░░/███/░░░` | ✗ |
| *ya* | 468 | `░░█/░█░/███` | 184 | `░░░/███/░█░` | ✗ |
| *ga* | 502 | `░██/░██/███` | 120 | `░░░/███/█░░` | ✗ |
| *ka* | 500 | `░░█/░██/███` | 312 | `░░░/███/░░█` | ✗ |
| *nga* | 509 | `█░█/███/███` | 16 | `░░░/░█░/░░░` | ✗ |
| *aa* | 322 | `░█░/░░░/█░█` | — | — | — |
| *ha* | 487 | `███/░░█/███` | 493 | `█░█/█░█/███` | ✗ |

Only **2 of 24 match**: *ma* (#457) and *la* (#484). The two systems are effectively independent designs using the same 3×3 grid.

**Key conflicts:**

- **wa = #511** — zakalwe2040 assigns *wa* to the all-cells-filled glyph. This is one of marainkit's 8 invariants ("Full stop · maximum · critical") and is likely intentional in zakalwe2040 (the fully-open, maximum-resonance bilabial). It directly collides with both Banks (#121, the only explicitly confirmed canonical phoneme assignment) and marainkit.
- **na = #493** — zakalwe2040's *na* occupies the same value Banks assigns to *h*.
- Several other zakalwe2040 values land on or near Banks-claimed indices.

**Structural observation:**

The 4×5 lattice is a proper superset of M1. The 3×3 slate region is exactly an M1 glyph; the upper/lower diacritic rows and tonal column extend it without contradiction. In principle a 4×5 Marain glyph carries an M1 glyph as its core with additional phonemic information layered on. The two systems are architecturally compatible — the phoneme *assignments* are not.

---

### Design notes — paths forward (marainkit)

These are open design questions, not resolved decisions.

**1. The abjad is a parallel system, not a variant.**
The near-total mismatch (22 of 24 different) means there is no easy merge path. Adopting zakalwe2040's abjad would require abandoning most of Banks' approximate phoneme assignments. Rejecting it means maintaining a separate, less-documented phoneme set. A hybrid — accepting only *ma* and *la* as confirmed cross-system values — is possible but probably doesn't gain much.

**2. The wa/#511 conflict is the sharpest edge.**
Banks' *w* = #121 is the *only* canonical phoneme index stated explicitly in text (not read from an image). If we ever commit to a marainkit phoneme layer, #121 should be treated as the highest-confidence single assignment in the system. Displacing it in favor of #511 would mean abandoning the one number Banks actually gave us.

**3. The 10th bit as long-vowel marker.**
Banks notes that each 9-bit glyph is followed by a **buffer bit** in transmission. That 10th bit is currently undefined within M1. One option: reserve it as a **vowel-length marker** — short vowel (default *a*) vs. long vowel. This would give every consonant glyph a paired long-vowel form without consuming any M1 index space, and would be consistent with zakalwe2040's diacritic architecture (which handles the same distinction, differently).

**4. Reassigning wa.**
If we do define a marainkit phoneme layer, *wa* needs a value that does not conflict with #511. The natural candidate is Banks' own #121 (already canonical). The zakalwe2040 pattern for *wa* (#511, all-filled) could be interpreted as an intentional homoiconic choice — a fully-resonant bilabial — but it permanently occupies a structurally significant glyph. Reassignment is clean; the question is what, if anything, #511 then represents phonemically.

**5. The 4×5 lattice as M2.**
If marainkit ever defines an extended encoding layer, zakalwe2040's 4×5 architecture (slate + diacritic channels + tonal channel) is the most developed community design for exactly that purpose. Even if we don't adopt the phoneme assignments, the lattice geometry is worth treating as a reference design for M2.

---

### Diacritics (short vowels)

| Diacritic | Position | Vowel | IPA |
|-----------|----------|-------|-----|
| *up* | Bar above letter | *a* | /æ/ |
| *out* | Dot above start | *u* | /ʊ/ |
| *down* | Bar below letter | *i* | /ɪ/ |
| *stop* | Dot above end | (zero vowel) | — |

### Emoting glyphs (22)

Non-verbal communication glyphs organized into four categories. Unicode equivalents given as approximate reference.

**Logical signals**

| Glyph | Unicode approx. | Meaning |
|-------|----------------|---------|
| *shacha* | 🖖 | Greetings · prosperity · peace · hello · bye |
| *samara* | 🤨 | Fascination · logic understood |

**Positive emotional signals**

| Glyph | Unicode approx. | Meaning |
|-------|----------------|---------|
| *hub* | 💛 | Love |
| *zing* | ✨ | Positivity |
| *yam* | 🙏 | Hope |
| *wun* | 💕 | Warmth |
| *shaa* | 🤣 | Laughter |
| *mar* | 😂 | Joy |
| *hoo* | 😊 | Happiness |
| *lang* | 🥰 | Romance |
| *gang* | 😘 | Affection |
| *shii* | 😉 | Synchronicity |
| *shai* | 👍 | Agreement |
| *zang* | 😲 | Surprise |
| *shuu* | 😍 | Infatuation |

**Necessary emotional signals**

| Glyph | Unicode approx. | Meaning |
|-------|----------------|---------|
| *ging* | 🥺 | Sympathy |
| *bay* | 😢 | Sadness |

**Negative emotional signals**

| Glyph | Unicode approx. | Meaning |
|-------|----------------|---------|
| *buz* | 😭 | Overwhelmed |
| *yan* | 🤢 | Disgust |
| *fin* | 😡 | Anger |
| *pil* | 🥱 | Fatigue |
| *paa* | 😨 | Fear |

### Numerals

#### marainkit — base 8 (octal)

Eight digits, 0–7. **Sequential-fill rule:** digit *n* = exactly *n* filled cells, reading order left→right top→bottom. Count the dots to read the digit. Visual progression is a tally filling the grid row by row. Consistent with Banks' base-8 system and his two implied values (#0 = zero, #1 = one). Digit 7 = #127 — stops one cell short of the Full invariant (#511). See [`glyph-index.md`](glyph-index.md) for index entries and full rationale.

Digit names adopted from zakalwe2040[^3] — standard Mandarin pinyin, digits 0–7 only (8 and 9 do not exist in base 8).

| Digit | Name | # | Glyph | Binary |
|-------|------|---|-------|--------|
| 0 | *líng* | 0 | `░░░`<br>`░░░`<br>`░░░` | `000000000` |
| 1 | *yī* | 1 | `█░░`<br>`░░░`<br>`░░░` | `100000000` |
| 2 | *èr* | 3 | `██░`<br>`░░░`<br>`░░░` | `110000000` |
| 3 | *sān* | 7 | `███`<br>`░░░`<br>`░░░` | `111000000` |
| 4 | *sì* | 15 | `███`<br>`█░░`<br>`░░░` | `111100000` |
| 5 | *wǔ* | 31 | `███`<br>`██░`<br>`░░░` | `111110000` |
| 6 | *liù* | 63 | `███`<br>`███`<br>`░░░` | `111111000` |
| 7 | *qī* | 127 | `███`<br>`███`<br>`█░░` | `111111100` |

Each glyph in a number sequence is one octal digit. Multi-digit numbers read left to right: the leftmost glyph is the largest group.[^11]

---

#### zakalwe2040 — base 10 (decimal)

**Decimal** (0–9). Names borrowed from **Mandarin Chinese**. Written **right to left**. The digit names follow Mandarin; the numbering system beyond single digits does not.[^3]

Note: Banks explicitly states that Marain encodes numbers in **base 8 (octal)**. zakalwe2040 uses base 10. These are architecturally incompatible choices — see design notes below.

| Digit | # | Pattern |
|-------|---|---------|
| 0 | 341 | `█░█/░█░/█░█` |
| 1 | 471 | `███/░█░/███` |
| 2 | 466 | `░█░/░█░/███` |
| 3 | 121 | `█░░/███/█░░` |
| 4 | 243 | `██░/░██/██░` |
| 5 | 95  | `███/██░/█░░` |
| 6 | 373 | `█░█/░██/█░█` |
| 7 | 125 | `█░█/███/█░░` |
| 8 | 317 | `█░█/███/░░█` |
| 9 | 381 | `█░█/███/█░█` |

### Mathematical and logical notation

Glyph design follows the principle of **homoiconicity** — glyphs allude to their meaning through form. Symmetry choices are informed by research on cognitive benefits of symbol symmetry alignment with operator commutativity.[^4]

**Arithmetic operators**

| Symbol | Name | # | Pattern |
|--------|------|---|---------|
| + | addition | 170 | `░█░/█░█/░█░` |
| × | multiplication | 495 | `███/█░█/███` |
| − | subtraction | 300 | `░░█/█░█/░░█` |
| ÷ | division | 364 | `░░█/█░█/█░█` |
| mod | modulo | 301 | `█░█/█░█/░░█` |

**Logic**

| Symbol | Name (Marain) | # | Pattern |
|--------|--------------|---|---------|
| & | *wa* (and / conjunction) | 284 | `░░█/██░/░░█` |
| \| | *ow* (or / disjunction) | 113 | `█░░/░██/█░░` |
| ! | *ma* (not / negation) | 343 | `███/░█░/█░█` |

**Equality and copula**

| Symbol | Name (Marain) | # | Pattern |
|--------|--------------|---|---------|
| = | *heeya* (equality) | 63 | `███/███/░░░` |
| := | *kun* (definition / assign) | 191 | `███/███/░█░` |
| iz | *iz* (copula — to be) | 186 | `░█░/███/░█░` |

**Punctuation**

| Symbol | Name (Marain) | # | Pattern |
|--------|--------------|---|---------|
| ? | *mahu* (question / λ-calculus) | 342 | `░██/░█░/█░█` |
| . | (period / decimal point) | 16 | `░░░/░█░/░░░` |
| , | (comma) | 128 | `░░░/░░░/░█░` |
| ; | (semicolon) | 144 | `░░░/░█░/░█░` |

**Brackets and delimiters**

| Symbol | # | Pattern |
|--------|---|---------|
| `>` | 81 | `█░░/░█░/█░░` |
| `<` | 276 | `░░█/░█░/░░█` |
| `]` | 211 | `██░/░█░/██░` |
| `[` | 406 | `░██/░█░/░██` |
| `)` | 251 | `██░/███/██░` |
| `(` | 446 | `░██/███/░██` |
| `}` | 479 | `███/██░/███` |
| `{` | 503 | `███/░██/███` |

---

### Numerals and notation — compatibility with Banks and marainkit

Patterns extracted from zakalwe2040 SVGs: `numerals.svg`, `binary-operators.svg`, `logic.svg`, `equality.svg`, `punctuation.svg`, `brackets.svg`.

**Agreements**

| # | Z-symbol | marainkit / Banks | Note |
|---|----------|-------------------|------|
| 16 | `.` (period) | marainkit **Point** · Banks *ng* (decimal point) | Only cross-system agreement. All three sources assign #16 to "decimal point". The strongest single confirmed value outside #121. |

**Conflicts with marainkit invariants**

| # | Invariant (marainkit) | Z-symbol | Z-group | Tension |
|---|-----------------------|----------|---------|---------|
| 170 | **Diamond** — danger · hazard | `+` | arithmetic | Homoiconic argument for `+`: a diamond is a rotated plus. But marainkit treats Diamond as a warning glyph. |
| 186 | **Cross** — alert · stop | `iz` (copula) | equality | "To be" sharing a value with "stop" is a hard semantic conflict. |
| 341 | **Checkerboard** — noise · interference | digit `0` | numerals | marainkit already reserves #0 (Empty, *nuul*) for zero/null. #341 for zero is a deliberate departure. |
| 495 | **Frame** — enclosure · container | `*` | arithmetic | Less obvious homoiconic reading (multiplication as enclosure?). |

**Conflicts with Banks**

| # | Banks | Z-symbol | Note |
|---|-------|----------|------|
| 121 | *w* — only explicitly-confirmed canonical phoneme | digit `3` | The sharpest single conflict in the entire system. |
| 170 | *oh* (phoneme, approx.) | `+` | Approximate reading only — lower confidence than #121. |
| 186 | *th* (phoneme, approx.) | `iz` (copula) | Approximate reading only. |

**Base-8 vs base-10**

Banks states explicitly that Marain encodes numbers in base 8. zakalwe2040 uses base 10 (10 digits, Mandarin names). This is the most fundamental structural split in the zakalwe2040 extensions — it cannot be resolved by reassigning a single value.

- Banks' base-8 requires 8 digit glyphs (0–7). Any 8 values could work; none have been published.
- zakalwe2040's base-10 requires 10 digit glyphs, two of which land on marainkit invariants (#341 for digit 0, and indirectly #341 again conflicts with marainkit's own #0 (*nuul*) = zero/null assignment).
- marainkit treats #0 (Empty, *nuul*) as zero/null — consistent with Banks' base-8 where "empty = zero". zakalwe2040 chose Checkerboard (#341) for digit 0 instead, possibly to keep #0 as a word-space or separator distinct from a numeric zero.

---

### Design notes — numerals and notation (marainkit)

**1. #16 as decimal point is the firmest anchor.**
Banks, marainkit (geometric derivation), and zakalwe2040 all independently converge on #16 for "decimal point / period". This is the most multiply-confirmed assignment in the entire system and should be treated as fixed.

**2. Base-8 or base-10?**
Banks is unambiguous: base 8. Following him means needing 8 digit glyphs, none of which are published. An octal system would avoid the digit-3 = #121 conflict entirely (digit 3 in base 8 could be assigned to any unclaimed value). Base-10 offers broader compatibility with everyday use but contradicts the source material. Decision needed before any numeral layer is built.

**3. The Diamond/+ conflict is the most defensible zakalwe2040 choice.**
`+` = #170 (Diamond) is homoiconic: a diamond is visually a rotated plus sign. The assignment is elegant and intentional. It does, however, permanently occupy a marainkit invariant. If we want to preserve Diamond as a warning glyph *and* use `+` for addition, they cannot share the same value. One option: define `+` as a non-invariant value and keep Diamond reserved; another is to accept the dual meaning (warning and arithmetic operator, distinguished by context).

**4. The copula conflict is harder to resolve.**
*iz* (to be) = #186 (Cross = alert/stop) has no homoiconic justification. It appears to be an arbitrary assignment that happened to land on a structurally significant invariant. This is a candidate for reassignment if marainkit defines a notation layer.

**5. Brackets are entirely clean.**
None of the 8 bracket/delimiter values (#81, #276, #211, #406, #251, #446, #479, #503) conflict with marainkit invariants or Banks' claimed phonemes. The bracket system could be adopted wholesale with no conflicts — and the designs are visually coherent (open/close pairs are bit-mirror images of each other).

**6. Logic operators and equality are also largely clean.**
The and/or/not values (#284, #113, #343) and equality operators (#63, #191) don't conflict with invariants or Banks. Only *iz* (#186) is problematic. Adopting the logic and equality set minus *iz* would work cleanly.

---

## Reddit conlang (u/comradelenin456, u/ratioprosperous)[^5]

Uses Banks' glyph alphabet as its writing system but adds a full synthetic grammar. Non-canonical; widely used in the community including for tattoos.

Features: flexible word order · no tenses · six grammatical cases · fourth-person pronouns · genderless third-person pronoun. No independent glyph extensions beyond Banks' alphabet.

---

## marain-tools.netlify.app[^6]

Live tool implementing romanized Marain → glyphs → 9-bit binary. Uses a 9-bit bitmap encoding. Known example:

> *ra'yuh prenva zawen* → "I ride aboard a spaceship"
> Gloss: `p1sg+NOM spaceship+ACC ride`

Three input modes: romanized Marain · direct Marain font characters · nine-bit binary. Developers note: not all bit strings produce valid character encodings. Compound words, punctuation, and numbers not yet fully supported.

---

## tomdionysus/marain-font[^7]

TrueType implementation of Banks' glyph alphabet. No published glyph table in the repo — the font file itself is the artifact. The author sent the font to Banks via his publishers; no response on record.

---

## Open questions

- What are the remaining ~480 non-alphabetic glyph assignments? Banks specifies categories (base-8 numerals, punctuation, units, constants, elements) but not the actual mappings.
- Should the 8 marainkit invariant glyphs be treated as reserved values in any implementation?
- Is Banks' "figure 1" (the number 1) the value `#1` (`000000001`) — top-left cell only? This is the most natural reading but not stated explicitly.
- **Phoneme layer decision**: if marainkit defines a phoneme assignment set, does it follow Banks' approximate image-read values, zakalwe2040's abjad, or a new mapping? Only *ma* (#457) and *la* (#484) have cross-system agreement; *w*/#121 is the sole explicitly-stated Banks value.
- **Buffer bit**: Banks defines a 10th buffer bit after each 9-bit glyph but does not assign it meaning. Reserve as long-vowel marker? Leave undefined?
- **wa conflict**: zakalwe2040 assigns *wa* = #511 (marainkit "Full"). If marainkit adopts a phoneme layer, this must be resolved. Banks' #121 is the most defensible assignment for *wa* / *w*.
- **M2 lattice**: should the 4×5 zakalwe2040 lattice be treated as a reference design for a marainkit extended encoding layer? If so, do the phoneme assignments carry over or only the geometry?
- **Number base**: Banks says base-8; zakalwe2040 uses base-10. Which does marainkit follow? (Base-8 avoids the digit-3 = #121 conflict entirely.)
- **Brackets**: zakalwe2040's 8 bracket/delimiter glyphs have no conflicts with invariants or Banks — adopt wholesale?
- **`iz` reassignment**: zakalwe2040's copula *iz* = #186 (Cross, marainkit invariant). If a notation layer is defined, should *iz* be reassigned to a non-invariant value?
- **Diamond as `+` vs warning**: can #170 carry both meanings (addition and danger) distinguished by context, or must they be separated?

---

[^1]: Iain M. Banks, *"A Few Notes on Marain"*, published in *Scripta Manent* (date unknown). Full text at [`docs/source/a-few-notes-on-marain.md`](../../docs/source/a-few-notes-on-marain.md). Note: the *Scripta Manent* attribution appears across multiple fan sites but no publication date has been confirmed. See footnote in that document.

[^2]: marainkit project, derived geometrically from the 3×3 binary grid. See [`encoding/docs/invariant-glyphs.md`](invariant-glyphs.md). These values are a mathematical property of the grid, not a design decision — they would hold in any conforming implementation.

[^3]: zakalwe2040, *Tonal Marain: Language of the Culture*, [github.com/zakalwe2040/marain](https://github.com/zakalwe2040/marain). All Tonal Marain glyph names, phonemes, emoting glyphs, numerals, and operator definitions in this document are sourced from that repo's README. Community work — not endorsed by the Banks estate.

[^4]: Reference cited by zakalwe2040: Centre for Mathematical Cognition, Loughborough University — research on cognitive advantages of symmetric mathematical symbols. The original paper is linked in the zakalwe2040 README.

[^11]: **Base 8 counting primer.** In base 8 there are only 8 digits (0–7) — no 8 or 9. After 7, the ones column resets to 0 and the next column ticks up: 7 → 10 → 11 → ... → 17 → 20. Each column is worth 8× the column to its right (ones · eights · sixty-fours · 512s), vs 10× in decimal. So octal `10` = eight things, octal `20` = sixteen things, octal `100` = sixty-four things. The written symbols look the same as decimal but represent different quantities — in Marain there is no decimal system to cause confusion, so the notation is unambiguous.

[^5]: Reddit users u/comradelenin456 and u/ratioprosperous, via r/TheCulture and r/Marain. Non-canonical synthetic grammar built on Banks' alphabet. No independent glyph extensions.

[^6]: [marain-tools.netlify.app](https://marain-tools.netlify.app) — author unknown. Implements romanization → glyph → binary pipeline. The most complete live implementation of the phoneme-to-glyph mapping currently available.

[^7]: tomdionysus (Tom Cully), [github.com/tomdionysus/marain-font](https://github.com/tomdionysus/marain-font). TrueType font for Banks' Marain alphabet. Font sent to Banks via publishers; no response recorded.
