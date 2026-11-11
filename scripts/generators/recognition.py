"""
scripts/generators/recognition.py

Generates achievement-motif-v2.svg (and achievement-motif.svg) (1200x430) strictly reproducing
the reference layout: Dual hero cards (700x250 and 476x250) with large background watermark text,
animated connector line at y=300, and 5-column score strip with serif 40 typography.
"""

from .common import load_profile, validate_and_save_svg, xml_escape

def generate_recognition() -> None:
    profile = load_profile()

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 430" width="1200" height="430" role="img" aria-labelledby="ach-title ach-desc">
  <title id="ach-title">Recognition — Proof, on the record.</title>
  <desc id="ach-desc">Google Cybersecurity Professional Certificate (98.81%). Published Research Author in IJNRD 2025. 3+ Industry Internships (Axcentra, Devtown, Codsoft). B.E. Computer Science from DYPIEMR.</desc>

  <defs>
    <linearGradient id="ach-bg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#041207"/>
      <stop offset="1" stop-color="#000000"/>
    </linearGradient>
    <radialGradient id="ach-glow-a" cx="85%" cy="0%" r="90%">
      <stop offset="0" stop-color="#00FF66" stop-opacity=".45"/>
      <stop offset="1" stop-color="#00240E" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="ach-glow-b" cx="90%" cy="0%" r="90%">
      <stop offset="0" stop-color="#05FFA1" stop-opacity=".35"/>
      <stop offset="1" stop-color="#00240E" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="ach-hair" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#00FF66" stop-opacity="0"/>
      <stop offset=".4" stop-color="#00FF66"/>
      <stop offset=".6" stop-color="#05FFA1"/>
      <stop offset="1" stop-color="#05FFA1" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="ach-outline" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#00FF66" stop-opacity=".45"/>
      <stop offset="1" stop-color="#00FF66" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="ach-sheen" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#FFFFFF" stop-opacity="0"/>
      <stop offset=".5" stop-color="#FFFFFF" stop-opacity=".08"/>
      <stop offset="1" stop-color="#FFFFFF" stop-opacity="0"/>
    </linearGradient>
    <clipPath id="ach-clip-a"><rect x="0" y="0" width="700" height="250" rx="16"/></clipPath>
    <clipPath id="ach-clip-b"><rect x="0" y="0" width="476" height="250" rx="16"/></clipPath>
    <linearGradient id="ach-trace" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#E6FFF0"/><stop offset=".45" stop-color="#00FF66"/><stop offset="1" stop-color="#00FF66" stop-opacity="0"/>
    </linearGradient>
  </defs>

  <style>
    .ach-serif {{ font-family: Georgia, "Iowan Old Style", "Palatino Linotype", "Times New Roman", serif; }}
    .ach-mono {{ font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace; }}
    .ach-sans {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; }}
    .ach-in {{ animation: ach-in 1.2s cubic-bezier(.16,1,.3,1) both; }}
    .a1 {{ animation-delay: .1s; }} .a2 {{ animation-delay: .35s; }} .a3 {{ animation-delay: .6s; }}
    .ach-draw {{ stroke-dasharray: 1200; stroke-dashoffset: 1200; animation: ach-draw 2.6s cubic-bezier(.65,0,.35,1) .8s forwards; }}
    @keyframes ach-in {{ from {{ opacity: 0.85; transform: translateY(6px); }} to {{ opacity: 1; transform: none; }} }}
    @keyframes ach-draw {{ to {{ stroke-dashoffset: 0; }} }}
    @media (prefers-reduced-motion: reduce) {{
      .ach-in {{ animation: none; }}
      .ach-draw {{ animation: none; stroke-dashoffset: 0; }}
    }}
    .ach-trace-a {{ stroke-dasharray: 340 1900; stroke-dashoffset: 2240; animation: ach-trace-a 6s linear infinite; }}
    .ach-trace-b {{ stroke-dasharray: 260 1452; stroke-dashoffset: 1712; animation: ach-trace-b 6s linear -3s infinite; }}
    @keyframes ach-trace-a {{ to {{ stroke-dashoffset: 0; }} }}
    @keyframes ach-trace-b {{ to {{ stroke-dashoffset: 0; }} }}
    @media (prefers-reduced-motion: reduce) {{ .ach-trace-a, .ach-trace-b {{ display: none; }} }}
  </style>

  <rect width="1200" height="430" rx="20" fill="url(#ach-bg)"/>
  <rect x=".5" y=".5" width="1199" height="429" rx="19.5" fill="none" stroke="#00FF66" stroke-opacity=".16"/>

  <!-- Google Cybersecurity Hero Card (700x250) -->
  <g class="ach-in a1"><g transform="translate(24 24)">
    <g clip-path="url(#ach-clip-a)">
      <rect width="700" height="250" fill="#020C05"/>
      <rect width="700" height="250" fill="url(#ach-glow-a)"/>
      <text class="ach-serif" x="684" y="124" text-anchor="end" font-size="128" font-weight="300" letter-spacing="-6" fill="url(#ach-outline)">98.81%</text>
      <rect x="-300" y="0" width="260" height="250" fill="url(#ach-sheen)" transform="skewX(-18)">
        <animate attributeName="x" values="-300;900;900" keyTimes="0;.35;1" dur="9s" begin="2s" repeatCount="indefinite"/>
      </rect>
    </g>
    <rect x=".5" y=".5" width="699" height="249" rx="15.5" fill="none" stroke="#00FF66" stroke-opacity=".38"/>
    <rect class="ach-trace-a" x=".5" y=".5" width="699" height="249" rx="15.5" fill="none" stroke="url(#ach-trace)" stroke-width="1.8" stroke-linecap="round"/>
    <rect x="40" y="0" width="300" height="1" fill="url(#ach-hair)"/>
    <text class="ach-mono" x="36" y="154" font-size="12" letter-spacing="2.6" fill="#00FF66">GOOGLE · CYBERSECURITY PROFESSIONAL</text>
    <text class="ach-serif" x="34" y="204" font-size="46" font-weight="300" letter-spacing="-1" fill="#E6FFF0">98.81% Aggregate Score</text>
    <text class="ach-sans" x="36" y="230" font-size="14" fill="#88B99A">Coursera · 8 Specialized Modules · Network Defense &amp; Threat Mitigation</text>
  </g></g>

  <!-- Published Research Hero Card (476x250) -->
  <g class="ach-in a2"><g transform="translate(700 24)">
    <g transform="translate(24 0)">
      <g clip-path="url(#ach-clip-b)">
        <rect width="476" height="250" fill="#020C05"/>
        <rect width="476" height="250" fill="url(#ach-glow-b)"/>
        <text class="ach-serif" x="490" y="132" text-anchor="end" font-size="150" font-style="italic" font-weight="300" letter-spacing="-6" fill="none" stroke="#00FF66" stroke-opacity=".25">IJNRD</text>
      </g>
      <rect x=".5" y=".5" width="475" height="249" rx="15.5" fill="none" stroke="#00FF66" stroke-opacity=".3"/>
      <rect class="ach-trace-b" x=".5" y=".5" width="475" height="249" rx="15.5" fill="none" stroke="url(#ach-trace)" stroke-width="1.8" stroke-linecap="round"/>
      <rect x="40" y="0" width="220" height="1" fill="url(#ach-hair)"/>
      <text class="ach-mono" x="32" y="154" font-size="12" letter-spacing="2.6" fill="#00FF66">INTERNATIONAL JOURNAL · MAY 2025</text>
      <text class="ach-serif" x="30" y="204" font-size="46" font-weight="300" letter-spacing="-1" fill="#E6FFF0">Published Author</text>
      <text class="ach-sans" x="32" y="230" font-size="14" fill="#88B99A">IJNRD Volume 10 · Health Management &amp; Nutrient AI</text>
    </g>
  </g></g>

  <!-- Animated connector across the score strip -->
  <path class="ach-draw" d="M24 300 H1176" stroke="#00FF66" stroke-opacity=".35"/>

  <!-- Score strip: 5 columns -->
  <g class="ach-in a3 ach-sans" font-size="13" fill="#88B99A">
    <g transform="translate(36 300)">
      <circle cx="0" cy="0" r="3.5" fill="#00FF66"/>
      <text class="ach-mono" y="34" font-size="11" letter-spacing="2" fill="#00FF66">ACADEMICS</text>
      <text class="ach-serif" y="78" font-size="40" font-weight="300" fill="#E6FFF0">2025</text>
      <text y="102">B.E. Computer Science · DYPIEMR</text>
    </g>
    <g transform="translate(266 300)">
      <circle cx="0" cy="0" r="3.5" fill="#00FF66"/>
      <text class="ach-mono" y="34" font-size="11" letter-spacing="2" fill="#00FF66">CYBERSECURITY</text>
      <text class="ach-serif" y="78" font-size="40" font-weight="300" fill="#E6FFF0">98.81%</text>
      <text y="102">Google Professional Certificate</text>
    </g>
    <g transform="translate(496 300)">
      <circle cx="0" cy="0" r="3.5" fill="#00FF66"/>
      <text class="ach-mono" y="34" font-size="11" letter-spacing="2" fill="#00FF66">EXPERIENCE</text>
      <text class="ach-serif" y="78" font-size="40" font-weight="300" fill="#E6FFF0">3+</text>
      <text y="102">SWE Trainee &amp; Dev Internships</text>
    </g>
    <g transform="translate(726 300)">
      <circle cx="0" cy="0" r="3.5" fill="#00FF66"/>
      <text class="ach-mono" y="34" font-size="11" letter-spacing="2" fill="#00FF66">RESEARCH</text>
      <text class="ach-serif" y="78" font-size="40" font-weight="300" fill="#E6FFF0">IJNRD</text>
      <text y="102">May 2025 · Paper ID 2505070</text>
    </g>
    <g transform="translate(956 300)">
      <circle cx="0" cy="0" r="3.5" fill="#00FF66"/>
      <text class="ach-mono" y="34" font-size="11" letter-spacing="2" fill="#00FF66">PROBLEM SOLVING</text>
      <text class="ach-serif" y="78" font-size="40" font-weight="300" fill="#E6FFF0">Java</text>
      <text y="102">OOP &amp; Data Structures</text>
    </g>
  </g>
</svg>'''
    validate_and_save_svg("achievement-motif-v2.svg", svg)
    validate_and_save_svg("achievement-motif.svg", svg)
