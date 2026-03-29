# CLAUDE.md

See also: [./docs/DESIGN_PHILOSOPHY.md](./docs/DESIGN_PHILOSOPHY.md)

## What this is

A **contextual semantic design language** — a token-driven style system where visual
presentation is determined by a structured context model, not by ad-hoc theming.

Context is defined by three axes:

| Axis        | Values                                                          |
|-------------|------------------------------------------------------------------|
| **Type**    | `document` · `hud` · `code` · `alert-surface`                  |
| **Viewing** | `daylight` · `indoor` · `low-light` · `glare-motion`           |
| **Status**  | `normal` · `attention` · `warn` · `critical`                   |

Example contexts:
- `document / daylight / normal` — reading an Obsidian note at a desk
- `hud / low-light / critical` — monitoring display in a dark room, something is wrong

**What changes across axes — and what does not:**

Only these vary: contrast · color intensity · density (spacing/size) · emphasis

Typography is **stable across all modes**. No font swapping per context.
Structural differences come from weight, size, and spacing — not typeface changes.

Long-term: add reader context axes (language/locale, situation, device) and integrate
Marain phonetic encoding as a visual/semantic layer.

**Immediate scope:** Document styles for informational web pages and Obsidian vaults.

---

## Project structure

```
marain/
├── display/        ← adaptive display system (CSS tokens, context model, fonts) ← you are here
├── encoding/       ← base-9 / binary encoding
└── docs/           ← cross-cutting specs
```

## What's built

- `themes/culture/index.html` — design reference page (document / daylight / normal)
- `themes/culture/style.css` — full token system + component styles
- CSS token system v1: `surface-*`, `text-*`, `line-*`, `accent`, `warn`, `critical`, `yes`
- Context switching via `data-mode` attribute — dark mode tokens proposed and previewed
- Fonts locked: Atkinson Hyperlegible + Intel One Mono
- State scale 1–9 visualised (prototype, colors not final)

---

## Viewing adaptation rules

**Daylight → Low-light:** reduce brightness · increase contrast slightly · avoid pure white

**Document → HUD:** compress layout · increase information density · sharpen contrast edges · reduce decorative spacing

---

## Priority queue

1. ~~Lock `document / daylight / normal` as the canonical baseline~~ — **done**
2. ~~Define context-switching mechanism~~ — **done: `data-mode` attribute on `<html>`**
3. Build `document / low-light / normal` (dark mode) — tokens proposed, not finalized
4. Build `hud / low-light / normal` as the third context target
5. Status escalation system — map base-9 index (0–8) to token set
6. `attention` state (between normal and warn) — token and component design
7. Marain encoding integration (experimental)

---

## Rules — apply to all work

- **Token-driven only.** No hardcoded color, spacing, or type values.
- **Context via CSS only.** Class switching or data attributes — no JS style injection.
- **Legibility first.** Glyph disambiguation required (Il1, O0, rn/m). Personality is irrelevant.
- **States scale, don't shout.** warn/critical must be clear but not visually loud in normal conditions.
- **Escalation = contrast + structure, not color alone.** Color signals state; contrast and layout density carry the weight.
- **Test method:** 60-second sustained reading, not first impression.

---

## Fonts (locked)

| Role        | Font                     |
|-------------|--------------------------|
| UI/Content  | Atkinson Hyperlegible    |
| Code/Tokens | Intel One Mono           |

Typography is stable across all contexts. These do not change per mode.

---

## Future axes (not yet designed)

- Reader language / locale → affects font, encoding, direction
- Situation (ambient conditions, urgency)
- Marain glyph integration for phonetic / semantic encoding
