# display/

Adaptive display system for marainkit — a token-driven style system where visual presentation is determined by a structured context model, not ad-hoc theming.

---

## Context model

Three axes define every display state:

| Axis | Values |
|------|--------|
| **Type** | `document` · `hud` · `code` · `alert-surface` |
| **Viewing** | `daylight` · `indoor` · `low-light` · `glare-motion` |
| **Status** | `normal` · `attention` · `warn` · `critical` |

Context is declared via `data-mode` attribute on `<html>`. No JS style injection — CSS only.

Example contexts:
- `document / daylight / normal` — reading an Obsidian note at a desk ← **baseline, built**
- `document / low-light / normal` — dark mode ← tokens proposed, not finalized
- `hud / low-light / normal` — monitoring display in a dark room ← not yet built

---

## What's built

- `themes/culture/style.css` — full token system + component styles
- `themes/culture/index.html` — design reference page (document / daylight / normal)
- CSS token system v1: `surface-*`, `text-*`, `line-*`, `accent`, `warn`, `critical`, `yes`
- Dark mode token set proposed (`[data-mode="dark"]`) — candidates, not finalized
- State scale 1–9 visualised (prototype, colors not final)
- Components: buttons, badges, notices, forms, tables, breadcrumbs, code blocks, sidebar

---

## Design principles

- **Token-driven only.** No hardcoded color, spacing, or type values in components.
- **Context via CSS only.** `data-mode` attribute — no JS style injection.
- **Legibility first.** Glyph disambiguation required (`Il1`, `O0`, `rn/m`). Personality is irrelevant.
- **States scale, don't shout.** `warn`/`critical` must be clear but not loud in normal conditions.
- **Escalation = contrast + structure, not color alone.** Color signals state; contrast and layout density carry the weight.
- **Test method:** 60-second sustained reading, not first impression.
- **Structure over decoration.** The interface should disappear during use.

---

## Color tokens

### Light mode — `document / daylight / normal`

Warm neutral palette. Paper-like surfaces, no pure white or black.

**Surfaces**
| Token | Value | Notes |
|-------|-------|-------|
| `--surface-0` | `hsl(42 24% 95%)` | Page background — warm off-white |
| `--surface-1` | `hsl(42 18% 92%)` | Card / panel |
| `--surface-2` | `hsl(42 14% 88%)` | Raised element |
| `--surface-inset` | `hsl(42 16% 90%)` | Code block, inset area |

**Text**
| Token | Value | Notes |
|-------|-------|-------|
| `--text-0` | `hsl(30 12% 18%)` | Primary — deep warm brown |
| `--text-1` | `hsl(30  9% 33%)` | Secondary |
| `--text-2` | `hsl(30  7% 48%)` | Muted — captions, labels |

**Lines**
| Token | Value | Notes |
|-------|-------|-------|
| `--line-0` | `hsl(38 12% 82%)` | Subtle divider |
| `--line-1` | `hsl(38 12% 72%)` | Standard border |
| `--line-strong` | `hsl(38 10% 58%)` | Emphasis border |

**Interactive**
| Token | Value | Notes |
|-------|-------|-------|
| `--focus` | `hsl(210 52% 42%)` | Focus ring |
| `--accent` | `hsl(210 42% 40%)` | Links, primary actions — muted blue |

**States**
| Token | Value | Notes |
|-------|-------|-------|
| `--warn` | `hsl( 39 58% 48%)` | Amber — attention/warning |
| `--critical` | `hsl(  5 63% 36%)` | Dark red — critical |
| `--yes` | `hsl(126 32% 31%)` | Forest green — confirmed/approved |

---

### Dark mode — `document / low-light / normal` *(proposed)*

Warm dark — earth-aligned, not cold/blue. These are candidates, not final. Test against HUD targets before finalizing.

**Surfaces**
| Token | Value |
|-------|-------|
| `--surface-0` | `hsl(30  6% 11%)` |
| `--surface-1` | `hsl(30  6% 14%)` |
| `--surface-2` | `hsl(30  5% 18%)` |
| `--surface-inset` | `hsl(30  8%  9%)` |

