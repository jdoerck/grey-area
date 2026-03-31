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

**language** → *encoding* → **glyph** → **font** → **display**

- `language/` defines the linguistic raw material: grammar, phonemes, translated content
- `encoding/` converts that material into 9-bit binary glyph indices (0–511); each index maps to a canonical 3×3 binary-grid representation — this is the **glyph**
- A **font** is a renderer: it takes a glyph index and produces visual output for a specific medium; fonts are chosen by user preference and constrained only by the resolution of the medium (PPI or equivalent)
- `display/` provides the context-adaptive visual system — the token layer, context model, and status escalation that govern how fonts render within a given context

The glyph is the stable canonical unit. It exists independently of any font or display technology — it can be rendered on screen, carved in stone, woven into fabric, or transmitted as a radio bitstream. The font is just one way to make it visible.

Integration points:
- The base-9 index maps directly to the status escalation system in the display layer:
  `0–2` neutral · `3–5` attention · `6–7` warning · `8` critical
- Both share the principle: structure carries meaning, decoration does not

Cross-cutting specs live in `docs/` at this root when they span both subprojects.

---

## Fonts

Collected Marain and UI fonts live in `Fonts/` at the repo root. Not tracked in git (third-party,
unlicensed for redistribution). Reference only.

---

## AI tooling conventions

This project uses Claude Code (and may use other AI tools in future). Any AI working in this repo must follow these conventions.

### CLAUDE.md files

Claude Code requires a file named `CLAUDE.md` to load project context. The filename is hardcoded.

**Do not put content directly in a `CLAUDE.md` file.** Instead:

1. Create a `direction.md` alongside it containing the actual guidance.
2. Make the `CLAUDE.md` a single-line import shim:
   ```
   @direction.md
   ```
   (At the repo root, the root `CLAUDE.md` imports `@direction.md` in the same directory.)

This keeps all project guidance in tool-agnostic files that any human, AI, or future tool can read without knowing what Claude Code is. See `docs/ai-tooling.md` for the full rationale.

### Adding a new subproject

If you create a new subdirectory that needs AI context:

1. Create `<dir>/direction.md` with the subproject guidance.
2. Create `<dir>/CLAUDE.md` containing only `@direction.md`.
3. Add the subproject to the table in this file and to `docs/ai-tooling.md`.
