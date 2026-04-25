#!/usr/bin/env python3
"""
Generate an HTML glyph table from encoding/docs/glyph-table.tsv.

Reads TSV file and generates a complete HTML document with:
- SVG icons showing 3×3 binary grids
- Table rows with ID, name, icon, glyph references, key, meaning, proposed_by

Usage:  python3 direction/scripts/generate-glyph-table.py
Output: docs/index.html

Run from the repo root.
"""

import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent.parent


def binary_to_grid(binary_str: str) -> list[int]:
    """
    Convert a 9-bit binary string to a list of filled cell indices (0-8).

    Binary string like "000000001" maps to a 3×3 grid:
      0 1 2
      3 4 5
      6 7 8

    Returns list of indices where value is '1' (filled).
    """
    if not binary_str or len(binary_str) != 9:
        return []
    return [i for i, bit in enumerate(binary_str) if bit == '1']


def cell_to_svg_coords(cell_idx: int, cell_size: int = 12, gap: float = 2.0) -> tuple[float, float]:
    """
    Convert a cell index (0-8) to SVG x, y coordinates.

    Grid layout:
      0 1 2
      3 4 5
      6 7 8

    Returns (x, y) for top-left of the cell in SVG.
    """
    row = cell_idx // 3
    col = cell_idx % 3
    x = col * (cell_size + gap) + gap
    y = row * (cell_size + gap) + gap
    return (x, y)


def generate_svg(binary_str: str) -> str:
    """
    Generate an SVG element for a 3×3 binary grid.

    Each filled cell is rendered as a rounded square.
    """
    filled_cells = binary_to_grid(binary_str)

    # SVG parameters
    cell_size = 10
    gap = 2.0
    svg_size = 3 * cell_size + 4 * gap  # 38

    # Build rectangles for filled cells
    rects = []
    for cell_idx in filled_cells:
        x, y = cell_to_svg_coords(cell_idx, cell_size, gap)
        rects.append(
            f'              <rect\n'
            f'                x="{x}"\n'
            f'                y="{y}"\n'
            f'                width="{cell_size}"\n'
            f'                height="{cell_size}"\n'
            f'                rx="2.2"\n'
            f'                fill="#1a1a1a"\n'
            f'              />'
        )

    # Build SVG
    if rects:
        svg = (
            f'            <svg\n'
            f'              xmlns="http://www.w3.org/2000/svg"\n'
            f'              width="{int(svg_size)}"\n'
            f'              height="{int(svg_size)}"\n'
            f'              viewBox="0 0 {int(svg_size)} {int(svg_size)}"\n'
            f'            >\n'
            + '\n'.join(rects) + '\n'
            f'            </svg>'
        )
    else:
        svg = (
            f'            <svg\n'
            f'              xmlns="http://www.w3.org/2000/svg"\n'
            f'              width="{int(svg_size)}"\n'
            f'              height="{int(svg_size)}"\n'
            f'              viewBox="0 0 {int(svg_size)} {int(svg_size)}"\n'
            f'            ></svg>'
        )

    return svg


def get_row_class(proposed_by: str) -> str:
    """Determine CSS row class based on proposed_by value."""
    proposed_by = proposed_by.strip().lower()
    if 'marainkit' in proposed_by and 'invariant' not in proposed_by:
        # Check if this is an invariant glyph by looking at the pattern
        # Invariants are typically marked with specific patterns
        return 'cat-inv'
    elif 'zakalwe' in proposed_by:
        return 'cat-zak'
    elif 'banks' in proposed_by:
        return 'cat-num'
    return ''


def escape_html(text: str) -> str:
    """Escape HTML special characters."""
    return (text
            .replace('&', '&amp;')
            .replace('<', '&lt;')
            .replace('>', '&gt;')
            .replace('"', '&quot;')
            .replace("'", '&#39;'))


def read_glyph_table(tsv_path: Path) -> list[dict]:
    """Read the TSV glyph table and return list of glyph dicts."""
    glyphs = []

    with open(tsv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter='\t')
        for row in reader:
            glyphs.append({
                'id': row['id'].strip(),
                'name': row['name'].strip(),
                'binary': row['binary'].strip(),
                'reference_glyph_exists': row['reference_glyph_exists'].strip(),
                'glyph_exists': row['glyph_exists'].strip(),
                'key': row['key'].strip(),
                'meaning': row['meaning'].strip(),
                'proposed_by': row['proposed_by'].strip(),
                'banks_char': row.get('banks_char', '').strip(),
                'regular_char': row.get('regular_char', '').strip(),
            })

    return glyphs


