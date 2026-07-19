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

### 2026-07-19 — Week 11 — Women in AI leadership at large tech companies

- Report: reports/2026-07-19_leadership-big-tech.md (+ whitepaper, + PDF)
- Topic source: rotation row 9 (standard ISO-week rotation; confirmed as next by Week 10 colophon). Featured Healthcare R&D track (H2) last ran 2026-06-29 — within its 4-week window — so no override; H2 (gender bias inside medical AI) becomes eligible next week. **Manual/off-schedule run** — owner initiated this run on Sunday, a day ahead of the Monday 09:00 CST routine. Logged as owner-initiated.
- Top 3 statistics found:
  1. Women hold <14% of senior executive roles in AI (vs 22% of the AI workforce, ~29% at AI entry level) — Interface EU *AI's Missing Link* 2024 (Revelio Labs, ~1.6M AI professionals)
  2. At 39 leading AI orgs, women are 30% of leadership overall but 10% of CEO/top-tech roles (4 CEOs, 4 CTOs); 86% of HR execs vs 22% of product/eng/science execs — Russell Reynolds *AI for All* 2025
  3. Google, Meta, and Microsoft published no diversity report in 2025 — ending Google's 11-year women-in-leadership series at 32.8% (from 20.8% in 2014); women's share of new C-suite hires plateaued at ~27% since 2022 (WEF/LinkedIn 2026)
- Sources cited: 21 (Tier 1: 3, Tier 2: 12, Tier 3: 6)
- New sources added to sources.md: WEF *Closing the Gender Gap in Senior Leadership 2026*; Russell Reynolds *AI for All*; Google *2024 Diversity Annual Report*; Amazon *Our Workforce Data*; Apple *Inclusion & Diversity*; NVIDIA *Sustainability Report FY2025*; Intel *2023-24 CSR Report*; Meta *2022 Diversity Report*; illumyn Impact/Partners Project (via Crunchbase News); Spencer Stuart *2025 US Technology Board Index*; Altrata *Gender Diversity in Corporate America 2025*; Revelio Labs *Rise and Fall of DEI*; The Conference Board *Corporate Diversity Disclosure 2025*; Coqual *The Sponsor Dividend*; HR Brew diversity-report cessation coverage
- WAI-Test review: **SHIP — 100%** (format 6/6, content 6/6, data 6/6); test/results/leadership-big-tech.json
- Tracked metrics updated in dashboard/metrics.md: women in AI/technical executive leadership (new series); company-reported women-in-leadership by firm (new series); women's share of new C-suite/CEO/CTO hires (new series); women on AI-company boards vs public benchmarks (new series)
- Notable gaps in evidence this week: Google/Meta/Microsoft stopped publishing diversity reports in 2025 (evidence base is shrinking); no frontier AI lab (OpenAI, Anthropic, DeepMind) has ever published workforce diversity data; no gender split exists for Chief AI Officers; "leadership" defined 7 incompatible ways across company reports; no race × gender cut in any AI-leadership dataset
- Run health: OK

### 2026-07-13 — Week 10 — Women founders in AI startups: funding share

- Report: reports/2026-07-13_startup-funding.md (+ whitepaper, + PDF)
- Topic source: rotation row 8 (standard ISO-week rotation; confirmed as next by Week 9 colophon). Featured Healthcare R&D track (H-series) resumes later this month. **Manual/off-schedule run** — the Monday 09:00 CST cloud routine did not fire today; owner initiated this run manually. Logged as manual run.
- Top 3 statistics found:
  1. Startups with ≥1 female founder captured a record 27.7% of US VC deal value ($73.6B) in 2025 — but two-thirds went to AI and Anthropic + Scale AI alone took >$30B; excluding those two, female founders raised just $42.8B, below 2021–22 (PitchBook 2025 US All In, via Fortune)
  2. All-female founding teams took just 1% of US VC funding / 6% of deals in 2024 — lowest since 2017, down from 2% in 2023 (PitchBook 2024 US All In)
  3. Globally, of $289B deployed in 2024, all-women teams received 2.3% ($6.7B) vs 83.6% all-male / 14.1% mixed (PitchBook)
- Sources cited: 8 (Tier 1: 2, Tier 2: 4, Tier 3: 2)
- New sources added to sources.md: PitchBook *2025 US All In*; PitchBook *2024 US All In*; Fortune (Broadsheet) female-founders/AI analysis (Mar 2026); Atomico *State of European Tech 2024* (via Sifted); Inc. all-women-teams-1% coverage; Crunchbase News *female-founder peak 2023* and *female-founded unicorns* pieces
- WAI-Test review: **SHIP — 100%** (format 6/6, content 6/6, data 6/6); test/results/startup-funding.json
- Tracked metrics updated in dashboard/metrics.md: female-founded US VC share (≥1 founder vs all-women teams); AI concentration of female-founder dollars; global gender allocation of VC; European female-founder share
- Notable gaps in evidence this week: no recurring AI-sector × gender funding series; "≥1 female founder" metric is composition-sensitive (two mega-rounds swing the aggregate); no health-AI/femtech gender-funding cut (closest anchor Rock Health "women+ health" 6.6%)
- Run health: OK

### 2026-07-06 — Week 9 — Women & AI research: authorship of top-tier papers

- Report: reports/2026-07-06_research-authorship.md (+ whitepaper, + PDF)
- Topic source: rotation row 7 (standard ISO-week rotation). Featured Healthcare R&D track (H1) ran last week (2026-06-29) and does not override this week; resumes next month. Manual run initiated by owner (a day before the Monday cloud routine); logged as owner-initiated.
- Top 3 statistics found:
  1. 10.6% female first authors / 9.7% female last authors at ICLR 2020 — roughly half women's ~24% CS-PhD share (Tran et al., *An Open Review of OpenReview*, 2020) [dated]
  2. Female-first-authored NLP papers cited ~34% less (37.6 vs 50.4), gap persists controlling for academic age + 66 topics (Mohammad, ACL 2020) [dated]
  3. Double-blind review is the one lever with causal evidence: single-blind reviewers favored famous authors ×1.63, top companies ×2.10; female-author odds ×0.78 (Tomkins et al., PNAS 2017) [dated]
- Sources cited: 12 (Tier 1: 8, Tier 2: 3, Tier 3: 1)
- New sources added to sources.md: Tran et al. *An Open Review of OpenReview* (arXiv 2010.05137); Nesta *Gender Diversity in AI Research* (2019); Mohammad *Gender Gap in NLP Research* (ACL 2020); Element AI *Global AI Talent Report 2019*; CRA *2024 Taulbee Survey*; Tomkins et al. *Reviewer bias in single- vs double-blind peer review* (PNAS 2017); Budden et al. *Double-blind review favours female authors* (TREE 2008); WEF *Global Gender Gap Report 2025*; Zhao et al. *Voices of Her* (2023)
- WAI-Test review: **SHIP — 100%** (format 6/6, content 6/6, data 6/6); test/results/research-authorship.json
- Tracked metrics updated in dashboard/metrics.md: top-venue female authorship (first/last); NLP citation gap; CS-PhD female share (Taulbee series extended); AI-engineering skill share (2025)
- Notable gaps in evidence this week: no venue-specific women's-authorship share exists for 2023–2025 (best data pre-2021); Stanford AI Index dropped author-gender reporting after 2024; no gender × AI-specialty cross-tab; all figures rest on name-based gender inference (excludes non-binary); WiML/Rising Stars lack causal evaluation
- Run health: OK

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
