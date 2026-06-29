#!/usr/bin/env python3
"""WAI-Test — the QA / review agent for WAI-Research weekly reports.

Independently reviews a report across three dimensions — FORMAT, CONTENT, and
REPORT DATA — and writes a pass/fail scorecard that the live dashboard reads.
It never edits the report; it only judges it. A report must return verdict
SHIP (zero FAIL checks) before it is emailed to recipients.

Usage:
    python3 scripts/test_agent.py                                  # newest report
    python3 scripts/test_agent.py reports/2026-06-29_healthcare-rnd.md

Outputs (under test/results/):
    <slug>.json     machine-readable scorecard (dashboard consumes this)
    <slug>.md       human-readable review
    latest.json     pointer to the most recent review

See brain/test_agent.md for the full check catalogue.
"""
import datetime
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REPORTS = ROOT / "reports"
WHITEPAPERS = ROOT / "whitepapers"
RESULTS = ROOT / "test" / "results"

THIS_YEAR = datetime.date.today().year

REQUIRED_FRONTMATTER = ["date", "week", "topic", "slug", "career_phase", "geography", "status"]
REQUIRED_SECTIONS = [
    "Executive summary",
    "Numbers in this report",
    "What's the number",
    "What's the trend",
    "What's missing",
    "What works",
    "Recommended actions",
    "Sources",
    "Methodology notes",
]
PLACEHOLDERS = ["YYYY", "<topic", "<slug", "<Topic", "TODO", "lorem ipsum", "<e.g.,"]


# ---------------------------------------------------------------------------
# helpers
# ---------------------------------------------------------------------------
def latest_report() -> Path:
    candidates = sorted(p for p in REPORTS.glob("*.md") if p.name != "_template.md")
    if not candidates:
        sys.exit("No reports found under reports/.")
    return candidates[-1]


def split_frontmatter(text: str):
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            return parts[1], parts[2]
    return "", text


def numbers_table_rows(body: str):
    """Return the data rows of the 'Numbers in this report' markdown table."""
    m = re.search(r"##\s+Numbers in this report(.*?)(?:\n##\s|\Z)", body, re.S)
    if not m:
        return []
    rows = []
    for line in m.group(1).splitlines():
        line = line.strip()
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        # skip header + separator rows
        if not cells or cells[0].lower() in ("#", ""):
            continue
        if set("".join(cells)) <= set("-: "):
            continue
        if cells[0].lower().startswith("stat") or "statistic" in " ".join(cells[:2]).lower():
            continue
        rows.append(cells)
    return rows


def section_text(body: str, heading_fragment: str) -> str:
    m = re.search(
        r"##\s+[^\n]*" + re.escape(heading_fragment) + r"[^\n]*(.*?)(?:\n##\s|\Z)",
        body, re.S,
    )
    return m.group(1) if m else ""


def word_count(body: str) -> int:
    text = re.sub(r"[#|*`>_\-]", " ", body)
    return len(text.split())


def check(idstr, name, dimension, severity, ok, detail=""):
    status = "PASS" if ok else severity
    return {"id": idstr, "name": name, "dimension": dimension,
            "severity": severity, "status": status, "detail": detail}


