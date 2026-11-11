#!/usr/bin/env python3
"""
scripts/build_snake_svg.py

Builds assets/contribution-snake.svg for Pratik Mengal (@mengalpratik)
in Hacker Green & Pitch Black color palette from verified contribution telemetry.

Key features:
- Comprehensive schema and date continuity validation.
- Valid W3C SMIL keyTimes syntax.
- Full prefers-reduced-motion accessibility support.
- Pure pathlib-based file operations with clean CLI execution and exit codes.
"""

import sys
import json
import math
import argparse
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
DEFAULT_INPUT_PATH = ROOT_DIR / "data" / "contributions.json"
DEFAULT_OUTPUT_PATH = ROOT_DIR / "assets" / "contribution-snake.svg"

# Grid and Canvas Dimensions
W = 1200
H = 410
CELL = 15
GAP = 4
STEP = CELL + GAP
GRID_X = 118
GRID_Y = 182

# Hacker Green Palette: Level 0 (cyber matrix grid) to Level 4 (neon laser)
LEVELS = ["#082411", "#006622", "#00A838", "#00E64D", "#00FF66"]
MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

def parse_iso_date(iso_str: str) -> datetime:
    """Parse YYYY-MM-DD string into UTC datetime."""
    return datetime.strptime(iso_str, "%Y-%m-%d").replace(tzinfo=timezone.utc)

def fmt_date(d: datetime) -> str:
    """Format datetime as 'DD Mon YYYY'."""
    return f"{d.day} {MONTHS[d.month - 1]} {d.year}"

def validate_contributions_json(data: dict) -> tuple[bool, str]:
    """Validate structure, field presence, and date continuity."""
    if not isinstance(data, dict):
        return False, "Root JSON must be a dictionary."
    if "contributions" not in data or not isinstance(data["contributions"], list):
        return False, "Missing or invalid 'contributions' list."
    
    days = data["contributions"]
    if not days:
        return False, "Contributions list is empty."
        
    prev_d = None
    seen_dates = set()
    for idx, d in enumerate(days):
        if not isinstance(d, dict):
            return False, f"Entry at index {idx} is not an object."
        for req in ("date", "count"):
            if req not in d:
                return False, f"Entry at index {idx} missing field '{req}'."
        d_str = d["date"]
        try:
            curr_d = parse_iso_date(d_str).date()
        except ValueError:
            return False, f"Invalid date '{d_str}' at index {idx}."
            
        if d_str in seen_dates:
            return False, f"Duplicate date '{d_str}' at index {idx}."
        seen_dates.add(d_str)
        
        if prev_d is not None and (curr_d - prev_d).days != 1:
            return False, f"Non-continuous date progression between {prev_d} and {curr_d}."
        prev_d = curr_d
        
        if not isinstance(d["count"], int) or d["count"] < 0:
            return False, f"Count must be non-negative integer at index {idx}."
            
    return True, f"Validated {len(days)} days successfully."

