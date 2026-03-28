# text2marain

Convert text into a Marain-style binary SVG. Each character is UTF-8 encoded to binary, then rendered as a grid of black (1) and white (0) squares. Output can be exported as SVG or GIF.

Based on [binary2marain](https://github.com/turfptax/binary2marain).


## Background

Marain is the constructed language of the Culture, the post-scarcity civilization at the center of Iain M. Banks' Culture novels. Banks didn't develop it in exhaustive detail the way Tolkien built Elvish, but he laid out enough of its structure and philosophy to make it feel coherent and intentional.

Marain is described as a language that was deliberately designed — engineered from the ground up rather than evolved organically. The Culture, being a civilization of near-godlike Minds and hyper-rational values, created a language optimized for precision, clarity, and expressiveness rather than inheriting one through historical accident.

Marain is written in a base-9 (ternary) grid system — a 3×3 matrix of cells, each of which can be in one of three states. This gives it a very geometric, almost digital quality. The script is designed to be writable in multiple orientations and directions, which suits a civilization where people might be in all sorts of physical configurations (zero-g, different body orientations, etc.).

Marain has a single gender-neutral third-person pronoun, which Banks used in the novels when referring to Culture people whose gender (or current gender — Culture citizens can change sex) wasn't specified. It gets transliterated roughly as something like "xe" in the English text.

Banks implied that Marain was shaped to reduce ambiguity and to subtly encode Culture values — egalitarian, non-hierarchical, not structured around dominance or status the way many natural languages are.

---

## Web app

Requires a local server for ES module imports:

```bash
npm run serve
```

Then open `http://localhost:3000/web/index.html`.

- Paste text or upload a `.txt` or `.md` file
- Click **Generate** to render the Marain grid
- Download as **SVG** (vector) or **GIF** (lossless raster)

---

## CLI

```bash
node src/cli.js "Some text to encode"  # inline text
node src/cli.js path/to/file.txt       # from file
node src/cli.js                        # interactive prompt
```

Output files are written to `./output/`.

---

## Python (reference)

The original Python implementation is preserved in `python/`:

```bash
cd python
pip install -e .
binary2marain "Some text"
```

---

## Project structure

```
src/
  core.js     — shared logic: text → binary → SVG
  gif.js      — GIF encoder + SVG-to-GIF canvas renderer
  cli.js      — Node.js CLI entry point
web/
  index.html  — browser UI
python/       — original Python implementation
output/       — generated files (gitignored)
```