# Marain as a Four-Layer System

> **Evidence labels used in this document:**
> `[canonical]` — directly from Banks source text ·
> `[inference]` — consistent with canon, not explicitly stated ·
> `[project decision]` — deliberate choice where canon is silent ·
> `[speculative]` — interesting hypothesis, not yet tested
>
> *See [evidence-labels.md](evidence-labels.md) for full definitions.*

---

## The Native Medium: Tightbeam Laser

The most important reframing: **[inference]** Marain was designed for transmission, not inscription.

The source supports: binary encoding mattered to Banks; tightbeam transmission is canonical; the buffer bit and extended packet structure imply a transmission-oriented design. What the source does not explicitly state: that the written script is a rendering of a transmission-first signal, or that inscription is secondary.

**[canonical]** A tightbeam laser carries a binary bitstream across interstellar space. **[inference]** The 3×3 glyph system is what you get when you *render* that bitstream for human eyes — the script is downstream of the signal. This is a project interpretation, consistent with canon but not directly stated.

This interpretation implies:
- **[canonical]** Binary encoding is the substrate — not a simplification
- **[inference]** Human-readable glyphs are essentially a **debug view** of the transmission
- **[project decision]** GCU Grey Area is correctly understood as a **renderer**, not a writing system
- **[inference]** Tone and emotional content baked into the bitstream means affect is **propositional**, not performative

---

## Layer Model

```
┌─────────────────────────────────────────────────────┐
│  LAYER 4 — TRANSMISSION PROTOCOL                    │
│  Tightbeam laser · Bitstream · Parity/error check   │
│  Rotation redundancy · Encryption tier · Bandwidth  │
├─────────────────────────────────────────────────────┤
│  LAYER 3 — DATA ENCODING STANDARD                   │
│  9-bit glyph unit · 512 states · Tone as data bits  │
│  Spatial grouping · No privileged direction         │
├─────────────────────────────────────────────────────┤
│  LAYER 2 — CONSTRUCTED LANGUAGE (CONLANG)           │
│  Phoneme set · Abjad structure · Gender-neutral     │
│  pronouns · Non-hierarchical grammar · 5 tones      │
├─────────────────────────────────────────────────────┤
│  LAYER 1 — VISUAL SCRIPT (GLYPH RENDERER)           │
│  3×3 binary grid · Rotation-invariant glyphs        │
│  Macro 3×3 layout · SVG/GIF output                  │
│  ← GCU Grey Area currently lives here               │
└─────────────────────────────────────────────────────┘
         ↓ all layers produce the same bitstream ↓
```

**Key insight:** Tone and emotional meaning live simultaneously in Layer 2 (conlang) and Layer 3 (encoding). They are not a separate channel — affect is in the signal itself.

---

## Subproject Mapping

| Layer | Subproject | Notes |
|-------|-----------|-------|
| Layer 4 | (out of scope) | Transmission protocol — not implemented |
| Layer 3 | `encoding/` | Current core: UTF-8 → binary → SVG grid |
| Layer 2 | `language/` | Phoneme composition, tonal encoding (Column B) |
| Layer 1 | `encoding/` + `display/` | Glyph rendering + adaptive display |

**Column A** of the tool (UTF-8 → binary → glyphs) operates in Layer 1.
**Column B** (Marain phoneme composition with tonal encoding) would pull in Layer 2.

The gap no one has filled: a tool that lets you compose in Marain phonemes *and* see the exact bits being generated — a bridge between Layer 2 and Layer 3. That is the long-term goal of this project.

---

## Project Scope

GCU Grey Area is a **renderer** — a way of visualising what a tightbeam signal looks like when laid out spatially. Column A encodes arbitrary UTF-8 text. Column B will compose in Marain phonemes with tonal encoding. Both produce the same binary output format.

The tool sits at the intersection of conlang, data encoding standard, visual script, and transmission protocol.
