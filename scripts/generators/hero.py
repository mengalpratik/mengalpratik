"""
scripts/generators/hero.py

Generates hero-banner.svg (1200x480) with embedded base64 avatar, HUD radar, and reduced-motion support.
"""

from .common import load_profile, get_avatar_b64, validate_and_save_svg, xml_escape

def generate_hero() -> None:
    profile = load_profile()
    avatar_b64 = get_avatar_b64()
    
    avatar_markup = (
        f'<image href="data:image/jpeg;base64,{avatar_b64}" x="855" y="110" width="230" height="230" preserveAspectRatio="xMidYMid slice"/>'
        if avatar_b64 else '<rect x="855" y="110" width="230" height="230" fill="#051408"/>'
    )
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 480" width="1200" height="480" role="img" aria-labelledby="hero-title hero-desc">
  <title id="hero-title">{xml_escape(profile["name"])} — {xml_escape(profile["title"])}</title>
  <desc id="hero-desc">{xml_escape(profile["education"]["degree"])} at {xml_escape(profile["education"]["short_institution"])}. Google Cybersecurity Certified (98.81%). Axcentra SWE Intern. Full-Stack MERN, Java, Python &amp; Neural Systems.</desc>
  <defs>
    <!-- Background Gradients -->
    <radialGradient id="hero-bg" cx="50%" cy="30%" r="90%">
      <stop offset="0" stop-color="#051408"/>
      <stop offset="50%" stop-color="#020803"/>
      <stop offset="100%" stop-color="#000000"/>
    </radialGradient>
    <radialGradient id="hero-glow-green" cx="50%" cy="50%" r="50%">
      <stop offset="0" stop-color="#00FF66" stop-opacity="0.35"/>
      <stop offset="100%" stop-color="#00FF66" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="hero-glow-cyan" cx="50%" cy="50%" r="50%">
      <stop offset="0" stop-color="#05FFA1" stop-opacity="0.25"/>
      <stop offset="100%" stop-color="#05FFA1" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="hero-name-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0" stop-color="#E6FFF0"/>
      <stop offset="35%" stop-color="#00FF66"/>
      <stop offset="70%" stop-color="#05FFA1"/>
      <stop offset="100%" stop-color="#00FF41"/>
    </linearGradient>
    <linearGradient id="hero-sheen" x1="-300" y1="0" x2="0" y2="0" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="#FFFFFF" stop-opacity="0"/>
      <stop offset="50%" stop-color="#FFFFFF" stop-opacity="0.9"/>
      <stop offset="100%" stop-color="#FFFFFF" stop-opacity="0"/>
      <animateTransform attributeName="gradientTransform" type="translate" values="0 0; 1500 0; 1500 0" keyTimes="0; 0.45; 1" dur="7s" begin="1.5s" repeatCount="indefinite"/>
    </linearGradient>
    <linearGradient id="hero-scanline" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#00FF66" stop-opacity="0"/>
      <stop offset="50%" stop-color="#00FF66" stop-opacity="0.08"/>
      <stop offset="100%" stop-color="#00FF66" stop-opacity="0"/>
    </linearGradient>

    <!-- Matrix Grid Pattern -->
    <pattern id="hero-grid" width="32" height="32" patternUnits="userSpaceOnUse">
      <path d="M 32 0 L 0 0 0 32" fill="none" stroke="#00FF66" stroke-width="0.75" stroke-opacity="0.06"/>
      <circle cx="0" cy="0" r="1" fill="#00FF66" fill-opacity="0.25"/>
    </pattern>

    <!-- Clip Paths -->
    <clipPath id="hero-clip"><rect width="1200" height="480" rx="20"/></clipPath>
    <clipPath id="avatar-clip"><circle cx="970" cy="225" r="115"/></clipPath>
  </defs>

  <style>
    .mono {{ font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", "Fira Code", monospace; }}
    .sans {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif; }}
    .display {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Fira Code", monospace; font-weight: 900; }}

    .blink {{ animation: blink 1.2s infinite; }}
    @keyframes blink {{ 0%, 49% {{ opacity: 1; }} 50%, 100% {{ opacity: 0; }} }}

    .pulse-dot {{ animation: pulse 2s ease-in-out infinite; }}
    @keyframes pulse {{ 0%, 100% {{ transform: scale(1); opacity: 0.9; }} 50% {{ transform: scale(1.3); opacity: 0.4; }} }}

    .radar-spin {{ animation: spin 24s linear infinite; transform-origin: 970px 225px; }}
    .radar-spin-rev {{ animation: spin-rev 35s linear infinite; transform-origin: 970px 225px; }}
    @keyframes spin {{ from {{ transform: rotate(0deg); }} to {{ transform: rotate(360deg); }} }}
    @keyframes spin-rev {{ from {{ transform: rotate(360deg); }} to {{ transform: rotate(0deg); }} }}

    @media (prefers-reduced-motion: reduce) {{
      .radar-spin, .radar-spin-rev, .pulse-dot, .blink {{ animation: none; }}
      .hero-motion {{ display: none; }}
    }}
  </style>

  <g clip-path="url(#hero-clip)">
    <!-- Base Canvas -->
    <rect width="1200" height="480" fill="url(#hero-bg)"/>
    <rect width="1200" height="480" fill="url(#hero-grid)"/>

    <!-- Ambient Glows -->
    <ellipse cx="250" cy="240" rx="320" ry="200" fill="url(#hero-glow-green)"/>
    <ellipse cx="970" cy="225" rx="260" ry="260" fill="url(#hero-glow-cyan)"/>

    <!-- Scanline traveling beam -->
    <g class="hero-motion">
      <rect x="0" y="-120" width="1200" height="120" fill="url(#hero-scanline)">
        <animate attributeName="y" values="-120;480" dur="9s" repeatCount="indefinite"/>
      </rect>
    </g>

    <!-- Outer Border Frame with Corner Brackets -->
    <rect x="18" y="18" width="1164" height="444" rx="14" fill="none" stroke="#00FF66" stroke-width="1" stroke-opacity="0.25"/>
    <rect x="24" y="24" width="1152" height="432" rx="10" fill="none" stroke="#003B19" stroke-width="0.8" stroke-dasharray="16 8"/>

    <!-- Corner Reticles -->
    <path d="M 28 42 L 28 28 L 42 28" fill="none" stroke="#00FF66" stroke-width="2.5"/>
    <path d="M 1172 42 L 1172 28 L 1158 28" fill="none" stroke="#00FF66" stroke-width="2.5"/>
    <path d="M 28 438 L 28 452 L 42 452" fill="none" stroke="#00FF66" stroke-width="2.5"/>
    <path d="M 1172 438 L 1172 452 L 1158 452" fill="none" stroke="#00FF66" stroke-width="2.5"/>

    <!-- Left Header Status Pill -->
    <g transform="translate(54, 52)">
      <rect width="470" height="26" rx="13" fill="#040F06" stroke="#00FF66" stroke-width="1" stroke-opacity="0.4"/>
      <circle cx="15" cy="13" r="4.5" fill="#00FF66" class="pulse-dot"/>
      <text class="mono" x="28" y="17" font-size="10.5" font-weight="700" letter-spacing="1.6" fill="#00FF66">GOOGLE CYBERSECURITY CERTIFIED (98.81%) · PUNE, IN</text>
    </g>

    <!-- Terminal Command Initiation -->
    <text class="mono" x="54" y="112" font-size="13" letter-spacing="1.2" fill="#05FFA1">
      <tspan fill="#00FF66">root@neuro-core:~$</tspan> ./boot_kernel.sh --user={profile["handle"]} --auth=verified
    </text>

    <!-- Main Identity Name -->
    <text class="display" x="52" y="178" font-size="62" letter-spacing="-1" fill="url(#hero-name-grad)">{profile["name"].upper()}</text>
    <text class="display" x="52" y="178" font-size="62" letter-spacing="-1" fill="url(#hero-sheen)">{profile["name"].upper()}</text>

    <!-- Subtitle Role -->
    <g transform="translate(54, 214)">
      <rect x="0" y="-18" width="620" height="26" rx="4" fill="#00240E" fill-opacity="0.6"/>
      <text class="mono" x="12" y="0" font-size="13" font-weight="600" letter-spacing="1.4" fill="#E6FFF0">
        FULL-STACK SOFTWARE ENGINEER · CYBERSECURITY ANALYST · AI SYSTEMS
      </text>
    </g>

    <!-- Terminal Bio & System Description -->
    <g class="mono" font-size="12.5" fill="#88B99A" transform="translate(54, 248)">
      <text x="0" y="0">> B.E. Computer Science at <tspan fill="#00FF66">DYPIEMR</tspan> · Published Research Author in <tspan fill="#00FF66">IJNRD 2025</tspan></text>
      <text x="0" y="24">> Software Engineering Trainee at <tspan fill="#00FF66">Axcentra</tspan> · Ex-Intern at <tspan fill="#E6FFF0">Devtown (MERN)</tspan> &amp; <tspan fill="#E6FFF0">Codsoft (Java)</tspan></text>
      <text x="0" y="48">> Core: <tspan fill="#E6FFF0">Full-Stack MERN, Secure Systems, Python AI Pipelines &amp; Cloud Architecture</tspan></text>
    </g>

    <!-- Tech Stacks Chips Row -->
    <g transform="translate(54, 340)">
      <g transform="translate(0, 0)">
        <rect width="144" height="28" rx="14" fill="#030C05" stroke="#00FF66" stroke-width="1.2" stroke-opacity="0.6"/>
        <text class="mono" x="15" y="18" font-size="11" font-weight="600" letter-spacing="1" fill="#00FF66">{xml_escape(profile["hero_chips"][0])}</text>
      </g>
      <g transform="translate(154, 0)">
        <rect width="168" height="28" rx="14" fill="#030C05" stroke="#00FF66" stroke-width="1.2" stroke-opacity="0.6"/>
        <text class="mono" x="15" y="18" font-size="11" font-weight="600" letter-spacing="1" fill="#00FF66">{xml_escape(profile["hero_chips"][1])}</text>
      </g>
      <g transform="translate(332, 0)">
        <rect width="144" height="28" rx="14" fill="#030C05" stroke="#00FF66" stroke-width="1.2" stroke-opacity="0.6"/>
        <text class="mono" x="15" y="18" font-size="11" font-weight="600" letter-spacing="1" fill="#00FF66">{xml_escape(profile["hero_chips"][2])}</text>
      </g>
      <g transform="translate(486, 0)">
        <rect width="138" height="28" rx="14" fill="#030C05" stroke="#00FF66" stroke-width="1.2" stroke-opacity="0.6"/>
        <text class="mono" x="15" y="18" font-size="11" font-weight="600" letter-spacing="1" fill="#00FF66">{xml_escape(profile["hero_chips"][3])}</text>
      </g>
    </g>

    <!-- Terminal Footer Status -->
    <g transform="translate(54, 412)">
      <text class="mono" font-size="12" letter-spacing="1.2" fill="#72A884">
        STATUS: ONLINE · PROTOCOL: TLS 1.3 · <tspan fill="#00FF66">linkedin.com/in/pratikmengal-</tspan>
      </text>
      <rect x="420" y="-12" width="8" height="14" fill="#00FF66" class="blink"/>
    </g>

    <!-- RIGHT COLUMN: CYBERNETIC RADAR HUD + AVATAR -->
    <g transform="translate(0, 0)">
      <circle cx="970" cy="225" r="150" fill="none" stroke="#00FF66" stroke-width="0.8" stroke-opacity="0.25" stroke-dasharray="8 6"/>
      <circle cx="970" cy="225" r="162" fill="none" stroke="#00FF66" stroke-width="1.2" stroke-opacity="0.35"/>

      <g class="radar-spin">
        <circle cx="970" cy="225" r="140" fill="none" stroke="#05FFA1" stroke-width="1.4" stroke-dasharray="120 40 60 40" stroke-opacity="0.7"/>
        <circle cx="1110" cy="225" r="3.5" fill="#00FF66"/>
        <circle cx="830" cy="225" r="3.5" fill="#00FF66"/>
      </g>

      <g class="radar-spin-rev">
        <circle cx="970" cy="225" r="126" fill="none" stroke="#00FF66" stroke-width="1" stroke-dasharray="50 30 90 30" stroke-opacity="0.5"/>
        <circle cx="970" cy="99" r="3" fill="#05FFA1"/>
        <circle cx="970" cy="351" r="3" fill="#05FFA1"/>
      </g>

      <text class="mono" x="970" y="58" text-anchor="middle" font-size="9" fill="#00FF66" letter-spacing="1">000°</text>
      <text class="mono" x="1144" y="229" font-size="9" fill="#00FF66" letter-spacing="1">090°</text>
      <text class="mono" x="970" y="398" text-anchor="middle" font-size="9" fill="#00FF66" letter-spacing="1">180°</text>
      <text class="mono" x="784" y="229" font-size="9" fill="#00FF66" letter-spacing="1">270°</text>

      <line x1="970" y1="62" x2="970" y2="82" stroke="#00FF66" stroke-width="1.5"/>
      <line x1="970" y1="368" x2="970" y2="388" stroke="#00FF66" stroke-width="1.5"/>
      <line x1="808" y1="225" x2="828" y2="225" stroke="#00FF66" stroke-width="1.5"/>
      <line x1="1112" y1="225" x2="1132" y2="225" stroke="#00FF66" stroke-width="1.5"/>

      <!-- Avatar Photo & Frame -->
      <g clip-path="url(#avatar-clip)">
        <rect x="850" y="105" width="240" height="240" fill="#030C05"/>
        {avatar_markup}
        <rect x="850" y="105" width="240" height="240" fill="#00FF66" fill-opacity="0.18" style="mix-blend-mode: screen;"/>
        <rect x="850" y="105" width="240" height="240" fill="#001809" fill-opacity="0.35" style="mix-blend-mode: multiply;"/>
      </g>

      <circle cx="970" cy="225" r="115" fill="none" stroke="#00FF66" stroke-width="2.5" stroke-opacity="0.85"/>
      <circle cx="970" cy="225" r="118" fill="none" stroke="#05FFA1" stroke-width="0.8" stroke-opacity="0.5"/>

      <!-- Corner Brackets -->
      <path d="M 830 115 L 815 115 L 815 130" fill="none" stroke="#00FF66" stroke-width="2"/>
      <path d="M 1110 115 L 1125 115 L 1125 130" fill="none" stroke="#00FF66" stroke-width="2"/>
      <path d="M 830 335 L 815 335 L 815 320" fill="none" stroke="#00FF66" stroke-width="2"/>
      <path d="M 1110 335 L 1125 335 L 1125 320" fill="none" stroke="#00FF66" stroke-width="2"/>

      <!-- Floating Badges -->
      <g transform="translate(795, 90)">
        <rect width="112" height="20" rx="3" fill="#020803" stroke="#00FF66" stroke-width="0.8" stroke-opacity="0.6"/>
        <text class="mono" x="8" y="14" font-size="9" font-weight="700" fill="#00FF66">GOOGLE 98.81%</text>
      </g>
      <g transform="translate(1040, 90)">
        <rect width="84" height="20" rx="3" fill="#020803" stroke="#05FFA1" stroke-width="0.8" stroke-opacity="0.6"/>
        <text class="mono" x="8" y="14" font-size="9" font-weight="700" fill="#05FFA1">AI / AGENT</text>
      </g>
      <g transform="translate(1040, 340)">
        <rect width="90" height="20" rx="3" fill="#020803" stroke="#00FF66" stroke-width="0.8" stroke-opacity="0.6"/>
        <text class="mono" x="8" y="14" font-size="9" font-weight="700" fill="#00FF66">IJNRD AUTHOR</text>
      </g>
      <g transform="translate(805, 340)">
        <rect width="95" height="20" rx="3" fill="#020803" stroke="#05FFA1" stroke-width="0.8" stroke-opacity="0.6"/>
        <text class="mono" x="8" y="14" font-size="9" font-weight="700" fill="#05FFA1">3+ INTERNSHIPS</text>
      </g>
    </g>
  </g>
</svg>'''
    validate_and_save_svg("hero-banner.svg", svg)