def generate_table_row(glyph: dict) -> str:
    """Generate an HTML table row for a single glyph."""
    glyph_id = glyph['id']
    name = glyph['name']
    binary = glyph['binary']
    key = glyph['key']
    meaning = glyph['meaning']
    proposed_by = glyph['proposed_by']

    # Determine row class
    row_class = get_row_class(proposed_by)
    row_class_attr = f' class="{row_class}"' if row_class else ''

    # Generate SVG icon
    svg = generate_svg(binary)

    # Determine glyph display using character mappings
    banks_char = glyph.get('banks_char', '')
    regular_char = glyph.get('regular_char', '')

    if banks_char:
        banks_glyph = f'<span class="m2-glyph">{escape_html(banks_char)}</span>'
    else:
        banks_glyph = '<span class="m2-missing">—</span>'

    if regular_char:
        regular_glyph = f'<span class="mr-glyph">{escape_html(regular_char)}</span>'
    else:
        regular_glyph = '<span class="m2-missing">—</span>'

    # Escape HTML in text fields
    name_html = escape_html(name)
    meaning_html = escape_html(meaning)
    proposed_by_html = escape_html(proposed_by)
    key_html = escape_html(key)

    row = (
        f'        <tr{row_class_attr}>\n'
        f'          <td class="col-num">{glyph_id}</td>\n'
        f'          <td class="col-name">{name_html}</td>\n'
        f'          <td class="col-icon">\n'
        f'{svg}\n'
        f'          </td>\n'
        f'          <td class="col-glyph">{banks_glyph}</td>\n'
        f'          <td class="col-glyph-reg">{regular_glyph}</td>\n'
        f'          <td class="col-key">{key_html}</td>\n'
        f'          <td class="col-meaning">{meaning_html}</td>\n'
        f'          <td class="col-proposed">{proposed_by_html}</td>\n'
        f'        </tr>'
    )

    return row


