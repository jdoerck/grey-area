# AI Tooling — Conventions and Decisions

## Direction files

Each directory in this project carries a `direction.md` — a plain markdown file containing the
governing principles, scope, and rules for that part of the project. These files are the primary
source of truth for anyone working in this codebase, whether that means a human contributor, an
AI assistant, or a future tool that doesn't exist yet.

`direction.md` files are written to be read directly, requiring no special software or knowledge
of any particular tool. Any AI assistant can be pointed at one; any human can open one in a text
editor.

| Location | Purpose |
|----------|---------|
| `direction.md` | Root-level principles, cross-cutting architecture, subproject map |
| `display/direction.md` | Display system — tokens, context model, rendering rules |
| `display/fonts/direction.md` | Font selection and rendering constraints |
| `language/direction.md` | Linguistic layer — phonemes, grammar, vocabulary |

---

## Transparency and community

`direction.md` files are committed to the repository in full and in the open. This is intentional.

The direction these files set is not owned by any individual contributor or tool vendor. Anyone
reading this project — whether as a potential contributor, a community member, or a future
maintainer — can see exactly what instructions are being given to AI tools working on this
codebase, and why.

Changes to `direction.md` files are open for discussion. If a community grows around this
project, those files are as much a community document as any other part of the spec.

---

## The `direction/` knowledge base

The `direction/` directory at the repo root is a shared knowledge base for all contributors —
human and AI alike. It exists alongside `direction.md` but serves a different purpose:

| | `direction.md` | `direction/` |
|---|---|---|
| **Contains** | Governing principles and rules | Accumulated insights, decisions, scripts |
| **Changes** | Rarely — by deliberate choice | Frequently — as work happens |
| **Written by** | Project owners | Any contributor during the course of work |
| **Audience** | Orients anyone new to the project | Helps active contributors avoid re-learning |

### Why a separate directory

`direction.md` sets the rules. `direction/` captures the reasoning and artifacts that build
up as those rules are applied. A design decision, the rationale behind a non-obvious technical
choice, a utility script that was useful once and will be useful again — these belong in
`direction/` rather than `notes/` because they are working knowledge, not finished documentation.

The distinction matters for longevity: finished docs tend to go stale because no one is sure
when they're allowed to change them. Working knowledge files are expected to evolve — they get
updated in place as understanding improves.

### `direction/scripts/`

Scripts written during development are saved here as canonical versions and updated in place
when they improve. This prevents the same utility being re-written from scratch in each session
and ensures any contributor (or AI) can reuse prior work rather than reinventing it.

See `direction/index.md` for the current inventory of notes and scripts.

---

## Adding a new subproject

If you create a new subdirectory that needs its own contributor context:

1. Create `<dir>/direction.md` with the subproject guidance.
2. Add the subproject to the table in the root `direction.md` and to the Direction files table above.
3. Point any AI tool or contributor at `<dir>/direction.md` before starting work.

---

## The design principle

Don't couple your knowledge to your tools. `direction.md` files are plain markdown — readable
by any person or tool, requiring no special software, surviving any change in the AI or editor
tooling landscape.

If a specific tool requires a context file with a particular name (a project manifest, a settings
shim, a hardcoded filename), that file should be a one-line pointer to `direction.md`, not a
place where content lives. Content lives in `direction.md`.
