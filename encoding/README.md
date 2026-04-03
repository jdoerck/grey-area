# encoding/

Encoding spec for marainkit — defines the glyph space, binary structure, and decision backlog for the Marain writing system.

The canonical unit is a **9-bit slate**: a 3×3 binary grid with 512 possible states. Each state is a glyph. The full 16-bit word wraps the slate in upper and lower channels that carry context.

> **Status:** Active spec. Glyph catalogue and invariant vocabulary are settled. Phoneme assignment, number base, and channel semantics are open decisions.

---

## Key documents

| Document | Contents |
|----------|----------|
| [`docs/glyphs.md`](docs/glyphs.md) | Full glyph catalogue — canonical (Banks), community, and marainkit-derived values |
| [`docs/channels.md`](docs/channels.md) | 16-bit word structure: slate + upper/lower channels |
| [`docs/invariant-glyphs.md`](docs/invariant-glyphs.md) | The 8 rotation/mirror-invariant glyphs and their vocabularies |
| [`docs/layout.md`](docs/layout.md) | Linear vs. macro 3×3 vs. radial layout options |
| [`docs/roadmap.md`](docs/roadmap.md) | Decision backlog — what must be decided before building |
| [`docs/glyph-decisions.md`](docs/glyph-decisions.md) | Glyph assignment comparison across Banks, zakalwe2040, and marainkit |
| [`docs/glyph-index.md`](docs/glyph-index.md) | Glyph index |

---

## Structure

```
encoding/
└── docs/
    ├── glyphs.md
    ├── channels.md
    ├── invariant-glyphs.md
    ├── layout.md
    ├── roadmap.md
    ├── glyph-decisions.md
    └── glyph-index.md
```
