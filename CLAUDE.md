# CLAUDE.md — marain

A Marain-inspired system for structured, legible, context-adaptive information display.
Inspired by the Culture novels of Iain M. Banks.

---

## Subprojects

| Directory | Purpose |
|-----------|---------|
| [`encoding/`](encoding/CLAUDE.md) | Binary/base-9 Marain encoder — text → SVG/GIF grid output |
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

The encoding layer (base-9 binary grid) and the display layer (CSS token system) are currently
developed independently. The long-term integration point:

- The base-9 scale maps to the status escalation system in the color/display layer
- Marain glyph output from `encoding/` could become a rendering target in `display/`
- Both share the principle: structure carries meaning, decoration does not

Cross-cutting specs live in `docs/` at this root when they span both subprojects.

---

## Fonts

Collected Marain and UI fonts live in `Fonts/` at the repo root. Not tracked in git (third-party,
unlicensed for redistribution). Reference only.
