# language/ — Direction

Please read the root [`direction.md`](../direction.md) first.

The linguistic layer: grammar, phonemes, translations, and canonical Marain properties.

---

## What Marain Is

Marain is the constructed language of the Culture — **engineered rather than evolved**. The Culture's hyperintelligent AI Minds designed it from scratch to exploit the Sapir-Whorf hypothesis: that language shapes society.

**Canonical properties:**
- Written in a **3×3 matrix** of binary cells (each filled or empty) — 9 bits, 512 possible glyphs
- Glyphs are designed to be **readable in any orientation** — no privileged direction
- Contains a **single gender-neutral third-person pronoun**
- Structured to reduce ambiguity and encode Culture values: egalitarian, non-hierarchical, non-dominant
- Used galaxy-wide as a de facto *lingua franca*

**Canonical source:** Banks' essay *"A Few Notes on Marain"* — describes glyphs, pronunciation, data transmission.

---

## Encryption Tiers

| Tier | Description |
|------|-------------|
| **M1** | Basic nonary Marain, 3×3 grid. All Culture citizens can read this. |
| **M8–M16** | Encrypted variants used by Contact Section. |
| **M32** | Special Circumstances only — highest encryption. |

> This project operates entirely at M1.

---

## Community Prior Art

**Reddit conlang** (u/comradelenin456, u/ratioprosperous): synthetic language built on Banks' alphabet. Flexible word order, no tenses, six grammatical cases, fourth-person pronouns, genderless third-person. Non-canonical but community-adopted.

**Tonal Marain** ([zakalwe2040/marain](https://github.com/zakalwe2040/marain)): adds five emotional tones (Mandarin-derived), 24-character abjad, 4×5 dot lattice divided into diacritic channels + 3×3 [slate](../notes/glossary.md#slate). Most relevant prior art for a phoneme composition layer (Column B). Claims to support both graphemes and logograms.

**marain-tools.netlify.app**: live tool mapping English phonemes to Marain glyphs. Reference for authentic phonemic approach. Supports three input modes: romanized Marain, direct Marain font input, and nine-bit binary.

**Marain Font** ([tomdionysus/marain-font](https://github.com/tomdionysus/marain-font)): TrueType font for the Marain language. Author sent it to Banks via his publishers.

### Why Hindu and Chinese visual influences dominate community interpretations

- **Chinese:** Structural — tonal system, logographic compression, contained character-as-unit. zakalwe2040 makes this explicit with Mandarin tone names.
- **Hindu/Sanskrit:** Philosophical — ternary triadic thinking maps onto Hindu cosmology; Sanskrit's prestige as a "designed" sacred language with systematic phonology mirrors how Banks frames Marain.
- **The real driver:** Banks' committed anti-Eurocentrism. A utopian civilisation that *designed* its language would draw on non-Western knowledge traditions. The community correctly reads this signal.

#### Cautionary mirror: Esperanto

Esperanto is the most-cited modern attempt at a "neutral" auxiliary language, and the most-cited reason it has stayed marginal — outside the geopolitics — is that it is not neutral. Modern typological scoring puts Esperanto at roughly 75% feature-overlap with European languages and 54% with the world's average language. Its phoneme inventory (/x/, /ʒ/, /ts/, the diphthong /eu̯/) and its lexicon (Romance + Germanic + a little Slavic) make it markedly easier for a Spanish speaker than for a Mandarin speaker. Zamenhof was not negligent; he could only draw on the languages he knew. The lesson for marainkit is structural, not moral: *if you do not deliberately resist the gravitational pull of the designer's source languages, you will reproduce them.* Phoneme set design (`phonemes/`), grammar choices, and any vocabulary work need an explicit anti-default — non-Indo-European phonemic features, non-SVO-default grammar options, vocabulary roots that are not transparently European. The community's instinct to lean on CJK and Sanskrit-adjacent influences is the right defence; it should be a documented requirement, not a stylistic preference. See [`../direction/esperanto-and-hangul.md`](../direction/esperanto-and-hangul.md) §"Esperanto: design choices" and §"Lessons for marain" for the full argument.

---

## Subproject Structure

```
language/
├── phonemes/       ← phoneme set definitions
├── translations/   ← translated content
└── raw/            ← source material
```

---

## Priority Queue

1. Phoneme set definition (abjad structure)
2. Grammar rules (word order, cases, pronouns)
3. Tonal encoding spec (bridge to encoding/ layer)

**Column B (phoneme picker UI) is a research track, not active backlog.** It depends on all three items above, plus: phoneme inventory authority, glyph assignment policy, tone encoding, register semantics, and vocabulary provenance. None of these are resolved. Keep the ideas — they are worth exploring — but treat Column B as a direction the project is working *toward*, not a task that's close to buildable. See [`notes/tracks.md`](../notes/tracks.md).
