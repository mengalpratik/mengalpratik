"""
scripts/generators/hero.py

Generates hero-banner.svg (1200x480) strictly reproducing the reference layout composition:
editorial serif typography, orbital radar system, arch portrait frame, terminal indicator,
and Hacker Green / Pitch Black theme.
"""

from .common import load_profile, get_avatar_b64, validate_and_save_svg, xml_escape

def generate_hero() -> None:
    profile = load_profile()
    avatar_b64 = get_avatar_b64()
    
    avatar_markup = (
        f'''<image href="data:image/jpeg;base64,{avatar_b64}" x="847" y="84" width="236" height="296" preserveAspectRatio="xMidYMid slice"/>
        <rect x="847" y="84" width="236" height="296" fill="#00FF66" fill-opacity="0.15" style="mix-blend-mode: screen;"/>
        <rect x="847" y="84" width="236" height="296" fill="#020D05" fill-opacity="0.25" style="mix-blend-mode: multiply;"/>'''
        if avatar_b64 else
        '''<rect x="847" y="84" width="236" height="296" fill="#020E05"/>
        <path d="M 850 120 L 1080 120 M 850 160 L 1080 160 M 850 200 L 1080 200 M 850 240 L 1080 240 M 850 280 L 1080 280 M 850 320 L 1080 320" stroke="#00FF66" stroke-opacity="0.12" stroke-width="1"/>
        <path d="M 890 90 L 890 380 M 930 90 L 930 380 M 970 90 L 970 380 M 1010 90 L 1010 380 M 1050 90 L 1050 380" stroke="#00FF66" stroke-opacity="0.12" stroke-width="1"/>
        <circle cx="965" cy="232" r="60" fill="none" stroke="#00FF66" stroke-width="1" stroke-opacity="0.4"/>
        <circle cx="965" cy="232" r="30" fill="#00FF66" fill-opacity="0.15"/>
        <text class="hero-mono" x="965" y="236" text-anchor="middle" font-size="12" letter-spacing="2" fill="#00FF66">CYBER//CORE</text>'''
    )

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 480" width="1200" height="480" role="img" aria-labelledby="hero-title hero-desc">
  <title id="hero-title">{xml_escape(profile["name"])} — {xml_escape(profile["tagline"])}</title>
  <desc id="hero-desc">{xml_escape(profile["title"])}. {xml_escape(profile["education"]["degree"])} at {xml_escape(profile["education"]["short_institution"])}. Google Cybersecurity Certified (98.81%).</desc>

  <defs>
    <radialGradient id="hero-bg" cx="72%" cy="38%" r="80%">
      <stop offset="0" stop-color="#041408"/>
      <stop offset="0.55" stop-color="#020A04"/>
      <stop offset="1" stop-color="#000000"/>
    </radialGradient>
    <radialGradient id="hero-light-a" cx="50%" cy="50%" r="50%">
      <stop offset="0" stop-color="#00FF66" stop-opacity="0.45"/>
      <stop offset="1" stop-color="#00FF66" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="hero-light-b" cx="50%" cy="50%" r="50%">
      <stop offset="0" stop-color="#05FFA1" stop-opacity="0.25"/>
      <stop offset="1" stop-color="#05FFA1" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="hero-name-grad" x1="60" y1="0" x2="420" y2="0" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="#E6FFF0"/>
      <stop offset="0.55" stop-color="#00FF66"/>
      <stop offset="1" stop-color="#05FFA1"/>
    </linearGradient>
    <linearGradient id="hero-sheen" x1="-260" y1="0" x2="-40" y2="0" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="#E6FFF0" stop-opacity="0"/>
      <stop offset="0.5" stop-color="#FFFFFF" stop-opacity="0.85"/>
      <stop offset="1" stop-color="#E6FFF0" stop-opacity="0"/>
      <animateTransform attributeName="gradientTransform" type="translate" values="0 0; 760 0; 760 0" keyTimes="0; 0.35; 1" dur="8s" begin="3s" repeatCount="indefinite"/>
    </linearGradient>
    <linearGradient id="hero-scan" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#00FF66" stop-opacity="0"/>
      <stop offset="0.5" stop-color="#00FF66" stop-opacity="0.04"/>
      <stop offset="1" stop-color="#00FF66" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="hero-rule" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#00FF66" stop-opacity="0"/>
      <stop offset="0.2" stop-color="#05FFA1"/>
      <stop offset="0.75" stop-color="#00471B"/>
      <stop offset="1" stop-color="#00471B" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="hero-orbit-grad" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#00FF66" stop-opacity="0.6"/>
      <stop offset="0.5" stop-color="#05FFA1" stop-opacity="0.2"/>
      <stop offset="1" stop-color="#00FF66" stop-opacity="0"/>
    </linearGradient>
    <clipPath id="hero-arch">
      <path d="M847 380 V202 A118 118 0 0 1 1083 202 V380 Z"/>
    </clipPath>
    <filter id="hero-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="glow"/>
      <feMerge>
        <feMergeNode in="glow"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>

  <style>
    .hero-serif {{ font-family: Georgia, "Iowan Old Style", "Palatino Linotype", "Times New Roman", serif; }}
    .hero-mono {{ font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace; }}
    .hero-sans {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; }}
    .hero-rise {{ animation: hero-rise 1s cubic-bezier(.16,1,.3,1) both; }}
    .hero-fade {{ animation: hero-fade 1.2s ease both; }}
    .d1 {{ animation-delay: .05s; }}
    .d2 {{ animation-delay: .15s; }}
    .d3 {{ animation-delay: .25s; }}
    .d4 {{ animation-delay: .35s; }}
    .d5 {{ animation-delay: .45s; }}
    .d6 {{ animation-delay: .55s; }}
    .hero-draw {{ stroke-dasharray: 600; stroke-dashoffset: 600; animation: hero-draw 2.2s cubic-bezier(.65,0,.35,1) .6s forwards; }}
    .hero-signal {{ stroke-dasharray: 400; stroke-dashoffset: 400; animation: hero-signal 2.6s cubic-bezier(.65,0,.35,1) 1.2s forwards; }}
    @keyframes hero-rise {{ from {{ opacity: 0.85; transform: translateY(8px); }} to {{ opacity: 1; transform: none; }} }}
    @keyframes hero-fade {{ from {{ opacity: 0.85; }} to {{ opacity: 1; }} }}
    @keyframes hero-draw {{ to {{ stroke-dashoffset: 0; }} }}
    @keyframes hero-signal {{ to {{ stroke-dashoffset: 0; }} }}
    @media (prefers-reduced-motion: reduce) {{
      .hero-rise, .hero-fade {{ animation: none; }}
      .hero-draw, .hero-signal {{ animation: none; stroke-dashoffset: 0; }}
      .hero-motion {{ display: none; }}
    }}
  </style>

  <rect width="1200" height="480" rx="20" fill="url(#hero-bg)"/>
  <rect width="1200" height="480" rx="20" fill="url(#hero-scan)"/>

  <!-- Ambient light pool behind the portrait -->
  <circle cx="965" cy="232" r="280" fill="url(#hero-light-a)"/>
  <circle cx="965" cy="232" r="160" fill="url(#hero-light-b)"/>

  <!-- Orbital system circling the portrait -->
  <g transform="translate(965 232)" class="hero-fade d3">
    <circle r="212" fill="none" stroke="#00FF66" stroke-opacity=".12" stroke-dasharray="1 10">
      <animateTransform attributeName="transform" type="rotate" from="0" to="-360" dur="140s" repeatCount="indefinite"/>
    </circle>
    <circle r="190" fill="none" stroke="url(#hero-orbit-grad)" stroke-width="1"/>
    <circle r="160" fill="none" stroke="#00FF66" stroke-opacity=".18" stroke-dasharray="2 7"/>
    <g>
      <animateTransform attributeName="transform" type="rotate" from="360" to="0" dur="95s" repeatCount="indefinite"/>
      <circle cx="0" cy="160" r="2.5" fill="#E6FFF0"/>
      <circle cx="-160" cy="0" r="2" fill="#00FF66" fill-opacity=".7"/>
    </g>
    <!-- Orbital Nodes & Labels -->
    <g class="hero-mono" font-size="9" letter-spacing="1.5" fill="#88B99A">
      <g transform="translate(-6 -190)"><circle r="3" fill="#00FF66"/><text x="10" y="4" fill="#00FF66">AI</text></g>
      <g transform="translate(150 -96)"><circle r="3" fill="#05FFA1"/><text x="10" y="4" fill="#05FFA1">MERN</text></g>
      <g transform="translate(150 110)"><circle r="3" fill="#00FF66"/><text x="10" y="4" fill="#00FF66">CYBER</text></g>
      <g transform="translate(-158 40)"><circle r="3" fill="#05FFA1"/><text x="-14" y="4" text-anchor="end" fill="#05FFA1">DATA</text></g>
    </g>
  </g>

  <!-- Portrait Arch -->
  <g class="hero-fade d4">
    <path d="M835 392 V202 A130 130 0 0 1 1095 202 V392 Z" fill="none" stroke="#00FF66" stroke-opacity=".25">
      <animate attributeName="stroke-opacity" values=".15;.45;.15" dur="5s" repeatCount="indefinite"/>
    </path>
    <g clip-path="url(#hero-arch)">
      {avatar_markup}
    </g>
  </g>

  <!-- Signal path drawing itself through the composition -->
  <path class="hero-signal" d="M600 342 C 680 338, 740 330, 780 318 S 828 300, 847 300" fill="none" stroke="#00FF66" stroke-opacity=".5" stroke-width="1.2"/>
  <circle cx="600" cy="342" r="3" fill="#E6FFF0" filter="url(#hero-glow)" opacity=".9">
    <animateMotion dur="5s" repeatCount="indefinite" begin="4.4s" path="M600 342 C 680 338, 740 330, 780 318 S 828 300, 847 300" keyPoints="0;1" keyTimes="0;1" calcMode="spline" keySplines=".45 0 .55 1"/>
  </circle>

  <!-- Terminal indicator -->
  <g class="hero-fade d1" transform="translate(72 64)">
    <rect width="322" height="34" rx="17" fill="#030E06" stroke="#00FF66" stroke-opacity=".3"/>
    <circle cx="20" cy="17" r="4" fill="#00FF66">
      <animate attributeName="opacity" values="1;.35;1" dur="2.4s" repeatCount="indefinite"/>
    </circle>
    <text class="hero-mono" x="34" y="21.5" font-size="12" fill="#88B99A">~/mengalpratik<tspan fill="#00FF66"> $ </tspan><tspan fill="#E6FFF0">build --resilient</tspan></text>
    <rect x="300" y="10" width="7" height="14" fill="#00FF66">
      <animate attributeName="opacity" values="1;1;0;0" keyTimes="0;.5;.5;1" dur="1.1s" repeatCount="indefinite"/>
    </rect>
  </g>

  <!-- Eyebrow -->
  <g class="hero-rise d2">
    <line x1="72" y1="136" x2="104" y2="136" stroke="#00FF66"/>
    <text class="hero-mono" x="116" y="140" font-size="12.5" letter-spacing="3.4" fill="#00FF66">FULL-STACK · CYBERSECURITY · AI SYSTEMS</text>
  </g>

  <!-- Editorial Name -->
  <text class="hero-serif hero-rise d3" x="68" y="230" font-size="92" font-weight="300" letter-spacing="-2.5" fill="#E6FFF0">Pratik</text>
  <text class="hero-serif hero-rise d4" x="68" y="318" font-size="92" font-style="italic" font-weight="300" letter-spacing="-2.5" fill="url(#hero-name-grad)">Mengal<tspan fill="#00FF66">.</tspan></text>

  <!-- Light sweeping across the name -->
  <g class="hero-fade d6" pointer-events="none">
    <text class="hero-serif" x="68" y="230" font-size="92" font-weight="300" letter-spacing="-2.5" fill="url(#hero-sheen)">Pratik</text>
    <text class="hero-serif" x="68" y="318" font-size="92" font-style="italic" font-weight="300" letter-spacing="-2.5" fill="url(#hero-sheen)">Mengal.</text>
  </g>

  <!-- Glowing underline -->
  <path class="hero-draw" d="M72 346 C 220 340, 420 352, 600 342" fill="none" stroke="url(#hero-rule)" stroke-width="2" stroke-linecap="round" filter="url(#hero-glow)"/>

  <!-- Positioning Subtitle -->
  <text class="hero-mono hero-rise d5" x="72" y="384" font-size="13" letter-spacing="2.6" fill="#E6FFF0">FULL-STACK SOFTWARE ENGINEER  ·  CYBERSECURITY ANALYST  ·  AI SYSTEMS</text>
  <text class="hero-serif hero-rise d6" x="72" y="420" font-size="19" font-style="italic" fill="#88B99A">Engineering intelligence. Building resilient architectures.</text>

  <!-- Meta strip -->
  <g class="hero-fade d6">
    <line x1="72" y1="446" x2="1128" y2="446" stroke="#00FF66" stroke-opacity=".14"/>
    <text class="hero-mono" x="72" y="466" font-size="10.5" letter-spacing="2" fill="#88B99A">B.E. COMPUTER SCIENCE · DYPIEMR, AKURDI, PUNE · GRADUATE</text>
    <text class="hero-mono" x="1128" y="466" text-anchor="end" font-size="10.5" letter-spacing="2" fill="#00FF66">GOOGLE CYBERSECURITY 98.81% · IJNRD RESEARCH AUTHOR</text>
  </g>

  <!-- Outer Frame -->
  <rect x=".5" y=".5" width="1199" height="479" rx="19.5" fill="none" stroke="#00FF66" stroke-opacity=".18"/>
</svg>'''
    validate_and_save_svg("hero-banner.svg", svg)
