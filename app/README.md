# WAI-Research — Agent Operations Dashboard (app)

A **Streamlit application** (not a static HTML file) that renders the agent's operations
dashboard from the repository's **live data**: the WAI-Test scorecard
(`test/results/latest.json`), the report files in `reports/`, and the weekly schedule.
Electric-blue Medtronic theme, interactive Plotly charts.

## Run it on your Mac

From this `app/` folder:

```bash
./run.sh
```

That installs dependencies on first run, starts the app, and opens it in your browser at
**http://localhost:8501**.

Or run it directly:

```bash
cd app
python3 -m streamlit run dashboard.py
```

(If `streamlit` isn't on your PATH, `python3 -m streamlit ...` always works.)

## What it shows
- **Pipeline** — Research → Write → WAI-Test → Schedule/Email, with live last-run stats.
- **WAI-Test review** — three interactive gauges (format / content / data) and all 18 checks, read live from `test/results/latest.json`.
- **Latest finding** — women's share by layer of health-AI R&D (interactive bar).
- **Scheduler** — Monday 09:00 CST cadence and the Medtronic distribution list.
- **Topics** — the featured Healthcare R&D track, the standard rotation, and completed weeks.

## How it stays current
The app reads the repo each time it loads. After a weekly run regenerates
`test/results/latest.json` and adds a report, refresh the browser tab (or it auto-reloads
with `runOnSave`) and the numbers update — no edits to the app needed.

## Files
- `dashboard.py` — the Streamlit app
- `.streamlit/config.toml` — electric-blue Medtronic theme
- `requirements.txt` — streamlit, plotly, pandas
- `run.sh` — one-command launcher (installs deps, starts, opens browser)
