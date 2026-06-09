# Women in AI — Weekly Market Research Agent

A scheduled research agent that produces a deep-research report every **Monday at 09:00 CST** on a rotating topic related to women in artificial intelligence: representation, leadership, career paths, struggles, gaps, statistics, and action recommendations.

## What this agent delivers (every Monday)

1. **One focused report** on the week's rotating topic (see `brain/topic_rotation.md`).
2. **Statistics with citations** — every percentage and number traces back to a named published source (report, paper, dataset, or institution).
3. **Source list** — white papers, statistical reports, academic publications, industry studies.
4. **Analysis** — what the data means, what's changing, what's stuck.
5. **Action recommendations** — concrete next steps the reader can take based on the findings.
6. **Dashboard update** — running metrics, topics covered, key numbers logged over time.

## Directory layout

```
MarketResearch/
├── README.md                  ← This file
├── AGENT.md                   ← Agent persona, mission, output contract
├── brain/                     ← Persistent state (identity, goals, instructions, history)
│   ├── identity.md
│   ├── goals.md
│   ├── instructions.md        ← Step-by-step research workflow
│   ├── methodology.md         ← Research framework and quality bar
│   ├── topic_rotation.md      ← 52-week topic schedule
│   ├── sources.md             ← Trusted publishers and primary sources
│   └── history.md             ← Run log appended after each weekly run
├── reports/                   ← One markdown report per Monday
│   ├── _template.md
│   └── YYYY-MM-DD_topic.md
├── dashboard/                 ← Cross-report tracking
│   ├── dashboard.md           ← Main running dashboard
│   └── metrics.md             ← Time-series of tracked numbers
├── schedule/
│   └── cron_config.md         ← Schedule details and timezone notes
└── sources_archive/           ← Cached copies of referenced reports (PDFs, snapshots)
```

## How to run manually (off-schedule)

Open a Claude Code session in this directory and say:
> Run the Women in AI research agent for this week.

The agent will read `brain/`, pick the current week's topic from `topic_rotation.md`, produce a report into `reports/`, and update `dashboard/dashboard.md` and `brain/history.md`.

## How the schedule works

A cron routine is registered to wake the agent every Monday at 09:00 America/Chicago. See `schedule/cron_config.md`.
