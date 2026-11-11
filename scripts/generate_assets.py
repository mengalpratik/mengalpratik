#!/usr/bin/env python3
"""
Generator script for Pratik Mengal's Hacker Green & Pitch Black GitHub Profile SVGs.
Enhanced with:
- Exact verified certifications and earned badges from LinkedIn & Resume:
  * Google Cybersecurity Professional Certificate (98.81%)
  * Cyber Forensics & Threat Intelligence
  * Data Structures & Algorithms using Java
  * Programming using Java (Core & OOP)
  * Database Management System (DBMS & SQL)
  * Introduction to Cloud Computing
  * Software Engineering & Agile Methodologies (Scrum)
  * TCS ESG Virtual Experience Program
  * Published Research Paper (IJNRD 2025)
- Perfected vertical rhythm, compact HUD titles, and zero-gap alignment.
"""

import os
import base64
import xml.etree.ElementTree as ET

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS_DIR = os.path.join(ROOT_DIR, "assets")
AVATAR_PATH = os.path.join(ROOT_DIR, "avatar.png")
os.makedirs(ASSETS_DIR, exist_ok=True)

# Read avatar and convert to base64
avatar_b64 = ""
if os.path.exists(AVATAR_PATH):
    with open(AVATAR_PATH, "rb") as f:
        avatar_b64 = base64.b64encode(f.read()).decode("utf-8")

def validate_svg(filename, content):
    path = os.path.join(ASSETS_DIR, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.strip())
    try:
        ET.fromstring(content.strip())
        print(f"✓ Valid XML: {filename} ({len(content)} bytes)")
    except Exception as e:
        print(f"✗ XML Parse Error in {filename}: {e}")
        raise e

# -------------------------------------------------------------
# 1. HERO BANNER (1200x480)
# -------------------------------------------------------------
hero_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 480" width="1200" height="480" role="img" aria-labelledby="hero-title hero-desc">
  <title id="hero-title">Pratik Mengal — Full-Stack Software Engineer, Cybersecurity Analyst &amp; AI Systems Developer</title>
  <desc id="hero-desc">B.E. Computer Science at DYPIEMR. Google Cybersecurity Certified (98.81%). Axcentra SWE Intern. Full-Stack MERN, Java, Python &amp; Neural Systems.</desc>
  <defs>
    <!-- Background Gradients -->
    <radialGradient id="hero-bg" cx="50%" cy="30%" r="90%">
      <stop offset="0%" stop-color="#051408"/>
      <stop offset="50%" stop-color="#020803"/>
      <stop offset="100%" stop-color="#000000"/>
    </radialGradient>
    <radialGradient id="hero-glow-green" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#00FF66" stop-opacity="0.35"/>
      <stop offset="100%" stop-color="#00FF66" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="hero-glow-cyan" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#05FFA1" stop-opacity="0.25"/>
      <stop offset="100%" stop-color="#05FFA1" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="hero-name-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#E6FFF0"/>
      <stop offset="35%" stop-color="#00FF66"/>
      <stop offset="70%" stop-color="#05FFA1"/>
      <stop offset="100%" stop-color="#00FF41"/>
    </linearGradient>
    <linearGradient id="hero-laser-line" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00FF66" stop-opacity="0"/>
      <stop offset="20%" stop-color="#00FF66"/>
      <stop offset="80%" stop-color="#05FFA1"/>
      <stop offset="100%" stop-color="#05FFA1" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="hero-sheen" x1="-300" y1="0" x2="0" y2="0" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#FFFFFF" stop-opacity="0"/>
      <stop offset="50%" stop-color="#FFFFFF" stop-opacity="0.9"/>
      <stop offset="100%" stop-color="#FFFFFF" stop-opacity="0"/>
      <animateTransform attributeName="gradientTransform" type="translate" values="0 0; 1500 0; 1500 0" keyTimes="0; 0.45; 1" dur="7s" begin="1.5s" repeatCount="indefinite"/>
    </linearGradient>
    <linearGradient id="hero-scanline" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#00FF66" stop-opacity="0"/>
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
    <rect x="0" y="-120" width="1200" height="120" fill="url(#hero-scanline)">
      <animate attributeName="y" values="-120;480" dur="9s" repeatCount="indefinite"/>
    </rect>

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
      <tspan fill="#00FF66">root@neuro-core:~$</tspan> ./boot_kernel.sh --user=mengalpratik --auth=verified
    </text>

    <!-- Main Identity Name -->
    <text class="display" x="52" y="178" font-size="62" letter-spacing="-1" fill="url(#hero-name-grad)">PRATIK MENGAL</text>
    <text class="display" x="52" y="178" font-size="62" letter-spacing="-1" fill="url(#hero-sheen)">PRATIK MENGAL</text>

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
        <text class="mono" x="15" y="18" font-size="11" font-weight="600" letter-spacing="1" fill="#00FF66">MERN STACK ⚔️</text>
      </g>
      <g transform="translate(154, 0)">
        <rect width="168" height="28" rx="14" fill="#030C05" stroke="#00FF66" stroke-width="1.2" stroke-opacity="0.6"/>
        <text class="mono" x="15" y="18" font-size="11" font-weight="600" letter-spacing="1" fill="#00FF66">CYBERSECURITY 🛡️</text>
      </g>
      <g transform="translate(332, 0)">
        <rect width="144" height="28" rx="14" fill="#030C05" stroke="#00FF66" stroke-width="1.2" stroke-opacity="0.6"/>
        <text class="mono" x="15" y="18" font-size="11" font-weight="600" letter-spacing="1" fill="#00FF66">AI &amp; NEURAL SYS</text>
      </g>
      <g transform="translate(486, 0)">
        <rect width="138" height="28" rx="14" fill="#030C05" stroke="#00FF66" stroke-width="1.2" stroke-opacity="0.6"/>
        <text class="mono" x="15" y="18" font-size="11" font-weight="600" letter-spacing="1" fill="#00FF66">CLOUD &amp; DOCKER</text>
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
        {f'<image href="data:image/jpeg;base64,{avatar_b64}" x="855" y="110" width="230" height="230" preserveAspectRatio="xMidYMid slice"/>' if avatar_b64 else '<rect x="855" y="110" width="230" height="230" fill="#051408"/>'}
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
validate_svg("hero-banner.svg", hero_svg)

