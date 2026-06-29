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
