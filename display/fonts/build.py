#!/usr/bin/env python3
"""
Marain glyph renderer — build.py

Generates SVG previews and an HTML preview page for the Marain glyph set.
All rendering parameters are defined as tokens at the top of this file.

References:
  font-spec.md         — rendering requirements, context sizes, optical weight
  research.md          — AH + IOM principles: distinction, open counters, generous spacing
  cjk-mixed-scripts.md — optical weight normalisation, mixed-mode visual rhythm

Usage:
  source display/fonts/.venv/bin/activate
  python3 display/fonts/build.py
  open display/fonts/preview.html
"""

# ---------------------------------------------------------------------------
# Rendering tokens
# All parameters are defined here. No magic numbers below.
# ---------------------------------------------------------------------------

# Cell shape
CORNER_RATIO = 0.45     # Corner radius as fraction of cell size.
                        # Applied only to outer (unconnected) corners.
                        # 0   = hard square
                        # 0.5 = semicircular terminal (IOM-style)
                        # 1.0 = full circle / dot (AH-style)
                        # 0.45 gives a clear rounded terminal without going full dot.

# Colours
FILL_COLOUR  = "#1a1a1a"  # Near-black — consistent with AH's soft-black aesthetic
BG_COLOUR    = "transparent"

# Glyph padding (space around the 3×3 grid within the SVG bounding box)
GLYPH_PADDING = 2

# ---------------------------------------------------------------------------
# Rendering sizes — (cell_px, gap_px, label) — from font-spec §6.2
# ---------------------------------------------------------------------------

SIZES = [
    (3,  0, "11px · minimum"),
    (4,  1, "14px · code"),
    (6,  1, "20px · document"),
    (8,  2, "28px · hud"),
    (12, 2, "40px · critical"),
]

# ---------------------------------------------------------------------------
# Invariant glyphs — font-spec §5.1, encoding/docs/invariant-glyphs.md
# ---------------------------------------------------------------------------

INVARIANT_GLYPHS = {
    0:   ("Empty · nuul",  "structural"),
    16:  ("Point",         "structural"),
    170: ("Diamond",       "warning"),
    186: ("Cross",         "warning"),
    325: ("Corners",       "warning"),
    341: ("Checkerboard",  "warning"),
    495: ("Frame",         "structural"),
    511: ("Full",          "structural"),
}

# ---------------------------------------------------------------------------
# Path helpers
# ---------------------------------------------------------------------------

def rounded_rect_path(
    x0: float, y0: float, x1: float, y1: float, r: float,
    round_tl: bool, round_tr: bool, round_br: bool, round_bl: bool,
) -> str:
    """
    SVG path data for a rectangle with per-corner selective rounding.
    Corners set True receive a quadratic-bezier arc; False corners are sharp.
    Path is drawn clockwise starting from the top edge.
    """
    r = max(0.0, min(r, (x1 - x0) / 2, (y1 - y0) / 2))
    d = []

    # Move to start of top edge (after TL corner)
    d.append(f"M {x0 + (r if round_tl else 0):.2f},{y0:.2f}")

    # Top edge → TR corner
    d.append(f"L {x1 - (r if round_tr else 0):.2f},{y0:.2f}")
    if round_tr:
        d.append(f"Q {x1:.2f},{y0:.2f} {x1:.2f},{y0 + r:.2f}")

    # Right edge → BR corner
    d.append(f"L {x1:.2f},{y1 - (r if round_br else 0):.2f}")
    if round_br:
        d.append(f"Q {x1:.2f},{y1:.2f} {x1 - r:.2f},{y1:.2f}")

    # Bottom edge → BL corner
    d.append(f"L {x0 + (r if round_bl else 0):.2f},{y1:.2f}")
    if round_bl:
        d.append(f"Q {x0:.2f},{y1:.2f} {x0:.2f},{y1 - r:.2f}")

    # Left edge → TL corner
    d.append(f"L {x0:.2f},{y0 + (r if round_tl else 0):.2f}")
    if round_tl:
        d.append(f"Q {x0:.2f},{y0:.2f} {x0 + r:.2f},{y0:.2f}")

    d.append("Z")
    return " ".join(d)


# ---------------------------------------------------------------------------
# Core rendering function
# ---------------------------------------------------------------------------

