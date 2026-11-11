"""
tests/test_asset_references.py

Validates that all local asset references in README.md and preview.html exist on disk
and that no deprecated or broken 404 repository links are present.
"""

import re
import unittest
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

class TestAssetReferences(unittest.TestCase):
    def test_readme_local_assets_exist(self):
        readme_path = ROOT_DIR / "README.md"
        self.assertTrue(readme_path.exists())
        with open(readme_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Find all src="assets/..." references
        matches = re.findall(r'src="([^"]+)"', content)
        local_assets = [m for m in matches if not m.startswith("http")]
        self.assertGreater(len(local_assets), 10, "README should reference multiple local assets")

        for asset in local_assets:
            p = ROOT_DIR / asset
            self.assertTrue(p.exists(), f"README referenced non-existent asset: {asset}")

    def test_preview_local_assets_exist(self):
        preview_path = ROOT_DIR / "preview.html"
        self.assertTrue(preview_path.exists())
        with open(preview_path, "r", encoding="utf-8") as f:
            content = f.read()

        matches = re.findall(r'src="([^"]+)"', content)
        local_assets = [m for m in matches if not m.startswith("http")]
        self.assertGreater(len(local_assets), 10, "preview.html should reference multiple local assets")

        for asset in local_assets:
            p = ROOT_DIR / asset
            self.assertTrue(p.exists(), f"preview.html referenced non-existent asset: {asset}")

    def test_no_broken_404_repo_links(self):
        for doc_name in ["README.md", "preview.html"]:
            path = ROOT_DIR / doc_name
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
            # 404 links must not be present
            self.assertNotIn("https://github.com/mengalpratik/NeuroMatrix\"", content, f"Deprecated 404 link found in {doc_name}")
            self.assertNotIn("NeuroStore-mern-Ecommerce", content, f"404 NeuroStore link found in {doc_name}")
            # Verified links must be present
            self.assertIn("NeuroMatrixLearningAcademy", content, f"Missing NeuroMatrixLearningAcademy in {doc_name}")
            self.assertIn("myraa-ai-assistant", content, f"Missing myraa-ai-assistant in {doc_name}")
            self.assertIn("Axcentra-Internship-Work-2026", content, f"Missing Axcentra-Internship-Work-2026 in {doc_name}")

if __name__ == "__main__":
    unittest.main()
