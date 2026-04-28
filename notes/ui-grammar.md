# Marain UI Grammar v0.1

## Core Premise

Not a theme.  
A rendering grammar.

> Input → context (type, viewing, status)  
> Output → tokens, layout rules, emphasis

---

## 1. Axes (Input Space)

### Type
- document
- HUD
- code
- alert surface

### Viewing Conditions
- daylight
- indoor
- low light
- glare / motion

### Status
- normal
- attention
- warning
- critical

---

## 2. Rendering Rule

```
(type, viewing, status) → token set → render
```

---

## 3. What Changes (and What Doesn’t)

### Allowed to Change
- contrast
- color intensity
- spacing / density
- motion / emphasis

### Must Stay Stable
- typography family
- structural hierarchy

---

## 4. Base Layer (Document / Daylight / Normal)

Principles:
- warm surface (paper-like)
- low chroma
- soft contrast
- long-session readability

No drama.

---

## 5. State Escalation

| Level | Meaning    | Behavior |
|------|-----------|--------|
| 0–2  | Normal    | Neutral |
| 3–5  | Attention | Subtle hue shift |
| 6–7  | Warning   | Clear signal |
| 8    | Critical  | High contrast |

> Escalation = contrast + structure (not just color)

---

## 6. Viewing Adaptation

### Daylight → Low Light
- reduce brightness
- increase contrast slightly
- avoid pure white

### Document → HUD
- compress spacing
- increase density
- sharpen edges

---

## 7. Token System

All values defined as tokens:

- surface-0 / 1 / 2
- text-0 / 1 / 2
- line-0 / 1 / strong
- state-[0–8]

No hardcoded values.

---

## 8. Typography Rules

- Legibility over personality
- Avoid ambiguous glyphs (Il1, O0)
- Works across:
  - paragraphs
  - controls
  - alerts

Differences expressed via:
- size
- weight
- spacing

---

## 9. Mono Layer (Truth Channel)

Used for:
- code
- tokens
- identifiers

Requirements:
- unambiguous
- stable under transformation

Candidates:
- Intel One Mono
- IBM Plex Mono
- system fallback

---

## 10. System Goal

A display system that is:
- self-consistent
- partially self-describing
- recoverable without prior agreement

---

## Blunt Take

Most UI systems are aesthetic piles.

This is closer to:

> a deterministic display language

Risk:
- over-engineering

Reward:
- something that scales across context, device, and time

Keep it readable or it fails.
