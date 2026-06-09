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
