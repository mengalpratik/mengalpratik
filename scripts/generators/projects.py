"""
scripts/generators/projects.py

Generates compact, responsive project cards (1200x270) with embedded repository buttons.
"""

from .common import load_projects, validate_and_save_svg, xml_escape

def generate_projects() -> None:
    projects = load_projects()
    
    for p in projects:
        chips_xml = ""
        cx = 50
        for chip in p["chips"]:
            chip_esc = xml_escape(chip)
            cw = len(chip) * 8.5 + 22
            chips_xml += f'''
        <g transform="translate({cx}, 208)">
          <rect width="{cw}" height="24" rx="12" fill="#041207" stroke="#00FF66" stroke-width="0.9" stroke-opacity="0.45"/>
          <text class="p-mono" x="{cw/2}" y="16" text-anchor="middle" font-size="10" font-weight="600" fill="#00FF66">{chip_esc}</text>
        </g>'''
            cx += cw + 10

        metrics_xml = ""
        mx = 50
        for val, lbl in p["metrics"]:
            val_esc = xml_escape(val)
            lbl_esc = xml_escape(lbl)
            metrics_xml += f'''
        <g transform="translate({mx}, 166)">
          <text class="p-heading" font-size="22" fill="#E6FFF0">{val_esc}</text>
          <text class="p-sans" x="0" y="18" font-size="11" fill="#88B99A">{lbl_esc}</text>
        </g>'''
            mx += 175

        title_esc = xml_escape(p["title"])
        desc_esc = xml_escape(p["desc"])
        cat_esc = xml_escape(p["category"])
        built_esc = xml_escape(p["built"])

        svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 270" width="1200" height="270" role="img" aria-labelledby="p-{p['num']}-t">
  <title id="p-{p['num']}-t">{title_esc}: {desc_esc}</title>
  <defs>
    <linearGradient id="p-bg-{p['num']}" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#050F07"/>
      <stop offset="100%" stop-color="#020603"/>
    </linearGradient>
    <radialGradient id="p-glow-{p['num']}" cx="85%" cy="30%" r="75%">
      <stop offset="0" stop-color="#00FF66" stop-opacity="0.2"/>
      <stop offset="100%" stop-color="#00FF66" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="p-trace-{p['num']}" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#00FF66"/>
      <stop offset="100%" stop-color="#05FFA1" stop-opacity="0"/>
    </linearGradient>
  </defs>
  <style>
    .p-mono {{ font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", "Fira Code", monospace; }}
    .p-heading {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Fira Code", monospace; font-weight: 700; }}
    .p-sans {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", sans-serif; }}
    .p-trace {{ stroke-dasharray: 180 900; animation: p-trace 7s linear infinite; }}
    @keyframes p-trace {{ to {{ stroke-dashoffset: -1080; }} }}
    @media (prefers-reduced-motion: reduce) {{ .p-trace {{ animation: none; }} }}
  </style>

  <rect width="1200" height="270" fill="#000000"/>

  <g transform="translate(40, 10)">
    <rect width="1120" height="250" rx="14" fill="url(#p-bg-{p['num']})" stroke="#00FF66" stroke-width="1.2" stroke-opacity="0.3"/>
    <rect width="1120" height="250" rx="14" fill="url(#p-glow-{p['num']})"/>
    <rect class="p-trace" width="1120" height="250" rx="14" fill="none" stroke="url(#p-trace-{p['num']})" stroke-width="1.4"/>

    <!-- Category Pill -->
    <text class="p-mono" x="50" y="38" font-size="11" font-weight="700" letter-spacing="2.2" fill="#00FF66">{p['num']} · {cat_esc}</text>

    <!-- Project Title -->
    <text class="p-heading" x="48" y="76" font-size="34" letter-spacing="-0.8" fill="#E6FFF0">{title_esc}</text>

    <!-- Description -->
    <text class="p-sans" x="50" y="104" font-size="14" fill="#88B99A">{desc_esc}</text>

    <!-- Built Tagline -->
    <text class="p-mono" x="50" y="130" font-size="11.5" fill="#E6FFF0">
      <tspan fill="#05FFA1" font-weight="700">BUILT › </tspan>{built_esc}
    </text>

    <!-- Metrics Column -->
    {metrics_xml}

    <!-- Embedded Cyber Button at bottom right -->
    <g transform="translate(860, 185)">
      <rect width="210" height="38" rx="8" fill="#041A0B" stroke="#00FF66" stroke-width="1.2"/>
      <rect x="0" y="0" width="3" height="38" rx="1.5" fill="#00FF66"/>
      <text class="p-mono" x="18" y="24" font-size="11" font-weight="700" letter-spacing="1.5" fill="#00FF66">⚡ EXPLORE REPO ›</text>
    </g>

    <!-- Tech Stack Chips -->
    {chips_xml}
  </g>
</svg>'''
        validate_and_save_svg(p["filename"], svg)