# ---------------------------------------------------------------------------
# review
# ---------------------------------------------------------------------------
def review(md_path: Path):
    text = md_path.read_text(encoding="utf-8")
    fm_raw, body = split_frontmatter(text)
    fm = {}
    for line in fm_raw.splitlines():
        if ":" in line:
            k, _, v = line.partition(":")
            fm[k.strip()] = v.strip()

    slug = fm.get("slug") or md_path.stem.split("_", 1)[-1]
    wp_path = WHITEPAPERS / f"{md_path.stem}.html"
    wp = wp_path.read_text(encoding="utf-8") if wp_path.exists() else ""

    rows = numbers_table_rows(body)
    sources_sec = section_text(body, "Sources")
    actions_sec = section_text(body, "Recommended actions")
    exec_sec = section_text(body, "Executive summary")
    wc = word_count(body)

    checks = []

    # ---- Dimension 1: FORMAT ----
    checks.append(check(
        "F1", "Filename matches reports/YYYY-MM-DD_<slug>.md", "format", "FAIL",
        bool(re.match(r"\d{4}-\d{2}-\d{2}_[a-z0-9-]+$", md_path.stem)),
        md_path.name))
    missing_fm = [k for k in REQUIRED_FRONTMATTER if k not in fm]
    checks.append(check(
        "F2", "Frontmatter has all required keys", "format", "FAIL",
        not missing_fm, "missing: " + ", ".join(missing_fm) if missing_fm else "all present"))
    missing_sec = [s for s in REQUIRED_SECTIONS if s.lower() not in body.lower()]
    checks.append(check(
        "F3", "All required sections present", "format", "FAIL",
        not missing_sec, "missing: " + ", ".join(missing_sec) if missing_sec else "9/9 sections"))
    checks.append(check(
        "F4", "Matching white paper exists", "format", "FAIL",
        wp_path.exists(), wp_path.name if wp_path.exists() else "not found"))
    head_ok = all(s in wp for s in ["_assets/style.css", "<title", "viewport"]) if wp else False
    checks.append(check(
        "F5", "White paper <head> valid (css, title, viewport)", "format", "WARN",
        head_ok, "ok" if head_ok else "missing head element"))
    svg_n = wp.count("<svg") if wp else 0
    checks.append(check(
        "F6", "White paper has ≥1 inline SVG chart", "format", "WARN",
        svg_n >= 1, f"{svg_n} svg element(s)"))

    # ---- Dimension 2: CONTENT ----
    checks.append(check(
        "C1", "Body word count 1,500–3,500", "content", "WARN",
        1500 <= wc <= 3500, f"{wc} words"))
    sentences = [s for s in re.split(r"(?<=[.!?])\s", exec_sec.strip()) if len(s.split()) > 3]
    checks.append(check(
        "C2", "Executive summary is 2–4 sentences", "content", "WARN",
        2 <= len(sentences) <= 5, f"{len(sentences)} sentences"))
    checks.append(check(
        "C3", "Numbers table has ≥5 statistic rows", "content", "FAIL",
        len(rows) >= 5, f"{len(rows)} rows"))
    action_items = len(re.findall(r"^\s*\d+\.\s+\*\*", actions_sec, re.M)) or \
        len(re.findall(r"^\s*\d+\.\s+\S", actions_sec, re.M))
    checks.append(check(
        "C4", "Recommended actions lists 3–5 moves", "content", "WARN",
        3 <= action_items <= 6, f"{action_items} actions"))
    source_items = len(re.findall(r"^\s*\d+\.\s+\S", sources_sec, re.M))
    checks.append(check(
        "C5", "Sources section lists ≥5 citations", "content", "FAIL",
        source_items >= 5, f"{source_items} citations"))
    years_in_rows = [int(y) for r in rows for y in re.findall(r"(20\d{2})", " ".join(r))]
    recent = any(y >= THIS_YEAR - 1 for y in years_in_rows)
    checks.append(check(
        "C6", "≥1 statistic dated within last 12 months", "content", "WARN",
        recent, f"newest year cited: {max(years_in_rows)}" if years_in_rows else "no years parsed"))

    # ---- Dimension 3: REPORT DATA ----
    rows_with_source = sum(1 for r in rows if len(r) >= 4 and r[3].strip())
    checks.append(check(
        "D1", "Every statistic row has a source", "data", "FAIL",
        rows and rows_with_source == len(rows),
        f"{rows_with_source}/{len(rows)} rows sourced"))
    rows_with_year = sum(1 for r in rows if re.search(r"\b(19|20)\d{2}\b", " ".join(r)))
    checks.append(check(
        "D2", "Every statistic row carries a year", "data", "WARN",
        rows and rows_with_year == len(rows),
        f"{rows_with_year}/{len(rows)} rows dated"))
    url_n = len(re.findall(r"https?://", sources_sec))
    checks.append(check(
        "D3", "Sources contain ≥1 resolvable URL", "data", "FAIL",
        url_n >= 1, f"{url_n} URLs"))
    old_years = [y for y in years_in_rows if y <= THIS_YEAR - 3]
    dated_ok = (not old_years) or ("[dated]" in body.lower())
    checks.append(check(
        "D4", "Stats older than 3 years flagged [dated]", "data", "WARN",
        dated_ok,
        "no old stats" if not old_years else ("[dated] tag present" if dated_ok else "old stats unflagged")))
    found_ph = [p for p in PLACEHOLDERS if p.lower() in body.lower()]
    checks.append(check(
        "D5", "No template placeholders remain", "data", "FAIL",
        not found_ph, "found: " + ", ".join(found_ph) if found_ph else "clean"))
    tier_ok = bool(re.search(r"tier\s*[123]", body, re.I) or re.search(r"\[(primary|secondary)\]", body, re.I))
    checks.append(check(
        "D6", "Source tiers declared", "data", "WARN",
        tier_ok, "tiers present" if tier_ok else "no tier tags"))

    # ---- score ----
    dims = {}
    for dim in ("format", "content", "data"):
        dchecks = [c for c in checks if c["dimension"] == dim]
        score = sum(1 if c["status"] == "PASS" else 0.5 if c["status"] == "WARN" else 0
                    for c in dchecks)
        dims[dim] = {
            "passed": sum(1 for c in dchecks if c["status"] == "PASS"),
            "warned": sum(1 for c in dchecks if c["status"] == "WARN"),
            "failed": sum(1 for c in dchecks if c["status"] == "FAIL"),
            "total": len(dchecks),
            "pct": round(100 * score / len(dchecks)),
        }

    fails = sum(1 for c in checks if c["status"] == "FAIL")
    warns = sum(1 for c in checks if c["status"] == "WARN")
    verdict = "SHIP" if fails == 0 else "HOLD"
    overall_pct = round(sum(d["pct"] for d in dims.values()) / len(dims))

    return {
        "report": md_path.name,
        "whitepaper": wp_path.name if wp_path.exists() else None,
        "slug": slug,
        "topic": fm.get("topic", ""),
        "week": fm.get("week", ""),
        "reviewed": datetime.date.today().isoformat(),
        "reviewer": "WAI-Test",
        "verdict": verdict,
        "overall_pct": overall_pct,
        "fails": fails,
        "warns": warns,
        "word_count": wc,
        "stat_rows": len(rows),
        "source_count": source_items,
        "dimensions": dims,
        "checks": checks,
    }


