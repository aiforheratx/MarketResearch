# test/ — WAI-Test review agent

This directory holds the **QA / review agent** that checks every weekly report before it is emailed.

- **Spec:** [`../brain/test_agent.md`](../brain/test_agent.md) — the full catalogue of checks and the scoring rules.
- **Runner:** [`../scripts/test_agent.py`](../scripts/test_agent.py) — validates a report across three dimensions (**format**, **content**, **report data**) and writes a scorecard.
- **Results:** `results/<slug>.json`, `results/<slug>.md`, and `results/latest.json` (the live operations dashboard reads `latest.json`).

## Run it

```bash
python3 scripts/test_agent.py                                  # newest report
python3 scripts/test_agent.py reports/2026-06-29_healthcare-rnd.md
```

Exit code `0` = verdict **SHIP** (zero FAIL checks). Exit code `1` = verdict **HOLD** — the report does not email until the flagged checks are fixed.

The pipeline order is: Research Agent → Report Writer → **WAI-Test** → Scheduler/Email. See [`../docs/agent-dashboard.html`](../docs/agent-dashboard.html) for the live view.
