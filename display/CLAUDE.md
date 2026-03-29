# CLAUDE.md

See also: [./docs/DESIGN_PHILOSOPHY.md](./docs/DESIGN_PHILOSOPHY.md)

## What this is

A **contextual semantic design language** — a token-driven style system where visual
presentation is determined by a structured context model, not by ad-hoc theming.

Context is defined by three axes:

| Axis      | Values (examples)                        |
|-----------|------------------------------------------|
| **Type**     | `document` · `hud`                    |
| **Viewing**  | `internal-daylight` · `low-light`     |
| **Status**   | `normal` · `warn` · `critical`        |

Example contexts:
- `document / internal-daylight / normal` — reading an Obsidian note at a desk
- `hud / low-light / high-alert` — monitoring display in a dark room, something is wrong

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

- `culture/index.html` — font evaluation prototype (document / daylight / normal baseline)
- CSS token system v1: `surface-*`, `text-*`, `line-*`, `accent`, `warn`, `critical`, `yes`
- Font switching: Inter / IBM Plex Sans / Atkinson Hyperlegible
- Mono switching: Intel One Mono / IBM Plex Mono / system fallback
- Webfont status detection

No font is locked yet. Document mode is working but not finalized.

---

## Priority queue

1. Lock `document / internal-daylight / normal` as the canonical baseline context
2. Define the context-switching mechanism (CSS class vs. data attribute — TBD)
3. Build `hud / low-light / normal` as the second context target
4. Status escalation system (base-9 concept — see DESIGN_PHILOSOPHY.md)
5. Marain encoding integration (experimental)

---

## Rules — apply to all work

- **Token-driven only.** No hardcoded color, spacing, or type values.
- **Context via CSS only.** Class switching or data attributes — no JS style injection.
- **Legibility first.** Glyph disambiguation required (Il1, O0, rn/m). Personality is irrelevant.
- **States scale, don't shout.** warn/critical must be clear but not visually loud in normal conditions.
- **Test method:** 60-second sustained reading, not first impression.

---

## Font candidates (not locked)

| Role        | Candidates                                         |
|-------------|-----------------------------------------------------|
| UI/Content  | Inter · IBM Plex Sans · Atkinson Hyperlegible       |
| Code/Tokens | Intel One Mono · IBM Plex Mono · system mono        |

---

## Future axes (not yet designed)

- Reader language / locale → affects font, encoding, direction
- Situation (ambient conditions, urgency)
- Marain glyph integration for phonetic / semantic encoding
