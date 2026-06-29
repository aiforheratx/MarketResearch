---
date: 2026-06-29
week: 8
topic: Women & AI in healthcare R&D: the state of representation
slug: healthcare-rnd
career_phase: all
geography: global
status: final
---

# Women & AI in healthcare R&D: the state of representation

*Week 8 report — 2026-06-29 — Featured priority track (H1)*

## Executive summary

Women are a structural minority at every layer of AI in healthcare R&D: roughly **12% of AI researchers and 16% of AI academic faculty** (UNESCO, 2024), and **under 40% of authors on medical-AI papers** — a share that, in radiology, *falls* the more central AI becomes to the work. This is not only an equity problem; it is encoded into the product, with state-of-the-art chest-X-ray AI shown to **systematically underdiagnose female patients** (Nature Medicine, 2021), built on trial data where women were only **~34–38% of participants** (JACC, 2018; Circulation, 2020). The single most useful thing a medtech R&D leader can do this week is audit one model's training data for sex balance — because the representation gap in the room is reproducing itself in the algorithm.

## Numbers in this report

| # | Statistic | Year | Source | Tag |
|---|---|---|---|---|
| 1 | 12% of AI researchers are women; 38% gender gap in AI research positions (vs. 21% in general science R&D) | 2024 | UNESCO, *Women for Ethical AI* | [primary] |
| 2 | 16% of AI academic faculty and 18% of AI startup executives are women | 2024 | UNESCO, *Women for Ethical AI* | [primary] |
| 3 | 22.3% female first authors / 27.3% female senior authors on AI radiology papers (453 articles, 24 countries) | 2023 | Yan et al., *Can Assoc Radiol J* | [primary] |
| 4 | 35.7% female first / 37.4% female senior authors on AI breast-imaging papers (115 studies) | 2024 | *Eur J Radiology* | [primary] |
| 5 | Chest-X-ray AI classifiers selectively **underdiagnose** female (and other under-served) patients | 2021 | Seyyed-Kalantari et al., *Nature Medicine* | [primary] [dated] |
| 6 | Women were 34% of participants in trials supporting 36 FDA cardiovascular-drug approvals (n=224,417) | 2018 | *J Am Coll Cardiol* (JACC) | [primary] [dated] |
| 7 | Women were 38.2% of participants across 740 cardiovascular trials (862,652 adults) | 2010–17 | *Circulation* | [primary] [dated] |
| 8 | $671M — 6.6% of 2024 US digital-health funding — went to "women+ health" solutions (highest since 2021) | 2024 | Rock Health | [secondary] |
| 9 | All-female founding teams captured ~1–2% of US VC funding; female-founder deal-value share fell 20.8%→19.9% | 2024 | PitchBook, *All In* | [secondary] |
| 10 | Biopharma technical leadership: ~20% of CSOs and ~14% of CTOs are women; <10% of biopharma CEOs | 2025 | Pharma's Almanac | [secondary] |
| 11 | Women are ~40% of the medtech workforce but only 21% of executives | 2022 | Medical Design & Outsourcing | [secondary] [dated] |
| 12 | Women are 27% of US business-R&D employees but just 12% in engineering/technology R&D | 2020 | NSF NCSES (NSF 23-328) | [primary] [dated] |

Tags: `[primary]` `[secondary]` `[dated]` `[contested]` `[methodology gap]`

## 1. What's the number?

There is no single audited figure for "women's share of the health-AI workforce" — the intersection of two fields that each measure gender separately and neither measures cleanly. So the picture has to be assembled from four adjacent measurements, each with a named source.

**The research layer.** UNESCO's 2024 *Women for Ethical AI* outlook study — a synthesis of international indices — puts women at **12% of AI researchers** and **16% of AI academic faculty**, with an **18%** share of AI-startup executives. UNESCO frames the research-position gap as **38%**, nearly double the **21%** gap it finds in general scientific R&D. Stanford HAI's AI Index corroborates the academic pipeline: women are roughly **22.1% of CS PhD graduates** and **16% of tenure-track CS faculty** (2024 report, data to 2022 — `[dated]`). The 2026 AI Index, released in April, describes the diversity needle as still "unmoving."

