# CLAUDE.md — marain

A **deterministic display language** — a rendering grammar where context inputs
produce display outputs predictably and consistently.

Input: `(type, viewing, status)` → Output: tokens + layout rules + emphasis rules

Inspired by the Culture novels of Iain M. Banks.

---

## Subprojects

| Directory | Purpose |
|-----------|---------|
| [`language/`](language/) | Linguistic layer — grammar, phonemes, translations |
| [`encoding/`](encoding/CLAUDE.md) | Rosetta stone — converts language → base-9 grid (SVG/GIF) |
| [`display/`](display/CLAUDE.md)   | Adaptive display system — CSS tokens, typography, context model |

See each subproject's `CLAUDE.md` for scope, rules, and priority queue.

---

## Cross-cutting principles

- **Token-driven only.** No hardcoded values anywhere in the stack.
- **Legibility first.** Glyph disambiguation required at every layer (visual and encoded).
- **Context is explicit.** Display and behavior adapt to declared context (type / viewing / status), not guesswork.
- **States scale, don't shout.** Warn/critical must be clear but not loud in normal conditions.

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
