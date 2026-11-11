"""
scripts/generators/titles.py

Generates compact, accessible section title banners (1200x90) with reduced-motion support.
"""

from .common import validate_and_save_svg

TITLES_CONFIG = [
    ("title-about.svg", "01", "KERNEL // PROFILE", "About — Initializing System Specs.", "WHO I AM"),
    ("title-recognition.svg", "02", "BENCHMARKS // PROOF", "Recognition — Proof, on the record.", "MILESTONES"),
    ("title-work.svg", "03", "SHIPPED SYSTEMS // PRODUCTION", "Selected work — Products, not assignments.", "CODEBASES"),
    ("title-toolkit.svg", "04", "NEURAL CORE // STACK", "Toolkit — The tools I reach for.", "TECH STACK"),
    ("title-commits.svg", "05", "TELEMETRY // BUILDS", "Commit telemetry — Continuous builds.", "ACTIVITY"),
    ("title-certifications.svg", "06", "CREDENTIALS &amp; BADGES // PROOF", "Certifications &amp; Earned Badges — Verified.", "EDUCATION"),
    ("title-connect.svg", "07", "TRANSMISSION // NETWORK", "Connect — Let's build something extraordinary.", "OPEN CHANNELS"),
]

def generate_titles() -> None:
    for filename, num, sub, heading, tag in TITLES_CONFIG:
        left_heading = heading.split("—")[0] + "— " if "—" in heading else heading
        right_heading = heading.split("—")[1] if "—" in heading else ""
        
        svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 90" width="1200" height="90" role="img" aria-labelledby="t-title-{num}">
  <title id="t-title-{num}">{num} {heading}</title>
  <defs>
    <linearGradient id="ta-line-{num}" x1="40" y1="0" x2="1160" y2="0" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="#00FF66"/>
      <stop offset="0.6" stop-color="#00471B"/>
      <stop offset="1" stop-color="#00471B" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="ta-sheen-{num}" x1="-300" y1="0" x2="0" y2="0" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="#E6FFF0"/>
      <stop offset="0.5" stop-color="#00FF66"/>
      <stop offset="1" stop-color="#E6FFF0"/>
      <animateTransform attributeName="gradientTransform" type="translate" values="0 0; 1500 0; 1500 0" keyTimes="0; 0.4; 1" dur="7s" begin="1s" repeatCount="indefinite"/>
    </linearGradient>
    <radialGradient id="ta-pulse-{num}">
      <stop offset="0" stop-color="#FFFFFF"/>
      <stop offset="0.4" stop-color="#00FF66" stop-opacity="0.8"/>
      <stop offset="1" stop-color="#00FF66" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <style>
    .ta-mono {{ font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", "Fira Code", monospace; }}
    .ta-heading {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Fira Code", monospace; font-weight: 700; }}
    @media (prefers-reduced-motion: reduce) {{
      .ta-motion {{ display: none; }}
    }}
  </style>

  <rect width="1200" height="90" fill="#000000"/>

  <!-- Top Metadata Indicator -->
  <g transform="translate(40, 24)">
    <rect width="48" height="18" rx="3" fill="#041207" stroke="#00FF66" stroke-width="0.8"/>
    <text class="ta-mono" x="8" y="13" font-size="10.5" font-weight="700" letter-spacing="1.5" fill="#00FF66">[{num}]</text>
    <text class="ta-mono" x="62" y="13" font-size="10.5" letter-spacing="2.2" fill="#72A884">{sub}</text>
  </g>

  <!-- Section Heading -->
  <text class="ta-heading" x="38" y="64" font-size="34" letter-spacing="-0.5" fill="#E6FFF0">
    {left_heading}<tspan fill="url(#ta-sheen-{num})">{right_heading}</tspan>
  </text>

  <!-- Right Tag -->
  <text class="ta-mono" x="1160" y="24" text-anchor="end" font-size="10.5" letter-spacing="2.4" fill="#00FF66">{tag}</text>

  <!-- Base Rule Line -->
  <path d="M40 82 H1160" stroke="url(#ta-line-{num})" stroke-width="1.2"/>

  <!-- Traveling Pulse Laser Dot -->
  <g class="ta-motion">
    <circle cx="40" cy="82" r="5" fill="url(#ta-pulse-{num})" opacity="0">
      <animate attributeName="cx" values="40;1160" dur="6s" begin="1.2s" repeatCount="indefinite" calcMode="spline" keyTimes="0;1" keySplines=".45 0 .55 1"/>
      <animate attributeName="opacity" values="0;1;0" keyTimes="0;0.15;1" dur="6s" begin="1.2s" repeatCount="indefinite"/>
    </circle>
  </g>
</svg>'''
        validate_and_save_svg(filename, svg)
