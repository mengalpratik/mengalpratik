# Repository Audit & Technical Review
**Target Repository:** `mengalpratik/mengalpratik`  
**Default Branch:** `main`  
**Initial Audited Commit SHA:** `fa6deeee3db502ea5730a54e0f07a67a27193f90`  
**Audit Date:** 2026-11-11  
**Auditor Roles:** Senior Software Engineer, Repository Auditor, SVG Engineer, Python Developer, Accessibility Specialist, QA Engineer

---

## 1. Executive Summary

This audit document presents an evidence-backed engineering analysis of the `mengalpratik/mengalpratik` repository. The repository powers the GitHub profile README for Pratik Mengal (@mengalpratik), presenting a "Hacker Green & Pitch Black" cyberpunk terminal visual identity, project showcases, verified credentials, and GitHub contribution telemetry.

The audit verified all tracked files, commit history, external links, live GitHub API telemetry, user resume evidence (`resume.pdf`), and published literature. While the visual design direction and presentation are strong, the repository suffered from severe architectural fragility, broken external repository links (HTTP 404s), hardcoded and inaccurate telemetry metrics, unverified credential badge phrasing, missing accessibility for reduced motion, invalid SMIL animation syntax, and an absence of automated regression testing or CI workflows.

---

## 2. File Inventory & Categorization

| Path | File Type | Responsibility / Role | Authority / Nature |
|---|---|---|---|
| `README.md` | Markdown | Primary GitHub profile rendered page | Presentation / Output |
| `preview.html` | HTML | Local browser preview mirroring profile layout | Presentation / Output |
| `avatar.png` | PNG (18.4 KB) | Source profile avatar photo | Authoritative Source (Binary) |
| `resume.pdf` | PDF (467 KB) | Owner's resume document (Gitignored) | Reference Evidence |
| `.gitignore` | Config (44 B) | Git ignore patterns | Configuration |
| `data/contributions.json` | JSON | 368-day daily contribution counts and levels | Data Snapshot |
| `scripts/build_snake_svg.py` | Python (264 lines) | Generates `contribution-snake.svg` | Generation Script |
| `scripts/generate_assets.py` | Python (1,159 lines) | Monolithic generator for all other 18 SVGs | Generation Script |
| `assets/hero-banner.svg` | SVG (1200x480) | Top banner with HUD radar, bio & avatar | Generated Asset |
| `assets/about-intro.svg` | SVG (1200x410) | Terminal intro panel & focus cards | Generated Asset |
| `assets/achievement-motif.svg`| SVG (1200x420) | Milestones, Google Cyber & research metrics | Generated Asset |
| `assets/project-neuromatrix.svg`| SVG (1200x270) | Project card 01 | Generated Asset |
| `assets/project-myraa.svg` | SVG (1200x270) | Project card 02 | Generated Asset |
| `assets/project-neurostore.svg`| SVG (1200x270) | Project card 03 | Generated Asset |
| `assets/project-axcentra.svg` | SVG (1200x270) | Project card 04 | Generated Asset |
| `assets/tech-constellation.svg`| SVG (1200x440) | 6-grid tech stack cards | Generated Asset |
| `assets/contribution-snake.svg`| SVG (1200x410) | Animated snake eating contribution cells | Generated Asset |
| `assets/github-telemetry.svg` | SVG (1200x240) | Offline telemetry & language distribution | Generated Asset |
| `assets/certifications.svg` | SVG (1200x490) | 8 credential cards & 5 badge chips | Generated Asset |
| `assets/footer-signature.svg` | SVG (1200x200) | Script signature & network metadata | Generated Asset |
| `assets/title-about.svg` | SVG (1200x90) | Section header 01 | Generated Asset |
| `assets/title-recognition.svg` | SVG (1200x90) | Section header 02 | Generated Asset |
| `assets/title-work.svg` | SVG (1200x90) | Section header 03 | Generated Asset |
| `assets/title-toolkit.svg` | SVG (1200x90) | Section header 04 | Generated Asset |
| `assets/title-commits.svg` | SVG (1200x90) | Section header 05 | Generated Asset |
| `assets/title-certifications.svg`| SVG (1200x90) | Section header 06 | Generated Asset |
| `assets/title-connect.svg` | SVG (1200x90) | Section header 07 | Generated Asset |

---

## 3. Architecture Overview & Relationships

### Current Flow:
1. `data/contributions.json` is read by `scripts/build_snake_svg.py` to produce `assets/contribution-snake.svg`.
2. `scripts/generate_assets.py` contains inline hardcoded profile data, project metrics, credential titles, and SVG templates. It reads `avatar.png` (encoded as base64) and writes 18 SVG files into `assets/`.
3. `README.md` references the 19 SVG files in `assets/` and 5 external shields.io badges.
4. `preview.html` independently duplicates the image links and layout of `README.md`.

