"""
tests/test_svg_validation.py

Validates XML syntax, viewBox consistency, ID uniqueness, URL references, and reduced-motion support.
"""

import re
import glob
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
ASSETS_DIR = ROOT_DIR / "assets"

EXPECTED_SVGS = [
    "about-intro.svg",
    "achievement-motif.svg",
    "certifications.svg",
    "contribution-snake.svg",
    "footer-signature.svg",
    "github-telemetry.svg",
    "hero-banner.svg",
    "project-axcentra.svg",
    "project-myraa.svg",
    "project-neuromatrix.svg",
    "project-neurostore.svg",
    "tech-constellation.svg",
    "title-about.svg",
    "title-certifications.svg",
    "title-commits.svg",
    "title-connect.svg",
    "title-recognition.svg",
    "title-toolkit.svg",
    "title-work.svg",
]

class TestSVGValidation(unittest.TestCase):
    def test_all_expected_svgs_exist(self):
        for svg_name in EXPECTED_SVGS:
            p = ASSETS_DIR / svg_name
            self.assertTrue(p.exists(), f"Asset {svg_name} must exist in assets/")

    def test_svg_xml_parsing_and_viewbox(self):
        for svg_name in EXPECTED_SVGS:
            path = ASSETS_DIR / svg_name
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()

            # 1. XML Parse
            try:
                root = ET.fromstring(content)
            except ET.ParseError as e:
                self.fail(f"XML parse error in {svg_name}: {e}")

            # 2. Dimensions & ViewBox
            vb = root.get("viewBox")
            w = root.get("width")
            h = root.get("height")
            self.assertIsNotNone(vb, f"{svg_name} missing viewBox")
            self.assertIsNotNone(w, f"{svg_name} missing width")
            self.assertIsNotNone(h, f"{svg_name} missing height")

            vb_parts = vb.split()
            self.assertEqual(len(vb_parts), 4, f"Invalid viewBox in {svg_name}: {vb}")
            vb_w, vb_h = vb_parts[2], vb_parts[3]
            self.assertEqual(str(int(float(vb_w))), str(int(float(w))), f"Width mismatch in {svg_name}")
            self.assertEqual(str(int(float(vb_h))), str(int(float(h))), f"Height mismatch in {svg_name}")

    def test_svg_unique_ids(self):
        for svg_name in EXPECTED_SVGS:
            path = ASSETS_DIR / svg_name
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
            ids = re.findall(r'id=[\"\']([^\"\']+)[\"\']', content)
            dup_ids = [x for x in set(ids) if ids.count(x) > 1]
            self.assertEqual(dup_ids, [], f"Duplicate IDs in {svg_name}: {dup_ids}")

    def test_svg_url_references(self):
        for svg_name in EXPECTED_SVGS:
            path = ASSETS_DIR / svg_name
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
            ids = set(re.findall(r'id=[\"\']([^\"\']+)[\"\']', content))
            refs = re.findall(r'url\(#([^)]+)\)', content)
            missing = [r for r in refs if r not in ids]
            self.assertEqual(missing, [], f"Unresolved URL references in {svg_name}: {missing}")

    def test_reduced_motion_coverage(self):
        """All continuously animated SVGs must include prefers-reduced-motion media query."""
        for svg_name in EXPECTED_SVGS:
            path = ASSETS_DIR / svg_name
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
            has_anim = bool(
                re.search(r'<(animate|animateTransform|animateMotion)', content) or
                'animation:' in content or
                '@keyframes' in content
            )
            if has_anim:
                self.assertIn(
                    'prefers-reduced-motion',
                    content,
                    f"Animated SVG {svg_name} missing @media (prefers-reduced-motion: reduce) style block"
                )

if __name__ == "__main__":
    unittest.main()