# -------------------------------------------------------------
# 2. TITLE SVGs (COMPACT 1200x90 FOR ZERO-GAP HUD SPACING)
# -------------------------------------------------------------
titles = [
    ("title-about.svg", "01", "KERNEL // PROFILE", "About — Initializing System Specs.", "WHO I AM"),
    ("title-recognition.svg", "02", "BENCHMARKS // PROOF", "Recognition — Proof, on the record.", "MILESTONES"),
    ("title-work.svg", "03", "SHIPPED SYSTEMS // PRODUCTION", "Selected work — Products, not assignments.", "CODEBASES"),
    ("title-toolkit.svg", "04", "NEURAL CORE // STACK", "Toolkit — The tools I reach for.", "TECH STACK"),
    ("title-commits.svg", "05", "TELEMETRY // BUILDS", "Commit telemetry — Continuous builds.", "ACTIVITY"),
    ("title-certifications.svg", "06", "CREDENTIALS &amp; BADGES // PROOF", "Certifications &amp; Earned Badges — Verified.", "EDUCATION"),
    ("title-connect.svg", "07", "TRANSMISSION // NETWORK", "Connect — Let's build something extraordinary.", "OPEN CHANNELS"),
]

for filename, num, sub, heading, tag in titles:
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 90" width="1200" height="90" role="img" aria-label="{num} {heading}">
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
    {heading.split('—')[0]}— <tspan fill="url(#ta-sheen-{num})">{heading.split('—')[1] if '—' in heading else ''}</tspan>
  </text>

  <!-- Right Tag -->
  <text class="ta-mono" x="1160" y="24" text-anchor="end" font-size="10.5" letter-spacing="2.4" fill="#00FF66">{tag}</text>

  <!-- Base Rule Line -->
  <path d="M40 82 H1160" stroke="url(#ta-line-{num})" stroke-width="1.2"/>

  <!-- Traveling Pulse Laser Dot -->
  <circle cx="40" cy="82" r="5" fill="url(#ta-pulse-{num})" opacity="0">
    <animate attributeName="cx" values="40;1160" dur="6s" begin="1.2s" repeatCount="indefinite" calcMode="spline" keyTimes="0;1" keySplines=".45 0 .55 1"/>
    <animate attributeName="opacity" values="0;1;0" keyTimes="0;0.15;1" dur="6s" begin="1.2s" repeatCount="indefinite"/>
  </circle>
</svg>'''
    validate_svg(filename, svg)

# -------------------------------------------------------------
# 3. ABOUT INTRO SVG (1200x410)
# -------------------------------------------------------------
about_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 410" width="1200" height="410" role="img" aria-labelledby="ab-title ab-desc">
  <title id="ab-title">About Pratik Mengal</title>
  <desc id="ab-desc">Full-Stack Software Engineer, Cybersecurity Analyst &amp; AI Systems Developer. B.E. at DYPIEMR. Google Cybersecurity Certified (98.81%). Axcentra SWE Intern. Primary languages TypeScript, Python and Java.</desc>
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
    .ab-mono { font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", "Fira Code", monospace; }
    .ab-heading { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Fira Code", monospace; font-weight: 700; }
    .ab-sans { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", sans-serif; }
    .ab-card { transition: transform 0.2s ease; }
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
      <tspan fill="#00FF66">mengalpratik@neuro-box:~$</tspan> cat /sys/dev/profile_summary.md
    </text>

    <!-- Narrative Intro -->
    <g class="ab-sans" font-size="14.5" fill="#E6FFF0" transform="translate(32, 100)">
      <text x="0" y="0">
        I am a <tspan font-weight="700" fill="#00FF66">Full-Stack Software Engineer</tspan> and <tspan font-weight="700" fill="#05FFA1">Google Certified Cybersecurity Analyst (98.81%)</tspan> graduating with B.E. from <tspan font-weight="600" fill="#E6FFF0">DYPIEMR</tspan>, Pune.
      </text>
      <text x="0" y="26" fill="#88B99A">
        Co-authored published research in <tspan fill="#00FF66" font-weight="600">IJNRD (May 2025)</tspan> on health management systems with nutrient analysis &amp; personalized recommendations.
      </text>
      <text x="0" y="52" fill="#88B99A">
        Proven industry experience across <tspan fill="#00FF66">Axcentra</tspan> (Software Engineering Trainee), <tspan fill="#E6FFF0">Devtown</tspan> (Full-Stack MERN Intern), and <tspan fill="#E6FFF0">Codsoft</tspan> (Java Software Developer).
      </text>
      <text x="0" y="78" fill="#88B99A">
        Shipped systems include <tspan fill="#E6FFF0">NeuroMatrix</tspan> (neural pipelines), <tspan fill="#E6FFF0">Myraa AI Assistant</tspan> (multi-modal agent), and <tspan fill="#E6FFF0">NeuroStore</tspan> (MERN platform).
      </text>
    </g>

    <!-- 3 Bottom Focus Highlight Cards -->
    <g transform="translate(32, 236)">
      <!-- Card 1 -->
      <g class="ab-card" transform="translate(0, 0)">
        <rect width="338" height="126" rx="12" fill="#030C05" stroke="#00FF66" stroke-width="1" stroke-opacity="0.35"/>
        <rect x="0" y="0" width="4" height="126" rx="2" fill="#00FF66"/>
        <text class="ab-mono" x="20" y="30" font-size="10.5" font-weight="700" letter-spacing="2" fill="#00FF66">CORE LANGUAGES</text>
        <text class="ab-heading" x="20" y="66" font-size="24" fill="#E6FFF0">Java · Python · TypeScript</text>
        <text class="ab-sans" x="20" y="94" font-size="13" fill="#88B99A">JavaScript (ES6+) · SQL · C/C++</text>
      </g>

      <!-- Card 2 -->
      <g class="ab-card" transform="translate(358, 0)">
        <rect width="338" height="126" rx="12" fill="#030C05" stroke="#00FF66" stroke-width="1" stroke-opacity="0.35"/>
        <rect x="0" y="0" width="4" height="126" rx="2" fill="#05FFA1"/>
        <text class="ab-mono" x="20" y="30" font-size="10.5" font-weight="700" letter-spacing="2" fill="#05FFA1">ARCHITECTURE &amp; MERN</text>
        <text class="ab-heading" x="20" y="66" font-size="24" fill="#E6FFF0">React · Node.js · Express</text>
        <text class="ab-sans" x="20" y="94" font-size="13" fill="#88B99A">MongoDB · REST APIs · Docker · JWT</text>
      </g>

      <!-- Card 3 -->
      <g class="ab-card" transform="translate(716, 0)">
        <rect width="338" height="126" rx="12" fill="#030C05" stroke="#00FF66" stroke-width="1" stroke-opacity="0.35"/>
        <rect x="0" y="0" width="4" height="126" rx="2" fill="#00FF66"/>
        <text class="ab-mono" x="20" y="30" font-size="10.5" font-weight="700" letter-spacing="2" fill="#00FF66">SECURITY &amp; AI</text>
        <text class="ab-heading" x="20" y="66" font-size="24" fill="#E6FFF0">Google Cyber (98.81%)</text>
        <text class="ab-sans" x="20" y="94" font-size="13" fill="#88B99A">Threat Mitigation · LLMs · Forensics</text>
      </g>
    </g>
  </g>
</svg>'''
validate_svg("about-intro.svg", about_svg)