def glyph_svg(
    index: int,
    cell_px: int,
    gap_px: int,
    fill: str = FILL_COLOUR,
    padding: int = GLYPH_PADDING,
) -> str:
    """
    Return a self-contained SVG for glyph `index`.

    Bit layout: bit 0 = top-left, bit 8 = bottom-right, row-major order.

    Connected cells:
      Adjacent filled cells have their shared gap removed — the two shapes
      extend toward each other and meet (with a tiny overlap to prevent
      hairline gaps under antialiasing). Inner corners at the join are sharp.
      Outer (unconnected) corners receive the CORNER_RATIO arc.

    This produces stroke-like forms where connected cells merge into a single
    visual shape, while isolated cells read as rounded marks.
    """
    glyph_dim = cell_px * 3 + gap_px * 2
    total     = glyph_dim + padding * 2
    corner_r  = cell_px * CORNER_RATIO

    def filled(r: int, c: int) -> bool:
        if r < 0 or r > 2 or c < 0 or c > 2:
            return False
        return bool((index >> (r * 3 + c)) & 1)

    paths = []
    for bit in range(9):
        if not (index >> bit) & 1:
            continue

        row, col = divmod(bit, 3)

        t = filled(row - 1, col)   # top neighbour filled?
        b = filled(row + 1, col)   # bottom
        lft = filled(row, col - 1) # left
        rgt = filled(row, col + 1) # right

        # Nominal cell bounds
        x0 = col * (cell_px + gap_px) + padding
        y0 = row * (cell_px + gap_px) + padding
        x1 = x0 + cell_px
        y1 = y0 + cell_px

        # Extend toward connected neighbours to fill the gap.
        # Small overlap (+0.5px) prevents hairline seams under antialiasing.
        ext = gap_px / 2 + 0.5 if gap_px > 0 else 0.0
        if t:   y0 -= ext
        if b:   y1 += ext
        if lft: x0 -= ext
        if rgt: x1 += ext

        # Round only the corners where BOTH adjacent edges are unconnected.
        # An inner corner (where two cells meet) stays sharp — this is what
        # creates clean L-shapes, T-junctions, and right angles in the strokes.
        cr = min(corner_r, (x1 - x0) / 2, (y1 - y0) / 2)

        paths.append(
            f'<path d="{rounded_rect_path(x0, y0, x1, y1, cr, not t and not lft, not t and not rgt, not b and not rgt, not b and not lft)}" fill="{fill}"/>'
        )

    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" '
        f'width="{total:.0f}" height="{total:.0f}" '
        f'viewBox="0 0 {total:.2f} {total:.2f}">'
        + "".join(paths)
        + "</svg>"
    )


# ---------------------------------------------------------------------------
# HTML preview generator
# ---------------------------------------------------------------------------

