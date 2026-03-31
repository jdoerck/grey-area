# AI Tooling — Conventions and Decisions

## Why CLAUDE.md files exist in this repo

Claude Code (Anthropic's CLI coding tool) looks for files named exactly `CLAUDE.md` to load as project context. The filename is hardcoded — it cannot be changed via configuration. See the official documentation: [docs.anthropic.com/en/docs/claude-code/memory](https://docs.anthropic.com/en/docs/claude-code/memory)

These files are a tool-specific requirement, not a design choice.

---

## Why they contain nothing

This project's cross-cutting principles require that documentation not be bound to a specific commercial platform, tooling vendor, or naming convention that could become obsolete. Naming the authoritative direction files `CLAUDE.md` would:

- Couple the project's core guidance to a single vendor's product name
- Make those files less discoverable to any other tool, human reader, or future AI system that doesn't know what `CLAUDE.md` means
- Contradict the substrate-independence and future-proofing principles that govern all other decisions in this project

Claude Code supports an `@import` syntax that allows a `CLAUDE.md` to reference an external file. Each `CLAUDE.md` in this repo is therefore a one-line shim:

```
@direction.md
```

or for the root:

```
@docs/direction.md
```

The actual content lives in `direction.md` files named and located on the project's own terms.

---

## Direction files

| CLAUDE.md location | Imports |
|--------------------|---------|
| `CLAUDE.md` | `direction.md` |
| `display/CLAUDE.md` | `display/direction.md` |
| `display/fonts/CLAUDE.md` | `display/fonts/direction.md` |
| `language/CLAUDE.md` | `language/direction.md` |

---

## Transparency and community

The `CLAUDE.md` and `direction.md` files are committed to the repository in full and in the open. This is intentional.

The direction these files set is not owned by any individual contributor or tool vendor. Anyone reading this project — whether as a potential contributor, a community member, or a future maintainer — can see exactly what instructions are being given to AI tools working on this codebase, and why.

Changes to `direction.md` files are open for discussion. If a community grows around this project, those files are as much a community document as any other part of the spec.

> Note: `CLAUDE.md` files contain an HTML comment explaining this — but HTML comments are invisible when rendered on GitHub. This section exists to make that reasoning visible to anyone browsing the project without reading raw source.

---

## If you use a different AI tool

`direction.md` files are plain markdown. Any AI assistant, human reader, or future tool can be pointed at them directly without knowing what Claude Code is.

---

## If Claude Code changes its conventions

If Anthropic updates Claude Code to support configurable filenames or a different context mechanism, the `CLAUDE.md` shims can be removed or updated without touching any content. All project guidance stays intact in the `direction.md` files.

---

## Where this convention is enforced

The rule — "CLAUDE.md is a shim; content lives in direction.md" — is written into the root `direction.md` under **AI tooling conventions**. Any AI reading project context before doing work will receive these instructions directly, without needing to find this document first.