### Architectural Flaws in Current Design:
- **No Single Source of Truth:** Data (e.g., college name, internships, research paper, tech skills) is copied across `generate_assets.py`, `README.md`, `preview.html`, and individual SVG strings.
- **Tight Coupling:** Content (data) is embedded directly inside procedural string templates in Python rather than in clean JSON models.
- **Overwriting Risk:** Modifying an SVG manually is completely destroyed upon running `generate_assets.py`.
- **Desynchronization:** `preview.html` and `README.md` drift apart whenever changes are made to either file.

---

## 4. Confirmed Defects & Root Causes

### Defect 1: Broken External Project URLs (HTTP 404)
- **Severity:** High
- **Files:** `README.md` (lines 24, 36), `scripts/generate_assets.py` (lines 566, 589), `preview.html` (lines 71, 79).
- **Description:** 
  - `https://github.com/mengalpratik/NeuroMatrix` returns HTTP 404 Not Found. The owner's actual public repository is `https://github.com/mengalpratik/NeuroMatrixLearningAcademy`.
  - `https://github.com/mengalpratik/NeuroStore-mern-Ecommerce` returns HTTP 404 Not Found. No public repository exists under this name on the user's account.
- **Root Cause:** Manual drafting of repository URLs without verifying against GitHub API or handling repository renames.

### Defect 2: Inaccurate & Fabricated Language Telemetry
- **Severity:** Medium-High
- **Files:** `assets/github-telemetry.svg`, `scripts/generate_assets.py` (lines 1065–1103).
- **Description:** `github-telemetry.svg` displays hardcoded language percentages: Java 28%, JavaScript 26%, Python 16%, TypeScript 15%, HTML/CSS 15%.
  - Actual telemetry queried from GitHub's REST API across all 24 public repositories reveals:
    - **TypeScript:** 721,623 bytes (**32.0%**)
    - **JavaScript:** 626,249 bytes (**27.7%**)
    - **Python:** 479,808 bytes (**21.3%**)
    - **CSS/HTML:** 311,191 bytes (**13.8%**)
    - **Java:** 107,233 bytes (**4.8%**)
- **Root Cause:** Arbitrary static percentages were hardcoded into the generator without computing them from the GitHub API.

### Defect 3: Undefined Telemetry Metric ("100% Active Codebases")
- **Severity:** Medium
- **Files:** `assets/github-telemetry.svg`, `README.md` (line 55).
- **Description:** Claims "100% ACTIVE CODEBASES" and "SYSTEM AVAILABILITY". This claim has no defined computational formula and is factually misleading.
- **Root Cause:** Buzzword-heavy copy inserted without metric backing.

### Defect 4: Misleading Credential & Badge Labels
- **Severity:** Medium-High
- **Files:** `assets/certifications.svg`, `scripts/generate_assets.py` (lines 837, 851, 865, 879).
- **Description:**
  - `COMPTIA SECURITY+ ALIGNED`: Course notes state Google Cybersecurity helps prepare for CompTIA Security+, but no official CompTIA credential is held.
  - `ENTERPRISE JAVA EXPERT`: Course title in resume is "Programming using Java".
  - `500+ PROBLEMS SOLVED`: Solved-problem count is an unverified descriptive assertion on a course badge.
  - `★ GOOGLE VERIFIED PRO`: Promotional endorsement not found on Coursera credentials.
- **Root Cause:** Exaggerated marketing labels applied over standard course and simulation completions.

### Defect 5: Missing Reduced-Motion Media Queries in Animated SVGs
- **Severity:** Medium (Accessibility violation / WCAG 2.1 2.3.3)
- **Files:** `assets/title-about.svg`, `assets/title-recognition.svg`, `assets/title-work.svg`, `assets/title-toolkit.svg`, `assets/title-commits.svg`, `assets/title-certifications.svg`, `assets/title-connect.svg`.
- **Description:** All 7 title banners contain infinite looping `<animateTransform>` sheens and `<animate>` laser dots, but contain zero `@media (prefers-reduced-motion: reduce)` style blocks.
- **Root Cause:** Omission of accessibility media queries in `titles` generation loop in `generate_assets.py`.

### Defect 6: Invalid SMIL Animation Syntax in `build_snake_svg.py`
- **Severity:** Medium
- **Files:** `scripts/build_snake_svg.py` (line 124, 156), `assets/contribution-snake.svg`.
- **Description:** 
  - `keyTimes="0;{eat_time}"` specifies only two keyTimes without terminating at `1`. The W3C SMIL recommendation requires keyTimes lists to start at 0 and end at 1.
  - `values="{color};{LEVELS[0]}"` lacks a trailing value corresponding to the remaining time of the loop.
