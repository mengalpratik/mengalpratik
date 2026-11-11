"""
tests/test_generators.py

Validates that running asset generators is deterministic and produces consistent SVG outputs.
"""

import sys
import unittest
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
SCRIPTS_DIR = ROOT_DIR / "scripts"
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

from generate_assets import generate_all_assets
from build_snake_svg import build_snake_svg

class TestGenerators(unittest.TestCase):
    def test_generators_execution_and_determinism(self):
        # 1. Run generation
        success_assets = generate_all_assets()
        self.assertTrue(success_assets, "generate_all_assets() should return True")

        success_snake = build_snake_svg()
        self.assertTrue(success_snake, "build_snake_svg() should return True")

        # Snapshot current content of all SVGs
        assets_dir = ROOT_DIR / "assets"
        snapshots = {}
        for svg_file in assets_dir.glob("*.svg"):
            with open(svg_file, "r", encoding="utf-8") as f:
                snapshots[svg_file.name] = f.read()

        # 2. Re-run generation
        self.assertTrue(generate_all_assets())
        self.assertTrue(build_snake_svg())

        # 3. Assert byte-identical determinism
        for svg_file in assets_dir.glob("*.svg"):
            with open(svg_file, "r", encoding="utf-8") as f:
                second_run = f.read()
            self.assertEqual(
                snapshots[svg_file.name],
                second_run,
                f"Generator output for {svg_file.name} is non-deterministic between consecutive runs!"
            )

if __name__ == "__main__":
    unittest.main()