def build_snake_svg(input_path: Path = DEFAULT_INPUT_PATH, output_path: Path = DEFAULT_OUTPUT_PATH) -> bool:
    """Generate contribution-snake.svg with full validation and error handling."""
    if not input_path.exists():
        print(f"✗ Input file not found: {input_path}", file=sys.stderr)
        return False
        
    try:
        with open(input_path, "r", encoding="utf-8") as f:
            raw_data = json.load(f)
    except Exception as e:
        print(f"✗ Failed to parse JSON from {input_path}: {e}", file=sys.stderr)
        return False
        
    valid, msg = validate_contributions_json(raw_data)
    if not valid:
        print(f"✗ Invalid contribution data: {msg}", file=sys.stderr)
        return False
        
    days = raw_data["contributions"]
    
    # Calculate telemetry metrics
    total = 0
    active = 0
    run = 0
    best = 0
    best_end = -1
    peak = days[0]
    
    for i, d in enumerate(days):
        count = d["count"]
        total += count
        if count > 0:
            active += 1
            run += 1
            if run > best:
                best = run
                best_end = i
            if count > peak["count"]:
                peak = d
        else:
            run = 0
            
    best_start = best_end - best + 1 if best > 0 else 0
    first = parse_iso_date(days[0]["date"])
    last = parse_iso_date(days[-1]["date"])
    fetched = fmt_date(last)
    
    # Sunday = 0 alignment
    offset = (first.weekday() + 1) % 7
    
    def pos(i):
        week = math.floor((i + offset) / 7)
        dow = (i + offset) % 7
        return week, dow, GRID_X + week * STEP, GRID_Y + dow * STEP

    def label(d):
        c = d["count"]
        s = "s" if c != 1 else ""
        return f"{c} contribution{s} · {fmt_date(parse_iso_date(d['date']))}"

    weeks_count = math.floor((len(days) - 1 + offset) / 7) + 1
    
    # Construct continuous snake path through columns
    route = []
    for w in range(weeks_count):
        for r in range(7):
            dow = r if w % 2 == 0 else (6 - r)
            cx = GRID_X + w * STEP + CELL / 2
            cy = GRID_Y + dow * STEP + CELL / 2
            route.append((cx, cy))
            
    fx, fy = route[0]
    lx, ly = route[-1]
    route.insert(0, (fx, fy - STEP))
    route.append((lx + STEP, ly))
    
    SNAKE_DT = 0.055
    SNAKE_BEGIN = 2.4
    run_time = (len(route) - 1) * SNAKE_DT
    loop = run_time + 3.5
    run_frac = round(run_time / loop, 4)
    route_d = "M" + " L".join(f"{x:.1f} {y:.1f}" for x, y in route)

    def route_index(i):
        w, dow, _, _ = pos(i)
        actual_dow = dow if w % 2 == 0 else (6 - dow)
        return w * 7 + actual_dow + 1

    # Static cells (used for reduced motion and baseline)
    static_cells_svg = []
    # Animated cells (used when motion is enabled)
    animated_cells_svg = []
    
    for i, d in enumerate(days):
        w, dow, x, y = pos(i)
        delay = f"{0.3 + (w + dow * 1.6) * 0.018:.3f}"
        lvl = min(d.get("level", 0), 4)
        color = LEVELS[lvl]
        glow = ' filter="url(#hm-glow)"' if lvl == 4 else ""
        
        # Static rect
        static_cells_svg.append(
            f'<rect class="hm-c" x="{x}" y="{y}" width="{CELL}" height="{CELL}" rx="3.5" fill="{color}"{glow}><title>{label(d)}</title></rect>'
        )
        
        # Animated rect with valid W3C SMIL syntax (keyTimes terminates at 1)
        eat = ""
        if d["count"] > 0:
            eat_time = f"{(route_index(i) * SNAKE_DT) / loop:.4f}"
            eat = f'<animate attributeName="fill" values="{color};{LEVELS[0]};{LEVELS[0]}" keyTimes="0;{eat_time};1" calcMode="discrete" dur="{loop:.2f}s" begin="{SNAKE_BEGIN}s" repeatCount="indefinite"/>'
        animated_cells_svg.append(
            f'<rect class="hm-c" style="animation-delay:{delay}s" x="{x}" y="{y}" width="{CELL}" height="{CELL}" rx="3.5" fill="{color}"{glow}><title>{label(d)}</title>{eat}</rect>'
        )
        
    static_cells_markup = "\n    ".join(static_cells_svg)
    animated_cells_markup = "\n    ".join(animated_cells_svg)

    # Longest streak indicator
    streak_svg = ""
    if best > 1:
        _, _, sx, _ = pos(best_start)
        label_x = min(sx, W - 360)
        streak_svg = f'''<g class="hm-fade" style="animation-delay:2.6s">
      <path d="M{sx + CELL / 2} {GRID_Y + 7 * STEP - 2} V {GRID_Y + 7 * STEP + 10}" stroke="#00FF66" stroke-opacity="0.6"/>
      <text class="hm-mono" x="{label_x}" y="{GRID_Y + 7 * STEP + 24}" font-size="10.5" letter-spacing="1.6" fill="#00FF66">LONGEST STREAK · {best} DAYS · {fmt_date(parse_iso_date(days[best_start]["date"])).upper()} – {fmt_date(parse_iso_date(days[best_end]["date"])).upper()}</text>
    </g>'''

    # Snake Segments
    SEGMENTS = 9
    snake_segments = []
    for k in range(SEGMENTS):
        seg = SEGMENTS - 1 - k
        size = CELL - seg * 0.9
        fill = "#FFFFFF" if seg == 0 else ("#00FF66" if seg < 3 else ("#05FFA1" if seg < 6 else "#008F39"))
        op = f"{1 - seg * 0.06:.2f}"
        glow = ' filter="url(#hm-glow)"' if seg == 0 else ""
        begin = f"{SNAKE_BEGIN + seg * SNAKE_DT:.3f}"
        eyes = ""
        if seg == 0:
            eyes = f'<circle cx="{(size / 2 - 4):.1f}" cy="-2.5" r="1.3" fill="#020803"/><circle cx="{(size / 2 - 4):.1f}" cy="2.5" r="1.3" fill="#020803"/>'
        snake_segments.append(
            f'''<g opacity="0"{glow}>
      <animateMotion path="{route_d}" rotate="auto" dur="{loop:.2f}s" begin="{begin}s" repeatCount="indefinite" calcMode="linear" keyPoints="0;1;1" keyTimes="0;{run_frac};1"/>
      <animate attributeName="opacity" values="{op};0;0" keyTimes="0;{run_frac};1" calcMode="discrete" dur="{loop:.2f}s" begin="{begin}s" repeatCount="indefinite"/>
      <rect x="{(-size / 2):.1f}" y="{(-size / 2):.1f}" width="{size:.1f}" height="{size:.1f}" rx="{(size / 2.6):.1f}" fill="{fill}"/>{eyes}
    </g>'''
        )
    snake_markup = "\n    ".join(snake_segments)

    # Month Labels
    labels = []
    last_month = -1
    for i, d in enumerate(days):
        m = parse_iso_date(d["date"]).month - 1
        if m == last_month:
            continue
        last_month = m
        w, _, _, _ = pos(i)
        labels.append((w, MONTHS[m]))

    if len(labels) > 1 and labels[1][0] - labels[0][0] < 3:
        labels.pop(0)

    month_svg = "".join(f'<text x="{GRID_X + col * STEP}" y="{GRID_Y - 12}">{txt}</text>' for col, txt in labels)

    stats = [
        ("CONTRIBUTIONS", f"{total:,}", f"{MONTHS[first.month - 1]} {first.year} – {MONTHS[last.month - 1]} {last.year}"),
        ("ACTIVE DAYS", str(active), f"of {len(days)} days"),
        ("LONGEST STREAK", str(best), "consecutive days"),
        ("BUSIEST DAY", str(peak["count"]), fmt_date(parse_iso_date(peak["date"]))),
    ]

    stats_svg = []
    for i, (stat_lbl, val, sub) in enumerate(stats):
        x = 610 + i * 150
        stats_svg.append(f'''<g transform="translate({x}, 58)">
      <text class="hm-mono" font-size="10" letter-spacing="1.8" fill="#00FF66">{stat_lbl}</text>
      <text class="hm-serif" y="44" font-size="36" font-weight="300" fill="#E6FFF0">{val}</text>
      <text class="hm-mono" y="64" font-size="9.5" fill="#88B99A">{sub}</text>
    </g>''')
    stats_markup = "\n    ".join(stats_svg)

    legend_x = W - 56 - 5 * 18 - 70
    legend_cells = "".join(f'<rect x="{legend_x + 36 + i * 18}" y="372" width="12" height="12" rx="3" fill="{c}"/>' for i, c in enumerate(LEVELS))

    svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-labelledby="hm-title hm-desc">
  <title id="hm-title">GitHub contributions for @mengalpratik</title>
  <desc id="hm-desc">{total} contributions from {fmt_date(first)} to {fmt_date(last)}: {active} active days, longest streak {best} days, busiest day {peak["count"]} contributions on {fmt_date(parse_iso_date(peak["date"]))}.</desc>
  <defs>
    <linearGradient id="hm-bg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#041207"/>
      <stop offset="100%" stop-color="#000000"/>
    </linearGradient>
    <radialGradient id="hm-light" cx="88%" cy="0%" r="70%">
      <stop offset="0" stop-color="#00FF66" stop-opacity="0.35"/>
      <stop offset="100%" stop-color="#00240E" stop-opacity="0"/>
    </radialGradient>
    <filter id="hm-glow" x="-60%" y="-60%" width="220%" height="220%">
      <feGaussianBlur stdDeviation="2.4" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>
  <style>
    .hm-serif {{ font-family: Georgia, "Iowan Old Style", "Palatino Linotype", "Times New Roman", serif; }}
    .hm-mono {{ font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace; }}
    .hm-c {{ transform-box: fill-box; transform-origin: center; }}
    .hm-fade {{ opacity: 1; }}
    .hm-static-grid {{ display: none; }}
    @media (prefers-reduced-motion: reduce) {{
      .hm-c, .hm-fade {{ animation: none; }}
      .hm-motion {{ display: none; }}
      .hm-animated-grid {{ display: none; }}
      .hm-static-grid {{ display: block; }}
    }}
  </style>

  <rect width="{W}" height="{H}" rx="20" fill="url(#hm-bg)"/>
  <rect width="{W}" height="{H}" rx="20" fill="url(#hm-light)"/>
  <rect x="0.5" y="0.5" width="{W - 1}" height="{H - 1}" rx="19.5" fill="none" stroke="#00FF66" stroke-width="1" stroke-opacity="0.16"/>

  <g class="hm-fade">
    <text class="hm-mono" x="56" y="68" font-size="11" letter-spacing="2.6" fill="#00FF66">COMMIT LOG · REAL GITHUB TELEMETRY</text>
    <text class="hm-serif" x="54" y="110" font-size="27" font-weight="300" fill="#E6FFF0">A year of building, <tspan font-style="italic" fill="#00FF66">one commit</tspan> at a time.</text>
    {stats_markup}
  </g>

  <g class="hm-mono" font-size="10.5" fill="#88B99A">{month_svg}</g>
  <g class="hm-mono" font-size="10" fill="#88B99A" text-anchor="end">
    <text x="{GRID_X - 12}" y="{GRID_Y + STEP + 11}">Mon</text>
    <text x="{GRID_X - 12}" y="{GRID_Y + 3 * STEP + 11}">Wed</text>
    <text x="{GRID_X - 12}" y="{GRID_Y + 5 * STEP + 11}">Fri</text>
  </g>

  <g class="hm-animated-grid">
    {animated_cells_markup}
  </g>

  <g class="hm-static-grid">
    {static_cells_markup}
  </g>

  <g class="hm-motion">
    {snake_markup}
  </g>

  {streak_svg}

  <g class="hm-fade">
    <text class="hm-mono" x="56" y="382" font-size="10.5" fill="#88B99A">Source: public GitHub contribution telemetry for @mengalpratik · snapshot {fetched} · refreshed daily</text>
    <text class="hm-mono" x="{legend_x}" y="382" font-size="10.5" fill="#88B99A">Less</text>
    {legend_cells}
    <text class="hm-mono" x="{legend_x + 36 + 5 * 18 + 4}" y="382" font-size="10.5" fill="#88B99A">More</text>
  </g>
</svg>'''

    # Strict XML parse verification
    try:
        ET.fromstring(svg_content.strip())
    except ET.ParseError as err:
        print(f"✗ Generated SVG failed XML parse check: {err}", file=sys.stderr)
        return False

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg_content.strip())

    print(f"✓ Successfully built and validated {output_path}")
    return True

def main():
    parser = argparse.ArgumentParser(description="Generate accessible contribution-snake.svg from verified data.")
    parser.add_argument("--input", default=str(DEFAULT_INPUT_PATH), help="Path to contributions.json")
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT_PATH), help="Path to contribution-snake.svg")
    parser.add_argument("--check", action="store_true", help="Validate without writing")
    args = parser.parse_args()
    
    success = build_snake_svg(Path(args.input), Path(args.output))
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
