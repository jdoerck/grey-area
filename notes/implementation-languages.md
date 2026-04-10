# Implementation Language Decisions

*Decided April 2026*

## Canonical stack

| Layer | Format/Language | Rationale |
|-------|----------------|-----------|
| Data | JSON + plain text (UTF-8, TSV/CSV) | Most future-proof format; readable with no software; universal support |
| Reference implementation | Python | Dominant in tooling and scientific computing; widely available; open |
| Web/interactive | HTML + JavaScript (vanilla) | Universal; runs anywhere with a browser; no compilation step |
| Graphics | SVG | Already in use; open spec; stable; renderable without software |

**Rule:** Define data in JSON first. Python and JS are consumers of it. Every other implementation can be derived from those two.

---

## Evaluation notes

### Strong candidates (may add later)
- **Lua** — small, embeddable, used in editors (Neovim), games, embedded systems; very portable
- **C** — runs on everything, forever; a Marain renderer in C would be the most substrate-independent option possible

### Excluded
| Language | Reason |
|----------|--------|
| Swift / Kotlin | Platform-locked |
| TypeScript | Adds a compilation step; ages faster than JS |
| Rust | Excellent but toolchain-heavy for a 100-year horizon |
| Electron / React Native | Framework-dependent; high churn |

---

## Governing principle

This stack is evaluated against the project's 100-year horizon and substrate-independence principle. The key mapping file is a plain data format first — implementations are just consumers of it.

Prefer open, published, stable specifications over convenient current tooling.
