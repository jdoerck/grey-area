# Roadmap

High-level direction and planned work for the grey-area project.

---

## Current state

- Core Marain encoder working: text → UTF-8 binary → SVG grid
- CLI and web UI functional
- SVG and GIF export supported

---

## Near term

### `tools/convert.js` — unified input conversion
- epub → plain text via Pandoc
- PDF → plain text via Marker (default) or MinerU (`--ocr` flag)
- markdown → plain text via Pandoc
- Batch mode for entire directories
- Output clean `.txt` files to `./output/`
- See `docs/input-pipeline.md` for full spec

### Input pipeline cleanup
- Validate that input is plain text before encoding
- Warn or auto-convert if markdown syntax characters are detected

---

## Medium term

### LLM ingestion pipeline
- Batch convert epub library to plain text
- Structure output for chunking (preserve chapter breaks as semantic boundaries)
- Target: feed into home LLM and Claude

### Claude API integration (home LLM)
- Connect local LLM to Claude API
- Persistent memory system — conversation history → RAG retrieval
- This is a significant project in its own right; treat as a separate workstream

---

## Open questions

- Should `tools/convert.js` be callable from the web UI, or CLI only?
- Chapter-per-file vs single merged file for LLM ingestion — decide when home LLM chunking strategy is clearer
- Tonal Marain (`zakalwe2040/marain`) — worth exploring as an extension to the encoder?