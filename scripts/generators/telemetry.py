"""
scripts/generators/telemetry.py

Generates github-telemetry.svg (1200x240) rendering verified repository metrics and language telemetry.
"""

from .common import load_telemetry, validate_and_save_svg

def generate_telemetry() -> None:
    data = load_telemetry()
    langs = data["languages"]
    
    # 5 language telemetry bars
    lang_bars_xml = []
    base_bar_w = 460
    for i, l in enumerate(langs):
        y_off = i * 30
        pct = l["pct"]
        bar_fill_w = max(int(base_bar_w * (pct / 100.0)), 6)
        color = l["color"]
        
        lang_bars_xml.append(f'''<g transform="translate(0, {y_off})">
          <text class="tel-mono" x="0" y="10" font-size="11" font-weight="600" fill="#E6FFF0">{l["name"]}</text>
          <text class="tel-mono" x="460" y="10" text-anchor="end" font-size="11" font-weight="700" fill="{color}">{pct}%</text>
          <rect x="0" y="16" width="460" height="6" rx="3" fill="#020D05"/>
          <rect x="0" y="16" width="{bar_fill_w}" height="6" rx="3" fill="{color}"/>
        </g>''')
        
    lang_bars_markup = "\n        ".join(lang_bars_xml)

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 240" width="1200" height="240" role="img" aria-labelledby="tel-title tel-desc">
  <title id="tel-title">GitHub Telemetry &amp; Language Distribution</title>
  <desc id="tel-desc">Real telemetry metrics: {data["public_repos"]} Public Repos, {data["contributions_year"]} Verified Contributions, {data["peak_daily_velocity"]} Peak Daily Velocity. Top languages: TypeScript 32%, JavaScript 28%, Python 21%, CSS &amp; HTML 14%, Java 5%.</desc>
  <defs>
    <linearGradient id="tel-bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#050F07"/>
      <stop offset="100%" stop-color="#020603"/>
    </linearGradient>
    <radialGradient id="tel-glow" cx="80%" cy="30%" r="70%">
      <stop offset="0" stop-color="#00FF66" stop-opacity="0.18"/>
      <stop offset="100%" stop-color="#00FF66" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="tel-trace" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#00FF66"/>
      <stop offset="50%" stop-color="#05FFA1"/>
      <stop offset="100%" stop-color="#00FF66" stop-opacity="0"/>
    </linearGradient>
  </defs>
  <style>
    .tel-mono {{ font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", "Fira Code", monospace; }}
    .tel-heading {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Fira Code", monospace; font-weight: 700; }}
    .tel-sans {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", sans-serif; }}
    .tel-trace {{ stroke-dasharray: 200 1100; animation: tel-trace 8s linear infinite; }}
    @keyframes tel-trace {{ to {{ stroke-dashoffset: -1300; }} }}
    @media (prefers-reduced-motion: reduce) {{ .tel-trace {{ animation: none; }} }}
  </style>

  <rect width="1200" height="240" fill="#000000"/>

  <g transform="translate(40, 10)">
    <rect width="1120" height="220" rx="14" fill="url(#tel-bg)" stroke="#00FF66" stroke-width="1.2" stroke-opacity="0.3"/>
    <rect width="1120" height="220" rx="14" fill="url(#tel-glow)"/>
    <rect class="tel-trace" width="1120" height="220" rx="14" fill="none" stroke="url(#tel-trace)" stroke-width="1.4"/>

    <!-- LEFT COLUMN: 4 METRICS CARDS -->
    <g transform="translate(36, 26)">
      <text class="tel-mono" x="0" y="0" font-size="10.5" font-weight="700" letter-spacing="2" fill="#00FF66">GITHUB TELEMETRY &amp; METRICS</text>

      <g transform="translate(0, 18)">
        <!-- Metric 1: Repos -->
        <g transform="translate(0, 0)">
          <rect width="240" height="66" rx="8" fill="#030C05" stroke="#00FF66" stroke-width="0.8" stroke-opacity="0.4"/>
          <rect x="0" y="0" width="3" height="66" rx="1.5" fill="#00FF66"/>
          <text class="tel-mono" x="16" y="24" font-size="9.5" font-weight="700" letter-spacing="1.5" fill="#72A884">PUBLIC REPOSITORIES</text>
          <text class="tel-heading" x="16" y="52" font-size="26" fill="#E6FFF0">{data["public_repos"]} <tspan font-size="12" fill="#00FF66">REPOS</tspan></text>
        </g>

        <!-- Metric 2: Total Contributions -->
        <g transform="translate(260, 0)">
          <rect width="240" height="66" rx="8" fill="#030C05" stroke="#05FFA1" stroke-width="0.8" stroke-opacity="0.4"/>
          <rect x="0" y="0" width="3" height="66" rx="1.5" fill="#05FFA1"/>
          <text class="tel-mono" x="16" y="24" font-size="9.5" font-weight="700" letter-spacing="1.5" fill="#72A884">VERIFIED CONTRIBUTIONS</text>
          <text class="tel-heading" x="16" y="52" font-size="26" fill="#E6FFF0">{data["contributions_year"]} <tspan font-size="12" fill="#05FFA1">YEAR</tspan></text>
        </g>

        <!-- Metric 3: Peak Velocity -->
        <g transform="translate(0, 78)">
          <rect width="240" height="66" rx="8" fill="#030C05" stroke="#05FFA1" stroke-width="0.8" stroke-opacity="0.4"/>
          <rect x="0" y="0" width="3" height="66" rx="1.5" fill="#05FFA1"/>
          <text class="tel-mono" x="16" y="24" font-size="9.5" font-weight="700" letter-spacing="1.5" fill="#72A884">PEAK VELOCITY</text>
          <text class="tel-heading" x="16" y="52" font-size="26" fill="#E6FFF0">{data["peak_daily_velocity"]} <tspan font-size="12" fill="#05FFA1">CONTRIBS / DAY</tspan></text>
        </g>

        <!-- Metric 4: Codebase Health -->
        <g transform="translate(260, 78)">
          <rect width="240" height="66" rx="8" fill="#030C05" stroke="#00FF66" stroke-width="0.8" stroke-opacity="0.4"/>
          <rect x="0" y="0" width="3" height="66" rx="1.5" fill="#00FF66"/>
          <text class="tel-mono" x="16" y="24" font-size="9.5" font-weight="700" letter-spacing="1.5" fill="#72A884">OPEN ACCESS</text>
          <text class="tel-heading" x="16" y="52" font-size="26" fill="#E6FFF0">100% <tspan font-size="12" fill="#00FF66">PUBLIC ACCESS</tspan></text>
        </g>
      </g>
    </g>

    <!-- Vertical Divider -->
    <line x1="566" y1="26" x2="566" y2="194" stroke="#003B19" stroke-width="1.2" stroke-dasharray="6 4"/>

    <!-- RIGHT COLUMN: TOP LANGUAGES BREAKDOWN -->
    <g transform="translate(596, 26)">
      <text class="tel-mono" x="0" y="0" font-size="10.5" font-weight="700" letter-spacing="2" fill="#05FFA1">PRIMARY LANGUAGE TELEMETRY</text>

      <!-- Language Bars -->
      <g transform="translate(0, 20)">
        {lang_bars_markup}
      </g>
    </g>
  </g>
</svg>'''
    validate_and_save_svg("github-telemetry.svg", svg)
