"""
scripts/generators/projects.py

Generates project cards (1200x370) strictly matching the reference layout geometry:
viewBox 1200x370, left-side editorial typography with 3 metrics columns and tech badge chips,
right-side interactive cyber illustrations with matrix grid backdrop, and animated tracing borders.
"""

from .common import load_projects, validate_and_save_svg, xml_escape

def get_right_illustration(num: str, title: str) -> str:
    if num == "01":  # NeuroMatrix Learning Academy
        return '''<g transform="translate(800 42)">
        <!-- Terminal Window Frame -->
        <rect width="340" height="230" rx="12" fill="#010803" stroke="#00FF66" stroke-opacity=".35"/>
        <path d="M0 12 a12 12 0 0 1 12 -12 H328 a12 12 0 0 1 12 12 V32 H0 Z" fill="#031407"/>
        <line x1="0" y1="32" x2="340" y2="32" stroke="#00FF66" stroke-opacity=".2"/>
        <circle cx="18" cy="16" r="4.5" fill="#00FF66"/><circle cx="32" cy="16" r="4.5" fill="#05FFA1"/><circle cx="46" cy="16" r="4.5" fill="#00471B"/>
        <text class="p-mono" x="170" y="20" text-anchor="middle" font-size="10.5" fill="#88B99A">neuromatrix://curriculum_core.py</text>
        
        <!-- Code editor lines -->
        <g class="p-mono" font-size="11" fill="#88B99A" transform="translate(20 54)">
          <text y="0"><tspan fill="#05FFA1">class</tspan> <tspan fill="#E6FFF0">NeuroMatrix</tspan>:</text>
          <text y="20">    <tspan fill="#05FFA1">def</tspan> <tspan fill="#00FF66">__init__</tspan>(self, days=112):</text>
          <text y="40">        self.modules = <tspan fill="#E6FFF0">15</tspan></text>
          <text y="60">        self.status = <tspan fill="#00FF66">&quot;PRODUCTION&quot;</tspan></text>
          <text y="90">    <tspan fill="#05FFA1">def</tspan> <tspan fill="#00FF66">execute_curriculum</tspan>(self):</text>
          <text y="110">        <tspan fill="#05FFA1">return</tspan> <tspan fill="#E6FFF0">TelemetryEngine.eval()</tspan></text>
        </g>
        
        <!-- Progress bar -->
        <g transform="translate(20 192)">
          <rect width="300" height="22" rx="6" fill="#00240E" stroke="#00FF66" stroke-opacity=".4"/>
          <rect width="280" height="22" rx="6" fill="#00FF66" fill-opacity=".25"/>
          <text class="p-mono" x="150" y="15" text-anchor="middle" font-size="10" font-weight="700" fill="#00FF66">✓ 112 / 112 DAYS COMPLETED · 100%</text>
        </g>
      </g>'''
    elif num == "02":  # Myraa AI Assistant
        return '''<g transform="translate(800 42)">
        <!-- Neural Agent Node Network -->
        <rect width="340" height="230" rx="12" fill="#010803" stroke="#05FFA1" stroke-opacity=".3"/>
        
        <!-- Connecting Beziers -->
        <path d="M 170 115 C 100 115, 80 65, 80 65" fill="none" stroke="#00FF66" stroke-opacity=".4" stroke-dasharray="4 4"/>
        <path d="M 170 115 C 240 115, 260 65, 260 65" fill="none" stroke="#05FFA1" stroke-opacity=".4" stroke-dasharray="4 4"/>
        <path d="M 170 115 C 100 115, 80 175, 80 175" fill="none" stroke="#05FFA1" stroke-opacity=".4" stroke-dasharray="4 4"/>
        <path d="M 170 115 C 240 115, 260 175, 260 175" fill="none" stroke="#00FF66" stroke-opacity=".4" stroke-dasharray="4 4"/>
        
        <!-- Satellite Nodes -->
        <g transform="translate(80 65)">
          <circle r="22" fill="#021408" stroke="#00FF66" stroke-width="1.2"/>
          <text class="p-mono" y="4" text-anchor="middle" font-size="8.5" fill="#00FF66">LLM</text>
        </g>
        <g transform="translate(260 65)">
          <circle r="22" fill="#021408" stroke="#05FFA1" stroke-width="1.2"/>
          <text class="p-mono" y="4" text-anchor="middle" font-size="8.5" fill="#05FFA1">TOOLS</text>
        </g>
        <g transform="translate(80 175)">
          <circle r="22" fill="#021408" stroke="#05FFA1" stroke-width="1.2"/>
          <text class="p-mono" y="4" text-anchor="middle" font-size="8.5" fill="#05FFA1">MEMORY</text>
        </g>
        <g transform="translate(260 175)">
          <circle r="22" fill="#021408" stroke="#00FF66" stroke-width="1.2"/>
          <text class="p-mono" y="4" text-anchor="middle" font-size="8.5" fill="#00FF66">STREAM</text>
        </g>
        
        <!-- Central Agent Core -->
        <g transform="translate(170 115)">
          <circle r="36" fill="#00240E" stroke="#00FF66" stroke-width="1.6"/>
          <circle r="44" fill="none" stroke="#05FFA1" stroke-width="0.8" stroke-dasharray="6 4">
            <animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="20s" repeatCount="indefinite"/>
          </circle>
          <text class="p-mono" y="-4" text-anchor="middle" font-size="10.5" font-weight="700" fill="#E6FFF0">MYRAA</text>
          <text class="p-mono" y="12" text-anchor="middle" font-size="8.5" fill="#00FF66">AGENT</text>
        </g>
        
        <!-- Bottom Status -->
        <text class="p-mono" x="170" y="218" text-anchor="middle" font-size="9.5" letter-spacing="1.5" fill="#88B99A">STREAMING WEBSOCKETS · MULTI-TURN AI</text>
      </g>'''
    elif num == "03":  # NEURO//NODE Interface
        return '''<g transform="translate(800 42)">
        <!-- Cyber Command Center Dashboard -->
        <rect width="340" height="230" rx="12" fill="#010803" stroke="#00FF66" stroke-opacity=".3"/>
        
        <!-- Cluster Card 1 -->
        <g transform="translate(18 20)">
          <rect width="144" height="84" rx="8" fill="#031609" stroke="#00FF66" stroke-opacity=".35"/>
          <rect x="0" y="0" width="3" height="84" rx="1.5" fill="#00FF66"/>
          <text class="p-mono" x="12" y="22" font-size="9" letter-spacing="1.5" fill="#00FF66">LOCAL CLUSTER</text>
          <text class="p-serif" x="12" y="52" font-size="24" font-weight="300" fill="#E6FFF0">0ms</text>
          <text class="p-sans" x="12" y="70" font-size="10" fill="#88B99A">offline UI latency</text>
        </g>
        
        <!-- Cluster Card 2 -->
        <g transform="translate(178 20)">
          <rect width="144" height="84" rx="8" fill="#031609" stroke="#05FFA1" stroke-opacity=".35"/>
          <rect x="0" y="0" width="3" height="84" rx="1.5" fill="#05FFA1"/>
          <text class="p-mono" x="12" y="22" font-size="9" letter-spacing="1.5" fill="#05FFA1">DATA SOVEREIGNTY</text>
          <text class="p-serif" x="12" y="52" font-size="24" font-weight="300" fill="#E6FFF0">100%</text>
          <text class="p-sans" x="12" y="70" font-size="10" fill="#88B99A">air-gapped privacy</text>
        </g>
        
        <!-- Signal / Audio Matrix Waveform -->
        <g transform="translate(18 122)">
          <rect width="304" height="90" rx="8" fill="#020E05" stroke="#00FF66" stroke-opacity=".25"/>
          <path d="M 20 168 L 50 148 L 80 178 L 110 138 L 140 162 L 170 142 L 200 172 L 230 150 L 260 168 L 290 140" fill="none" stroke="#00FF66" stroke-width="1.5"/>
          <text class="p-mono" x="14" y="22" font-size="9" letter-spacing="1.5" fill="#88B99A">MATRIX TELEMETRY CLUSTERS</text>
          <circle cx="290" cy="50" r="4" fill="#05FFA1"/>
        </g>
      </g>'''
    else:  # Axcentra Engineering Suite
        return '''<g transform="translate(800 42)">
        <!-- Enterprise Architecture Flow -->
        <rect width="340" height="230" rx="12" fill="#010803" stroke="#00FF66" stroke-opacity=".3"/>
        
        <text class="p-mono" x="20" y="26" font-size="10" letter-spacing="2" fill="#00FF66">ENTERPRISE PIPELINE</text>
        
        <!-- Step 1: Client UI -->
        <g transform="translate(24 46)">
          <rect width="80" height="50" rx="6" fill="#021408" stroke="#00FF66" stroke-opacity=".4"/>
          <text class="p-mono" x="40" y="24" text-anchor="middle" font-size="9" fill="#00FF66">CLIENT</text>
          <text class="p-mono" x="40" y="38" text-anchor="middle" font-size="8" fill="#88B99A">React / Web</text>
        </g>
        
        <path d="M 104 71 H 130" stroke="#00FF66" stroke-width="1.2"/>
        
        <!-- Step 2: REST Gateway -->
        <g transform="translate(130 46)">
          <rect width="80" height="50" rx="6" fill="#00240E" stroke="#05FFA1"/>
          <text class="p-mono" x="40" y="24" text-anchor="middle" font-size="9" font-weight="700" fill="#E6FFF0">GATEWAY</text>
          <text class="p-mono" x="40" y="38" text-anchor="middle" font-size="8" fill="#05FFA1">JWT / RBAC</text>
        </g>
        
        <path d="M 210 71 H 236" stroke="#00FF66" stroke-width="1.2"/>
        
        <!-- Step 3: Backend Services -->
        <g transform="translate(236 46)">
          <rect width="80" height="50" rx="6" fill="#021408" stroke="#00FF66" stroke-opacity=".4"/>
          <text class="p-mono" x="40" y="24" text-anchor="middle" font-size="9" fill="#00FF66">SERVICES</text>
          <text class="p-mono" x="40" y="38" text-anchor="middle" font-size="8" fill="#88B99A">Node / Java</text>
        </g>
        
        <!-- Audit / Specs Bar -->
        <g transform="translate(24 122)">
          <rect width="292" height="88" rx="8" fill="#020E05" stroke="#00FF66" stroke-opacity=".25"/>
          <text class="p-mono" x="16" y="24" font-size="9.5" fill="#E6FFF0">> SWE Trainee Tenure: 2026</text>
          <text class="p-mono" x="16" y="44" font-size="9.5" fill="#88B99A">> Modular Enterprise Web Applications</text>
          <text class="p-mono" x="16" y="64" font-size="9.5" fill="#00FF66">> Rigorous Code Review &amp; Agile Sprints</text>
        </g>
      </g>'''

