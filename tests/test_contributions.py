"""
tests/test_contributions.py

Validates schema, date continuity, level bounds, and count integrity of contributions.json.
"""

import json
import unittest
from datetime import datetime
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT_DIR / "data"

class TestContributions(unittest.TestCase):
    def setUp(self):
        c_path = DATA_DIR / "contributions.json"
        self.assertTrue(c_path.exists(), "data/contributions.json must exist")
        with open(c_path, "r", encoding="utf-8") as f:
            self.data = json.load(f)

    def test_structure(self):
        self.assertIn("total", self.data)
        self.assertIn("contributions", self.data)
        self.assertIsInstance(self.data["contributions"], list)
        self.assertGreater(len(self.data["contributions"]), 300)

    def test_date_continuity_and_uniqueness(self):
        days = self.data["contributions"]
        seen_dates = set()
        prev_date = None

        for idx, entry in enumerate(days):
            d_str = entry["date"]
            # Validate ISO format
            curr_date = datetime.strptime(d_str, "%Y-%m-%d").date()

            # Uniqueness
            self.assertNotIn(d_str, seen_dates, f"Duplicate date found: {d_str}")
            seen_dates.add(d_str)

            # 1-day step continuity
            if prev_date is not None:
                delta = (curr_date - prev_date).days
                self.assertEqual(delta, 1, f"Gap in dates between {prev_date} and {curr_date} (index {idx})")
            prev_date = curr_date

    def test_counts_and_levels(self):
        days = self.data["contributions"]
        calc_total = 0
        for idx, entry in enumerate(days):
            count = entry["count"]
            level = entry["level"]

            self.assertIsInstance(count, int)
            self.assertGreaterEqual(count, 0, f"Negative count at {entry['date']}")
            self.assertIsInstance(level, int)
            self.assertTrue(0 <= level <= 4, f"Level {level} out of range [0, 4] at {entry['date']}")

            if count == 0:
                self.assertEqual(level, 0, f"Zero count should have level 0 at {entry['date']}")
            else:
                self.assertGreater(level, 0, f"Non-zero count {count} should have level > 0 at {entry['date']}")

            calc_total += count

        declared_total = self.data.get("total", {}).get("lastYear")
        if declared_total is not None:
            self.assertEqual(calc_total, declared_total, f"Declared total ({declared_total}) != calculated ({calc_total})")

if __name__ == "__main__":
    unittest.main()