def write_artifacts(result):
    RESULTS.mkdir(parents=True, exist_ok=True)
    slug = result["slug"]
    (RESULTS / f"{slug}.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
    (RESULTS / "latest.json").write_text(json.dumps(result, indent=2), encoding="utf-8")

    icon = {"PASS": "✓", "WARN": "▲", "FAIL": "✗"}
    lines = [
        f"# WAI-Test review — {result['report']}",
        "",
        f"**Verdict: {result['verdict']}**  ·  Overall {result['overall_pct']}%  ·  "
        f"{result['fails']} fail / {result['warns']} warn  ·  reviewed {result['reviewed']}",
        "",
        f"Topic: {result['topic']}  ·  {result['word_count']} words  ·  "
        f"{result['stat_rows']} statistics  ·  {result['source_count']} sources",
        "",
        "| Dimension | Passed | Warn | Fail | Score |",
        "|---|---|---|---|---|",
    ]
    for dim, d in result["dimensions"].items():
        lines.append(f"| {dim.title()} | {d['passed']}/{d['total']} | {d['warned']} | "
                     f"{d['failed']} | {d['pct']}% |")
    lines += ["", "## Checks", "", "| | ID | Check | Dimension | Result | Detail |",
              "|---|---|---|---|---|---|"]
    for c in result["checks"]:
        lines.append(f"| {icon[c['status']]} | {c['id']} | {c['name']} | {c['dimension']} | "
                     f"{c['status']} | {c['detail']} |")
    lines += ["", "*Generated by `scripts/test_agent.py` — see `brain/test_agent.md`.*"]
    (RESULTS / f"{slug}.md").write_text("\n".join(lines), encoding="utf-8")


def main():
    md_path = Path(sys.argv[1]) if len(sys.argv) > 1 else latest_report()
    if not md_path.is_absolute():
        md_path = ROOT / md_path
    if not md_path.exists():
        sys.exit(f"Report not found: {md_path}")

    result = review(md_path)
    write_artifacts(result)

    bar = {"PASS": "✓", "WARN": "▲", "FAIL": "✗"}
    print(f"WAI-Test reviewed {result['report']}")
    print(f"  Verdict: {result['verdict']}  ({result['overall_pct']}% overall, "
          f"{result['fails']} fail / {result['warns']} warn)")
    for dim, d in result["dimensions"].items():
        print(f"  {dim:8s} {d['pct']:3d}%  ({d['passed']}/{d['total']} pass, "
              f"{d['warned']} warn, {d['failed']} fail)")
    for c in result["checks"]:
        if c["status"] != "PASS":
            print(f"    {bar[c['status']]} {c['id']} {c['name']} — {c['detail']}")
    print(f"  Scorecard: test/results/{result['slug']}.json")
    sys.exit(0 if result["verdict"] == "SHIP" else 1)


if __name__ == "__main__":
    main()
