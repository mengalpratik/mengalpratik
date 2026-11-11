"""
scripts/generators/about.py

Generates about-intro.svg (1200x410) with terminal frame, narrative bio, and focus highlight cards.
"""

from .common import load_profile, validate_and_save_svg, xml_escape

def generate_about() -> None:
    profile = load_profile()
    cards = profile["focus_cards"]
    
    cards_xml = []
    card_offsets = [0, 358, 716]
    for i, c in enumerate(cards):
        cx = card_offsets[i]
        accent = c["accent"]
        cards_xml.append(f'''<g class="ab-card" transform="translate({cx}, 0)">
        <rect width="338" height="126" rx="12" fill="#030C05" stroke="#00FF66" stroke-width="1" stroke-opacity="0.35"/>
        <rect x="0" y="0" width="4" height="126" rx="2" fill="{accent}"/>
        <text class="ab-mono" x="20" y="30" font-size="10.5" font-weight="700" letter-spacing="2" fill="{accent}">{xml_escape(c["category"])}</text>
        <text class="ab-heading" x="20" y="65" font-size="19.5" letter-spacing="-0.3" fill="#E6FFF0">{xml_escape(c["primary"])}</text>
        <text class="ab-sans" x="20" y="94" font-size="13" fill="#88B99A">{xml_escape(c["secondary"])}</text>
      </g>''')
      
    cards_markup = "\n      ".join(cards_xml)

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 410" width="1200" height="410" role="img" aria-labelledby="ab-title ab-desc">
  <title id="ab-title">About {xml_escape(profile["name"])}</title>
  <desc id="ab-desc">{xml_escape(profile["title"])}. {xml_escape(profile["education"]["degree"])} at {xml_escape(profile["education"]["short_institution"])}. Google Cybersecurity Certified (98.81%). Axcentra SWE Intern. Primary languages TypeScript, Python and Java.</desc>
  <defs>
    <linearGradient id="ab-bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#050F07"/>
      <stop offset="100%" stop-color="#020603"/>
    </linearGradient>
    <radialGradient id="ab-glow" cx="80%" cy="20%" r="70%">
      <stop offset="0" stop-color="#00FF66" stop-opacity="0.18"/>
      <stop offset="100%" stop-color="#00FF66" stop-opacity="0"/>
    </radialGradient>
    <pattern id="ab-scan" width="4" height="4" patternUnits="userSpaceOnUse">
      <rect width="4" height="1" fill="#00FF66" opacity="0.04"/>
    </pattern>
  </defs>
  <style>
    .ab-mono {{ font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", "Fira Code", monospace; }}
    .ab-heading {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Fira Code", monospace; font-weight: 700; }}
    .ab-sans {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", sans-serif; }}
    .ab-card {{ transition: transform 0.2s ease; }}
  </style>

  <g transform="translate(40, 10)">
    <rect width="1120" height="390" rx="16" fill="url(#ab-bg)" stroke="#00FF66" stroke-width="1.2" stroke-opacity="0.3"/>
    <rect width="1120" height="390" rx="16" fill="url(#ab-glow)"/>
    <rect width="1120" height="390" rx="16" fill="url(#ab-scan)"/>

    <!-- Terminal Window Top Bar -->
    <path d="M 0 16 A 16 16 0 0 1 16 0 L 1104 0 A 16 16 0 0 1 1120 16 L 1120 40 L 0 40 Z" fill="#020904" stroke="#003B19" stroke-width="1"/>
    <circle cx="28" cy="20" r="5" fill="#FF5F56" fill-opacity="0.8"/>
    <circle cx="46" cy="20" r="5" fill="#FFBD2E" fill-opacity="0.8"/>
    <circle cx="64" cy="20" r="5" fill="#27C93F" fill-opacity="0.8"/>
    <text class="ab-mono" x="560" y="24" text-anchor="middle" font-size="11" letter-spacing="1.5" fill="#72A884">neuro-terminal://profile/pratik_mengal.sys</text>

    <!-- Shell Prompt -->
    <text class="ab-mono" x="32" y="70" font-size="13" fill="#05FFA1">
      <tspan fill="#00FF66">{profile["handle"]}@neuro-box:~$</tspan> cat /sys/dev/profile_summary.md
    </text>

    <!-- Narrative Intro -->
    <g class="ab-sans" font-size="16" fill="#E6FFF0" transform="translate(32, 90)">
      <text x="0" y="20">
        I am a <tspan font-weight="700" fill="#00FF66">Full-Stack Software Engineer</tspan> and <tspan font-weight="700" fill="#05FFA1">Google Certified Cybersecurity Analyst (98.81%)</tspan> graduating with B.E. from <tspan font-weight="600" fill="#E6FFF0">DYPIEMR</tspan>, Pune.
      </text>
      <text x="0" y="48" fill="#88B99A">
        Co-authored published research in <tspan fill="#00FF66" font-weight="600">IJNRD (May 2025)</tspan> on health management systems with nutrient analysis &amp; personalized recommendations.
      </text>
      <text x="0" y="76" fill="#88B99A">
        Proven industry experience across <tspan fill="#00FF66">Axcentra</tspan> (Software Engineering Trainee), <tspan fill="#E6FFF0">Devtown</tspan> (Full-Stack MERN Intern), and <tspan fill="#E6FFF0">Codsoft</tspan> (Java Software Developer).
      </text>
      <text x="0" y="104" fill="#88B99A">
        Shipped systems include <tspan fill="#E6FFF0">NeuroMatrix</tspan> (Python Academy), <tspan fill="#E6FFF0">Myraa AI Assistant</tspan> (multi-modal agent), and <tspan fill="#E6FFF0">NEURO//NODE</tspan> (local dashboard).
      </text>
    </g>

    <!-- 3 Bottom Focus Highlight Cards -->
    <g transform="translate(32, 236)">
      {cards_markup}
    </g>
  </g>
</svg>'''
    validate_and_save_svg("about-intro.svg", svg)