**The authorship layer** is where health-AI gets specific, because bibliometrics let you measure it directly. In AI radiology research across four North American journals (453 articles, 24 countries), women were **22.3% of first authors and 27.3% of senior authors** (Yan et al., *CARJ* 2023). In AI breast-imaging specifically — a subfield with more women overall — the figures are higher: **35.7% first and 37.4% senior authors** across 115 studies (*European Journal of Radiology*, 2024). A related analysis in that literature reports that female authorship roughly *halves* once AI becomes the explicit research focus (≈37% on AI papers vs. ≈64% on non-AI breast-imaging papers) — a striking observation we treat as `[contested]` pending direct confirmation against the primary PDF, but one that is directionally consistent across radiology subspecialties.

**The capital layer.** Founders are where money meets representation. PitchBook's 2024 *All In* report finds **all-female founding teams captured ~1–2% of US VC** and that the female-founder share of US deal *value* slipped from **20.8% (2023) to 19.9% (2024)**. Rock Health's complementary cut — which tracks the *topic* rather than founder gender — shows **$671M, or 6.6%**, of 2024 US digital-health funding went to "women+ health" solutions, the highest share since 2021 but still a rounding error against the sector total.

**The leadership and engineering layer.** In biopharma, women hold roughly **20% of CSO and 14% of CTO** roles — the seats that set R&D and AI strategy — and **fewer than 10% of CEO** roles (Pharma's Almanac, 2025). In medtech, women are about **40% of the workforce but only 21% of executives** (Medical Design & Outsourcing, 2022 — `[dated]`). And at the bench, NSF data show women are **27% of US business-R&D employees but just 12% in engineering/technology R&D** — the lowest share of any function (NSF NCSES 23-328, 2020 data — `[dated]`).

## 2. What's the trend?

Where time series exist, movement is slow and uneven:

| Year | Statistic | Source |
|---|---|---|
| 2016 | ~25% of AI "talent" (skill-listers) are women | WEF GGGR (LinkedIn) |
| 2024 | ~27% of AI talent; 29.4% of AI-engineering skill-listers (2025) | WEF GGGR 2024 |
| 2018 | Biotech executive teams ~25% women | PharmaVoice |
| 2021 | Biotech executive teams 35% women — then plateau | PharmaVoice |
| 2023 | AI breast-imaging senior-author share rising over time | Eur J Radiology |

The trend is **slow improvement at the entry/skill layer, a plateau at leadership, and stagnation in the underlying data**. The biotech leadership share climbed ten points in three years (2018–2021) and then stopped. AI-talent share has crept up roughly two points in eight years. Authorship in medical-AI is inching up in the most-watched subfields but remains below 40%. Critically, the ILO reported in 2025 that **women face higher workplace exposure to generative-AI automation than men** — meaning the population most underrepresented in *building* health AI is most exposed to being *displaced* by AI generally.

## 3. What's missing?

This topic has more documented gaps than almost any prior week:

- **No audited statistic for women's share of the health-AI workforce specifically.** Every number above is a proxy from a broader AI or broader health-tech population. UNESCO itself flags that the data is "sparse, outdated, too broad, and often omits gender dimensions" — a meta-gap acknowledged by a Tier-1 source.
- **No gender data for AI drug discovery or computational biology.** The fastest-growing application of AI in R&D has no audited representation figure; biotech-leadership numbers are the closest proxy.
- **Founder gender within health-AI funding is unmeasured.** Rock Health tracks the women's-health *topic*; PitchBook tracks founder *gender* across all sectors; neither isolates "women-founded health-AI."
- **Medtech-specific AI/R&D engineering gender data does not exist.** Only broad medtech (21% exec) and broad business-R&D (12% engineering) figures are available, both pre-2023.
- **No intervention study measures representation gains in health-AI or medtech R&D.** Every "what works" example below comes from general women-in-STEM or global-health programs.
- **Several core bias and trial-participation numbers are pre-2023** (`[dated]`) — still authoritative and widely cited, but the field has not refreshed them.

## 4. What works?

No intervention has yet been evaluated *specifically* for women in health-AI or medtech R&D with quantified representation outcomes — itself a gap. The strongest adjacent evidence, with measured outcomes:

- **Female Global Scholars Program (global health research).** A mixed-methods evaluation reports the cohort produced **35 first-author papers, 12 oral presentations, 8 grants, and 5 promotions** — concrete research-productivity gains, not just satisfaction scores (*PMC*, 2024). Tier 2.
- **HIGHER Women consortium mentoring.** Measured increases in **peer-reviewed publications and conference presentations** among participants (*PMC*, 2023). Tier 2.
- **CRA-W Grad Cohort Workshop (computing).** A formally evaluated intervention for retaining women in computing graduate programs — the model most transferable to AI R&D pipelines (*PMC*, 2017). Tier 2.
- **AI4ALL.** 91% of participants report increased interest in AI careers and 78% plan to continue STEM education (program-reported, Tier 3 / self-reported).

*Untested but frequently cited:* female-only digital-literacy cohorts (improved self-efficacy and AI-bias awareness, qualitative only); femtech accelerators; "women in medtech" ERGs — widely promoted, none with published comparison-group representation outcomes in this sector.

## 5. Recommended actions

1. **Read** — Seyyed-Kalantari et al., *Underdiagnosis bias of artificial intelligence algorithms applied to chest radiographs* (Nature Medicine, 2021). It is the single clearest demonstration that under-representation in the data becomes under-diagnosis in the clinic.
2. **Share** — the pairing of two numbers: women are **34% of cardiovascular trial participants** (JACC) yet the AI trained on that data is deployed to *both* sexes. It reframes diversity from an HR metric to a model-validity metric.
3. **Ask** — put one question to your R&D or AI governance team: *"For our highest-stakes model, what is the sex balance of the training data, and have we measured performance separately for women?"* This is the gap analysis made operational.
4. **Track** — watch the **female senior-author share in medical-AI literature** (currently 27–37% depending on subfield). It is the leading indicator of who will lead the next decade of clinical-AI R&D, and it is publicly measurable each year.
5. **Act** — in your next model-validation review or hiring rubric, add a sex-disaggregated performance check and require at least one woman R&D scientist on the review. The biopharma evidence (only ~14% of CTOs are women) shows the decision layer is where the gap concentrates — and where a single structural rule changes who is in the room.

## Sources

1. UNESCO, *Women for Ethical AI: Outlook Study on Artificial Intelligence and Gender*, 2024. https://unesdoc.unesco.org/ark:/48223/pf0000391719 — Methodology: synthesis of international indices; global; defines AI research/faculty/executive populations. Tier 1.
2. Stanford HAI, *2024 AI Index Report — Diversity (Ch. 8)*, 2024. https://hai.stanford.edu/ai-index/2024-ai-index-report/diversity — Methodology: CRA Taulbee + Informatics Europe; US/Canada/Europe; data to 2022. Tier 1.
3. Stanford HAI, *2026 AI Index Report*, 2026. https://hai.stanford.edu/ai-index/2026-ai-index-report — Methodology: annual multi-source index. Tier 1.
4. World Economic Forum, *Global Gender Gap Report 2024*, 2024. https://www3.weforum.org/docs/WEF_GGGR_2024.pdf — Methodology: LinkedIn skill data + ILO labor data; global. Tier 1.
5. International Labour Organization, *New ILO data confirm women face higher workplace risks from generative AI*, 2025. https://www.ilo.org/resource/news/new-ilo-data-confirm-women-face-higher-workplace-risks-generative-ai-men — Methodology: global occupational exposure modelling. Tier 1.
6. Yan et al., *Female Authorship in Artificial Intelligence Research in North American Radiology Journals*, Canadian Association of Radiologists Journal, 2023. https://pubmed.ncbi.nlm.nih.gov/36062579/ — Methodology: 453 articles, 4 journals, 24 countries; gender inferred. Tier 2.
7. *Authorship gender trends in AI breast-imaging research*, European Journal of Radiology, 2024. https://pubmed.ncbi.nlm.nih.gov/38492508/ — Methodology: 115 AI breast-imaging articles; gender by self-declaration survey; search to July 2022. Tier 2.
8. Seyyed-Kalantari et al., *Underdiagnosis bias of artificial intelligence algorithms applied to chest radiographs in under-served patient populations*, Nature Medicine, 2021. https://www.nature.com/articles/s41591-021-01595-0 — Methodology: 3 large + 1 multi-source chest-X-ray datasets; deep-learning classifiers. Tier 1. `[dated]`
9. *Participation of Women in Clinical Trials Supporting FDA Approval of Cardiovascular Drugs*, JACC, 2018. https://www.jacc.org/doi/10.1016/j.jacc.2018.02.070 — Methodology: 36 approvals, n=224,417 participants. Tier 1. `[dated]`
10. *Women's Participation in Cardiovascular Clinical Trials 2010–2017*, Circulation, 2020. https://www.ahajournals.org/doi/10.1161/CIRCULATIONAHA.119.043594 — Methodology: 740 trials, 862,652 adults; participation-to-prevalence ratios. Tier 1. `[dated]`
11. Rock Health, *Women in Focus: understanding women as digital-health consumers*, 2024. https://rockhealth.com/insights/women-in-focus-understanding-women-as-digital-health-consumers/ — Methodology: US digital-health VC deals; "women+ health" = solutions addressing women's health. Tier 3.
12. PitchBook, *2024 US All In: Female Founders in the VC Ecosystem*, 2024. https://pitchbook.com/news/reports/2024-us-all-in-female-founders-in-the-vc-ecosystem — Methodology: all US VC; founding-team gender classification. Tier 3.
13. Pharma's Almanac, *Breaking the Biopharma Glass Ceiling: Why Female Leadership Still Lags*, 2025. https://www.pharmasalmanac.com/articles/breaking-the-biopharma-glass-ceiling-why-female-leadership-still-lags — Methodology: biopharma C-suite analysis. Tier 3.
14. Medical Design & Outsourcing, *Diversity in medtech: just 21% of executive roles are held by women*, 2022. https://www.medicaldesignandoutsourcing.com/diversity-in-medtech-just-21-of-executives-roles-are-held-by-women/ — Methodology: medtech company survey; US-centric. Tier 3. `[dated]`
15. NSF NCSES, *Women in Business R&D (NSF 23-328)*, 2020 data. https://ncses.nsf.gov/pubs/nsf23328 — Methodology: US Business R&D and Innovation Survey (BRDIS); national. Tier 1. `[dated]`
16. *Female Global Scholars Program — mixed-methods evaluation*, 2024. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11132512/ — Methodology: cohort evaluation; research-productivity outcomes. Tier 2.
17. *CRA-W Grad Cohort Workshop evaluation*, 2017. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5222789/ — Methodology: longitudinal evaluation of women in computing graduate programs. Tier 2.

## Methodology notes for this report

This is the first report in the **featured Women & AI in healthcare R&D track (H1)**; it overrides the standard ISO-week rotation (Week 8). Because no source measures the health-AI intersection directly, every workforce figure here is a proxy assembled from adjacent populations — flagged accordingly. Two reliability caveats carried from the evidence gathering: (1) the "female authorship halves when AI is the focus" observation is tagged `[contested]` because the non-AI comparison figure could not be verified against the primary PDF (the AI-paper shares themselves are PubMed-confirmed); (2) several seminal bias and trial-participation figures are pre-2023 (`[dated]`) and have not been refreshed — their vintage is noted, not hidden. Follow-up to chase next week (H2): whether any 2025–2026 study has quantified sex-disaggregated performance of a deployed clinical AI model.

---

*Filed by WAI-Research. Reviewed by WAI-Test before release. See `brain/methodology.md` for definitions and `brain/sources.md` for the running source list.*
