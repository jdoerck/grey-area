# marainkit — Project Direction

A **deterministic display language** — a rendering grammar where context inputs
produce display outputs predictably and consistently.

Input: `(type, viewing, status)` → Output: tokens + layout rules + emphasis rules

Inspired by the Culture novels of Iain M. Banks.

---

## Subprojects

| Directory | Purpose |
|-----------|---------|
| [`language/`](language/) | Linguistic layer — grammar, phonemes, translations |
| [`encoding/`](encoding/) | Rosetta stone — converts language → base-9 grid (SVG/GIF) |
| [`display/`](display/)   | Adaptive display system — CSS tokens, typography, context model |

See each subproject's `direction.md` for scope, rules, and priority queue.

---

## Cross-cutting principles

- **Token-driven only.** No hardcoded values anywhere in the stack.
- **Legibility first.** Glyph disambiguation required at every layer (visual and encoded).
- **Context is explicit.** Display and behavior adapt to declared context (type / viewing / status), not guesswork.
- **States scale, don't shout.** Warn/critical must be clear but not loud in normal conditions.
- **Future-proof by default.** Every technical choice is evaluated against a 100-year horizon. Prefer open, published, stable specifications over convenient current tooling.
- **Substrate independence.** Nothing in this stack should require a specific platform, operating system, power grid, or institution to remain legible. Formats must be readable with minimal tooling — ideally with none beyond human eyes.
- **Respect for resources.** Lean storage, lean compute. No redundant data, no server dependencies where a file will do, no runtime complexity that a static format can replace. Efficiency is a design value, not an optimisation pass.

---

## How the subprojects connect

**language** → *encoding* → **display**

- `language/` defines the linguistic raw material: grammar, phonemes, translated content
- `encoding/` is the rosetta stone: converts that material into base-9 binary grid form
- `display/` renders output and provides the context-adaptive visual system

Integration points:
- The base-9 index maps directly to the status escalation system in the display layer:
  `0–2` neutral · `3–5` attention · `6–7` warning · `8` critical
- Marain glyph output from `encoding/` could become a rendering target in `display/`
- Both share the principle: structure carries meaning, decoration does not

Cross-cutting specs live in `docs/` at this root when they span both subprojects.

---

## Fonts

Collected Marain and UI fonts live in `Fonts/` at the repo root. Not tracked in git (third-party,
unlicensed for redistribution). Reference only.
