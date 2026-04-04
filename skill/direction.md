# skill/ — Claude Skills

This directory contains Claude Code skills for this repo. Skills are markdown prompts that
activate domain expertise or project context when invoked with `/skill-name` in Claude Code.

---

## How skills work

Claude Code loads skills from `~/.claude/skills/<name>.md`. Run `./skill/install.sh` to
symlink each skill in this directory into that location. After installing, invoke with
`/marain`, `/workflow`, etc.

Skills live in the repo so they evolve with the code. The install script creates symlinks —
not copies — so edits here are picked up immediately without reinstalling.

---

## Directory convention

Each skill lives in its own subdirectory matching the slash command name:

```
skill/
└── <name>/
    └── <name>.md    ← the skill content (this is what Claude Code loads)
```

`install.sh` discovers all `<name>/<name>.md` pairs automatically.

---

## Extractability

Skills in this repo are designed to be separable. Each skill file is marked with layer
boundaries so it's clear what is project-specific versus portable domain knowledge:

- **Layer 1 — Domain activation:** General expertise, no project coupling. Portable as-is.
- **Layer 2 — Scientific standards:** Behavioral rules, no project coupling. Portable as-is.
- **Layer 3 — Project orientation:** Project-specific. Replace with a URL or stub when
  extracting to a standalone skill.

---

## Adding a new skill

1. Create `skill/<name>/`.
2. Create `skill/<name>/<name>.md` with the skill content.
3. Run `./skill/install.sh <name>` (or `./skill/install.sh` to reinstall all).
4. Add a row to the table below.

---

## Skills in this repo

| Skill | Slash command | Purpose |
|-------|--------------|---------|
| [marain](marain/marain.md) | `/marain` | Linguistic + encoding rigour for Marain language and font work |
