# language/

Linguistic layer for marainkit — phoneme set, grammar, and translated content.

Marain is a **constructed language engineered by the Culture's Minds** to exploit the Sapir-Whorf hypothesis: language shapes society. It is egalitarian, non-hierarchical, and non-dominant by design.

> **Status:** Early spec. Canonical properties are documented. Phoneme set, grammar rules, and tonal encoding are not yet defined.

---

## Canonical properties

- Written in a **3×3 matrix** of cells (ternary / base-9)
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
| [`phonemes/`](phonemes/) | Phoneme set definitions *(not yet written)* |
| [`translations/`](translations/) | Translated content *(not yet written)* |

---

## Priority queue

1. Phoneme set definition (abjad structure)
2. Grammar rules (word order, cases, pronouns)
3. Tonal encoding spec (bridge to `encoding/` layer)
4. Column B: phoneme picker UI feeding into binary output

---

## Structure

```
language/
├── phonemes/       ← phoneme set definitions
└── translations/   ← translated content
```
