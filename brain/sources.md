# Trusted sources for women-in-AI research

The agent prioritizes these sources when gathering statistics. Each entry includes what kind of number you can expect, the cadence of publication, and the URL stem to query.

Sources are grouped by tier. **Tier 1 = primary, methodologically transparent.** Tier 2 and 3 are still usable but need a primary citation behind any number used.

When a new credible source is discovered during a weekly run, append it here (note the tier, what it publishes, and the year of the most recent issue you've seen).

---

## Tier 1 — Primary, authoritative

### Annual index reports
- **Stanford HAI — AI Index Report** — annual, headline statistics on the AI ecosystem including a diversity chapter. hai.stanford.edu
- **World Economic Forum — Global Gender Gap Report** — annual, gender gap across economic participation, education, health, political empowerment, with an AI-specific cut in recent years. weforum.org
- **McKinsey + LeanIn.org — Women in the Workplace** — annual, US tech and corporate ladder data, useful for benchmarking the "broken rung" specifically. womenintheworkplace.com
- **OECD — Going Digital reports, AI Observatory** — periodic, OECD-country AI workforce data. oecd.ai
- **UNESCO — I'd Blush If I Could; Women in AI** — periodic, global view with strong Global South coverage. unesco.org

### Government and statistical agencies
- **US National Science Foundation — NCSES Diversity and STEM** — biennial, the canonical US dataset for women in computing and STEM. ncses.nsf.gov
- **US Bureau of Labor Statistics — Current Population Survey occupational data** — annual, occupational counts including "computer and information research scientists". bls.gov
- **Eurostat — Human resources in science and technology** — annual, EU workforce data. ec.europa.eu/eurostat
- **UK Office for National Statistics — Labour Force Survey** — quarterly, UK tech occupational data. ons.gov.uk

### Industry/employer-side data
- **LinkedIn Economic Graph — Future of Work / AI talent reports** — periodic, very large sample of self-reported AI roles. economicgraph.linkedin.com
- **GitHub — Octoverse** — annual, open-source contributor demographics where available. octoverse.github.com
- **PitchBook — All In: Female Founders in the VC Ecosystem** — annual, female-founder funding share including AI cuts. pitchbook.com
- **Crunchbase News — Diversity Spotlight, funding to female founders** — periodic. news.crunchbase.com

### Academic / conference data
- **NeurIPS / ICML / ICLR / ACL Diversity & Inclusion reports** — often per-conference, author and attendee demographics. Check each conference's D&I committee page.
- **Computing Research Association — Taulbee Survey** — annual, North American CS PhD demographics including AI specialization where available. cra.org

### Healthcare R&D — women & AI in medicine (featured track sources)
- **UNESCO — Women for Ethical AI: Outlook Study on AI and Gender** (2024) — global synthesis; women as % of AI researchers/faculty/executives. unesdoc.unesco.org/ark:/48223/pf0000391719 — Tier 1
- **International Labour Organization — generative-AI workplace exposure by gender** (2025) — ilo.org — Tier 1
- **NSF NCSES — Women in Business R&D (NSF 23-328)** (2020 data) — US business-R&D workforce by function/gender. ncses.nsf.gov/pubs/nsf23328 — Tier 1
- **Nature Medicine — Seyyed-Kalantari et al., Underdiagnosis bias of AI on chest radiographs** (2021) — algorithmic underdiagnosis of female/under-served patients. nature.com — Tier 1
- **JACC — Participation of Women in CV Drug-Approval Trials** (2018) — women's share of trial participants (training-data proxy). jacc.org — Tier 1
- **Circulation — Women's Participation in Cardiovascular Clinical Trials 2010–2017** (2020) — ahajournals.org — Tier 1
- **Canadian Association of Radiologists Journal (CARJ) — Yan et al., female authorship in AI radiology** (2023) — pubmed.ncbi.nlm.nih.gov/36062579 — Tier 2
- **European Journal of Radiology — authorship gender in AI breast imaging** (2024) — pubmed.ncbi.nlm.nih.gov/38492508 — Tier 2
- **Rock Health — Women in Focus / digital-health funding** (annual) — "women+ health" funding share. rockhealth.com — Tier 3
- **Pharma's Almanac — biopharma leadership gender (CSO/CTO/CEO)** (2025) — pharmasalmanac.com — Tier 3
- **Medical Design & Outsourcing — diversity in medtech** (2022) — medtech workforce vs. executive gender. medicaldesignandoutsourcing.com — Tier 3
- **PharmaVoice — women in biotech/pharma leadership trends** — pharmavoice.com — Tier 3

---

## Tier 2 — Credible specialists and advocacy organizations with audited methodology

- **AnitaB.org / Grace Hopper Celebration research** — anitab.org
- **Catalyst.org** — corporate gender data, broader than AI but useful for benchmarks. catalyst.org
- **AI Now Institute** — qualitative + workforce research on AI labor. ainowinstitute.org
- **Women in AI (WAI)** — womeninai.co
- **AI4ALL** — pipeline interventions. ai-4-all.org
- **Women in Machine Learning (WiML)** — wimlworkshop.org
- **Black in AI** — blackinai.github.io
- **Latinx in AI** — latinxinai.org
- **Queer in AI** — queerinai.com
- **Re:Work / Rework Women in AI** — eventer/researcher hybrid. re-work.co
- **Element AI Global Talent Report (legacy, now via ServiceNow)** — periodic global AI talent census including gender. Archive copies via Wayback Machine.
- **Nesta — UK innovation and AI workforce research** — nesta.org.uk
- **Brookings Institution — AI workforce research** — brookings.edu
- **Pew Research Center — STEM and tech workforce** — pewresearch.org
- **Holon IQ — global AI ecosystem maps** — holoniq.com

---

## Tier 3 — Industry and consultancy reports (use for analysis, anchor numbers to a Tier 1/2 source)

- Deloitte — Women in Tech and AI annual updates
- BCG — Women in Tech, AI for women research
- Accenture — Getting to Equal series
- Gartner — diversity in AI talent
- KPMG — Women in tech and AI
- PwC — Women in Tech series
- Bain — AI workforce reports

---

## Tier 3.5 — Aggregator news/analysis (good for finding leads, not citing primary stats)

- VentureBeat AI coverage
- MIT Technology Review
- Wired
- TechCrunch (especially for funding data — confirm against PitchBook)
- The Information
- Rest of World (excellent for Global South AI labor)

---

## Tier 4 — Datasets to query directly

- **arXiv** — for AI/ML papers; pair with author-gender inference research carefully (noisy signal).
- **OpenReview** — review data for NeurIPS, ICLR with some demographic disclosures.
- **Google Scholar profiles** — for individual citation counts (gender citation gap research).
- **Crunchbase API / PitchBook API** — funding rounds with founder gender where labeled.
- **LinkedIn search (compliant scraping or LinkedIn-published reports)** — workforce composition by company.

---

## Source-discovery prompts to try each week

- `<topic> filetype:pdf site:.edu`
- `<topic> filetype:pdf site:.gov`
- `<topic> "women" "AI" "<year>" report`
- `<topic> "diversity report" "machine learning"`
- `<topic> site:oecd.ai OR site:weforum.org OR site:unesco.org`
- `<topic> "Taulbee" OR "AI Index" OR "Global Gender Gap"`

---

## Sources discovered and confirmed across reports 1–5 (demo run, 2026-06-09)

### Tier 1 — confirmed primary sources used
- Stanford HAI — *AI Index Report 2024* (Chapter 6 Education; Chapter 8 Diversity). https://hai.stanford.edu/ai-index/2024-ai-index-report
- Stanford HAI — *AI Index Report 2023* and *AI Index Report 2025*
- World Economic Forum — *Global Gender Gap Report 2024*. https://www3.weforum.org/docs/WEF_GGGR_2024.pdf
- World Economic Forum — *Gender Parity in the Intelligent Age* whitepaper (Mar 2025)
- LinkedIn Economic Graph — *Generative AI and Gender* (2024). https://economicgraph.linkedin.com/content/dam/me/economicgraph/en-us/PDF/generative-ai-and-gender.pdf
- LinkedIn Economic Graph — *Women and Future Jobs / AI Talent Index*
- OECD.AI — *2023 LinkedIn AI workforce analysis* and live AI talent indicators. https://oecd.ai
- UNESCO — *Women for Ethical AI: Outlook Study* (Oct 2024). https://unesdoc.unesco.org/ark:/48223/pf0000391719
- UNESCO — *Cracking the Code* (2017); *Status and Trends: Gender Gap in Science*
- McKinsey + LeanIn — *Women in the Workplace 2024* and *2025*. https://wiw-report.s3.us-east-1.amazonaws.com/Women_in_the_Workplace_2025.pdf
- CRA — *Taulbee Survey 2022, 2023, 2024*. https://cra.org
- NSF NCSES — *Diversity and STEM 2023* (NSF 23-315); *Women, Minorities, and Persons with Disabilities in S&E 2021* (NSF 21-321); *Doctorate Recipients from US Universities 2023 (SED)*; *Postdoctoral Appointments Rise*; *Science & Engineering Indicators 2024*
- NCES — *Digest of Education Statistics 2023, Table 325.35*. https://nces.ed.gov/programs/digest/d23/tables/dt23_325.35.asp
- College Board — AP CS Female Diversity Award participation data
- HESA — *UK Higher Education Student Statistics 2023/24 (SB271)*
- OECD — *Education at a Glance 2023*
- Eurostat — *ICT specialists 2024*; *ICT education statistics*; *Gender pay gap statistics*
- BLS — *Highlights of Women's Earnings 2024*; *OEWS Computer/Information Research Scientists*; *Data Scientists OOH*
- ONS UK — *Gender pay gap in the UK 2024 (ASHE)*
- Destatis — *Gender Pay Gap 2024 (Germany)*
- INSEE — *Gender pay gap 2024 (France)*
- Indeed Hiring Lab — *AI at Work Report 2025*
- PNAS / NIH PMC — *Grad Cohort Workshop evaluation* (PMC5222789)
- McKinsey/LeanIn — *Repairing the broken rung on the career ladder for women in technical roles* (technical-roles cut, 2021 — 52 women promoted to manager per 100 men in technical roles; the three enablers). https://www.mckinsey.com/industries/technology-media-and-telecommunications/our-insights/repairing-the-broken-rung-on-the-career-ladder-for-women-in-technical-roles  [Tier 1/2]
- McKinsey — *Diversity Matters Even More* (2023 — gender-diverse leadership 48% more likely to outperform; 1,265 companies, 23 countries). https://www.mckinsey.com/capabilities/people-and-organizational-performance/our-insights/diversity-matters-even-more

### Tier 2 — confirmed credible secondary sources used
- Interface EU — *AI's Missing Link* (2024). https://www.interface-eu.org/publications/ai-gender-gap
- WEF — *How AI is worsening workplace gender gaps* (2025); pairs with *Gender Parity in the Intelligent Age* (men ~22% higher daily AI use). https://www.weforum.org/stories/2025/05/how-ai-is-worsening-workplace-gender-gaps-and-how-we-can-course-correct-7828b8eae9/
- Women in Tech Network — *Women in Tech Stats 2025/2026* (STEM pipeline: 29% entry / 24.4% managerial / 12.2% C-suite; secondary aggregation of WitW). https://www.womentech.net/en-us/women-in-tech-stats
- HR Brew — *Women have made strides … but a broken rung persists* (Dec 2025; WitW 2025 sponsorship and senior-women burnout figures). https://www.hr-brew.com/stories/2025/12/09/women-have-made-strides-in-the-workplace-in-recent-years-but-a-broken-rung-persists-report-finds  [Tier 3]
- AI Now Institute — *Discriminating Systems* (2019)
- AnitaB.org — *Top Companies for Women Technologists 2023* (program paused 2024)
- Pew Research — pay gap and negotiation reports (2024, 2023)
- AAUW — *The Simple Truth 2024/2026*
- IWPR — *National Wage Gap Fact Sheet 2024*
- National Women's Law Center — *Window Into the Wage Gap*
- National Partnership for Women & Families — *AI and Emerging Risks for Women Workers* (2024)
- Payscale — *2024 Gender Pay Gap Report* and *2026* update
- Levels.fyi — *Gender Pay Gap Report Q1 2024*
- Carta — *Analyzing the Gender Equity Gap (Gap Table)*
- Kapor Center — *Tech Leavers Study 2017*
- American Institutes for Research — *Girls Who Code Program Evaluation* (March 2024, ERIC ED647331)
- UCLA / Linda Sax — *BRAID Initiative* longitudinal study (NSF Award 1525737)
- WiML Workshop, MIT Rising Stars in EECS, CRA-W Grad Cohort
- Bostwick & Weinberg — *Nevertheless She Persisted* (NBER / JOLE) [paywalled]
- Canaan & Mouganie — Advisor Gender Impact (JHR) [paywalled]
- Gaule & Piacentini — Advisor like me (Research Policy) [paywalled]
- Vanderbilt / Kennedy — negotiation research (2023)
- SWE — *India Tertiary Education 2025*
- Cullen Z. — *Is Pay Transparency Good?* (JEP 2024)
- Arnold et al. — *Impact of Pay Transparency in Job Postings*

### Tier 3 — used as analysis/context (anchor numbers always traced to Tier 1/2)
- Google *Diversity Annual Report 2024*
- Microsoft *Global D&I Report 2024*
- Russell Reynolds Associates — *AI for All*
- Deloitte — *Women in AI 2024*
- Salesforce *Equality Updates 2023*
- Alan Turing Institute — *Where are the Women*
- NASSCOM — *India Tech Compensation Benchmarking 2024* [paywalled for full data]
- Monster Salary Index / IIMA — India gender pay gap
- IBEF — India AI/ML enrollment
- Code2040 *Fellows program data*
- AI4ALL *Results*
- Rockman et al. *Black Girls CODE case study 2017*
- CACM — *Toward Improving Female Retention in CS*

---

## Sources discovered and confirmed — Week 9 (2026-07-06, research authorship)

### Tier 1 — primary / peer-reviewed
- Tran, D. et al. — *An Open Review of OpenReview: A Critical Analysis of the ML Conference Review Process* (2020). arXiv:2010.05137. ICLR 2017–2020 OpenReview records; women 10.6% first / 9.7% last authors at ICLR 2020; acceptance 23.5% vs 27.1%. https://arxiv.org/abs/2010.05137 — Tier 1 [dated]
- Mohammad, S. — *Gender Gap in Natural Language Processing Research: Disparities in Authorship and Citations* (ACL 2020). ACL Anthology corpus; 29.2% first / 25.5% last female authors; 37.6 vs 50.4 citation gap. https://aclanthology.org/2020.acl-main.702/ — Tier 1 [dated]
- Tomkins, A., Zhang, M. & Heavlin, W. — *Reviewer bias in single- versus double-blind peer review* (PNAS 2017; WSDM 2017 experiment). arXiv:1702.00502. Single-blind favors famous ×1.63 / top companies ×2.10; female ×0.78. https://arxiv.org/abs/1702.00502 — Tier 1 [dated]
- Budden, A. et al. — *Double-blind review favours increased representation of female authors* (Trends in Ecology & Evolution, 2008). https://pubmed.ncbi.nlm.nih.gov/17963996/ — Tier 1 [dated]
- Computing Research Association — *2024 Taulbee Survey* (data 2023–24); 25.9% female CS/CE/I PhD recipients. https://datavisualization.cra.org/TaulbeeSurvey/CRA_Taulbee_Survey_Report_2024.html — Tier 1
- World Economic Forum — *Global Gender Gap Report 2025* (LinkedIn Economic Graph); 29.4% AI-engineering skill-listers women (first YoY decline). https://www.weforum.org/publications/global-gender-gap-report-2025/ — Tier 1

### Tier 2 — credible specialist
- Nesta (Stathoulopoulos & Mateos-Garcia) — *Gender Diversity in AI Research* (2019). ~1.5M arXiv papers; 13.8% female AI authors; company/country breakdowns. https://www.nesta.org.uk/report/gender-diversity-ai/ — Tier 2 [dated]
- Zhao, F. et al. — *Voices of Her: Analyzing Gender Differences in the AI Publication World* (2023). arXiv:2305.14597. 78K AI researchers; citation gap + co-authorship homophily. https://arxiv.org/abs/2305.14597 — Tier 2

### Tier 3 — industry
- Element AI — *Global AI Talent Report 2019*. ~12% female authors at top-21 AI conferences; 18% of papers with ≥1 female author (original page defunct; via secondary coverage). https://techhq.com/2019/04/theres-a-global-ai-talent-shortage-and-a-lack-of-diversity/ — Tier 3 [dated]

**Data note (Week 9):** No venue-specific women's-authorship share exists for 2023–2025; Stanford AI Index dropped author-gender reporting after its 2024 edition. All authorship figures rely on name-based gender inference (excludes non-binary). The "~19–21% of AI-specific PhDs are women" figure is unverified against a primary cross-tab — treat as [methodology gap].

---

## Sources discovered and confirmed — Week 10 (2026-07-13, startup funding)

### Tier 1 — primary funding datasets
- PitchBook — *2025 US All In: Female Founders in the VC Ecosystem* (2026). Record $73.6B / 27.7% of US VC deal value to ≥1-female-founder startups; two-thirds to AI; ex-Anthropic/Scale AI = $42.8B. https://pitchbook.com/news/reports/2025-us-all-in-female-founders-in-the-vc-ecosystem — Tier 1
- PitchBook — *2024 US All In: Female Founders in the VC Ecosystem* (Mar 2025). All-female teams 1% of US VC / 6% of deals (lowest since 2017); ≥1-female value share 19.9% (from 20.8%), count share 25.1%; $38.8B total; global $289B split 83.6% all-male / 14.1% mixed / 2.3% all-women ($6.7B). https://pitchbook.com/news/reports/2024-us-all-in-female-founders-in-the-vc-ecosystem — Tier 1

### Tier 2 — credible secondary / named coverage
- Fortune (Hinchliffe, E., *The Broadsheet*) — *Venture dollars to female founders doubled to a record $73 billion last year — but Anthropic and Scale AI skewed the data* (6 Mar 2026). Carries the $42.8B ex-two-companies figure and two-thirds-to-AI share. https://fortune.com/2026/03/06/venture-dollars-female-founders-pitchbook-ai/ — Tier 2
- Atomico — *State of European Tech 2024*, women-founder chapter (via Sifted, Dec 2024). Europe female founders €5.76B / 12% of VC (down 12% YoY); all-women teams 6% flat since 2016; 25% of largest female-founder rounds to AI. https://sifted.eu/articles/women-founded-startups-funding-2024 — Tier 2
- Inc. (Conrad, J.) — *Wholly Women-Led Companies Attracted Just 1 Percent of VC Funding in 2024* (Mar 2025). Secondary corroboration of PitchBook 1% all-women-team figure. https://www.inc.com/jennifer-conrad/wholly-women-led-companies-attracted-just-1-of-vc-funding-in-2024-tanking-an-already-abysmal-stat/91156396 — Tier 2

### Tier 3 — named industry research
- Crunchbase News (Teare, G.) — *The Portion of US VC Funding That Went to Female Founders Hit a New Peak in 2023, Thanks to Massive AI Deals* (2024). AI-sector cut: >50% of US AI dollars (~$21B, 360+ rounds) touched ≥1-female-founder firm, but <20% of AI rounds had one. https://news.crunchbase.com/diversity/us-vc-funding-female-founders-peaked-2023-ai-openai-anthropic/ — Tier 3 [dated]
- Crunchbase News (Teare, G.) — *As Funding Fell, So Did the Number of New Female-Founded Unicorn Startups* (2025). Only 7 US female-founded unicorns across 2023–24 (5 of 7 AI-related) vs dozens in 2021. https://news.crunchbase.com/diversity/female-founded-unicorn-startups-ai-anthropic-zum/ — Tier 3

**Data note (Week 10):** No recurring series measures the female-founded share of *AI-sector* funding specifically — it surfaces only in one-off analyses. The "≥1 female founder" metric is composition-sensitive: two 2025 mega-rounds (Anthropic, Scale AI) swing the US aggregate to a record 27.7% while access measures (all-female-team share, deal counts) regress. Health-AI/femtech gender-funding cut remains unbroken-out (closest anchor: Rock Health "women+ health" 6.6% of digital-health funding, from Week 8).

---

## Sources discovered and confirmed — Week 11 (2026-07-19, AI leadership at large tech companies)

### Tier 1 — primary / institutional
- **WEF, *Closing the Gender Gap in Senior Leadership* (June 2026)** — LinkedIn EGRI data, 39–41 economies; C-suite hires time series 2015–2025; CTO share 8.6%. https://reports.weforum.org/docs/WEF_Closing_the_Gender_Gap_in_Senior_Leadership_2026.pdf
- **WEF, *Gender Parity in the Intelligent Age* (March 2025)** — LinkedIn EGRI; STEM C-suite 12.2% vs STEM managers 24.4%. https://reports.weforum.org/docs/WEF_Gender_Parity_in_the_Intelligent_Age_2025.pdf

### Tier 2 — company-reported primary data (self-reported; final editions noted)
- **Google, *2024 Diversity Annual Report*** — 11-year women-in-leadership series 20.8%→32.8% (2014–2024); FINAL edition, no 2025 report. https://static.googleusercontent.com/media/belonging.google/en//diversity-annual-report/2024/static/pdfs/google_2024_diversity_annual_report.pdf
- **Microsoft, *2024 Global Diversity & Inclusion Report*** — Executive band 29.0% (only falling level); FINAL edition. https://blogs.microsoft.com/blog/2024/10/23/microsofts-2024-global-diversity-inclusion-report-our-most-global-transparent-report-yet/
- **Meta, *2022 Diversity Report*** — 36.7% leadership (director+); FINAL edition (nothing since 2022) [dated]. https://about.fb.com/news/2022/07/metas-diversity-report-2022/
- **Amazon, *Our Workforce Data*** — senior leaders (L8+) 26.3% global (2024); still publishing. https://www.aboutamazon.com/news/workplace/our-workforce-data
- **Apple, *Inclusion & Diversity*** — leadership (all managers) 33% (Dec 2024); still publishing. https://www.apple.com/diversity/
- **NVIDIA, *Sustainability Report FY2025*** — "Leaders" 13.5%, Managers 18.7%, workforce 21.2%. https://images.nvidia.com/aem-dam/Solutions/documents/NVIDIA-Sustainability-Report-Fiscal-Year-2025.pdf
- **Intel, *2023-24 Corporate Responsibility Report*** — senior leadership (grade 10+) 19.0% (2023). https://csrreportbuilder.intel.com/pdfbuilder/pdfs/CSR-2023-24-Full-Report.pdf
- **Spencer Stuart, *2025 U.S. Technology Board Index*** — women 34% of new tech-board seats (down from 39%). https://www.spencerstuart.com/-/media/2025/10/techbi/2025-us-technology-spencer-stuart-board-index.pdf
- **Altrata, *Gender Diversity in Corporate America 2025*** — S&P 500 board share 33.7%, first decline in a decade. https://altrata.com/reports/gender-diversity-in-corporate-america-in-2025
- **Revelio Labs, *The Rise and Fall of DEI in Corporate America* (2025)** — 2,600+ DEI-titled roles cut since 2023; women 71% of DEI incumbents. https://www.reveliolabs.com/news/social/the-rise-and-fall-of-dei-in-corporate-america/
- **The Conference Board, *Corporate Diversity Disclosure 2025*** — S&P 500 women-in-management disclosure down 16%. https://www.conference-board.org/press/corporate-diversity-disclosure-2025
- **Coqual, *The Sponsor Dividend* (2019)** — with sponsors, women promoted at the same rate as men [dated]. https://coqual.org/wp-content/uploads/2020/09/CoqualTheSponsorDividend_KeyFindingsCombined090720.pdf

### Tier 3 — named industry research / coverage
- **Russell Reynolds, *AI for All: The Case for More Women Leaders in AI* (Feb 2025)** — 426 executives at 39 AI orgs; 30% leadership / 10% CEO+top-tech; 86% HR vs 22% technical execs. https://www.russellreynolds.com/en/insights/articles/the-case-for-more-women-leaders-in-ai
- **illumyn Impact / Partners Project via Crunchbase News (Oct 2025)** — 15% of private-AI board seats; 43% of CA private AI cos zero women directors. https://news.crunchbase.com/diversity/governing-ai-companies-california-partners-project-illumyn/
- **HR Brew (Nov 2025)** — confirms Google/Meta/Microsoft published no 2025 diversity reports. https://www.hr-brew.com/stories/2025/11/19/some-tech-companies-abandon-diversity-reports-as-they-go-mum-on-dei
- **ESG Dive / Reuters (Feb 2025)** — Accenture DEI-goal sunset; 48% women / 30% women MDs reached. https://www.esgdive.com/news/accenture-rolls-back-dei-goals-to-comply-with-trump-executive-orders/739958/

### Negative findings worth remembering (do not cite the following)
- "OpenAI 2024 DEI report / 16% women in technical roles" — unverifiable; no such report exists on any OpenAI property.
- KORE1 "~22% of CAIO hires are women" — single staffing firm's own placements, sample undisclosed; anecdotal only.
- Gitnux Google-leadership figures — contradicted by Google's primary PDF; avoid gitnux.org.
