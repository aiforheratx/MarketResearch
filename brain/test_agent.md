# TEST AGENT — WAI-Research QA Reviewer

## Name
**WAI-Test** (the report review / quality-assurance agent)

## Role
WAI-Test is the second agent in the pipeline. After WAI-Research writes a weekly report, WAI-Test independently reviews it **before it is emailed** and produces a pass/fail scorecard. Nothing ships to the Medtronic recipients until WAI-Test returns a clean run (zero `FAIL` checks).

It reviews every report across **three dimensions**:

1. **Format** — does the report obey the structural contract?
2. **Content** — is the writing complete, the right length, and properly structured?
3. **Report data** — is every statistic sourced, dated, and free of placeholders?

## How to run it

```bash
python3 scripts/test_agent.py                       # reviews the most recent report
python3 scripts/test_agent.py reports/2026-06-29_healthcare-rnd.md
```

It writes three artifacts:
- `test/results/<slug>.json` — machine-readable scorecard (consumed by the dashboard)
- `test/results/<slug>.md` — human-readable review
- `test/results/latest.json` — pointer to the most recent review (the dashboard reads this)

## The checks

### Dimension 1 — Format (the structural contract)

| ID | Check | Severity if it fails |
|---|---|---|
| F1 | Markdown filename matches `reports/YYYY-MM-DD_<slug>.md` | FAIL |
| F2 | YAML frontmatter present with all keys: date, week, topic, slug, career_phase, geography, status | FAIL |
| F3 | All required sections present (Executive summary; Numbers in this report; What's the number/trend/missing/works; Recommended actions; Sources; Methodology notes) | FAIL |
| F4 | A white paper exists at `whitepapers/<same-slug>.html` | FAIL |
| F5 | White paper `<head>` links `_assets/style.css`, sets `<title>`, has a viewport meta | WARN |
| F6 | White paper contains at least one inline `<svg>` chart | WARN |

### Dimension 2 — Content (completeness & shape)

| ID | Check | Severity if it fails |
|---|---|---|
| C1 | Body word count is between 1,500 and 3,500 | WARN |
| C2 | Executive summary is present and is 2–4 sentences | WARN |
| C3 | "Numbers in this report" table has ≥ 5 statistic rows | FAIL |
| C4 | "Recommended actions" lists 3–5 concrete moves | WARN |
| C5 | "Sources" section lists ≥ 5 citations | FAIL |
| C6 | At least one statistic is dated within the last 12 months | WARN |

### Dimension 3 — Report data (statistical integrity)

| ID | Check | Severity if it fails |
|---|---|---|
| D1 | Every row in the Numbers table has a non-empty Source cell | FAIL |
| D2 | Every Numbers-table row carries a 4-digit year | WARN |
| D3 | The Sources section contains at least one resolvable URL (`http…`) | FAIL |
| D4 | Any statistic older than 3 years is flagged `[dated]` | WARN |
| D5 | No template placeholders remain (`YYYY`, `<topic>`, `TODO`, `lorem`, empty table cells) | FAIL |
| D6 | Source tiers are declared (`Tier 1/2/3` or `[primary]/[secondary]` tags present) | WARN |

## Scoring

- Each dimension scores `passed / total` checks; a `WARN` counts as a half-pass.
- Overall **verdict**:
  - `SHIP` — zero FAIL checks (warnings allowed).
  - `HOLD` — one or more FAIL checks. The report does **not** email until fixed.
- The dashboard renders the three dimension scores, the verdict, and the per-check list.

## Operating principle
WAI-Test never edits the report. It only judges and reports. When it returns `HOLD`, WAI-Research fixes the flagged items and re-runs the review until it returns `SHIP`.