- **Root Cause:** Incomplete SMIL keyframe specification in snake generation script.

### Defect 7: SMIL Loop Ignores `prefers-reduced-motion` in Snake & Hero SVGs
- **Severity:** Medium
- **Files:** `scripts/build_snake_svg.py`, `assets/hero-banner.svg`.
- **Description:** In `build_snake_svg.py`, while `.hm-motion` has `display: none` under reduced motion, the individual cells have SMIL `<animate>` elements that continue flashing because CSS `animation: none` only applies to CSS animations, not SVG SMIL elements.
- **Root Cause:** Failure to decouple static and animated SVG states or hide SMIL animated rects when reduced motion is requested.

### Defect 8: Lack of Input Validation in `build_snake_svg.py`
- **Severity:** Medium
- **Files:** `scripts/build_snake_svg.py`.
- **Description:** The script directly accesses `data["contributions"]` without verifying:
  - JSON schema & required fields (`date`, `count`, `level`)
  - Date uniqueness and 1-day step continuity
  - Non-negative counts and level bounds (0-4)
  - Calculated sum vs declared total
- **Root Cause:** Script was written as a quick utility script rather than a resilient data pipeline tool.

### Defect 9: Absence of Automated Testing and CI
- **Severity:** Medium
- **Files:** Repository root.
- **Description:** No unit tests, no XML validation checks, no broken reference checkers, and no GitHub Actions workflow exist.
- **Root Cause:** Engineering infrastructure was never initialized for the repository.

---

## 5. Risk Classification Matrix

| Finding | Severity | Likelihood | Impact | Classification |
|---|---|---|---|---|
| Broken Project URLs (404s) | High | 100% (Happening) | Public visitors face broken links | Critical |
| Misleading Credential Titles | Med-High | 100% | Credibility & professional integrity risk | High |
| Inaccurate Telemetry Percentages | Med-High | 100% | Factually incorrect claims on profile | High |
| Missing Reduced-Motion Accessibility | Medium | 100% | Vestibular disorder accessibility failure | Medium |
| Invalid SMIL keyTimes Syntax | Medium | High | Potential rendering failure in strict SVG engines | Medium |
| Unvalidated Contribution Ingestion | Medium | Medium | Generator crash on malformed JSON | Medium |
| Monolithic Generator Architecture | Low-Med | High | Fragile maintenance, hardcoded duplication | Medium |
| Missing CI & Automated Tests | Low-Med | High | Regressions escape unnoticed | Medium |

---

## 6. Recommended Architecture & Fix Strategy

### 6.1 Centralized Data Architecture
Extract all content into JSON models located in `data/`:
1. `data/profile.json`: Canonical owner profile, education, research, bio, and social links.
2. `data/projects.json`: Verified project records, GitHub URLs, accurate descriptions, and technology chips.
3. `data/certifications.json`: Verifiable certifications with exact titles, issuers, and clean badge chips.
4. `data/telemetry.json`: Computed language statistics, repository metrics, and dated snapshot metadata.

### 6.2 Modular Generator Architecture
Refactor `scripts/generate_assets.py` into a package:
```
scripts/
├── generators/
│   ├── __init__.py
│   ├── common.py           # Shared XML escaping, palette constants, styles, helpers
│   ├── hero.py             # Hero banner with avatar & HUD
│   ├── about.py            # Terminal intro & focus cards
│   ├── recognition.py      # Dual milestone panels & metric strip
│   ├── projects.py         # Compact project cards
│   ├── toolkit.py          # 6-grid tech stack constellation
│   ├── certifications.py   # Verified credentials & badges
│   ├── telemetry.py        # Calculated language distribution & stats
│   ├── titles.py           # Accessible section banners
│   └── footer.py           # Signature & connection metadata
├── generate_assets.py      # Centralized CLI entrypoint
├── build_snake_svg.py      # Hardened snake generator with schema validation
├── fetch_contributions.py  # Contribution retriever with offline fallback
└── validate_repository.py  # Comprehensive validator
```

### 6.3 Accessibility & SVG Standards
1. Add `@media (prefers-reduced-motion: reduce)` to all `title-*.svg` files.
2. Fix SMIL keyframe syntax to conform to W3C specification (`keyTimes="0;{eat_time};1"`).
3. Ensure all SVGs pass strict XML ElementTree parsing, ID uniqueness checks, and URL reference audits.

### 6.4 Quality Assurance & CI Workflow
1. Create unit tests under `tests/` utilizing standard library `unittest` (zero external dependencies).
2. Create `.github/workflows/ci.yml` verifying validation and generator determinism on GitHub Actions.
3. Synchronize `preview.html` and `README.md` to prevent content divergence.
