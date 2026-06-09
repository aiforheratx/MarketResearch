# Tracked metrics — time series

Append-only. Every weekly run that surfaces a value for a tracked metric appends a row. Never edit past rows; only append.

Format: one section per tracked metric. Within each section, one row per observation.

Row format: `| date_observed | value | year_of_value | source | report_file | notes |`

---

## % women in global AI workforce

| Observed | Value | Year of value | Source | Report | Notes |
|---|---|---|---|---|---|

## % women authoring NeurIPS papers (first author)

| Observed | Value | Year of value | Source | Report | Notes |
|---|---|---|---|---|---|

## % women in AI PhD programs (US, CRA Taulbee)

| Observed | Value | Year of value | Source | Report | Notes |
|---|---|---|---|---|---|

## % women in AI leadership (director+) at large AI employers

| Observed | Value | Year of value | Source | Report | Notes |
|---|---|---|---|---|---|

## Share of VC dollars to women-founded AI startups

| Observed | Value | Year of value | Source | Report | Notes |
|---|---|---|---|---|---|

## Pay gap, AI/ML roles (women's $ per men's $1)

| Observed | Value | Year of value | Source | Report | Notes |
|---|---|---|---|---|---|

## Conference keynote share (women, top-5 AI venues)

| Observed | Value | Year of value | Source | Report | Notes |
|---|---|---|---|---|---|

## % women in AI ethics / governance roles

| Observed | Value | Year of value | Source | Report | Notes |
|---|---|---|---|---|---|

## Gender citation gap, AI papers

| Observed | Value | Year of value | Source | Report | Notes |
|---|---|---|---|---|---|

## Black women's share of US AI workforce

| Observed | Value | Year of value | Source | Report | Notes |
|---|---|---|---|---|---|

---

## Adding a new tracked metric

When a weekly report introduces a number worth tracking over time:
1. Decide whether it belongs to an existing series or warrants a new one.
2. If new: add a section here with the standard 6-column header.
3. Add it to the headline table in `dashboard.md`.
4. Note the addition in the run's `history.md` entry.
