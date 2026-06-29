# Schedule configuration

## Cadence

Every **Monday at 09:00** America/Chicago.

- America/Chicago observes CST (UTC−6) in winter and CDT (UTC−5) in summer.
- Using the **America/Chicago** timezone (not a fixed UTC offset) means the wake time stays at 09:00 local through daylight-saving transitions.

## Cron expression

```
0 9 * * 1
```

With timezone: `America/Chicago`.

In UTC equivalents (for reference only — do not register with these; register against America/Chicago):
- Standard time (Nov–Mar): `0 15 * * 1` UTC
- Daylight time (Mar–Nov): `0 14 * * 1` UTC

## What the scheduled routine does

On each fire, the routine launches a Claude Code session in this working directory with the instruction:

> Run the WAI-Research weekly workflow. Follow `brain/instructions.md` exactly. Produce this week's report under `reports/`, run the WAI-Test review (`scripts/test_agent.py`), update `brain/history.md`, `brain/sources.md` (if new), the dashboards, and — once the report clears WAI-Test (verdict SHIP) — email it to the distribution list.

## Email distribution (after the report clears WAI-Test)

Every Monday at 09:00 America/Chicago, after the report passes the test agent, `scripts/send_report.py` emails the latest report (`.docx` + presentation `.html`) to:

| Recipient | Email |
|---|---|
| Mugdha Tasgaonkar | `mugdha.v.tasgaonkar@medtronic.com` |
| Sue Delfidio | `sue.delfidio@medtronic.com` |
| Tyler Stigen | `tyler.w.stigen@medtronic.com` |

The send step requires `GMAIL_USER` and `GMAIL_APP_PASSWORD` in the environment (or `scripts/email_credentials.env`). Recipients can be overridden for a single run with `EMAIL_TO="a@x.com,b@y.com"`. Verify without sending using:

```bash
python3 scripts/send_report.py --dry-run
```

## Manual override

To run off-schedule, open a Claude Code session in this directory and say:

> Run the WAI-Research weekly workflow now.

The agent will detect that it is being run manually, log it as `manual run` in `history.md`, and otherwise behave identically to a scheduled run.

## Schedule registration — REGISTERED

A **cloud routine** is registered (Claude Code `schedule` skill / routines):

| Field | Value |
|---|---|
| Name | WAI-Research weekly report |
| Routine ID | `trig_01EzKTGxN4bMctLR9CM33ShB` |
| Cron (UTC) | `0 14 * * 1` |
| Local time | Mondays 09:00 **CDT** (summer) |
| First run | 2026-07-06 09:00 CDT |
| Repo | github.com/aiforheratx/MarketResearch |
| Email | via **Gmail connector**, first-run scope = mugdha.v.tasgaonkar@medtronic.com only |
| Manage | https://claude.ai/code/routines/trig_01EzKTGxN4bMctLR9CM33ShB |

### Things to know about the cloud routine
- **It runs in Anthropic's cloud against the GitHub repo**, not this local machine. For it to use the new pipeline (test agent, healthcare track, updated dashboards), the local changes must be **committed and pushed** to `aiforheratx/MarketResearch`.
- **Email in the cloud uses the Gmail connector** (from your connected Gmail), because the local SMTP credentials in `scripts/email_credentials.env` are not available in the cloud. The local `scripts/send_report.py` path (SMTP from `info@aiforheratx.org`) still works when run **locally** and is what sent the first Week-8 report.
- **DST:** `0 14 * * 1` UTC = 09:00 CDT in summer. After the November switch to CST it lands at 08:00 local — update the cron to `0 15 * * 1` then (or accept the one-hour shift).
- To restore the full 3-recipient list (add Sue and Tyler), remove the `EMAIL_TO` lines from `scripts/email_credentials.env` (local) and update the routine prompt's first-run scope.

To list/edit/run the routine, use the `schedule` skill. Do not edit the cron expression here without re-registering.
