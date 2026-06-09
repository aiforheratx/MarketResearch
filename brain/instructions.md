# Instructions — Weekly Run Workflow

Follow these steps in order. Do not skip steps. If a step fails, log the failure in `brain/history.md` and continue.

---

## Step 0 — Load context

Read, in this order:
1. `brain/identity.md`
2. `brain/goals.md`
3. `brain/methodology.md`
4. `brain/topic_rotation.md`
5. `brain/sources.md`
6. `brain/history.md` (last 8 entries minimum)

## Step 1 — Select this week's topic

- Compute the ISO week number for today's date.
- Look up the topic in `brain/topic_rotation.md` for that week.
- If the topic was covered within the last 8 weeks (check `history.md`), pick the next unused topic from the rotation.
- Write the chosen topic and slug down before continuing.

## Step 2 — Research plan (write before searching)

Draft, in scratch, a one-paragraph plan that answers:
- What question is this week's topic answering?
- Which 3–5 primary sources are likely to have the strongest data on it?
- What time-series numbers should I look up for the dashboard (so we can track movement)?

## Step 3 — Gather evidence

Use WebSearch and WebFetch (and Apify Actors for scraping when needed). Prioritize sources in this order:
1. **Primary statistical reports** — government datasets (BLS, NSF, Eurostat), institutional reports (Stanford HAI AI Index, World Economic Forum Global Gender Gap, UNESCO, McKinsey, OECD).
2. **Peer-reviewed academic papers** — preferably indexed (Nature, Science, PNAS, arXiv with venue acceptance, JMLR, NeurIPS/ICML/ICLR proceedings).
3. **Named industry research** — LinkedIn Economic Graph, Glassdoor Economic Research, GitHub Octoverse, HolonIQ, PitchBook (for funding), Crunchbase News research arm.
4. **Advocacy organizations with audited methodology** — AnitaB.org, Catalyst, LeanIn, AI Now Institute, Women in AI, AI4ALL, WiML, Black in AI.
5. **Investigative journalism** — only for narrative; the underlying number must trace to one of categories 1–4.

For each candidate source, record:
- Publisher name
- Title and year
- URL
- The specific statistic(s) or finding(s) you'll cite
- Methodology note (sample size, geography, definition of "women in AI")

If a source is paywalled, capture the abstract and any quoted figures from secondary coverage, and flag the limitation.

## Step 4 — Cross-check disagreements

For any headline statistic, find a second source. If they conflict by more than a few points, surface both in the report.

## Step 5 — Write the report

Use `reports/_template.md`. Filename: `reports/YYYY-MM-DD_<topic-slug>.md`.

The report must contain:
- A 3-sentence executive summary stating the single most important finding.
- A "Numbers in this report" box near the top: 5–10 headline statistics with sources.
- Body sections covering: state of the data, what it means, what's missing, what works.
- A "Sources" section at the end with full citations (publisher, title, year, link, methodology note).
- A "Recommended actions" section: 3–5 concrete moves the reader can make (read this paper, share this dataset, attend this event, advocate for this policy, ask this question in their org).

Word count: 1,500–3,500.

## Step 6 — Update the brain

- Append a new entry to `brain/history.md` using the format in that file.
- Add any new primary sources to `brain/sources.md` (deduplicate against existing entries).

## Step 7 — Update the dashboard

- Refresh `dashboard/dashboard.md` with: topics covered to date, most-cited sources, headline statistics tracked over time.
- Append this week's tracked time-series numbers to `dashboard/metrics.md`.

## Step 8 — Self-check before declaring done

Confirm all of:
- [ ] Every statistic in the report has a citation.
- [ ] At least one statistic is dated within the last 12 months.
- [ ] At least one new source was added to `brain/sources.md`, OR a justification is logged in `history.md` for why no new source was needed.
- [ ] The report filename matches `YYYY-MM-DD_<slug>.md` exactly.
- [ ] `history.md` entry written.
- [ ] `dashboard.md` shows this week's report in its "Recent reports" list.

If any check fails, fix it before exiting.
