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

> Run the WAI-Research weekly workflow. Follow `brain/instructions.md` exactly. Produce this week's report under `reports/`, update `brain/history.md`, `brain/sources.md` (if new), and `dashboard/dashboard.md` and `dashboard/metrics.md`.

## Manual override

To run off-schedule, open a Claude Code session in this directory and say:

> Run the WAI-Research weekly workflow now.

The agent will detect that it is being run manually, log it as `manual run` in `history.md`, and otherwise behave identically to a scheduled run.

## Schedule registration

The cron routine is registered via the Claude Code `schedule` skill. The routine identifier and registration details are recorded by the skill at registration time.

To list, edit, or remove the schedule, use the `schedule` skill commands. Do not edit the cron expression here without re-registering.
