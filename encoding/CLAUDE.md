# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**grey-area** converts text into a Marain-style binary SVG (from Iain M. Banks' Culture series). Text is UTF-8 encoded to binary, then rendered as a grid of black (1) and white (0) squares. Output can be exported as SVG or GIF.

Originally based on [binary2marain](https://github.com/turfptax/binary2marain).

## Running

**CLI:**
```bash
node src/cli.js "Some text"       # inline text
node src/cli.js path/to/file.txt  # from file
node src/cli.js                   # interactive prompt
```
Output SVGs go to `./output/`.

**Web (requires a local server for ES module imports):**
```bash
npm run serve   # serves at http://localhost:3000 — open web/index.html
```

## Architecture

```
src/core.js    ← shared logic (no I/O); imported by both CLI and web page
src/cli.js     ← Node.js entry point
src/gif.js     ← GIF encoder + SVG-to-GIF canvas renderer
web/index.html ← browser UI; imports ../src/core.js and ../src/gif.js
output/        ← generated files (gitignored)
docs/          ← specs and architecture decisions
```

**`core.js` exports:**
- `buildSvg(text)` — full pipeline: returns SVG string from plain text
- `textToBinary(text)` — converts text to a binary string via UTF-8 encoding

**Layout constants in `core.js`:** `BYTE_ROWS`, `BYTE_SIZE`, `BYTE_LENGTH`, `WORD_CONSTANT` control the grid geometry. The binary string is padded to a multiple of 9, then each 9-bit window is rendered as a 3×3 block of `<rect>` elements.

## Conventions

- Shared logic goes in `src/core.js` — no I/O
- CLI entry point is `src/cli.js`
- Output files go to `./output/` (gitignored)
- Specs and architecture decisions live in `docs/` — check there for task context before making structural changes
- Use ES modules throughout (`import`/`export`), not CommonJS

## Text Input Pipeline

Plain text (`.txt`) is the preferred input format for both the Marain encoder and LLM ingestion. Markdown syntax characters (`#`, `*`, `_`, `[`, `]`, etc.) encode literally into the binary grid and must be stripped before encoding.

See `docs/input-pipeline.md` for full conversion spec and tool usage.

**Quick reference:**
```bash
# epub → plain text
pandoc input.epub -t plain -o output.txt

# PDF → plain text (Marker default, MinerU for scanned/complex)
marker_single input.pdf output/ --use_llm
pandoc output.md -t plain -o output.txt

# markdown → plain text
pandoc input.md -t plain -o output.txt

# unified wrapper (planned)
node tools/convert.js input.epub
node tools/convert.js input.pdf
node tools/convert.js input.pdf --ocr
node tools/convert.js ./library/
```

## Planned Features

- epub-to-plaintext conversion script (`tools/convert.js`)
- Batch processing for multiple input files
- LLM ingestion pipeline (home LLM, Claude)

## Design Support

[Marain Font](https://github.com/tomdionysus/marain-font)
A TrueType font for the Marain language as described in the Culture novels. The author actually sent the font to Banks via his publishers.

[Tonal Marain](https://github.com/zakalwe2040/marain)
A significantly extended version that adds a channel for emotional content through five tones, drawing partial origin from Mandarin Chinese. Uses a 4×5 grid lattice divided into four areas: upper diacritic channel, lower diacritic channel, tonal channel, and the core 3×3 slate. Claims to support both graphemes and logograms, making it a universal script.

[Marain Tools](https://marain-tools.netlify.app/)
A linguistically-grounded Marain conlang toolkit with three main features:

1. Romanization → Glyphs + English gloss
You type romanized Marain (e.g. rAyu prenva zawen) and it renders the actual Marain glyphs alongside an English grammatical gloss (p1sg+NOM spaceship+ACC ride → "I am riding aboard a spaceship"). The glossing annotates grammatical case on nouns and pronouns, and links words to dictionary entries. It's explicitly noted as incomplete — compound words, punctuation, and numbers don't gloss correctly yet.
2. Three input modes
Romanized Marain text (with digits 0–7 and some punctuation)
Direct input using the Marain font characters
Nine-bit binary representation (the raw ternary encoding) — though it notes most bit strings aren't valid character encodings