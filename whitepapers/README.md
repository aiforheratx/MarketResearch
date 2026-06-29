# White papers — WAI-Research

Presentation-quality versions of each weekly report, formatted as scholarly white papers with inline charts, statistic callouts, and a print-to-PDF stylesheet. Open any `.html` file in a browser; use **Print → Save as PDF** to export a paginated A4 PDF for sharing or print.

These complement (do not replace) the markdown reports in `../reports/`. Same evidence, presentation-ready format.

## Index

| Week | Date | Title | Markdown | White paper |
|---|---|---|---|---|
| 1 | 2026-05-11 | State of women in AI: representation across the workforce | [md](../reports/2026-05-11_workforce-representation.md) | [white paper](./2026-05-11_workforce-representation.html) |
| 2 | 2026-05-18 | The pipeline: women in undergraduate CS and AI programs | [md](../reports/2026-05-18_undergraduate-pipeline.md) | [white paper](./2026-05-18_undergraduate-pipeline.html) |
| 3 | 2026-05-25 | Graduate school: women in AI/ML PhD programs | [md](../reports/2026-05-25_phd-programs.md) | [white paper](./2026-05-25_phd-programs.html) |
| 4 | 2026-06-01 | Entry-level AI roles: first job in AI/ML | [md](../reports/2026-06-01_entry-level-roles.md) | [white paper](./2026-06-01_entry-level-roles.html) |
| 5 | 2026-06-08 | The pay gap in AI and machine learning roles | [md](../reports/2026-06-08_pay-gap.md) | [white paper](./2026-06-08_pay-gap.html) |
| 6 | 2026-06-15 | The broken rung: promotion from IC to first management | [md](../reports/2026-06-15_broken-rung.md) | [white paper](./2026-06-15_broken-rung.html) |
| 8 ⭐ | 2026-06-29 | Women & AI in healthcare R&D: the state of representation | [md](../reports/2026-06-29_healthcare-rnd.md) | [white paper](./2026-06-29_healthcare-rnd.html) |

## Style

- **Typography**: Charter / Iowan Old Style serif for headlines (academic), Inter for body.
- **Color**: Muted violet accent (`#6f3aa0`) on cream paper (`#fdfdfb`).
- **Layout**: Single-column, US Letter / A4 width, generous margins.
- **Charts**: Hand-coded inline SVG — no external dependencies, no scripts, no fonts loaded from CDN. Works offline. Prints crisply at any zoom.
- **Print CSS**: A4 page size with 1.6 cm margins; all background colors retained; URLs preserved as link text.

## Export to PDF

In any browser: **File → Print → Save as PDF**. The print stylesheet is tuned for A4. Each section page-breaks cleanly.

## Adding a new white paper (manual)

Copy `_template.html` to `YYYY-MM-DD_<slug>.html`, fill in the placeholders. The shared style lives at `_assets/style.css`.

## Adding a new white paper (agent)

The weekly run produces both the markdown report (under `../reports/`) and the white-paper HTML (here). See `../brain/instructions.md` Step 5.
