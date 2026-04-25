# language/

Linguistic layer for marainkit — phoneme set, grammar, and translated content.

Marain is a **constructed language engineered by the Culture's Minds** to exploit the Sapir-Whorf hypothesis: language shapes society. It is egalitarian, non-hierarchical, and non-dominant by design.

> **Status:** Early spec. Canonical properties are documented. Phoneme set, grammar rules, and tonal encoding are not yet defined.

---

## Canonical properties

- Written in a **3×3 matrix** of binary cells (each filled or empty) — 9 bits, 512 possible glyphs
- Glyphs are **readable in any orientation** — no privileged direction
- Single **gender-neutral third-person pronoun**
- Structured to reduce ambiguity and encode Culture values
- Used galaxy-wide as a de facto *lingua franca*

This project operates entirely at **M1** (basic nonary Marain, readable by all Culture citizens).

---

## Key documents

| Document | Contents |
|----------|----------|
| [`direction.md`](direction.md) | Full subproject direction — prior art, encryption tiers, priority queue |
| [`docs/vocabulary.md`](docs/vocabulary.md) | 430-word community vocabulary (Marain Tools) — format notes and DB import |
| [`vocabulary/vocabulary.tsv`](vocabulary/vocabulary.tsv) | Vocabulary data in TSV — canonical format for database import |
| [`docs/sanskrit-marain-dictionary-research.md`](docs/sanskrit-marain-dictionary-research.md) | Deep research: Sanskrit as donor language — consciousness terms, Navarasa, structural vocabulary, proposed Sanskrit names for invariant glyphs |
| [`phonemes/alphabet.md`](phonemes/alphabet.md) | 32-letter phoneme inventory with IPA and Marain lexorder |
| [`translations/sentences.md`](translations/sentences.md) | Example sentences with word-by-word and idiomatic glosses |

---

## Priority queue

1. Phoneme set definition (abjad structure)
2. Grammar rules (word order, cases, pronouns)
3. Tonal encoding spec (bridge to `encoding/` layer)

**Column B (phoneme picker UI) is a research track, not active backlog.** It depends on all three items above, plus several unsettled upstream questions: phoneme inventory authority, glyph assignment policy, tone encoding, register semantics, and vocabulary provenance. It is worth pursuing but is not close to actionable. See [`notes/tracks.md`](../notes/tracks.md).

---

## Structure

```
language/
├── docs/
│   ├── vocabulary.md                   ← vocabulary description + format notes
│   └── sanskrit-marain-dictionary-research.md  ← Sanskrit donor language research
├── vocabulary/
│   └── vocabulary.tsv                  ← 430-word community vocabulary (TSV)
├── phonemes/                           ← phoneme set definitions
│   ├── alphabet.md                     ← 32-letter inventory in Marain lexorder
│   └── alphabet.tsv                    ← machine-readable
├── translations/
│   └── sentences.md                    ← example sentences with glosses
└── raw/                                ← JS source files from Marain Tools
```
