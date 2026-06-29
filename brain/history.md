# Run history

Append a new entry at the **top** of this file after every weekly run. Use the format below verbatim. Do not modify past entries except to add a corrigendum block beneath them.

---

## Entry format

```
### YYYY-MM-DD — Week NN — <topic title>

- Report: reports/YYYY-MM-DD_<slug>.md
- Topic source: rotation row NN  (or: "override — <reason>")
- Top 3 statistics found:
  1. <stat with source>
  2. <stat with source>
  3. <stat with source>
- Sources cited: <count> (Tier 1: <n>, Tier 2: <n>, Tier 3: <n>)
- New sources added to sources.md: <list or "none">
- Tracked metrics updated in dashboard/metrics.md: <list>
- Notable gaps in evidence this week: <one line>
- Run health: OK | partial | failed — <one line if not OK>
```

---

## Entries (newest first)

### 2026-06-29 — Week 8 — Women & AI in healthcare R&D: the state of representation

- Report: reports/2026-06-29_healthcare-rnd.md (+ whitepaper, + .docx)
- Topic source: **override — featured Healthcare R&D track (H1)**. Skipped standard rotation rows 7–8; this is the reader's home sector (Medtronic medtech R&D) and the new standing priority track. Week 7 not filed (single-report-per-Monday cadence resumed on the featured track).
- Top 3 statistics found:
  1. 12% of AI researchers and 16% of AI faculty are women; AI research-position gender gap (38%) ~2× the general-science R&D gap (UNESCO, Women for Ethical AI, 2024)
  2. Female authorship of medical-AI papers stays <40% — 22.3% first authors in AI radiology (CARJ 2023), 35.7% in AI breast-imaging (Eur J Radiology 2024)
  3. Medical AI underdiagnoses women (chest-X-ray classifiers; Nature Medicine 2021), trained on trials only 34–38% female (JACC 2018; Circulation 2020)
- Sources cited: 17 (Tier 1: 9, Tier 2: 4, Tier 3: 4)
- New sources added to sources.md: UNESCO Women for Ethical AI; ILO generative-AI exposure 2025; Yan et al. CARJ female authorship; Eur J Radiology AI breast-imaging authorship; Seyyed-Kalantari Nature Medicine underdiagnosis; JACC women in CV drug-approval trials; Circulation women in CV trials; Rock Health Women in Focus; PitchBook All In Female Founders; Pharma's Almanac biopharma leadership; Medical Design & Outsourcing medtech diversity; NSF NCSES 23-328 women in business R&D; Female Global Scholars Program eval; CRA-W Grad Cohort eval
- New artifacts this run: brain/test_agent.md (WAI-Test spec); scripts/test_agent.py (runnable QA reviewer); docs/agent-dashboard.html (operations dashboard); featured Healthcare R&D track added to topic_rotation.md
- WAI-Test review: **SHIP — 100%** (format 6/6, content 6/6, data 6/6); test/results/healthcare-rnd.json
- Email distribution updated: now mugdha.v.tasgaonkar@medtronic.com, sue.delfidio@medtronic.com, tyler.w.stigen@medtronic.com (Mon 09:00 CST, after WAI-Test passes)
- Tracked metrics updated in dashboard/metrics.md: women in AI research/faculty; medical-AI female authorship; CV-trial female participation; biopharma/medtech leadership; health-AI founder funding
- Notable gaps in evidence this week: no audited statistic for women's share of the health-AI workforce specifically; no gender data for AI drug discovery; founder gender within health-AI funding unmeasured; no medtech-specific AI/R&D engineering gender data; no intervention study measuring representation gains in health-AI/medtech
- Run health: OK

### 2026-06-15 — Week 6 — The broken rung: promotion from IC to first management

- Report: reports/2026-06-15_broken-rung.md
- Topic source: rotation row 6 (sequential continuation of the weeks 1–5 backfill cadence)
- Top 3 statistics found:
  1. 52 women promoted to manager per 100 men in **technical roles** vs. 86 across all roles (McKinsey/LeanIn *Women in the Workplace 2021* — most recent technical-specific cut; [dated])
  2. All-industry rung rose to **93 per 100 men in 2025** (from 81 in 2024) — but **women of color stayed at 74 and Black women at 60, unchanged** (McKinsey/LeanIn *WitW 2025*)
  3. Representation pyramid: women 48% entry → 39% manager → 29% C-suite (all-industry, 2025); STEM steeper at 29% → 24.4% → 12.2% (2024)
