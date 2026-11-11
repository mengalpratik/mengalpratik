"""
scripts/generators/certifications.py

Generates certifications.svg (1200x490) presenting verified credentials and earned badges.
"""

from .common import load_certifications, validate_and_save_svg, xml_escape

def generate_certifications() -> None:
    data = load_certifications()
    creds = data["credentials"]
    accolades = data["accolades"]
    
    # 2 rows of 4 cards
    card_offsets_x = [0, 288, 576, 864]
    row1_xml = []
    row2_xml = []
    
    for i, c in enumerate(creds):
        row = i // 4
        col = i % 4
        cx = card_offsets_x[col]
        accent = c["accent"]
        
        track_esc = xml_escape(c["track"])
        title_esc = xml_escape(c["title"])
        status_esc = xml_escape(c["status"])
        skills_esc = xml_escape(c["skills"])
        badge_esc = xml_escape(c["badge"])
        
        card_content = f'''<g transform="translate({cx}, 0)">
      <rect width="265" height="174" rx="12" fill="url(#ce-card-bg)" stroke="#00FF66" stroke-width="1.2" stroke-opacity="0.35"/>
      <rect x="0" y="0" width="4" height="174" rx="2" fill="{accent}"/>
      <text class="ce-mono" x="18" y="28" font-size="10" font-weight="700" letter-spacing="1.8" fill="{accent}">{track_esc}</text>
      <text class="ce-heading" x="18" y="64" font-size="16.5" fill="#E6FFF0">{title_esc}</text>
      <text class="ce-sans" x="18" y="90" font-size="12.5" font-weight="600" fill="{accent}">{status_esc}</text>
      <text class="ce-sans" x="18" y="112" font-size="11.5" fill="#88B99A">{skills_esc}</text>
      <g transform="translate(18, 134)">
        <rect width="228" height="22" rx="4" fill="#00240E" stroke="{accent}" stroke-width="0.8"/>
        <text class="ce-mono" x="10" y="15" font-size="9.5" font-weight="700" fill="{accent}">{badge_esc}</text>
      </g>
    </g>'''
        if row == 0:
            row1_xml.append(card_content)
        else:
            row2_xml.append(card_content)
            
    row1_markup = "\n    ".join(row1_xml)
    row2_markup = "\n    ".join(row2_xml)
    
    # 5 Accolade chips in row 3
    chip_offsets = [0, 222, 434, 656, 884]
    chip_widths = [210, 200, 210, 216, 200]
    accolade_xml = []
    for i, acc in enumerate(accolades):
        ox = chip_offsets[i]
        cw = chip_widths[i]
        accent = acc["accent"]
        acc_text = xml_escape(acc["text"])
        accolade_xml.append(f'''<g transform="translate({ox}, 0)">
        <rect width="{cw}" height="28" rx="6" fill="#020C05" stroke="{accent}" stroke-width="0.9"/>
        <text class="ce-mono" x="12" y="18" font-size="10" font-weight="700" fill="{accent}">{acc_text}</text>
      </g>''')
    accolade_markup = "\n      ".join(accolade_xml)

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 490" width="1200" height="490" role="img" aria-labelledby="ce-title ce-desc">
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
    .ce-mono {{ font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", "Fira Code", monospace; }}
    .ce-heading {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Fira Code", monospace; font-weight: 700; }}
    .ce-sans {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", sans-serif; }}
  </style>

  <rect width="1200" height="490" fill="#000000"/>

  <!-- Row 1: 4 Cards -->
  <g transform="translate(36, 16)">
    {row1_markup}
  </g>

  <!-- Row 2: 4 Cards -->
  <g transform="translate(36, 206)">
    {row2_markup}
  </g>

  <!-- Row 3: 5 DISTINCT EARNED BADGE CHIPS -->
  <g transform="translate(36, 400)">
    <rect width="1128" height="74" rx="12" fill="url(#ce-badge-bg)" stroke="#00FF66" stroke-width="1" stroke-opacity="0.4"/>
    <text class="ce-mono" x="22" y="24" font-size="10" font-weight="700" letter-spacing="2" fill="#00FF66">VERIFIED BADGES &amp; ACCOLADES</text>

    <!-- 5 Badge Chips -->
    <g transform="translate(22, 34)">
      {accolade_markup}
    </g>
  </g>
</svg>'''
    validate_and_save_svg("certifications.svg", svg)
