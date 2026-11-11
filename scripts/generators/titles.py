"""
scripts/generators/titles.py

Generates section title banners (1200x120) strictly matching reference layout geometry,
typography hierarchy, and Hacker Green theme with reduced-motion support.
"""

from .common import validate_and_save_svg, xml_escape

TITLES_CONFIG = [
    ("title-about.svg", "01", "ABOUT", "Hello, I'm", "Pratik.", "WHO I AM"),
    ("title-recognition.svg", "02", "RECOGNITION", "Proof,", "on the record.", "CYBERSECURITY · RESEARCH · INDUSTRY"),
    ("title-work.svg", "03", "SELECTED WORK", "Products, not", "assignments.", "FOUR SYSTEMS · REAL CONSTRAINTS"),
    ("title-toolkit.svg", "04", "TOOLKIT", "The tools I", "reach for.", "LANGUAGES · MERN · CYBER · AI · CLOUD"),
    ("title-commits.svg", "05", "COMMIT LOG", "A year of", "building.", "REAL DATA · REFRESHED DAILY"),
    ("title-certifications.svg", "06", "CERTIFICATIONS", "Earned credentials,", "verified.", "GOOGLE · CISCO · ORACLE · UDEMY"),
    ("title-connect.svg", "07", "CONNECT", "Let's build something", "extraordinary.", "OPEN INBOX"),
]

def generate_titles() -> None:
    for filename, num, section_name, left_heading, right_heading, tag in TITLES_CONFIG:
        left_esc = xml_escape(left_heading)
        right_esc = xml_escape(right_heading)
        tag_esc = xml_escape(tag)
        sec_esc = xml_escape(section_name)
        full_title_esc = f"{num} {sec_esc}: {left_esc} {right_esc}"

        svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 120" width="1200" height="120" role="img" aria-label="{full_title_esc}">
  <defs>
    <linearGradient id="ta-line" gradientUnits="userSpaceOnUse" x1="40" y1="0" x2="1160" y2="0">
      <stop offset="0" stop-color="#00FF66"/>
      <stop offset=".6" stop-color="#00471B"/>
      <stop offset="1" stop-color="#00471B" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="ta-sheen" gradientUnits="userSpaceOnUse" x1="-300" y1="0" x2="0" y2="0">
      <stop offset="0" stop-color="#E6FFF0"/>
      <stop offset=".5" stop-color="#00FF66"/>
      <stop offset="1" stop-color="#E6FFF0"/>
      <animateTransform attributeName="gradientTransform" type="translate" values="0 0;1500 0;1500 0" keyTimes="0;.4;1" dur="7s" begin="1.5s" repeatCount="indefinite"/>
    </linearGradient>
    <radialGradient id="ta-pulse">
      <stop offset="0" stop-color="#FFFFFF"/>
      <stop offset=".5" stop-color="#00FF66" stop-opacity=".6"/>
      <stop offset="1" stop-color="#00FF66" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <style>
    .ta-serif {{ font-family: Georgia, "Iowan Old Style", "Palatino Linotype", "Times New Roman", serif; }}
    .ta-mono {{ font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace; }}
    .ta-sans {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; }}
    .ta-in {{ animation: ta-in 0.8s cubic-bezier(.16,1,.3,1) both; }}
    .ta-d2 {{ animation-delay: .1s; }} .ta-d3 {{ animation-delay: .2s; }}
    .ta-draw {{ stroke-dasharray: 1200; stroke-dashoffset: 1200; animation: ta-draw 1.8s cubic-bezier(.65,0,.35,1) .5s forwards; }}
    @keyframes ta-in {{ from {{ opacity: 0.85; transform: translateY(6px); }} to {{ opacity: 1; transform: none; }} }}
    @keyframes ta-draw {{ to {{ stroke-dashoffset: 0; }} }}
    @media (prefers-reduced-motion: reduce) {{ .ta-in {{ animation: none; }} .ta-draw {{ animation: none; stroke-dashoffset: 0; }} }}
  </style>
  <g class="ta-in">
    <text class="ta-mono" x="40" y="34" font-size="12" letter-spacing="3" fill="#88B99A"><tspan fill="#00FF66">{num}</tspan>   {sec_esc}</text>
  </g>
  <g class="ta-in ta-d2">
    <text class="ta-serif" x="38" y="84" font-size="44" font-weight="300" letter-spacing="-1" fill="#E6FFF0">{left_esc} <tspan font-style="italic" fill="url(#ta-sheen)">{right_esc}</tspan></text>
  </g>
  <g class="ta-in ta-d3">
    <text class="ta-mono" x="1160" y="34" text-anchor="end" font-size="10.5" letter-spacing="2.4" fill="#88B99A">{tag_esc}</text>
  </g>
  <path class="ta-draw" d="M40 106 H1160" stroke="url(#ta-line)" stroke-width="1"/>
  <circle cx="40" cy="106" r="7" fill="url(#ta-pulse)" opacity="0">
    <animate attributeName="cx" values="40;1160" dur="6s" begin="2.3s" repeatCount="indefinite" calcMode="spline" keyTimes="0;1" keySplines=".45 0 .55 1"/>
    <animate attributeName="opacity" values="0;1;0" keyTimes="0;.15;1" dur="6s" begin="2.3s" repeatCount="indefinite"/>
  </circle>
</svg>'''
        validate_and_save_svg(filename, svg)
