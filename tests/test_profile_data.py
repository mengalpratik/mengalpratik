"""
tests/test_profile_data.py

Validates schema, required fields, and integrity of centralized JSON data files.
"""

import json
import unittest
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT_DIR / "data"

class TestProfileData(unittest.TestCase):
    def test_profile_json_schema(self):
        p_path = DATA_DIR / "profile.json"
        self.assertTrue(p_path.exists(), "data/profile.json must exist")
        with open(p_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            
        required_keys = ["name", "handle", "title", "location", "email", "education", "research", "experience", "links", "focus_cards"]
        for k in required_keys:
            self.assertIn(k, data, f"profile.json missing key: {k}")
            
        self.assertEqual(data["name"], "Pratik Mengal")
        self.assertEqual(data["handle"], "mengalpratik")
        self.assertTrue(data["links"]["github"].startswith("https://github.com/"))
        self.assertEqual(len(data["focus_cards"]), 3)

    def test_projects_json_schema(self):
        p_path = DATA_DIR / "projects.json"
        self.assertTrue(p_path.exists(), "data/projects.json must exist")
        with open(p_path, "r", encoding="utf-8") as f:
            projects = json.load(f)
            
        self.assertIsInstance(projects, list)
        self.assertEqual(len(projects), 4, "Should have exactly 4 featured projects")
        
        filenames = set()
        for p in projects:
            for field in ("filename", "num", "category", "title", "repo_url", "desc", "built", "metrics", "chips"):
                self.assertIn(field, p, f"Project missing field: {field}")
            self.assertTrue(p["repo_url"].startswith("https://github.com/mengalpratik/"), f"Invalid repo url: {p['repo_url']}")
            # Ensure no 404 broken links are used
            self.assertNotIn("NeuroStore-mern-Ecommerce", p["repo_url"])
            self.assertNotEqual(p["repo_url"], "https://github.com/mengalpratik/NeuroMatrix")
            filenames.add(p["filename"])
            
        self.assertEqual(len(filenames), 4, "Project filenames must be unique")

    def test_certifications_json_schema(self):
        c_path = DATA_DIR / "certifications.json"
        self.assertTrue(c_path.exists(), "data/certifications.json must exist")
        with open(c_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            
        self.assertIn("credentials", data)
        self.assertIn("accolades", data)
        self.assertEqual(len(data["credentials"]), 8, "Must contain exactly 8 credentials")
        self.assertEqual(len(data["accolades"]), 5, "Must contain exactly 5 accolade chips")
        
        # Verify no unsupported claims
        for c in data["credentials"]:
            for misleading in ["COMPTIA SECURITY+ ALIGNED", "ENTERPRISE JAVA EXPERT", "500+ PROBLEMS SOLVED", "GOOGLE VERIFIED PRO"]:
                self.assertNotEqual(c["badge"], misleading, f"Misleading badge found: {c['badge']}")

    def test_telemetry_json_schema(self):
        t_path = DATA_DIR / "telemetry.json"
        self.assertTrue(t_path.exists(), "data/telemetry.json must exist")
        with open(t_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            
        self.assertEqual(data["public_repos"], 24)
        self.assertEqual(data["contributions_year"], 53)
        self.assertEqual(data["peak_daily_velocity"], 13)
        self.assertEqual(len(data["languages"]), 5)
        
        # Verify sum of percentages equals 100
        total_pct = sum(l["pct"] for l in data["languages"])
        self.assertEqual(total_pct, 100, "Language percentages must sum to 100%")

if __name__ == "__main__":
    unittest.main()
