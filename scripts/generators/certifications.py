"""
scripts/generators/certifications.py

Generates certifications.svg (1200x420) strictly matching the reference layout:
4 columns x 2 rows of 265x170 cards with corner badge dots, divider line at y=54,
animated tracing edges, clean unclipped 14px typography, and Hacker Green palette.
"""

from .common import validate_and_save_svg, xml_escape

CERTS_DATA = [
    # Row 1
    {
        "category": "GOOGLE",
        "dots": 2,
        "lines": [
            ("Google Cybersecurity", "#E6FFF0"),
            ("Professional Certificate", "#E6FFF0"),
            ("98.81% Aggregate Score", "#00FF66"),
        ],
        "col": 40,
        "row": 40,
        "delay": "0.20s",
        "edge_delay": "2.00s",
    },
    {
        "category": "CISCO",
        "dots": 2,
        "lines": [
            ("Cybersecurity Essentials", "#E6FFF0"),
            ("Network Defense &amp; Threat Intel", "#E6FFF0"),
            ("Packet Tracer &amp; Forensics", "#88B99A"),
        ],
        "col": 325,
        "row": 40,
        "delay": "0.32s",
        "edge_delay": "2.35s",
    },
    {
        "category": "ORACLE &amp; JAVA",
        "dots": 2,
        "lines": [
            ("Java Foundations Certified", "#E6FFF0"),
            ("Object-Oriented Programming", "#E6FFF0"),
            ("Data Structures &amp; Algorithms", "#05FFA1"),
        ],
        "col": 610,
        "row": 40,
        "delay": "0.44s",
        "edge_delay": "2.70s",
    },
    {
        "category": "DATABASE &amp; SQL",
        "dots": 2,
        "lines": [
            ("Database Management Systems", "#E6FFF0"),
            ("Relational Schema Design", "#E6FFF0"),
            ("SQL Indexing &amp; Queries", "#88B99A"),
        ],
        "col": 895,
        "row": 40,
        "delay": "0.56s",
        "edge_delay": "3.05s",
    },
    # Row 2
    {
        "category": "CLOUD &amp; DEVOPS",
        "dots": 2,
        "lines": [
            ("Cloud Computing Fundamentals", "#E6FFF0"),
            ("Docker &amp; Containerization", "#E6FFF0"),
            ("AWS Architecture Basics", "#00FF66"),
        ],
        "col": 40,
        "row": 230,
        "delay": "0.68s",
        "edge_delay": "3.40s",
    },
    {
        "category": "RESEARCH",
        "dots": 2,
        "lines": [
            ("IJNRD Published Author", "#E6FFF0"),
            ("May 2025 · Volume 10 Issue 5", "#E6FFF0"),
            ("Health Management &amp; AI", "#05FFA1"),
        ],
        "col": 325,
        "row": 230,
        "delay": "0.80s",
        "edge_delay": "3.75s",
    },
    {
        "category": "SOFTWARE ENG",
        "dots": 2,
        "lines": [
            ("Agile Software Engineering", "#E6FFF0"),
            ("Scrum &amp; Sprint Workflows", "#E6FFF0"),
            ("REST APIs &amp; Microservices", "#88B99A"),
        ],
        "col": 610,
        "row": 230,
        "delay": "0.92s",
        "edge_delay": "4.10s",
    },
    {
        "category": "INDUSTRY TRACK",
        "dots": 3,
        "lines": [
            ("Axcentra SWE Trainee", "#E6FFF0"),
            ("Devtown Full-Stack MERN", "#E6FFF0"),
            ("Codsoft Java Developer", "#00FF66"),
        ],
        "col": 895,
        "row": 230,
        "delay": "1.04s",
        "edge_delay": "4.45s",
    },
]

def generate_certifications() -> None:
    tiles_xml = []
    for c in CERTS_DATA:
        dots_xml = "".join(f'<circle cx="{238 - j * 11}" cy="31" r="3.5" fill="#00FF66"/>' for j in range(c["dots"]))
        lines_xml = "".join(
            f'<text class="ce-sans" x="22" y="{86 + k * 22}" font-size="14" fill="{color}">{text}</text>'
            for k, (text, color) in enumerate(c["lines"])
        )
        
        tiles_xml.append(f'''  <g class="ce-tile" style="animation-delay:{c['delay']}"><g transform="translate({c['col']} {c['row']})">
    <rect width="265" height="170" rx="14" fill="#020D05" stroke="#00FF66" stroke-opacity=".24"/>
    <rect width="265" height="170" rx="14" fill="none" stroke="url(#ce-edge)" stroke-width="1.2" class="ce-edge" style="animation-delay:{c['edge_delay']}"/>
    <text class="ce-mono" x="22" y="36" font-size="11.5" letter-spacing="2.6" fill="#00FF66">{c['category']}</text>
    {dots_xml}
    <line x1="22" y1="54" x2="243" y2="54" stroke="#00FF66" stroke-opacity=".15"/>
    {lines_xml}
  </g></g>''')

    tiles_markup = "\n".join(tiles_xml)

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 420" width="1200" height="420" role="img" aria-labelledby="ce-t ce-d">
  <title id="ce-t">Certifications &amp; Credentials</title>
  <desc id="ce-d">Google Cybersecurity Professional Certificate (98.81%); Cisco Cybersecurity Essentials; Oracle Java Foundations; Database Management Systems (SQL); Cloud Computing; IJNRD Published Author; Agile Software Engineering; and Industry Internship Credentials.</desc>
  <defs>
    <linearGradient id="ce-bg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#041207"/>
      <stop offset="1" stop-color="#000000"/>
    </linearGradient>
    <radialGradient id="ce-glow" cx="15%" cy="100%" r="70%">
      <stop offset="0" stop-color="#00FF66" stop-opacity=".3"/>
      <stop offset="1" stop-color="#00240E" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="ce-edge" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#E6FFF0"/>
      <stop offset="0.5" stop-color="#00FF66"/>
      <stop offset="1" stop-color="#00FF66" stop-opacity="0"/>
    </linearGradient>
  </defs>
  <style>
    .ce-serif {{ font-family: Georgia, "Iowan Old Style", "Palatino Linotype", "Times New Roman", serif; }}
    .ce-mono {{ font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace; }}
    .ce-sans {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; }}
    .ce-tile {{ animation: ce-in 1s cubic-bezier(.34,1.3,.64,1) both; }}
    .ce-edge {{ stroke-dasharray: 870; stroke-dashoffset: 870; animation: ce-edge 6s cubic-bezier(.65,0,.35,1) infinite; }}
    @keyframes ce-in {{ from {{ opacity: 0.85; transform: translateY(18px) scale(.97); }} to {{ opacity: 1; transform: none; }} }}
    @keyframes ce-edge {{ 0% {{ stroke-dashoffset: 870; opacity: 1; }} 40% {{ stroke-dashoffset: 0; opacity: 1; }} 60%, 100% {{ stroke-dashoffset: 0; opacity: 0; }} }}
    @media (prefers-reduced-motion: reduce) {{ .ce-tile {{ animation: none; }} .ce-edge {{ display: none; }} }}
  </style>

  <rect width="1200" height="420" rx="20" fill="url(#ce-bg)"/>
  <rect width="1200" height="420" rx="20" fill="url(#ce-glow)"/>
  <rect x=".5" y=".5" width="1199" height="419" rx="19.5" fill="none" stroke="#00FF66" stroke-opacity=".16"/>

{tiles_markup}
</svg>'''
    validate_and_save_svg("certifications.svg", svg)
