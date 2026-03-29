# Decisions

Running log of architectural and workflow decisions for the grey-area project.

---

## 2025-03-29

### Text input format
**Decision:** Plain text (`.txt`) is the preferred input format for both the Marain encoder and LLM ingestion.

**Rationale:** Markdown syntax characters (`#`, `*`, `_`, etc.) encode literally into the binary grid, producing noise. Plain text avoids a stripping step and works cleanly for both use cases.

**Implementation:** Use Pandoc for epub and markdown conversion:
```bash
pandoc input.epub -t plain -o output.txt
pandoc input.md -t plain -o output.txt
```

---

### epub conversion tool
**Decision:** Pandoc for epub → plain text.

**Rationale:** Reliable, no extra dependencies, handles epub well out of the box.

---

### PDF conversion tools
**Decision:** Marker as default, MinerU as fallback for problem documents.

**Rationale:** PDF has no guaranteed semantic structure so no single tool wins every case.

| Tool | Use when |
|------|----------|
| Marker | Clean, digitally-created PDFs. Fast, good CLI, `--use_llm` option for tricky pages. |
| MinerU | Scanned documents, complex multi-column layouts, tables and formulas need high accuracy. GPU recommended. |

Both output markdown; strip to plain text via Pandoc as a second step regardless of which tool was used. See `docs/input-pipeline.md` for full detail.

---

### epub converter placement
**Decision:** epub-to-plaintext conversion script will live in `tools/convert.js`, not `src/`.

**Rationale:** `src/` is reserved for encoder logic. `tools/` is a better home for pipeline utilities that are adjacent to the project but not part of the core encoding system.

---

### Claude toolchain workflow
**Decision:** Use Claude chat + Claude Code as the primary development environment. Skip Cowork for now.

**Rationale:** As a developer, Claude Code provides a superset of Cowork's capabilities. Cowork adds value for scheduled/async file tasks and non-developer users, but Claude Code handles everything needed here.

**Workflow:**
```
Claude chat (explore + decide) → docs/*.md (capture) → Claude Code (execute)
```

Decisions made in chat should be committed to `docs/` before closing the session. The repo is the source of truth, not chat history.

---

### CLAUDE.md as Code entry point
**Decision:** `CLAUDE.md` in the repo root is the primary context file for Claude Code sessions.

**Rationale:** Claude Code reads this file automatically. It should contain architecture, conventions, pipeline notes, and links to `docs/` specs — enough for Code to work without re-explanation each session.

---

### Persistent memory (deferred)
**Decision:** Defer building a persistent memory system for the home LLM until the LLM itself is further along.

**Rationale:** This is a meaningful project in its own right — essentially a RAG system over conversation history. Claude chat's built-in memory covers the need for now. Revisit once the local LLM and Claude API connection are established.