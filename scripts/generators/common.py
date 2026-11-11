"""
scripts/generators/common.py

Shared utilities, color palette constants, typography definitions, and SVG validator.
"""

import os
import re
import json
import base64
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent.parent
DATA_DIR = ROOT_DIR / "data"
ASSETS_DIR = ROOT_DIR / "assets"
AVATAR_PATH = ROOT_DIR / "avatar.png"

# Color Palette (Hacker Green & Pitch Black)
COLOR_BG_BLACK = "#000000"
COLOR_BG_DARK = "#020603"
COLOR_BG_CARD = "#030C05"
COLOR_PANEL_BG = "#040F06"
COLOR_GREEN_PRIMARY = "#00FF66"
COLOR_GREEN_CYAN = "#05FFA1"
COLOR_GREEN_LASER = "#00FF41"
COLOR_TEXT_PRIMARY = "#E6FFF0"
COLOR_TEXT_SECONDARY = "#88B99A"
COLOR_TEXT_MUTED = "#72A884"
COLOR_BORDER_DIM = "#003B19"
COLOR_BORDER_GREEN = "#00FF66"

# Common Typography CSS
FONTS_CSS = """
    .mono { font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", "Fira Code", monospace; }
    .sans { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", sans-serif; }
    .heading { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Fira Code", monospace; font-weight: 700; }
    .display { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Fira Code", monospace; font-weight: 900; }
"""

def xml_escape(text: str) -> str:
    """Escape special XML characters (&, <, >, \", ')."""
    if not isinstance(text, str):
        return str(text)
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
        .replace("'", "&apos;")
    )


def load_json(path: Path) -> dict | list:
    """Load JSON from specified path with utf-8 encoding."""
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def load_profile() -> dict:
    return load_json(DATA_DIR / "profile.json")

def load_projects() -> list:
    return load_json(DATA_DIR / "projects.json")

def load_certifications() -> dict:
    return load_json(DATA_DIR / "certifications.json")

def load_telemetry() -> dict:
    return load_json(DATA_DIR / "telemetry.json")

def get_avatar_b64() -> str:
    """Return base64 encoded avatar string or empty string if absent."""
    if AVATAR_PATH.exists():
        with open(AVATAR_PATH, "rb") as f:
            return base64.b64encode(f.read()).decode("utf-8")
    return ""

def validate_and_save_svg(filename: str, content: str) -> None:
    """Strictly validate SVG XML, viewBox, ID uniqueness, and URL references, then write to file."""
    content_clean = content.strip()
    
    # 1. XML Parse Check
    try:
        root = ET.fromstring(content_clean)
    except ET.ParseError as e:
        raise ValueError(f"XML parse error in {filename}: {e}")
        
    # 2. Dimensions & ViewBox Check
    vb = root.get("viewBox")
    w = root.get("width")
    h = root.get("height")
    if vb:
        vb_parts = vb.split()
        if len(vb_parts) == 4 and w and h:
            vb_w, vb_h = vb_parts[2], vb_parts[3]
            if str(int(float(vb_w))) != str(int(float(w))) or str(int(float(vb_h))) != str(int(float(h))):
                raise ValueError(f"viewBox dimension mismatch in {filename}: vb={vb_w}x{vb_h} vs w,h={w}x{h}")

    # 3. Duplicate ID Check
    ids = re.findall(r'id=[\"\']([^\"\']+)[\"\']', content_clean)
    dup_ids = [x for x in set(ids) if ids.count(x) > 1]
    if dup_ids:
        raise ValueError(f"Duplicate XML IDs found in {filename}: {dup_ids}")
        
    # 4. URL Reference Check
    refs = re.findall(r'url\(#([^)]+)\)', content_clean)
    missing_refs = [r for r in refs if r not in ids]
    if missing_refs:
        raise ValueError(f"Missing referenced IDs in {filename}: {missing_refs}")

    # 5. Write to assets directory
    ASSETS_DIR.mkdir(parents=True, exist_ok=True)
    out_path = ASSETS_DIR / filename
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(content_clean)
        
    print(f"✓ Validated & generated {filename} ({len(content_clean)} bytes)")