def generate_html(glyphs: list[dict]) -> str:
    """Generate a complete HTML document."""

    # Generate table rows
    rows = [generate_table_row(g) for g in glyphs]

    html = '''<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <title>Marain — Glyph Table</title>
    <meta name="description" content="Every assigned symbol in Marain — the constructed language of the Culture from Iain M. Banks' novels. Phonemes, numerals, operators, and invariant glyphs with binary indices and font comparisons." />
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link
      href="https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible+Next:ital,wght@0,400;0,700;1,400&display=swap"
      rel="stylesheet"
    />

    <style>
      @font-face {
        font-family: "MarainBanks";
        src: local("MarainBanks"), url("marain-banks/Marain-Banks.ttf") format("truetype");
      }
      @font-face {
        font-family: "MarainRegular";
        src: local("MarainRegular"), url("marain-regular/Marain-Regular.ttf") format("truetype");
      }
      :root {
        --bg: #f8f7f4;
        --surface: #fff;
        --rule: #d8d5d0;
        --text: #1a1a1a;
        --muted: #888;
        --accent: #4a6fa5;
        --inv-bg: #eef3fa;
        --inv-rule: #4a6fa5;
        --warn-bg: #fff7ed;
        --warn-rule: #c04a2a;
        --ff: "Atkinson Hyperlegible Next", "Atkinson Hyperlegible", sans-serif;
        --ff-mono: "Intel One Mono", "Cascadia Code", ui-monospace, monospace;
        --ff-marain: "MarainBanks", monospace;
        --ff-marain-reg: "MarainRegular", monospace;
      }
      *,
      *::before,
      *::after {
        box-sizing: border-box;
        margin: 0;
        padding: 0;
      }
      body {
        font-family: var(--ff);
        font-size: 15px;
        line-height: 1.6;
        background: var(--bg);
        color: var(--text);
        padding: 2.5rem 3rem;
        max-width: 1400px;
      }
      h1 {
        font-size: 1.4rem;
        font-weight: 700;
        margin-bottom: 0.3rem;
      }
      .subtitle {
        font-size: 0.85rem;
        color: var(--muted);
        margin-bottom: 1.8rem;
        font-style: italic;
      }
      .note {
        font-size: 0.8rem;
        color: var(--muted);
        margin-bottom: 1.2rem;
        font-style: italic;
      }
      .legend {
        display: flex;
        gap: 1.5rem;
        margin-bottom: 1.5rem;
        font-size: 0.8rem;
        flex-wrap: wrap;
      }
      .leg {
        display: flex;
        align-items: center;
        gap: 0.4rem;
      }
      .swatch {
        width: 12px;
        height: 12px;
        border-radius: 2px;
        border: 1px solid;
      }
      .sw-inv {
        background: var(--inv-bg);
        border-color: var(--inv-rule);
      }
      .sw-ph {
        background: var(--surface);
        border-color: var(--rule);
      }
      .sw-near {
        background: var(--warn-bg);
        border-color: var(--warn-rule);
      }
      table {
        border-collapse: collapse;
        width: 100%;
      }
      thead th {
        font-size: 0.75rem;
        font-weight: 700;
        letter-spacing: 0.06em;
        text-transform: uppercase;
        color: var(--muted);
        border-bottom: 2px solid var(--rule);
        padding: 0.4rem 0.8rem 0.4rem 0;
        text-align: left;
      }
      td {
        padding: 0.45rem 0.8rem 0.45rem 0;
        border-bottom: 1px solid var(--rule);
        vertical-align: middle;
      }
      tr:last-child td {
        border-bottom: none;
      }
      tr.cat-inv {
        background: var(--inv-bg);
      }
      tr.near-conflict {
        background: var(--warn-bg);
      }
      tr.cat-num {
        background: #f2f0fa;
      }
      tr.cat-zak {
        background: #f0faf2;
      }
      .col-num {
        font-family: var(--ff-mono);
        font-size: 0.8rem;
        color: var(--muted);
        width: 3rem;
        text-align: right;
        padding-right: 1rem;
      }
      .col-name {
        font-size: 0.88rem;
        width: 16rem;
      }
      .col-icon {
        width: 3rem;
        padding: 0.2rem 0.5rem 0.2rem 0;
      }
      .col-icon svg {
        display: block;
      }
      .col-glyph {
        width: 5rem;
        border-left: 2px solid var(--rule);
        padding-left: 1rem;
        text-align: center;
      }
      .m2-glyph {
        font-family: "MarainBanks", monospace;
        font-size: 2rem;
        line-height: 1;
        display: block;
      }
      .m2-missing {
        color: var(--muted);
        font-size: 0.75rem;
      }
      .col-glyph-reg {
        width: 5rem;
        border-left: 1px solid var(--rule);
        padding-left: 1rem;
        text-align: center;
      }
      .mr-glyph {
        font-family: "MarainRegular", monospace;
        font-size: 2rem;
        line-height: 1;
        display: block;
      }
      .col-key {
        font-family: var(--ff-mono);
        font-size: 0.75rem;
        color: var(--muted);
        width: 8rem;
      }
      .col-meaning {
        font-size: 0.85rem;
      }
      .col-proposed {
        font-size: 0.78rem;
        color: var(--muted);
        width: 8rem;
      }
      .flag {
        font-size: 0.72rem;
        color: var(--warn-rule);
        font-style: italic;
      }
      code {
        font-family: var(--ff-mono);
      }
    </style>
  </head>
  <body>
    <h1>Marain — Glyph Table</h1>
    <p class="subtitle">
      All assigned symbols in Marain — generated from encoding/docs/glyph-table.tsv
    </p>
    <div class="legend">
      <div class="leg">
        <div class="swatch sw-inv"></div>
        Invariant
      </div>
      <div class="leg">
        <div class="swatch sw-ph"></div>
        Phoneme (Banks)
      </div>
      <div class="leg">
        <div class="swatch sw-near"></div>
        Other
      </div>
    </div>
    <p class="note"><strong>Icon:</strong> 3×3 binary grid visualization · <strong>Banks / Marain Regular:</strong> font renderings · <strong>Key:</strong> input keystroke(s); IME = input method</p>
    <table>
      <thead>
        <tr>
          <th class="col-num">#</th>
          <th class="col-name">Name</th>
          <th class="col-icon">Icon</th>
          <th class="col-glyph">Banks</th>
          <th class="col-glyph-reg">Marain Regular</th>
          <th class="col-key">Key</th>
          <th class="col-meaning">Meaning(s)</th>
          <th class="col-proposed">Proposed by</th>
        </tr>
      </thead>
      <tbody>
''' + '\n'.join(rows) + '''
      </tbody>
    </table>
  </body>
</html>
'''

    return html


def main():
    """Main entry point."""
    tsv_path = ROOT / 'encoding' / 'docs' / 'glyph-table.tsv'
    output_path = ROOT / 'docs' / 'index.html'

    if not tsv_path.exists():
        sys.exit(f"Error: {tsv_path} not found")

    print(f"Reading {tsv_path}...")
    glyphs = read_glyph_table(tsv_path)
    print(f"Found {len(glyphs)} glyphs")

    print("Generating HTML...")
    html = generate_html(glyphs)

    print(f"Writing {output_path}...")
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"Done! Generated {output_path}")


if __name__ == "__main__":
    main()