- Sources cited: 10 (Tier 1: 5, Tier 2: 3, Tier 3: 2)
- New sources added to sources.md: McKinsey/LeanIn *Repairing the broken rung on the career ladder for women in technical roles* (2021 technical cut); McKinsey *Diversity Matters Even More* (2023); WEF *How AI is worsening workplace gender gaps* (2025); Women in Tech Network *Women in Tech Stats 2025/2026* (STEM pipeline); HR Brew WitW 2025 coverage
- Tracked metrics updated in dashboard/metrics.md: broken rung (all-industry, promotions-to-manager metric); broken rung by race (2025); broken rung technical roles (2021); representation pyramid by level
- Notable gaps in evidence this week: No AI-specific broken-rung number exists; the technical-roles cut (52) has not been refreshed since 2021; no intersectional race×gender promotion data inside AI/technical roles; "manager" vs. staff/principal-IC rung not disaggregated by gender
- Run health: OK

### 2026-06-08 — Week 5 — The pay gap in AI and machine learning roles

- Report: reports/2026-06-08_pay-gap.md
- Topic source: rotation row 5 (demo backfill run)
- Top 3 statistics found:
  1. $0.80 per $1.00: women's median weekly earnings in US Computer & Mathematical occupations, uncontrolled (BLS *Highlights of Women's Earnings 2024*)
  2. Women = 35% of equity-holding tech employees but hold only 20% of equity value (Carta Gap Table 2024)
  3. Colorado pay-transparency law: state gap narrowed 78¢ → 86¢ between 2021 and Jul 2025 (Women's Foundation of Colorado / Tejara)
- Sources cited: 22 (Tier 1: 7, Tier 2: 12, Tier 3: 3)
- New sources added to sources.md: BLS Highlights of Women's Earnings; ONS ASHE; Destatis GPG; INSEE GPG; Payscale Gender Pay Gap; Levels.fyi Gender Pay Gap; Carta Gap Table; NWLC Window Into the Wage Gap; IWPR National Wage Gap; AAUW Simple Truth; Salesforce Equality Updates; Cullen JEP 2024; Arnold et al. Pay Transparency; Alan Turing Institute Where are the Women; Monster Salary Index India; NASSCOM India Tech Compensation
- Tracked metrics updated in dashboard/metrics.md: pay gap (AI/ML, uncontrolled and controlled); pay gap by level; pay gap by country
- Notable gaps in evidence this week: No primary source isolates AI engineer / ML scientist pay gap; no intersectional cut inside AI; no published equity-equity audit at any AI lab
- Run health: OK

### 2026-06-01 — Week 4 — Entry-level AI roles: first job in AI/ML

- Report: reports/2026-06-01_entry-level-roles.md
- Topic source: rotation row 4 (demo backfill run)
- Top 3 statistics found:
  1. McKinsey/LeanIn *Women in the Workplace 2025*: entry-level women report 21% AI-tool encouragement from managers vs. 33% for men
  2. Broken rung: for every 100 men hired or promoted into entry-level/manager roles, only 81 women are (McKinsey/LeanIn 2024)
  3. Women's share of AI engineering skills in financial services declined from 31% (2016) to 28% (2023) (OECD.AI / LinkedIn)
- Sources cited: 19 (Tier 1: 9, Tier 2: 4, Tier 3: 6)
- New sources added to sources.md: OECD.AI AI workforce trends; McKinsey/LeanIn Women in the Workplace 2025; Google Diversity Annual Report; Microsoft Global D&I Report; Kapor Center Tech Leavers Study; Code2040 Fellows; AI4ALL Results; Indeed Hiring Lab AI at Work 2025; NASSCOM workforce voices
- Tracked metrics updated in dashboard/metrics.md: % women in global AI workforce; % women in EU ICT specialists; broken rung ratio
- Notable gaps in evidence this week: No published hiring funnel by gender for AI roles specifically; AI residency programs (Google, Meta, OpenAI, Anthropic) do not disclose demographics; AnitaB.org Top Companies benchmark paused in 2024
- Run health: OK

### 2026-05-25 — Week 3 — Graduate school: women in AI/ML PhD programs

- Report: reports/2026-05-25_phd-programs.md
- Topic source: rotation row 3 (demo backfill run)
- Top 3 statistics found:
  1. 25.9% of CS/CE/I PhD recipients in N. America are women — eighth consecutive annual rise (CRA Taulbee 2024)
  2. AI-specific PhD recipients: <19% women across the past decade; 21.3% in 2021 (Stanford HAI AI Index)
  3. Women in male-dominated PhD programs without female peers are 10 pp more likely to drop out before year 2 (Bostwick & Weinberg, NBER / Journal of Labor Economics)
- Sources cited: 19 (Tier 1: 12, Tier 2: 6, Tier 3: 1)
- New sources added to sources.md: CRA Taulbee Survey (multi-year); Stanford HAI AI Index Chapter 6; NSF NCSES Doctorate Recipients (SED); PNAS Grad Cohort Workshop evaluation; Bostwick & Weinberg JOLE; Canaan & Mouganie JHR; Gaule & Piacentini Research Policy; MIT Rising Stars in EECS; WiML; IBEF India AI/ML enrollment; UNESCO Status and Trends Gender Gap
- Tracked metrics updated in dashboard/metrics.md: % women in AI PhD programs (US); % women on AI tenure-track faculty
- Notable gaps in evidence this week: No public dataset of AI-PhD completion rates by gender (the single largest gap in the evidence base); no gender-disaggregated AI postdoc population; no intersectional race × gender CS PhD breakdown
- Run health: OK

### 2026-05-18 — Week 2 — The pipeline: women in undergraduate CS and AI programs

- Report: reports/2026-05-18_undergraduate-pipeline.md
- Topic source: rotation row 2 (demo backfill run)
- Top 3 statistics found:
  1. 22.6% of US CS bachelor's degrees earned by women in 2021–22 (NCES IPEDS Table 325.35)
  2. Historical peak: 37.1% in 1983–84; trough 17.6% in 2010–11 — the trajectory is reversible
  3. AP CS Principles: 33.8% female participation vs. AP CS A: 25.0% — entry-course design matters
- Sources cited: 17 (Tier 1: 11, Tier 2: 4, Tier 3: 2)
- New sources added to sources.md: NCES IPEDS Digest Table 325.35; NSF NCSES Diversity and STEM 2023 (NSF 23-315); NSF Women Minorities and Persons with Disabilities in S&E (NSF 21-321); College Board AP CS data; HESA UK Higher Education Student Statistics; OECD Education at a Glance; Eurostat ICT education; SWE India Tertiary Education; AIR Girls Who Code Evaluation; UCLA BRAID Initiative; Black Girls CODE evaluation; CACM Female Retention research
- Tracked metrics updated in dashboard/metrics.md: % women in US CS BAs; % women in UK CS entrants; % women in AP CS Principles vs AP CS A
- Notable gaps in evidence this week: No Tier 1 national statistic for women in AI-specific undergrad concentrations; no national US attrition rate for women in CS; AI4ALL and Kode With Klossy lack independent third-party evaluations
- Run health: OK

### 2026-05-11 — Week 1 — State of women in AI: representation across the workforce

- Report: reports/2026-05-11_workforce-representation.md
- Topic source: rotation row 1 (demo backfill run)
- Top 3 statistics found:
  1. Women hold 22% of global AI roles (Stanford HAI AI Index 2024; corroborated by UNESCO 2024 and Interface EU 2024)
  2. 30.5% of LinkedIn members listing AI engineering skills are women — the skill / role gap of 8–10 pp is the field's biggest unsolved problem (LinkedIn Economic Graph / WEF GGGR 2024)
  3. Under 14% of senior executive AI roles are held by women (Interface EU 2024)
- Sources cited: 16 (Tier 1: 10, Tier 2: 4, Tier 3: 2)
- New sources added to sources.md: Stanford HAI AI Index 2024 / 2023 / 2025; WEF Global Gender Gap Report; WEF Gender Parity in the Intelligent Age; LinkedIn Economic Graph Generative AI and Gender; UNESCO Women for Ethical AI; Interface EU AI's Missing Link; AI Now Institute Discriminating Systems; AnitaB.org Top Companies; National Partnership for Women & Families; Girls Who Code 2024 Annual Report + AIR evaluation; Deloitte Women in AI; Russell Reynolds AI for All
- Tracked metrics updated in dashboard/metrics.md: % women in global AI workforce; % women in AI engineering skills; % women in AI leadership
- Notable gaps in evidence this week: No primary source publishes women's share of Principal/Staff/Distinguished AI engineer roles; no 2023+ figure for Black women's share of AI-specific technical roles; no global absolute headcount of women in AI
- Run health: OK

### 2026-06-09 — Setup — Agent initialized

- Report: none (setup run)
- Topic source: n/a
- Top 3 statistics found: n/a (setup)
- Sources cited: 0
- New sources added to sources.md: initial source list seeded with Tier 1–4 publishers
- Tracked metrics updated in dashboard/metrics.md: schema created, no data yet
- Notable gaps in evidence this week: n/a (setup)
- Run health: OK — agent scaffolding created; first 5 weekly reports produced as a backfill demo run on 2026-06-09.