# -------------------------------------------------------------
# 4. ACHIEVEMENT MOTIF SVG (1200x420)
# -------------------------------------------------------------
achievement_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 420" width="1200" height="420" role="img" aria-labelledby="ach-title ach-desc">
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
    .ach-mono { font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", "Fira Code", monospace; }
    .ach-heading { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Fira Code", monospace; font-weight: 700; }
    .ach-sans { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", sans-serif; }
    .ach-trace { stroke-dasharray: 200 1000; animation: trace 8s linear infinite; }
    @keyframes trace { to { stroke-dashoffset: -1200; } }
    @media (prefers-reduced-motion: reduce) { .ach-trace { animation: none; } }
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
      <text class="ach-mono" x="32" y="208" font-size="11" letter-spacing="1.2" fill="#05FFA1">> DUAL CREDENTIAL ALIGNED · FORENSICS · THREAT MITIGATION</text>
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
      <text class="ach-heading" x="0" y="60" font-size="38" fill="#E6FFF0">23+</text>
      <text x="0" y="84" fill="#88B99A">Active Repositories</text>
      <text x="0" y="102" font-size="11" fill="#72A884">Open Source &amp; Systems</text>
    </g>

    <!-- Col 5 -->
    <g transform="translate(930, 0)">
      <circle cx="12" cy="12" r="3.5" fill="#00FF66"/>
      <text class="ach-mono" x="24" y="16" font-size="11" font-weight="700" letter-spacing="2" fill="#00FF66">ACADEMICS</text>
      <text class="ach-heading" x="0" y="60" font-size="34" fill="#E6FFF0">B.E. CSE</text>
      <text x="0" y="84" fill="#88B99A">DYPIEMR · Akurdi, Pune</text>
      <text x="0" y="102" font-size="11" fill="#72A884">Computer Science &amp; Eng.</text>
    </g>
  </g>
</svg>'''
validate_svg("achievement-motif.svg", achievement_svg)

# -------------------------------------------------------------
# 5. PROJECT SVGs (COMPACT 1200x360)
# -------------------------------------------------------------
projects = [
    {
        "filename": "project-neuromatrix.svg",
        "num": "01",
        "category": "AI / ML · NEURAL ENGINE",
        "title": "NeuroMatrix",
        "desc": "Neural model execution, data preprocessing, and vector pipeline optimization in Python.",
        "built": "modular neural pipelines › automated data transformations › high-throughput batching",
        "metrics": [("Real-Time", "Vector Processing"), ("Multi-Model", "Architecture"), ("Modular", "Pipeline Design")],
        "chips": ["Python", "Neural Nets", "AI Pipelines", "Vector Embeddings", "NumPy"]
    },
    {
        "filename": "project-myraa.svg",
        "num": "02",
        "category": "AGENTIC AI · LLM ORCHESTRATION",
        "title": "Myraa AI Assistant",
        "desc": "Autonomous multi-modal conversational assistant with streaming tool calling and agentic memory.",
        "built": "multi-turn dialogue system › type-safe TypeScript runtime › extensible agent toolchains",
        "metrics": [("Multi-Turn", "Autonomous Agent"), ("Type-Safe", "TypeScript Core"), ("Low Latency", "Streaming Inference")],
        "chips": ["TypeScript", "Python", "LLMs", "Tool Calling", "WebSockets", "Node.js"]
    },
    {
        "filename": "project-neurostore.svg",
        "num": "03",
        "category": "FULL-STACK · E-COMMERCE ARCHITECTURE",
        "title": "NeuroStore MERN Platform",
        "desc": "High-concurrency e-commerce architecture with multi-level JWT RBAC and payment state machine.",
        "built": "isolated tenant catalog › stateful cart &amp; order lifecycle › responsive React client",
        "metrics": [("Multi-Tier", "RBAC Auth Security"), ("High Uptime", "Resilient Backend"), ("Full-Stack", "MERN Architecture")],
        "chips": ["React", "Node.js", "Express", "MongoDB", "JWT Auth", "Docker"]
    },
    {
        "filename": "project-axcentra.svg",
        "num": "04",
        "category": "ENTERPRISE · PRODUCTION WEB SUITE",
        "title": "Axcentra Production Suite",
        "desc": "Production-grade enterprise web applications delivering high-performance UI and resilient services.",
        "built": "modular component architecture › automated API integrations › robust enterprise UX",
        "metrics": [("Production", "Shipped Codebases"), ("99.9%", "Reliability Target"), ("Modern UI", "Interactive Workflows")],
        "chips": ["JavaScript", "TypeScript", "Java", "REST APIs", "Modern CSS", "Git"]
    }
]

for p in projects:
    chips_xml = ""
    cx = 56
    for chip in p["chips"]:
        cw = len(chip) * 9 + 24
        chips_xml += f'''
        <g transform="translate({cx}, 308)">
          <rect width="{cw}" height="26" rx="13" fill="#041207" stroke="#00FF66" stroke-width="1" stroke-opacity="0.45"/>
          <text class="p-mono" x="{cw/2}" y="17" text-anchor="middle" font-size="10.5" font-weight="600" fill="#00FF66">{chip}</text>
        </g>'''
        cx += cw + 12

    metrics_xml = ""
    mx = 56
    for val, lbl in p["metrics"]:
        metrics_xml += f'''
        <g transform="translate({mx}, 258)">
          <text class="p-heading" font-size="30" fill="#E6FFF0">{val}</text>
          <text class="p-sans" y="24" font-size="12" fill="#88B99A">{lbl}</text>
        </g>'''
        mx += 220

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 360" width="1200" height="360" role="img" aria-labelledby="p-{p['num']}-t">
  <title id="p-{p['num']}-t">{p['title']}: {p['desc']}</title>
  <defs>
    <linearGradient id="p-bg-{p['num']}" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#050F07"/>
      <stop offset="100%" stop-color="#020603"/>
    </linearGradient>
    <radialGradient id="p-glow-{p['num']}" cx="85%" cy="30%" r="75%">
      <stop offset="0" stop-color="#00FF66" stop-opacity="0.22"/>
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
    .p-trace {{ stroke-dasharray: 200 1100; animation: p-trace 7s linear infinite; }}
    @keyframes p-trace {{ to {{ stroke-dashoffset: -1300; }} }}
    @media (prefers-reduced-motion: reduce) {{ .p-trace {{ animation: none; }} }}
  </style>

  <rect width="1200" height="360" fill="#000000"/>

  <g transform="translate(40, 10)">
    <rect width="1120" height="336" rx="16" fill="url(#p-bg-{p['num']})" stroke="#00FF66" stroke-width="1.2" stroke-opacity="0.3"/>
    <rect width="1120" height="336" rx="16" fill="url(#p-glow-{p['num']})"/>
    <rect class="p-trace" width="1120" height="336" rx="16" fill="none" stroke="url(#p-trace-{p['num']})" stroke-width="1.4"/>

    <text class="p-mono" x="56" y="54" font-size="11.5" font-weight="700" letter-spacing="2.6" fill="#00FF66">{p['num']} · {p['category']}</text>
    <text class="p-heading" x="54" y="106" font-size="42" letter-spacing="-1" fill="#E6FFF0">{p['title']}</text>
    <text class="p-sans" x="56" y="142" font-size="15.5" fill="#88B99A">{p['desc']}</text>

    <text class="p-mono" x="56" y="178" font-size="12.5" fill="#E6FFF0">
      <tspan fill="#05FFA1" font-weight="700">BUILT › </tspan>{p['built']}
    </text>

    {metrics_xml}
    {chips_xml}
  </g>
</svg>'''
    validate_svg(p["filename"], svg)

# -------------------------------------------------------------
# 6. TECH CONSTELLATION SVG (1200x500)
# -------------------------------------------------------------
tech_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 500" width="1200" height="500" role="img" aria-labelledby="tc-title tc-desc">
  <title id="tc-title">Tech Stack Constellation</title>
  <desc id="tc-desc">Languages: TypeScript, Python, Java, JavaScript, C/C++. AI/ML: LLMs, LangChain, Neural Networks, PyTorch. Frontend: React, Next.js, Tailwind CSS. Backend: Node.js, Express, FastAPI, REST, WebSockets, JWT. Data &amp; Cloud: MongoDB, PostgreSQL, Docker, AWS, Redis. DevOps &amp; Tools: Git, GitHub Actions, Linux CLI, Postman.</desc>
  <defs>
    <linearGradient id="tc-trace" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#00FF66"/>
      <stop offset="60%" stop-color="#05FFA1"/>
      <stop offset="100%" stop-color="#00FF66" stop-opacity="0"/>
    </linearGradient>
    <radialGradient id="tc-panel-glow" cx="80%" cy="20%" r="70%">
      <stop offset="0" stop-color="#00FF66" stop-opacity="0.12"/>
      <stop offset="100%" stop-color="#00FF66" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <style>
    .tc-mono { font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", "Fira Code", monospace; }
    .tc-heading { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Fira Code", monospace; font-weight: 700; }
    .tc-sans { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", sans-serif; }
    .tc-trace { stroke-dasharray: 180 940; animation: tc-trace 7s linear infinite; }
    @keyframes tc-trace { to { stroke-dashoffset: -1120; } }
    @media (prefers-reduced-motion: reduce) { .tc-trace { animation: none; } }
  </style>

  <rect width="1200" height="500" fill="#000000"/>

  <!-- Row 1: 3 Panels -->
  <g transform="translate(32, 20)">
    <!-- Panel 1: Languages -->
    <g transform="translate(0, 0)">
      <rect width="360" height="214" rx="14" fill="#040F06" stroke="#00FF66" stroke-width="1" stroke-opacity="0.3"/>
      <rect width="360" height="214" rx="14" fill="url(#tc-panel-glow)"/>
      <rect class="tc-trace" width="360" height="214" rx="14" fill="none" stroke="url(#tc-trace)" stroke-width="1.4"/>
      <text class="tc-mono" x="24" y="38" font-size="11" font-weight="700" letter-spacing="2.4" fill="#00FF66">01 // LANGUAGES</text>
      <text class="tc-heading" x="24" y="86" font-size="30" fill="#E6FFF0">Java · Python</text>
      <text class="tc-heading" x="24" y="126" font-size="24" fill="#05FFA1">JavaScript · TypeScript</text>
      <text class="tc-sans" x="24" y="162" font-size="16" fill="#88B99A">SQL · Bash · C / C++</text>
      <text class="tc-mono" x="24" y="190" font-size="10" letter-spacing="1.2" fill="#72A884">DATA STRUCTURES &amp; ALGORITHMS</text>
    </g>

    <!-- Panel 2: Cybersecurity & Forensics -->
    <g transform="translate(398, 0)">
      <rect width="360" height="214" rx="14" fill="#040F06" stroke="#00FF66" stroke-width="1" stroke-opacity="0.3"/>
      <rect width="360" height="214" rx="14" fill="url(#tc-panel-glow)"/>
      <rect class="tc-trace" style="animation-delay: -1.2s;" width="360" height="214" rx="14" fill="none" stroke="url(#tc-trace)" stroke-width="1.4"/>
      <text class="tc-mono" x="24" y="38" font-size="11" font-weight="700" letter-spacing="2.4" fill="#05FFA1">02 // CYBERSECURITY &amp; FORENSICS</text>
      <text class="tc-heading" x="24" y="86" font-size="28" fill="#E6FFF0">Google Cyber (98.8%)</text>
      <text class="tc-heading" x="24" y="126" font-size="22" fill="#00FF66">Network Defense · Linux/SQL</text>
      <text class="tc-sans" x="24" y="162" font-size="16" fill="#88B99A">Threat Mitigation · Python SIEM</text>
      <text class="tc-mono" x="24" y="190" font-size="10" letter-spacing="1.2" fill="#72A884">VULNERABILITY ASSESSMENT · SOC</text>
    </g>

    <!-- Panel 3: Frontend -->
    <g transform="translate(796, 0)">
      <rect width="360" height="214" rx="14" fill="#040F06" stroke="#00FF66" stroke-width="1" stroke-opacity="0.3"/>
      <rect width="360" height="214" rx="14" fill="url(#tc-panel-glow)"/>
      <rect class="tc-trace" style="animation-delay: -2.4s;" width="360" height="214" rx="14" fill="none" stroke="url(#tc-trace)" stroke-width="1.4"/>
      <text class="tc-mono" x="24" y="38" font-size="11" font-weight="700" letter-spacing="2.4" fill="#00FF66">03 // FRONTEND</text>
      <text class="tc-heading" x="24" y="86" font-size="34" fill="#E6FFF0">React · Next.js</text>
      <text class="tc-heading" x="24" y="126" font-size="24" fill="#05FFA1">Tailwind CSS · Redux</text>
      <text class="tc-sans" x="24" y="162" font-size="16" fill="#88B99A">HTML5 · CSS3 · Modern UI</text>
      <text class="tc-mono" x="24" y="190" font-size="10" letter-spacing="1.2" fill="#72A884">RESPONSIVE DESIGN · STATE MGMT</text>
    </g>
  </g>

  <!-- Row 2: 3 Panels -->
  <g transform="translate(32, 256)">
    <!-- Panel 4: Backend & APIs -->
    <g transform="translate(0, 0)">
      <rect width="360" height="214" rx="14" fill="#040F06" stroke="#00FF66" stroke-width="1" stroke-opacity="0.3"/>
      <rect width="360" height="214" rx="14" fill="url(#tc-panel-glow)"/>
      <rect class="tc-trace" style="animation-delay: -3.6s;" width="360" height="214" rx="14" fill="none" stroke="url(#tc-trace)" stroke-width="1.4"/>
      <text class="tc-mono" x="24" y="38" font-size="11" font-weight="700" letter-spacing="2.4" fill="#00FF66">04 // BACKEND &amp; APIS</text>
      <text class="tc-heading" x="24" y="86" font-size="28" fill="#E6FFF0">Node.js · Express</text>
      <text class="tc-heading" x="24" y="126" font-size="22" fill="#05FFA1">FastAPI · RESTful APIs</text>
      <text class="tc-sans" x="24" y="162" font-size="16" fill="#88B99A">WebSockets · Microservices</text>
      <text class="tc-mono" x="24" y="190" font-size="10" letter-spacing="1.2" fill="#72A884">JWT AUTH · RBAC SECURITY · CORS</text>
    </g>

    <!-- Panel 5: Data & Cloud -->
    <g transform="translate(398, 0)">
      <rect width="360" height="214" rx="14" fill="#040F06" stroke="#00FF66" stroke-width="1" stroke-opacity="0.3"/>
      <rect width="360" height="214" rx="14" fill="url(#tc-panel-glow)"/>
      <rect class="tc-trace" style="animation-delay: -4.8s;" width="360" height="214" rx="14" fill="none" stroke="url(#tc-trace)" stroke-width="1.4"/>
      <text class="tc-mono" x="24" y="38" font-size="11" font-weight="700" letter-spacing="2.4" fill="#05FFA1">05 // DATA &amp; CLOUD</text>
      <text class="tc-heading" x="24" y="86" font-size="26" fill="#E6FFF0">MongoDB · PostgreSQL</text>
      <text class="tc-heading" x="24" y="126" font-size="22" fill="#00FF66">Docker · AWS Cloud</text>
      <text class="tc-sans" x="24" y="162" font-size="16" fill="#88B99A">MySQL · Redis Caching</text>
      <text class="tc-mono" x="24" y="190" font-size="10" letter-spacing="1.2" fill="#72A884">SCHEMA DESIGN · NORMALIZATION · CI</text>
    </g>

    <!-- Panel 6: DevOps & Tools -->
    <g transform="translate(796, 0)">
      <rect width="360" height="214" rx="14" fill="#040F06" stroke="#00FF66" stroke-width="1" stroke-opacity="0.3"/>
      <rect width="360" height="214" rx="14" fill="url(#tc-panel-glow)"/>
      <rect class="tc-trace" style="animation-delay: -6.0s;" width="360" height="214" rx="14" fill="none" stroke="url(#tc-trace)" stroke-width="1.4"/>
      <text class="tc-mono" x="24" y="38" font-size="11" font-weight="700" letter-spacing="2.4" fill="#00FF66">06 // DEVOPS &amp; TOOLS</text>
      <text class="tc-heading" x="24" y="86" font-size="28" fill="#E6FFF0">Git · GitHub Actions</text>
      <text class="tc-heading" x="24" y="126" font-size="22" fill="#05FFA1">Linux / Bash Scripting</text>
      <text class="tc-sans" x="24" y="162" font-size="16" fill="#88B99A">Postman · VS Code · Agile Scrum</text>
      <text class="tc-mono" x="24" y="190" font-size="10" letter-spacing="1.2" fill="#72A884">SYSTEM DESIGN · OOP · UNIT TESTS</text>
    </g>
  </g>
</svg>'''
validate_svg("tech-constellation.svg", tech_svg)

# -------------------------------------------------------------
# 7. CERTIFICATIONS & EARNED BADGES SVG (1200x480)
# -------------------------------------------------------------
certs_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 480" width="1200" height="480" role="img" aria-labelledby="ce-title ce-desc">
  <title id="ce-title">Official Certifications &amp; Earned Badges</title>
  <desc id="ce-desc">Eight verified milestones from LinkedIn &amp; Resume: Google Cybersecurity (98.81%), Cyber Forensics, Java DSA, Core Java OOP, DBMS SQL, Cloud Computing, Agile Software Engineering, and TCS ESG Virtual Experience.</desc>
  <defs>
    <linearGradient id="ce-card-bg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#040F06"/>
      <stop offset="100%" stop-color="#020603"/>
    </linearGradient>
    <linearGradient id="ce-badge-bg" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#00240E"/>
      <stop offset="50%" stop-color="#031609"/>
      <stop offset="100%" stop-color="#00240E"/>
    </linearGradient>
  </defs>
  <style>
    .ce-mono { font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", "Fira Code", monospace; }
    .ce-heading { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Fira Code", monospace; font-weight: 700; }
    .ce-sans { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", sans-serif; }
  </style>

  <rect width="1200" height="480" fill="#000000"/>

  <!-- Row 1: 4 Cards -->
  <g transform="translate(36, 16)">
    <!-- Card 1: Google Cybersecurity -->
    <g transform="translate(0, 0)">
      <rect width="262" height="174" rx="12" fill="url(#ce-card-bg)" stroke="#00FF66" stroke-width="1.2" stroke-opacity="0.5"/>
      <rect x="0" y="0" width="4" height="174" rx="2" fill="#00FF66"/>
      <text class="ce-mono" x="18" y="28" font-size="10" font-weight="700" letter-spacing="1.8" fill="#00FF66">GOOGLE · COURSERA</text>
      <text class="ce-heading" x="18" y="66" font-size="18" fill="#E6FFF0">Google Cybersecurity</text>
      <text class="ce-sans" x="18" y="92" font-size="13" font-weight="600" fill="#00FF66">Score: 98.81 / 100 (8 Courses)</text>
      <text class="ce-sans" x="18" y="114" font-size="12" fill="#88B99A">Networks, Linux, SQL, Python</text>
      <!-- Badge Pill -->
      <g transform="translate(18, 136)">
        <rect width="224" height="22" rx="4" fill="#00240E" stroke="#00FF66" stroke-width="0.8"/>
        <text class="ce-mono" x="10" y="15" font-size="9.5" font-weight="700" fill="#00FF66">★ GOOGLE VERIFIED PROFESSIONAL</text>
      </g>
    </g>

    <!-- Card 2: Cyber Forensics -->
    <g transform="translate(288, 0)">
      <rect width="262" height="174" rx="12" fill="url(#ce-card-bg)" stroke="#00FF66" stroke-width="1" stroke-opacity="0.3"/>
      <rect x="0" y="0" width="4" height="174" rx="2" fill="#05FFA1"/>
      <text class="ce-mono" x="18" y="28" font-size="10" font-weight="700" letter-spacing="1.8" fill="#05FFA1">GOOGLE · FORENSICS</text>
      <text class="ce-heading" x="18" y="66" font-size="18" fill="#E6FFF0">Cyber Forensics &amp; SOC</text>
      <text class="ce-sans" x="18" y="92" font-size="13" font-weight="600" fill="#05FFA1">Threat Detection &amp; Response</text>
      <text class="ce-sans" x="18" y="114" font-size="12" fill="#88B99A">Vulnerability Mitigation</text>
      <g transform="translate(18, 136)">
        <rect width="224" height="22" rx="4" fill="#00240E" stroke="#05FFA1" stroke-width="0.8"/>
        <text class="ce-mono" x="10" y="15" font-size="9.5" font-weight="700" fill="#05FFA1">COMPTIA SECURITY+ ALIGNED</text>
      </g>
    </g>

    <!-- Card 3: DSA Java -->
    <g transform="translate(576, 0)">
      <rect width="262" height="174" rx="12" fill="url(#ce-card-bg)" stroke="#00FF66" stroke-width="1" stroke-opacity="0.3"/>
      <rect x="0" y="0" width="4" height="174" rx="2" fill="#00FF66"/>
      <text class="ce-mono" x="18" y="28" font-size="10" font-weight="700" letter-spacing="1.8" fill="#00FF66">JAVA · ALGORITHMS</text>
      <text class="ce-heading" x="18" y="66" font-size="17" fill="#E6FFF0">Data Structures &amp; Algo</text>
      <text class="ce-sans" x="18" y="92" font-size="13" font-weight="600" fill="#00FF66">Trees, Graphs, Recursion</text>
      <text class="ce-sans" x="18" y="114" font-size="12" fill="#88B99A">Dynamic Prog &amp; Complexity</text>
      <g transform="translate(18, 136)">
        <rect width="224" height="22" rx="4" fill="#00240E" stroke="#00FF66" stroke-width="0.8"/>
        <text class="ce-mono" x="10" y="15" font-size="9.5" font-weight="700" fill="#00FF66">500+ PROBLEMS SOLVED</text>
      </g>
    </g>

    <!-- Card 4: Java OOP -->
    <g transform="translate(864, 0)">
      <rect width="262" height="174" rx="12" fill="url(#ce-card-bg)" stroke="#00FF66" stroke-width="1" stroke-opacity="0.3"/>
      <rect x="0" y="0" width="4" height="174" rx="2" fill="#05FFA1"/>
      <text class="ce-mono" x="18" y="28" font-size="10" font-weight="700" letter-spacing="1.8" fill="#05FFA1">CORE JAVA · OOP</text>
      <text class="ce-heading" x="18" y="66" font-size="18" fill="#E6FFF0">Programming using Java</text>
      <text class="ce-sans" x="18" y="92" font-size="13" font-weight="600" fill="#05FFA1">OOP, Collections, Threads</text>
      <text class="ce-sans" x="18" y="114" font-size="12" fill="#88B99A">JDBC, Exception Handling</text>
      <g transform="translate(18, 136)">
        <rect width="224" height="22" rx="4" fill="#00240E" stroke="#05FFA1" stroke-width="0.8"/>
        <text class="ce-mono" x="10" y="15" font-size="9.5" font-weight="700" fill="#05FFA1">ENTERPRISE JAVA EXPERTISE</text>
      </g>
    </g>
  </g>

  <!-- Row 2: 4 Cards -->
  <g transform="translate(36, 206)">
    <!-- Card 5: DBMS -->
    <g transform="translate(0, 0)">
      <rect width="262" height="174" rx="12" fill="url(#ce-card-bg)" stroke="#00FF66" stroke-width="1" stroke-opacity="0.3"/>
      <rect x="0" y="0" width="4" height="174" rx="2" fill="#05FFA1"/>
      <text class="ce-mono" x="18" y="28" font-size="10" font-weight="700" letter-spacing="1.8" fill="#05FFA1">DATABASE · SQL</text>
      <text class="ce-heading" x="18" y="66" font-size="17" fill="#E6FFF0">Database Management</text>
      <text class="ce-sans" x="18" y="92" font-size="13" font-weight="600" fill="#05FFA1">Advanced SQL &amp; ERD Design</text>
      <text class="ce-sans" x="18" y="114" font-size="12" fill="#88B99A">Indexing, Tuning &amp; Concurrency</text>
      <g transform="translate(18, 136)">
        <rect width="224" height="22" rx="4" fill="#00240E" stroke="#05FFA1" stroke-width="0.8"/>
        <text class="ce-mono" x="10" y="15" font-size="9.5" font-weight="700" fill="#05FFA1">RELATIONAL ARCHITECTURE</text>
      </g>
    </g>

    <!-- Card 6: Cloud -->
    <g transform="translate(288, 0)">
      <rect width="262" height="174" rx="12" fill="url(#ce-card-bg)" stroke="#00FF66" stroke-width="1" stroke-opacity="0.3"/>
      <rect x="0" y="0" width="4" height="174" rx="2" fill="#00FF66"/>
      <text class="ce-mono" x="18" y="28" font-size="10" font-weight="700" letter-spacing="1.8" fill="#00FF66">CLOUD COMPUTING</text>
      <text class="ce-heading" x="18" y="66" font-size="18" fill="#E6FFF0">Introduction to Cloud</text>
      <text class="ce-sans" x="18" y="92" font-size="13" font-weight="600" fill="#00FF66">IaaS, PaaS, SaaS Models</text>
      <text class="ce-sans" x="18" y="114" font-size="12" fill="#88B99A">Virtualization &amp; Microservices</text>
      <g transform="translate(18, 136)">
        <rect width="224" height="22" rx="4" fill="#00240E" stroke="#00FF66" stroke-width="0.8"/>
        <text class="ce-mono" x="10" y="15" font-size="9.5" font-weight="700" fill="#00FF66">CLOUD NATIVE ARCHITECTURE</text>
      </g>
    </g>

    <!-- Card 7: Agile & SE -->
    <g transform="translate(576, 0)">
      <rect width="262" height="174" rx="12" fill="url(#ce-card-bg)" stroke="#00FF66" stroke-width="1" stroke-opacity="0.3"/>
      <rect x="0" y="0" width="4" height="174" rx="2" fill="#05FFA1"/>
      <text class="ce-mono" x="18" y="28" font-size="10" font-weight="700" letter-spacing="1.8" fill="#05FFA1">SOFTWARE ENGINEERING</text>
      <text class="ce-heading" x="18" y="66" font-size="17" fill="#E6FFF0">Agile Software Dev</text>
      <text class="ce-sans" x="18" y="92" font-size="13" font-weight="600" fill="#05FFA1">Scrum, Kanban, Sprint Life</text>
      <text class="ce-sans" x="18" y="114" font-size="12" fill="#88B99A">SDLC &amp; Version Control (Git)</text>
      <g transform="translate(18, 136)">
        <rect width="224" height="22" rx="4" fill="#00240E" stroke="#05FFA1" stroke-width="0.8"/>
        <text class="ce-mono" x="10" y="15" font-size="9.5" font-weight="700" fill="#05FFA1">AGILE PRACTITIONER</text>
      </g>
    </g>

    <!-- Card 8: TCS ESG -->
    <g transform="translate(864, 0)">
      <rect width="262" height="174" rx="12" fill="url(#ce-card-bg)" stroke="#00FF66" stroke-width="1" stroke-opacity="0.3"/>
      <rect x="0" y="0" width="4" height="174" rx="2" fill="#00FF66"/>
      <text class="ce-mono" x="18" y="28" font-size="10" font-weight="700" letter-spacing="1.8" fill="#00FF66">TCS · FORAGE</text>
      <text class="ce-heading" x="18" y="66" font-size="18" fill="#E6FFF0">TCS ESG Experience</text>
      <text class="ce-sans" x="18" y="92" font-size="13" font-weight="600" fill="#00FF66">Governance &amp; Sustainability</text>
      <text class="ce-sans" x="18" y="114" font-size="12" fill="#88B99A">Risk Mgmt &amp; Compliance</text>
      <g transform="translate(18, 136)">
        <rect width="224" height="22" rx="4" fill="#00240E" stroke="#00FF66" stroke-width="0.8"/>
        <text class="ce-mono" x="10" y="15" font-size="9.5" font-weight="700" fill="#00FF66">TATA CONSULTANCY SERVICES</text>
      </g>
    </g>
  </g>

  <!-- Row 3: EARNED BADGES SHOWCASE BAR -->
  <g transform="translate(36, 400)">
    <rect width="1128" height="60" rx="10" fill="url(#ce-badge-bg)" stroke="#00FF66" stroke-width="1" stroke-opacity="0.4"/>
    <text class="ce-mono" x="24" y="26" font-size="10" font-weight="700" letter-spacing="2" fill="#00FF66">VERIFIED BADGES &amp; ACCOLADES</text>
    <text class="ce-mono" x="24" y="46" font-size="11.5" fill="#E6FFF0">
      🛡️ Google Cybersecurity (98.81%)  ·  📄 IJNRD Author (2025)  ·  ☕ Java &amp; DSA Specialist  ·  ☁️ Cloud Architecture  ·  🤝 TCS Forage Experience
    </text>
  </g>
</svg>'''
validate_svg("certifications.svg", certs_svg)

# -------------------------------------------------------------
# 8. FOOTER SIGNATURE SVG (1200x200)
# -------------------------------------------------------------
footer_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 200" width="1200" height="200" role="img" aria-labelledby="sig-title">
  <title id="sig-title">Pratik Mengal — Engineering intelligence. Building resilient architectures.</title>
  <defs>
    <linearGradient id="sig-bg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#040F06"/>
      <stop offset="100%" stop-color="#000000"/>
    </linearGradient>
    <radialGradient id="sig-glow" cx="50%" cy="50%" r="50%">
      <stop offset="0" stop-color="#00FF66" stop-opacity="0.25"/>
      <stop offset="100%" stop-color="#00FF66" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="sig-name-grad" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#E6FFF0"/>
      <stop offset="50%" stop-color="#00FF66"/>
      <stop offset="100%" stop-color="#05FFA1"/>
    </linearGradient>
  </defs>
  <style>
    .sig-mono { font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", "Fira Code", monospace; }
    .sig-heading { font-family: Georgia, "Iowan Old Style", "Palatino Linotype", serif; }
    .sig-sans { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
  </style>

  <rect width="1200" height="200" fill="url(#sig-bg)"/>
  <ellipse cx="600" cy="100" rx="480" ry="80" fill="url(#sig-glow)"/>

  <line x1="40" y1="10" x2="1160" y2="10" stroke="#00FF66" stroke-width="1" stroke-opacity="0.3"/>

  <!-- Glowing Signature -->
  <text class="sig-heading" x="600" y="86" text-anchor="middle" font-size="60" font-style="italic" fill="url(#sig-name-grad)">
    Pratik Mengal
  </text>

  <!-- Tagline -->
  <text class="sig-sans" x="600" y="130" text-anchor="middle" font-size="16.5" fill="#E6FFF0" letter-spacing="0.5">
    Engineering intelligence. Designing secure &amp; resilient distributed architectures.
  </text>

  <!-- Telemetry Metadata Footer -->
  <text class="sig-mono" x="600" y="168" text-anchor="middle" font-size="11" letter-spacing="2.5" fill="#72A884">
    STATUS: 200 OK · PROTOCOL: HTTPS · HOST: mengalpratik.github.io · LOCATION: PUNE, INDIA
  </text>
</svg>'''
validate_svg("footer-signature.svg", footer_svg)

print("All enhanced SVGs successfully generated and verified!")
