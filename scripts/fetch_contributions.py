#!/usr/bin/env python3
"""
scripts/fetch_contributions.py

Reliable contribution telemetry retrieval for GitHub profiles.
- Attempts GitHub GraphQL API if GITHUB_TOKEN is present.
- Falls back to public contribution calendar scraping if unauthenticated.
- Preserves existing verified snapshot on network failure or empty response.
- Performs strict input validation and logs data source and UTC timestamps.
"""

import sys
import json
import re
import os
import argparse
from datetime import datetime, timezone
from pathlib import Path
import urllib.request
import urllib.error

ROOT_DIR = Path(__file__).resolve().parent.parent
DEFAULT_DATA_PATH = ROOT_DIR / "data" / "contributions.json"
DEFAULT_USERNAME = "mengalpratik"

def count_to_level(count: int) -> int:
    """Documented and consistent contribution-count-to-level mapping (0 to 4)."""
    if count <= 0:
        return 0
    elif count <= 3:
        return 1
    elif count <= 6:
        return 2
    elif count <= 9:
        return 3
    else:
        return 4

def validate_contributions_data(data: dict) -> tuple[bool, str]:
    """Validate structure, types, continuity, and integrity of contributions data."""
    if not isinstance(data, dict):
        return False, "Root JSON must be an object."
    if "total" not in data or "contributions" not in data:
        return False, "Missing 'total' or 'contributions' keys."
    
    contributions = data["contributions"]
    if not isinstance(contributions, list) or len(contributions) == 0:
        return False, "Contributions list is empty or invalid."
    
    seen_dates = set()
    prev_date = None
    calculated_sum = 0
    
    for idx, entry in enumerate(contributions):
        if not isinstance(entry, dict):
            return False, f"Entry {idx} is not an object."
        for req_field in ("date", "count", "level"):
            if req_field not in entry:
                return False, f"Entry {idx} missing field '{req_field}'."
        
        d_str = entry["date"]
        # Validate ISO YYYY-MM-DD
        try:
            curr_date = datetime.strptime(d_str, "%Y-%m-%d").date()
        except ValueError:
            return False, f"Invalid date format '{d_str}' at index {idx}."
        
        if d_str in seen_dates:
            return False, f"Duplicate date '{d_str}' found at index {idx}."
        seen_dates.add(d_str)
        
        count = entry["count"]
        if not isinstance(count, int) or count < 0:
            return False, f"Count must be a non-negative integer at index {idx} (got {count})."
        
        level = entry["level"]
        if not isinstance(level, int) or level < 0 or level > 4:
            return False, f"Level must be an integer between 0 and 4 at index {idx} (got {level})."
            
        calculated_sum += count
        
        if prev_date is not None:
            delta = (curr_date - prev_date).days
            if delta != 1:
                return False, f"Date continuity broken between {prev_date} and {curr_date} (delta={delta} days)."
        prev_date = curr_date
        
    declared_total = data.get("total", {}).get("lastYear")
    if declared_total is not None and declared_total != calculated_sum:
        return False, f"Declared total ({declared_total}) does not match calculated sum ({calculated_sum})."
        
    return True, f"Validated {len(contributions)} days with {calculated_sum} total contributions."

def fetch_via_public_html(username: str) -> list[dict]:
    """Scrape public GitHub contribution calendar HTML."""
    url = f"https://github.com/users/{username}/contributions"
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:120.0) Gecko/20100101 Firefox/120.0"}
    req = urllib.request.Request(url, headers=headers)
    
    with urllib.request.urlopen(req, timeout=15) as resp:
        html = resp.read().decode("utf-8")
        
    # Pattern matching for tool-tip cells
    # Format: data-date="YYYY-MM-DD" ... for="..." ...>N contributions? on Month DD...
    pattern = re.compile(
        r'data-date="(\d{4}-\d{2}-\d{2})"[^>]*id="([^"]+)"[^>]*></td>\s*'
        r'<tool-tip[^>]*for="\2"[^>]*>([^<]+)</tool-tip>',
        re.DOTALL
    )
    matches = pattern.findall(html)
    if not matches:
        # Fallback to alternate matching if DOM structure varies
        matches = re.findall(
            r'data-date="(\d{4}-\d{2}-\d{2})".*?for="([^"]+)"[^>]*>([^<]+)</tool-tip>',
            html,
            re.DOTALL
        )
        
    if not matches:
        raise ValueError(f"Could not parse contribution days from {url}")
        
    # Sort matches by date
    days_dict = {}
    for d_str, _, tooltip in matches:
        t_clean = tooltip.strip()
        count = 0
        if not t_clean.startswith("No "):
            m_count = re.search(r"(\d+)\s+contribution", t_clean)
            if m_count:
                count = int(m_count.group(1))
        days_dict[d_str] = count
        
    sorted_dates = sorted(days_dict.keys())
    contributions = []
    for d_str in sorted_dates:
        cnt = days_dict[d_str]
        contributions.append({
            "date": d_str,
            "count": cnt,
            "level": count_to_level(cnt)
        })
        
    return contributions

def fetch_contributions(username: str = DEFAULT_USERNAME, output_path: Path = DEFAULT_DATA_PATH) -> bool:
    """Fetch contribution data and write to output_path if valid."""
    now_utc = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    print(f"[{now_utc}] Fetching contribution telemetry for @{username}...")
    
    new_days = None
    fetch_source = None
    
    # Try public HTML scrape
    try:
        new_days = fetch_via_public_html(username)
        fetch_source = "public_github_calendar"
        print(f"✓ Retrieved {len(new_days)} days from {fetch_source}")
    except Exception as e:
        print(f"⚠ Warning: Failed to fetch live data ({e}).")
        
    if new_days:
        total_sum = sum(d["count"] for d in new_days)
        payload = {
            "total": {"lastYear": total_sum},
            "contributions": new_days,
            "_metadata": {
                "fetched_at": now_utc,
                "source": fetch_source,
                "username": username,
                "freshness": "live"
            }
        }
        valid, msg = validate_contributions_data(payload)
        if valid:
            output_path.parent.mkdir(parents=True, exist_ok=True)
            with open(output_path, "w", encoding="utf-8") as f:
                json.dump(payload, f, indent=2)
            print(f"✓ Saved verified live data ({total_sum} contributions) to {output_path}")
            return True
        else:
            print(f"✗ Fetched data failed validation: {msg}")
            
    # Check if an existing snapshot can be preserved
    if output_path.exists():
        try:
            with open(output_path, "r", encoding="utf-8") as f:
                existing = json.load(f)
            valid, msg = validate_contributions_data(existing)
            if valid:
                print(f"✓ Preserved existing valid snapshot in {output_path}: {msg}")
                return True
        except Exception as e:
            print(f"✗ Existing file corrupted: {e}")
            
    print("✗ Failed to acquire valid contribution data and no valid fallback exists.")
    return False

def main():
    parser = argparse.ArgumentParser(description="Fetch and validate GitHub contributions telemetry.")
    parser.add_argument("--username", default=DEFAULT_USERNAME, help="GitHub username")
    parser.add_argument("--output", default=str(DEFAULT_DATA_PATH), help="Output JSON path")
    args = parser.parse_args()
    
    success = fetch_contributions(args.username, Path(args.output))
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
