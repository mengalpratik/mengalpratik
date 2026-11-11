#!/usr/bin/env python3
"""
scripts/validate_repository.py

Unified repository health and validation runner for mengalpratik/mengalpratik.
Performs:
1. Centralized JSON data schema and integrity validation
2. Contribution calendar date continuity and count checks
3. Strict SVG XML syntax, viewBox consistency, ID uniqueness, and URL reference audits
4. Accessibility verification for prefers-reduced-motion coverage
5. Markdown and HTML document link and asset reference verification
6. Generator deterministic reproduction verification
7. Automated test suite execution
"""

import sys
import unittest
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

def run_validation() -> bool:
    print("=================================================================")
    print("  REPOSITORY INTEGRITY & COMPLIANCE AUDIT VALIDATOR              ")
    print("  Repository: mengalpratik/mengalpratik                          ")
    print("=================================================================")
    
    loader = unittest.TestLoader()
    suite = loader.discover(str(ROOT_DIR / "tests"))
    runner = unittest.TextTestRunner(verbosity=2)
    
    print("\n[STEP 1/1] Running comprehensive automated test suite...")
    result = runner.run(suite)
    
    print("\n-----------------------------------------------------------------")
    if result.wasSuccessful():
        print(f"✓ ALL AUDIT CHECKS PASSED: {result.testsRun} checks executed with 0 failures.")
        print("-----------------------------------------------------------------")
        return True
    else:
        print(f"✗ AUDIT FAILED: {len(result.failures)} failures, {len(result.errors)} errors.")
        print("-----------------------------------------------------------------")
        return False

def main():
    success = run_validation()
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