def preview_html() -> str:

    # --- Invariant glyph table ---
    inv_rows = []
    for idx, (name, role) in INVARIANT_GLYPHS.items():
        icon = "⚠" if role == "warning" else "◈"
        size_svgs = "".join(
            f'<span class="size-cell" title="{label}">'
            f'{glyph_svg(idx, cpx, gpx)}'
            f'<span class="size-label">{label.split("·")[0].strip()}</span>'
            f'</span>'
            for cpx, gpx, label in SIZES
        )
        inv_rows.append(
            f"<tr>"
            f'<td class="col-idx">#{idx}</td>'
            f'<td class="col-name">{icon} {name}</td>'
            f'<td class="col-glyphs">{size_svgs}</td>'
            f"</tr>"
        )

    # --- Full 512 grid at document size ---
    grid_cells = []
    for idx in range(512):
        svg     = glyph_svg(idx, cell_px=6, gap_px=1)
        bits    = bin(idx)[2:].zfill(9)
        inv_cls = " invariant" if idx in INVARIANT_GLYPHS else ""
        label   = f" · {INVARIANT_GLYPHS[idx][0]}" if idx in INVARIANT_GLYPHS else ""
        grid_cells.append(
            f'<div class="glyph-cell{inv_cls}" title="#{idx} ({bits}){label}">'
            f"{svg}"
            f'<span class="glyph-idx">{idx}</span>'
            f"</div>"
        )

    # --- Coexistence: inline with reference fonts ---
    inline_svgs = " ".join(
        glyph_svg(idx, cell_px=6, gap_px=1) for idx in INVARIANT_GLYPHS
    )

    # --- Connected-cell showcase: a few interesting glyphs at large size ---
    showcase_indices = [
        170, 186, 325, 341,         # invariant warning set
        495, 511, 0, 16,            # invariant structural set
        219, 438,                   # diagonal pairs
        73, 292,                    # horizontal / vertical strokes
        146, 73, 54, 108,           # various connected forms
        255, 256,                   # half-full
    ]
    showcase_cells = "".join(
        f'<div class="showcase-cell" title="#{i}">'
        f'{glyph_svg(i, cell_px=12, gap_px=2)}'
        f'<span class="glyph-idx">#{i}</span>'
        f'</div>'
        for i in showcase_indices
    )

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Marain Glyph Preview</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible+Next:ital,wght@0,200;0,300;0,400;0,700&display=swap" rel="stylesheet">
<style>
  :root {{
    --fill:    {FILL_COLOUR};
    --bg:      #f8f7f4;
    --surface: #ffffff;
    --rule:    #d8d5d0;
    --text:    #1a1a1a;
    --muted:   #888;
    --accent:  #4a6fa5;
    --ff-prose: 'Atkinson Hyperlegible Next', 'Atkinson Hyperlegible', sans-serif;
    --ff-code:  'Intel One Mono', 'Cascadia Code', 'Fira Code', ui-monospace, monospace;
  }}
  *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    font-family: var(--ff-prose);
    font-size: 16px;
    line-height: 1.65;
    background: var(--bg);
    color: var(--text);
    padding: 2.5rem 3rem;
    max-width: 1400px;
  }}
  h1 {{ font-size: 1.4rem; font-weight: 700; border-bottom: 1px solid var(--rule); padding-bottom: 0.6rem; margin-bottom: 0.4rem; }}
  h2 {{ font-size: 0.9rem; font-weight: 700; letter-spacing: 0.06em; text-transform: uppercase; color: var(--accent); margin: 2.5rem 0 0.4rem; }}
  .note {{ font-size: 0.8rem; color: var(--muted); margin-bottom: 1.2rem; font-style: italic; }}

  table {{ border-collapse: collapse; margin-bottom: 1rem; }}
  td {{ padding: 0.4rem 1.2rem 0.4rem 0; vertical-align: middle; }}
  .col-idx {{ font-family: var(--ff-code); font-size: 0.8rem; color: var(--muted); width: 3.5rem; }}
  .col-name {{ font-size: 0.88rem; width: 13rem; }}
  .col-glyphs {{ display: flex; gap: 1.5rem; align-items: flex-end; }}
  .size-cell {{ display: flex; flex-direction: column; align-items: center; gap: 3px; }}
  .size-label {{ font-family: var(--ff-code); font-size: 7px; color: var(--muted); }}

  .showcase {{ display: flex; flex-wrap: wrap; gap: 1rem; margin-bottom: 1rem; }}
  .showcase-cell {{ display: flex; flex-direction: column; align-items: center; gap: 4px; background: var(--surface); border: 1px solid var(--rule); padding: 8px 8px 4px; border-radius: 4px; }}
  .showcase-cell.invariant {{ border-color: var(--accent); background: #eef3fa; }}

  .coexist-block {{ background: var(--surface); border: 1px solid var(--rule); border-radius: 4px; padding: 1.2rem 1.5rem; margin-bottom: 0.75rem; }}
  .coexist-label {{ font-family: var(--ff-code); font-size: 0.7rem; color: var(--muted); text-transform: uppercase; letter-spacing: 0.08em; display: block; margin-bottom: 0.5rem; }}
  .ah-line {{ font-family: var(--ff-prose); font-size: 1rem; display: flex; flex-wrap: wrap; align-items: center; gap: 0.2em; line-height: 1.65; }}
  .iom-line {{ font-family: var(--ff-code); font-size: 0.875rem; display: flex; flex-wrap: wrap; align-items: center; gap: 0.2em; line-height: 1.6; }}
  .ah-line svg, .iom-line svg {{ vertical-align: middle; flex-shrink: 0; }}

  .grid-512 {{ display: flex; flex-wrap: wrap; gap: 3px; margin-top: 0.5rem; }}
  .glyph-cell {{ display: flex; flex-direction: column; align-items: center; background: var(--surface); border: 1px solid var(--rule); padding: 3px 3px 1px; border-radius: 3px; cursor: default; }}
  .glyph-cell:hover {{ border-color: var(--accent); }}
  .glyph-cell.invariant {{ border-color: var(--accent); background: #eef3fa; }}
  .glyph-idx {{ font-family: var(--ff-code); font-size: 7px; color: #bbb; margin-top: 1px; line-height: 1; }}
  .glyph-cell.invariant .glyph-idx {{ color: var(--accent); }}
</style>
</head>
<body>

<h1>Marain Glyph Preview — connected cells, rounded terminals</h1>
<p class="note">
  Adjacent filled cells merge into strokes. Outer corners: {CORNER_RATIO*100:.0f}% radius.
  Inner corners (cell joins): sharp. Fill: {FILL_COLOUR}.
</p>

<h2>Showcase — selected glyphs at large size (40px)</h2>
<p class="note">Shows the connected-cell effect clearly. Hover for index.</p>
<div class="showcase">{showcase_cells}</div>

<h2>Invariant Glyphs — all 5 sizes</h2>
<p class="note">⚠ warning · ◈ structural · sizes: 11px / 14px / 20px / 28px / 40px</p>
<table>{''.join(inv_rows)}</table>

<h2>Coexistence Test</h2>
<p class="note">Invariant glyphs inline with reference fonts at their actual sizes. Check vertical centre, optical weight, spacing rhythm.</p>
<div class="coexist-block">
  <span class="coexist-label">Atkinson Hyperlegible Next — prose (1rem)</span>
  <div class="ah-line">
    The eight invariant Marain glyphs are:
    {inline_svgs}
    — structural and warning vocabulary.
  </div>
</div>
<div class="coexist-block">
  <span class="coexist-label">Intel One Mono — code (0.875rem)</span>
  <div class="iom-line">
    glyph[0..7] = {inline_svgs} // invariant under D₄
  </div>
</div>

<h2>Full glyph space — 512 states at document size (20px) — hover for index</h2>
<p class="note">Blue border = invariant. The variation in form across the 512 states is the font's character.</p>
<div class="grid-512">{''.join(grid_cells)}</div>

</body>
</html>"""


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    import os

    here         = os.path.dirname(os.path.abspath(__file__))
    preview_path = os.path.join(here, "preview.html")

    with open(preview_path, "w", encoding="utf-8") as f:
        f.write(preview_html())

    print(f"Written: {preview_path}")
    print("Open in a browser to review.")
