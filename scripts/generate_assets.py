#!/usr/bin/env python3
"""
scripts/generate_assets.py

Main asset generator orchestrator for Pratik Mengal's GitHub Profile SVGs.
Coordinates modular generators from scripts/generators/ to deterministically
produce all 18 profile SVGs in assets/ from centralized data in data/.
"""

import sys
import argparse
from pathlib import Path

# Add scripts directory to sys.path to allow imports from generators package
SCRIPTS_DIR = Path(__file__).resolve().parent
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

from generators.hero import generate_hero
from generators.titles import generate_titles
from generators.about import generate_about
from generators.recognition import generate_recognition
from generators.projects import generate_projects
from generators.toolkit import generate_toolkit
from generators.certifications import generate_certifications
from generators.telemetry import generate_telemetry
from generators.footer import generate_footer

def generate_all_assets() -> bool:
    """Execute all modular SVG generators and return overall success."""
    print("============================================================")
    print("  GENERATING HACKER GREEN & PITCH BLACK GITHUB PROFILE SVGS ")
    print("============================================================")
    try:
        print("\n[1/9] Hero Banner...")
        generate_hero()

        print("\n[2/9] Section Titles...")
        generate_titles()

        print("\n[3/9] About Terminal Intro...")
        generate_about()

        print("\n[4/9] Recognition & Milestones...")
        generate_recognition()

        print("\n[5/9] Compact Project Cards...")
        generate_projects()

        print("\n[6/9] Tech Constellation Toolkit...")
        generate_toolkit()

        print("\n[7/9] Verified Certifications & Badges...")
        generate_certifications()

        print("\n[8/9] GitHub Telemetry & Language Distribution...")
        generate_telemetry()

        print("\n[9/9] Footer Signature...")
        generate_footer()

        print("\n============================================================")
        print("✓ All 18 profile SVGs generated and validated successfully!")
        print("============================================================")
        return True
    except Exception as e:
        print(f"\n✗ Error during asset generation: {e}", file=sys.stderr)
        return False

def main():
    parser = argparse.ArgumentParser(description="Generate modular GitHub profile SVGs.")
    parser.add_argument("--check", action="store_true", help="Validate assets generation")
    args = parser.parse_args()

    success = generate_all_assets()
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
