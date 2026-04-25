#!/usr/bin/env python3
"""
Generate PNG files of all glyphs from encoding/docs/glyph-table.tsv.

Uses ImageMagick's convert command to render each glyph's SVG icon to PNG.

Usage:  python3 direction/scripts/generate-glyph-pngs.py [size]
Output: docs/assets/glyphs/*.png

Run from the repo root. Optional size parameter (default 64px).
"""

import csv
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).parent.parent.parent


def binary_to_grid(binary_str: str) -> list[int]:
    """Convert a 9-bit binary string to a list of filled cell indices (0-8)."""
    if not binary_str or len(binary_str) != 9:
        return []
    return [i for i, bit in enumerate(binary_str) if bit == '1']


def cell_to_svg_coords(cell_idx: int, cell_size: int = 12, gap: float = 2.0) -> tuple[float, float]:
    """Convert a cell index (0-8) to SVG x, y coordinates."""
    row = cell_idx // 3
    col = cell_idx % 3
    x = col * (cell_size + gap) + gap
    y = row * (cell_size + gap) + gap
    return (x, y)


def generate_svg(binary_str: str) -> str:
    """Generate an SVG element for a 3×3 binary grid (rotated 180°)."""
    filled_cells = binary_to_grid(binary_str)

    cell_size = 10
    gap = 2.0
    svg_size = 3 * cell_size + 4 * gap

    rects = []
    for cell_idx in filled_cells:
        rotated_idx = 8 - cell_idx
        x, y = cell_to_svg_coords(rotated_idx, cell_size, gap)
        rects.append(
            f'        <rect\n'
            f'          x="{x}"\n'
            f'          y="{y}"\n'
            f'          width="{cell_size}"\n'
            f'          height="{cell_size}"\n'
            f'          rx="2.2"\n'
            f'          fill="#1a1a1a"\n'
            f'        />'
        )

    if rects:
        svg = (
            f'<?xml version="1.0" encoding="UTF-8"?>\n'
            f'<svg\n'
            f'  xmlns="http://www.w3.org/2000/svg"\n'
            f'  width="{int(svg_size)}"\n'
            f'  height="{int(svg_size)}"\n'
            f'  viewBox="0 0 {int(svg_size)} {int(svg_size)}"\n'
            f'>\n'
            + '\n'.join(rects) + '\n'
            f'</svg>'
        )
    else:
        svg = (
            f'<?xml version="1.0" encoding="UTF-8"?>\n'
            f'<svg\n'
            f'  xmlns="http://www.w3.org/2000/svg"\n'
            f'  width="{int(svg_size)}"\n'
            f'  height="{int(svg_size)}"\n'
            f'  viewBox="0 0 {int(svg_size)} {int(svg_size)}"\n'
            f'/>'
        )

    return svg


def read_glyph_table(tsv_path: Path) -> list[dict]:
    """Read the TSV glyph table."""
    glyphs = []
    with open(tsv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter='\t')
        for row in reader:
            glyphs.append({
                'id': row['id'].strip(),
                'binary': row['binary'].strip(),
            })
    return glyphs


def main():
    size = int(sys.argv[1]) if len(sys.argv) > 1 else 64

    tsv_path = ROOT / 'encoding' / 'docs' / 'glyph-table.tsv'
    output_dir = ROOT / 'docs' / 'assets' / 'glyphs'
    output_dir.mkdir(parents=True, exist_ok=True)

    if not tsv_path.exists():
        sys.exit(f"Error: {tsv_path} not found")

    print(f"Reading {tsv_path}...")
    glyphs = read_glyph_table(tsv_path)
    print(f"Found {len(glyphs)} glyphs")

    print(f"Generating PNGs at {size}px...")
    for glyph in glyphs:
        glyph_id = glyph['id'].zfill(3)
        binary = glyph['binary']

        svg_str = generate_svg(binary)
        png_path = output_dir / f"{glyph_id}.png"

        with tempfile.NamedTemporaryFile(mode='w', suffix='.svg', delete=False) as tmp:
            tmp.write(svg_str)
            tmp_path = tmp.name

        try:
            subprocess.run(
                ['convert', tmp_path, '-resize', f'{size}x{size}', str(png_path)],
                check=True,
                capture_output=True
            )
            print(f"  {glyph_id}: ✓")
        except subprocess.CalledProcessError as e:
            print(f"  {glyph_id}: ✗ (convert failed)")
        except FileNotFoundError:
            print(f"  {glyph_id}: ✗ (ImageMagick 'convert' not found)")
            sys.exit(1)
        finally:
            Path(tmp_path).unlink(missing_ok=True)

    print(f"Done! Generated {len(glyphs)} PNGs in {output_dir}")


if __name__ == "__main__":
    main()
