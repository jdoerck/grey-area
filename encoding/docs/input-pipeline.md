# Input Pipeline

Covers the full conversion path from source documents to plain text suitable for both the Marain encoder and LLM ingestion.

---

## Preferred input format

Plain text (`.txt`) is the target format for all encoding and LLM ingestion. Markdown syntax characters (`#`, `*`, `_`, `[`, `]`, etc.) encode literally into the binary grid and must be stripped before encoding.

---

## Conversion tools

### epub → plain text
**Tool:** Pandoc

```bash
pandoc input.epub -t plain -o output.txt
```

Reliable, no extra dependencies, handles epub well out of the box.

---

### PDF → plain text
PDF conversion is two steps: PDF → markdown, then markdown → plain text.

**Step 1: PDF → markdown**

Default to **Marker**. Fall back to **MinerU** for problem documents.

| Tool | Use when |
|------|----------|
| Marker | Clean, digitally-created PDFs — ebooks, papers, documentation. Fast, good CLI, supports `--use_llm` for tricky pages. |
| MinerU | Scanned documents, mixed scan/digital, complex multi-column layouts, or when tables and formulas need high accuracy. GPU recommended but not required. |

```bash
# Marker
marker_single input.pdf output/ --use_llm

# MinerU
mineru -p input.pdf -o output/
```

**Step 2: markdown → plain text**

```bash
pandoc input.md -t plain -o output.txt
```

This step is the same regardless of which PDF tool was used.

---

### markdown → plain text
**Tool:** Pandoc

```bash
pandoc input.md -t plain -o output.txt
```

---

## Planned: `tools/convert.js`

A unified CLI wrapper normalizing all conversion paths to plain text output:

```bash
node tools/convert.js input.epub       # epub → plain text via Pandoc
node tools/convert.js input.pdf        # PDF → plain text via Marker (default)
node tools/convert.js input.pdf --ocr  # PDF → plain text via MinerU
node tools/convert.js input.md         # markdown → plain text via Pandoc
node tools/convert.js ./library/       # batch: process entire directory
```

Output goes to `./output/` matching the encoder convention.

---

## LLM ingestion notes

- Single merged file per book is preferred for now
- Preserve chapter breaks as blank lines for semantic chunking later
- Chunking strategy to be revisited when home LLM retrieval layer is built

---

## Future

- Local LLM (via Ollama) as an alternative PDF conversion backend
- Auto-detect input format in `tools/convert.js`
- Validate plain text output before passing to encoder (warn on markdown syntax characters)