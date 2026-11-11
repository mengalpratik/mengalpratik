"""
scripts/generators/recognition.py

Generates achievement-motif.svg (1200x420) presenting verified recognition, research, and milestones.
"""

from .common import load_profile, validate_and_save_svg

def generate_recognition() -> None:
    profile = load_profile()
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 420" width="1200" height="420" role="img" aria-labelledby="ach-title ach-desc">
  <title id="ach-title">Recognition, Credentials and Milestones</title>
  <desc id="ach-desc">Google Cybersecurity Professional Certificate (98.81%). Published Research Author in IJNRD 2025. 3+ Software Engineering Internships (Axcentra, Devtown, Codsoft). B.E. Computer Science from DYPIEMR.</desc>
  <defs>
    <linearGradient id="ach-bg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#040D06"/>
      <stop offset="100%" stop-color="#020603"/>
    </linearGradient>
    <radialGradient id="ach-glow-a" cx="85%" cy="10%" r="80%">
      <stop offset="0" stop-color="#00FF66" stop-opacity="0.25"/>
      <stop offset="100%" stop-color="#00FF66" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="ach-glow-b" cx="15%" cy="90%" r="80%">
      <stop offset="0" stop-color="#05FFA1" stop-opacity="0.2"/>
      <stop offset="100%" stop-color="#05FFA1" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="ach-trace" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#00FF66"/>
      <stop offset="50%" stop-color="#05FFA1"/>
      <stop offset="100%" stop-color="#00FF66" stop-opacity="0"/>
    </linearGradient>
  </defs>
  <style>
    .ach-mono {{ font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", "Fira Code", monospace; }}
    .ach-heading {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Fira Code", monospace; font-weight: 700; }}
    .ach-sans {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", sans-serif; }}
    .ach-trace {{ stroke-dasharray: 200 1000; animation: trace 8s linear infinite; }}
    @keyframes trace {{ to {{ stroke-dashoffset: -1200; }} }}
    @media (prefers-reduced-motion: reduce) {{ .ach-trace {{ animation: none; }} }}
  </style>

  <rect width="1200" height="420" fill="#000000"/>

  <!-- Top Feature Cards (Dual Panels) -->
  <g transform="translate(40, 10)">
    <!-- Left Major Panel: Google Cyber & Research -->
    <g transform="translate(0, 0)">
      <rect width="630" height="236" rx="16" fill="url(#ach-bg)" stroke="#00FF66" stroke-width="1.2" stroke-opacity="0.35"/>
      <rect width="630" height="236" rx="16" fill="url(#ach-glow-a)"/>
      <rect class="ach-trace" width="630" height="236" rx="16" fill="none" stroke="url(#ach-trace)" stroke-width="1.5"/>

      <g transform="translate(32, 26)">
        <rect width="250" height="24" rx="4" fill="#00240E" stroke="#00FF66" stroke-width="1"/>
        <text class="ach-mono" x="12" y="16" font-size="10.5" font-weight="700" letter-spacing="1.5" fill="#00FF66">GOOGLE CERTIFIED &amp; RESEARCH</text>
      </g>
      <text class="ach-heading" x="32" y="92" font-size="26" fill="#E6FFF0">Google Cybersecurity &amp; IJNRD Author</text>
      <text class="ach-sans" x="32" y="122" font-size="14" fill="#00FF66" font-weight="600">Aggregate: 98.81 / 100 · Published Author (May 2025)</text>
      <text class="ach-sans" x="32" y="152" font-size="13" fill="#88B99A">
        Co-authored "Health management app: Nutrient analysis and personalized recommendations"
      </text>
      <text class="ach-sans" x="32" y="174" font-size="13" fill="#88B99A">
        published in IJNRD (ISSN: 2456-4184). Certified by Google in Networks, Threat Detection &amp; SQL.
      </text>
      <text class="ach-mono" x="32" y="208" font-size="11" letter-spacing="1.2" fill="#05FFA1">> PROFESSIONAL CERTIFICATE · FORENSICS · THREAT DETECTION</text>
    </g>

    <!-- Right Major Panel: Industry Internships -->
    <g transform="translate(654, 0)">
      <rect width="466" height="236" rx="16" fill="url(#ach-bg)" stroke="#00FF66" stroke-width="1.2" stroke-opacity="0.35"/>
      <rect width="466" height="236" rx="16" fill="url(#ach-glow-b)"/>
      <rect class="ach-trace" style="animation-delay: -4s;" width="466" height="236" rx="16" fill="none" stroke="url(#ach-trace)" stroke-width="1.5"/>

      <g transform="translate(28, 26)">
        <rect width="210" height="24" rx="4" fill="#00240E" stroke="#05FFA1" stroke-width="1"/>
        <text class="ach-mono" x="12" y="16" font-size="10.5" font-weight="700" letter-spacing="1.5" fill="#05FFA1">INDUSTRY EXPERIENCE</text>
      </g>
      <text class="ach-heading" x="28" y="92" font-size="26" fill="#E6FFF0">Full-Stack Industry Track</text>
      <text class="ach-sans" x="28" y="122" font-size="14" fill="#05FFA1" font-weight="600">Axcentra · Devtown · Codsoft</text>
      <text class="ach-sans" x="28" y="152" font-size="13" fill="#88B99A">
        Shipped production web modules at Axcentra; built full-stack MERN apps
      </text>
      <text class="ach-sans" x="28" y="174" font-size="13" fill="#88B99A">
        at Devtown; engineered OOP software at Codsoft.
      </text>
      <text class="ach-mono" x="28" y="208" font-size="11" letter-spacing="1.2" fill="#00FF66">> 3+ INTERNSHIPS · AGILE / SCRUM · MERN</text>
    </g>
  </g>

  <!-- Bottom Score Strip (5 Metrics Columns) -->
  <g class="ach-sans" font-size="13" fill="#88B99A" transform="translate(40, 280)">
    <!-- Col 1 -->
    <g transform="translate(0, 0)">
      <circle cx="12" cy="12" r="3.5" fill="#00FF66"/>
      <text class="ach-mono" x="24" y="16" font-size="11" font-weight="700" letter-spacing="2" fill="#00FF66">CYBERSECURITY</text>
      <text class="ach-heading" x="0" y="60" font-size="38" fill="#E6FFF0">98.81%</text>
      <text x="0" y="84" fill="#88B99A">Google Professional Cert</text>
      <text x="0" y="102" font-size="11" fill="#72A884">Coursera · 8 Specialized Modules</text>
    </g>

    <!-- Col 2 -->
    <g transform="translate(230, 0)">
      <circle cx="12" cy="12" r="3.5" fill="#05FFA1"/>
      <text class="ach-mono" x="24" y="16" font-size="11" font-weight="700" letter-spacing="2" fill="#05FFA1">RESEARCH</text>
      <text class="ach-heading" x="0" y="60" font-size="36" fill="#E6FFF0">IJNRD</text>
      <text x="0" y="84" fill="#88B99A">Published Author 2025</text>
      <text x="0" y="102" font-size="11" fill="#72A884">Health App Nutrient Analysis</text>
    </g>

    <!-- Col 3 -->
    <g transform="translate(460, 0)">
      <circle cx="12" cy="12" r="3.5" fill="#00FF66"/>
      <text class="ach-mono" x="24" y="16" font-size="11" font-weight="700" letter-spacing="2" fill="#00FF66">INTERNSHIPS</text>
      <text class="ach-heading" x="0" y="60" font-size="38" fill="#E6FFF0">3+</text>
      <text x="0" y="84" fill="#88B99A">Industry Work</text>
      <text x="0" y="102" font-size="11" fill="#72A884">Axcentra · Devtown · Codsoft</text>
    </g>

    <!-- Col 4 -->
    <g transform="translate(690, 0)">
      <circle cx="12" cy="12" r="3.5" fill="#05FFA1"/>
      <text class="ach-mono" x="24" y="16" font-size="11" font-weight="700" letter-spacing="2" fill="#05FFA1">REPOSITORIES</text>
      <text class="ach-heading" x="0" y="60" font-size="38" fill="#E6FFF0">24</text>
      <text x="0" y="84" fill="#88B99A">Public Repositories</text>
      <text x="0" y="102" font-size="11" fill="#72A884">Open Source &amp; Systems</text>
    </g>

    <!-- Col 5 -->
    <g transform="translate(930, 0)">
      <circle cx="12" cy="12" r="3.5" fill="#00FF66"/>
      <text class="ach-mono" x="24" y="16" font-size="11" font-weight="700" letter-spacing="2" fill="#00FF66">ACADEMICS</text>
      <text class="ach-heading" x="0" y="60" font-size="34" fill="#E6FFF0">B.E. CSE</text>
      <text x="0" y="84" fill="#88B99A">{profile["education"]["short_institution"]}</text>
      <text x="0" y="102" font-size="11" fill="#72A884">Computer Science &amp; Eng.</text>
    </g>
  </g>
</svg>'''
    validate_and_save_svg("achievement-motif.svg", svg)