def generate_projects() -> None:
    projects = load_projects()

    for p in projects:
        chips_xml = []
        cx = 56
        for idx, chip in enumerate(p["chips"]):
            chip_esc = xml_escape(chip)
            cw = len(chip) * 8 + 24
            delay = f"{1.0 + idx * 0.12:.2f}"
            chips_xml.append(
                f'''<g class="p-chip" style="animation-delay:{delay}s">
        <rect x="{cx}" y="314" width="{cw}" height="26" rx="13" fill="#031609" stroke="#00FF66" stroke-opacity=".35"/>
        <text class="p-mono" x="{cx + cw/2}" y="331" text-anchor="middle" font-size="11.5" fill="#E6FFF0">{chip_esc}</text>
      </g>'''
            )
            cx += cw + 10
        chips_markup = "\n      ".join(chips_xml)

        m = p["metrics"]
        m1_val, m1_lbl = xml_escape(m[0][0]), xml_escape(m[0][1])
        m2_val, m2_lbl = xml_escape(m[1][0]), xml_escape(m[1][1])
        m3_val, m3_lbl = xml_escape(m[2][0]), xml_escape(m[2][1])

        title_esc = xml_escape(p["title"])
        desc_esc = xml_escape(p["desc"])
        cat_esc = xml_escape(p["category"])
        built_esc = xml_escape(p["built"])
        right_illustration = get_right_illustration(p["num"], p["title"])

        svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 370" width="1200" height="370" role="img" aria-labelledby="p{p['num']}-t">
  <title id="p{p['num']}-t">{title_esc}: {desc_esc}</title>
  <defs>
    <linearGradient id="p{p['num']}-bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#041207"/>
      <stop offset="1" stop-color="#000000"/>
    </linearGradient>
    <radialGradient id="p{p['num']}-glow" cx="82%" cy="30%" r="55%">
      <stop offset="0" stop-color="#00FF66" stop-opacity=".45"/>
      <stop offset="1" stop-color="#00240E" stop-opacity="0"/>
    </radialGradient>
    <pattern id="p{p['num']}-grid" width="28" height="28" patternUnits="userSpaceOnUse">
      <path d="M28 0H0V28" fill="none" stroke="#00FF66" stroke-opacity=".07"/>
    </pattern>
    <filter id="p{p['num']}-glowf" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="3" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <clipPath id="p{p['num']}-clip"><rect width="1200" height="370" rx="18"/></clipPath>
    <linearGradient id="p{p['num']}-trace" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#E6FFF0"/><stop offset=".45" stop-color="#00FF66"/><stop offset="1" stop-color="#00FF66" stop-opacity="0"/>
    </linearGradient>
  </defs>
  <style>
    .p-serif {{ font-family: Georgia, "Iowan Old Style", "Palatino Linotype", "Times New Roman", serif; }}
    .p-mono {{ font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace; }}
    .p-sans {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; }}
    .p-in {{ animation: p-in 1.2s cubic-bezier(.16,1,.3,1) both; }}
    .p-d1 {{ animation-delay: .15s; }} .p-d2 {{ animation-delay: .4s; }}
    .p-chip {{ animation: p-chip .7s cubic-bezier(.34,1.56,.64,1) both; }}
    @keyframes p-chip {{ from {{ opacity: 0.85; transform: translateY(4px); }} to {{ opacity: 1; transform: none; }} }}
    .p-draw {{ stroke-dasharray: 600; stroke-dashoffset: 600; animation: p-draw 2s cubic-bezier(.65,0,.35,1) .5s forwards; }}
    @keyframes p-in {{ from {{ opacity: 0.85; transform: translateY(6px); }} to {{ opacity: 1; transform: none; }} }}
    @keyframes p-draw {{ to {{ stroke-dashoffset: 0; }} }}
    @media (prefers-reduced-motion: reduce) {{ .p-in, .p-chip {{ animation: none; }} .p-draw {{ animation: none; stroke-dashoffset: 0; }} }}
    .p-trace {{ stroke-dasharray: 564 3136; stroke-dashoffset: 3700; animation: p-trace 7s linear infinite; }}
    @keyframes p-trace {{ to {{ stroke-dashoffset: 0; }} }}
    @media (prefers-reduced-motion: reduce) {{ .p-trace {{ display: none; }} }}
  </style>
  <g clip-path="url(#p{p['num']}-clip)">
    <rect width="1200" height="370" fill="url(#p{p['num']}-bg)"/>
    <rect x="720" width="480" height="370" fill="url(#p{p['num']}-grid)"/>
    <rect width="1200" height="370" fill="url(#p{p['num']}-glow)"/>
    
    <!-- Left Column Content -->
    <g class="p-in p-d1">
      <text class="p-mono" x="56" y="62" font-size="12" letter-spacing="2.6" fill="#00FF66">{p['num']} · {cat_esc}</text>
      <text class="p-serif" x="54" y="126" font-size="52" font-weight="300" letter-spacing="-1.5" fill="#E6FFF0">{title_esc}</text>
      <text class="p-sans" x="56" y="166" font-size="17" fill="#88B99A">{desc_esc}</text>
      <text class="p-mono" x="56" y="200" font-size="12.5" fill="#E6FFF0"><tspan fill="#00FF66">BUILT ›</tspan> {built_esc}</text>
      <line class="p-draw" x1="56" y1="226" x2="680" y2="226" stroke="#00FF66" stroke-opacity=".3"/>
      
      <!-- 3 Metrics Columns -->
      <g transform="translate(56 266)">
        <text class="p-serif" font-size="34" font-weight="300" fill="#E6FFF0">{m1_val}</text>
        <text class="p-sans" y="24" font-size="12.5" fill="#88B99A">{m1_lbl}</text>
      </g>
      <g transform="translate(261 266)">
        <text class="p-serif" font-size="34" font-weight="300" fill="#E6FFF0">{m2_val}</text>
        <text class="p-sans" y="24" font-size="12.5" fill="#88B99A">{m2_lbl}</text>
      </g>
      <g transform="translate(466 266)">
        <text class="p-serif" font-size="34" font-weight="300" fill="#E6FFF0">{m3_val}</text>
        <text class="p-sans" y="24" font-size="12.5" fill="#88B99A">{m3_lbl}</text>
      </g>
      
      <!-- Tech Badge Chips -->
      {chips_markup}
    </g>
    
    <!-- Right Column Illustration -->
    <g class="p-in p-d2">
      {right_illustration}
    </g>
    
    <!-- Outer Border & Tracing Edge -->
    <rect x=".5" y=".5" width="1199" height="369" rx="17.5" fill="none" stroke="#00FF66" stroke-opacity=".2"/>
    <rect class="p-trace" style="animation-delay:0.0s" x=".5" y=".5" width="1199" height="369" rx="17.5" fill="none" stroke="url(#p{p['num']}-trace)" stroke-width="1.6" stroke-linecap="round"/>
  </g>
</svg>'''
        validate_and_save_svg(p["filename"], svg)