**Text**
| Token | Value |
|-------|-------|
| `--text-0` | `hsl(40 14% 86%)` |
| `--text-1` | `hsl(40 10% 66%)` |
| `--text-2` | `hsl(40  8% 46%)` |

**Lines**
| Token | Value |
|-------|-------|
| `--line-0` | `hsl(36  8% 20%)` |
| `--line-1` | `hsl(36  8% 26%)` |
| `--line-strong` | `hsl(36  8% 36%)` |

**Interactive & states**
| Token | Value |
|-------|-------|
| `--focus` | `hsl(210 58% 65%)` |
| `--accent` | `hsl(210 50% 62%)` |
| `--warn` | `hsl( 39 62% 60%)` |
| `--critical` | `hsl(  5 60% 58%)` |
| `--yes` | `hsl(126 35% 48%)` |

---

### Syntax highlighting *(hardcoded HSL — not yet tokenized)*

| Role | Value | Notes |
|------|-------|-------|
| Strings | `hsl(126 28% 34%)` | Warm green, near `--yes` |
| Numbers | `hsl( 39 50% 40%)` | Warm amber |
| Keywords | `var(--accent)` | |
| Property / tag | `hsl(210 38% 38%)` | Muted accent |
| Selector / attr | `hsl(195 38% 36%)` | Teal |
| Function | `hsl(200 42% 38%)` | |
| Regex | `hsl(  5 52% 40%)` | Muted critical |
| Comments | `var(--text-2)` | Italic |
| Punctuation | `var(--text-2)` | |

> TODO: add `[data-mode="dark"]` overrides for non-token values when dark mode is finalized.

---

## Typography

Stable across all contexts — no font swapping per mode.

| Role | Font | Rationale |
|------|------|-----------|
| UI / content | **Atkinson Hyperlegible** | High clarity, strong glyph disambiguation |
| Code / tokens | **Intel One Mono** | Clarity-first, unambiguous at small sizes |

Line height: `1.68` body · `1.6` code · `1.15` headings
Measure: `74ch` max line length

---

## State escalation (base-9)

The display layer maps to the same base-9 index as the encoding layer:

| Range | State | Token |
|-------|-------|-------|
| 0–2 | Normal | `--text-*` / `--surface-*` |
| 3–5 | Attention | `--accent` (proposed) |
| 6–7 | Warning | `--warn` |
| 8 | Critical | `--critical` |

Mapping to invariant glyphs (`encoding/docs/invariant-glyphs.md`) is proposed, not finalized.

---

## Fonts — custom Marain script

A programmatically-compiled Marain glyph font is planned. Each glyph is a 3×3 binary grid — defined as data, compiled to `.ttf`/`.otf` via fonttools + ufoLib2.

**Build pipeline (planned):**
```
cell patterns → build.py → .ufo source → .ttf / .otf
```

Unicode mapping: Private Use Area (PUA) `U+E000` onwards — standard approach for custom scripts.

See `fonts/CLAUDE.md` for full spec and open decisions.

---

## Priority queue

1. ~~Lock `document / daylight / normal` as baseline~~ — **done**
2. ~~Define context-switching mechanism~~ — **done: `data-mode` attribute**
3. Finalize `document / low-light / normal` dark mode tokens
4. Build `hud / low-light / normal`
5. Finalize state escalation — map base-9 index to token set
6. Design `attention` state (levels 3–5)
7. Tokenize syntax highlighting colors
8. Write `fonts/build.py` — compile Marain glyph font
9. Marain glyph integration (experimental)

---

## Structure

```
display/
├── themes/
│   └── culture/
│       ├── style.css     ← token system + all components
│       └── index.html    ← design reference page
├── fonts/
│   ├── CLAUDE.md         ← font build spec
│   ├── build.py          ← compiler (planned)
│   └── examples/         ← reference fonts (gitignored)
└── docs/
    └── DESIGN_PHILOSOPHY.md
```
