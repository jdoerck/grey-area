# Marain Display System – Design Notes

> **Track:** Encoding system (primary) + Philosophical argument — early design session notes for the display system. Goal and philosophy sections are working hypotheses; current-state sections are factual. This document predates the formal track and evidence-label systems; claims are not individually labelled. See [`../../notes/tracks.md`](../../notes/tracks.md).


## Core Idea
Build a visual language inspired by Marain:
- Minimal context needed to interpret
- Structured, logical, almost “inevitable”
- Designed for clarity across time, devices, and conditions

## Goals
- Reduce cognitive load
- Maximize readability over long sessions
- Create a system that adapts to context:
  - document vs HUD
  - daylight vs low light
  - normal vs alert

## Key Concepts

### 1. Typography as Language
Fonts are not aesthetic choices—they are part of meaning.

Requirements:
- Clear distinction between similar glyphs
- Comfortable for long reading
- Neutral tone

Observation:
- Inter = familiar, safe
- Plex = structured, technical
- Atkinson = high clarity, slightly unusual but strong candidate

### 2. Mono Fonts for Truth Layers
Code / tokens represent “ground truth”
- Must be unambiguous
- Must survive compression / transformation

Candidates:
- Intel One Mono (clarity-first)
- IBM Plex Mono (balanced)

### 3. Color Philosophy
Colors should feel “natural” to human perception:
- Warm neutrals (paper-like)
- Soft contrast
- No pure white / black extremes

States:
- Green (yes / approved)
- Yellow (warning)
- Red (critical)

Future:
- Map states to base-9 scale

### 4. Token-Based Design
Everything defined as variables:
- surfaces
- text
- lines
- states

No hardcoded styling.

### 5. UI Philosophy
- Structure over decoration
- Calm default state
- Alerts scale, not shout
- Interface should disappear during use

### 6. Testing Method
- 60-second reading test
- Switch fonts mid-reading
- Evaluate fatigue, not first impression

### 7. Long-Term Direction
- Marain-like encoding system
- Self-describing interfaces
- Embedded “Rosetta” hints in UI/data
- Cross-context rendering (document → HUD)

## Current State
- Document mode prototype complete
- Font switching working
- Mono switching working
- Color system established (v1)

## Next Moves
- HUD mode
- Contrast escalation rules
- Symbol system
- Encoding experiments (QR / structured glyphs)
