#!/usr/bin/env python3
"""Email the weekly WAI Market Research report — short, professional email with the
agent operations dashboard shown inline, and TWO attachments:
  1. the report (clean Word .docx — statistics, references, well formatted)
  2. the agent operations dashboard as a PDF

Sent every Monday at 09:00 America/Chicago (see schedule/cron_config.md), after the
report clears the WAI-Test review. Sent ON BEHALF OF Mugdha Tasgaonkar; this inbox is
managed by the WAI-Research agent for automated market-research report generation.

Recipients (full distribution): mugdha.v.tasgaonkar@, sue.delfidio@, tyler.w.stigen@medtronic.com
A first-run override (EMAIL_TO in scripts/email_credentials.env) can scope it to one address.

Credentials (env or scripts/email_credentials.env):
    GMAIL_USER, GMAIL_APP_PASSWORD, optional EMAIL_TO (comma-separated)

Usage:
    GMAIL_APP_PASSWORD=xxxx python3 scripts/send_report.py
    python3 scripts/send_report.py --dry-run    # show recipients/attachments, send nothing
    python3 scripts/send_report.py --preview     # write + open the HTML email locally, send nothing
"""
import json
import os
import re
import smtplib
import subprocess
import sys
import webbrowser
from email.message import EmailMessage
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REPORTS = ROOT / "reports"
DASH_HTML = ROOT / "docs" / "agent-dashboard.html"
DASH_PNG = ROOT / "docs" / "agent-dashboard.png"
DASH_PDF = ROOT / "docs" / "agent-dashboard.pdf"
LATEST_TEST = ROOT / "test" / "results" / "latest.json"
PREVIEW = ROOT / "scripts" / "last_email_preview.html"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

DEFAULT_RECIPIENTS = [
    "mugdha.v.tasgaonkar@medtronic.com",
    "sue.delfidio@medtronic.com",
    "tyler.w.stigen@medtronic.com",
    "marilise.kassouf1@medtronic.com",
]
SIGNATORY = "Mugdha Tasgaonkar"


def _load_credentials_file():
    creds_path = Path(__file__).resolve().parent / "email_credentials.env"
    if not creds_path.exists():
        return
    for line in creds_path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        os.environ.setdefault(key.strip(), value.strip())


def latest_report_md() -> Path:
    candidates = sorted(p for p in REPORTS.glob("*.md") if p.name != "_template.md")
    if not candidates:
        sys.exit("No reports found under reports/.")
    return candidates[-1]


def parse_report(md_path: Path):
    text = md_path.read_text(encoding="utf-8")
    fm, body = {}, text
    if text.startswith("---"):
        _, fm_raw, body = text.split("---", 2)
        for line in fm_raw.splitlines():
            if ":" in line:
                k, _, v = line.partition(":")
                fm[k.strip()] = v.strip()
    title_m = re.search(r"^#\s+(.+)$", body, re.M)
    title = title_m.group(1).strip() if title_m else fm.get("topic", md_path.stem)
    summary = ""
    sm = re.search(r"##\s+Executive summary\s*(.*?)(?:\n##\s)", body, re.S)
    if sm:
        summary = " ".join(sm.group(1).split())
    return {"date": fm.get("date", md_path.stem.split("_", 1)[0]),
            "week": fm.get("week", "?"), "topic": fm.get("topic", title),
            "title": title, "summary": summary}


def load_test():
    if LATEST_TEST.exists():
        try:
            return json.loads(LATEST_TEST.read_text())
        except Exception:
            return None
    return None


def _chrome(*args, timeout=120):
    if not Path(CHROME).exists():
        return False
    try:
        subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-sandbox", *args],
                       check=True, timeout=timeout,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except Exception:
        return False


def refresh_screenshot():
    """Regenerate docs/agent-dashboard.png from the dashboard HTML (best effort)."""
    if DASH_HTML.exists():
        _chrome("--hide-scrollbars", "--force-device-scale-factor=2",
                "--window-size=1320,3650", f"--screenshot={DASH_PNG}", DASH_HTML.as_uri())
    return DASH_PNG if DASH_PNG.exists() else None


def png_to_pdf(png_path: Path, pdf_path: Path):
    """Convert the dashboard screenshot PNG into a single-page PDF document."""
    if not png_path or not png_path.exists():
        return None
    try:
        from PIL import Image
        Image.open(png_path).convert("RGB").save(pdf_path, "PDF", resolution=150.0)
        return pdf_path if pdf_path.exists() else None
    except Exception:
        return None


def report_to_pdf(html_path: Path, pdf_path: Path):
    """Render the formal report HTML (HBR-style — prose, charts, references) to a clean PDF."""
    if html_path.exists() and _chrome("--no-pdf-header-footer",
                                      f"--print-to-pdf={pdf_path}", html_path.as_uri()):
        return pdf_path if pdf_path.exists() else None
    return None


def ensure_docx(md_path: Path):
    """The report as a clean Word document; build it from the markdown if missing."""
    docx_path = md_path.with_suffix(".docx")
    if not docx_path.exists():
        try:
            subprocess.run([sys.executable, str(ROOT / "scripts" / "md_to_doc.py"),
                            str(md_path), str(docx_path)], check=True,
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except Exception:
            return None
    return docx_path if docx_path.exists() else None


def build_bodies(meta, test):
    """Short, professional email with the dashboard shown inline (cid:dashboard)."""
    qa_line = ""
    qa_html = ""
    if test:
        qa_line = f" The WAI-Test review agent independently validated it (verdict {test['verdict']}, {test['overall_pct']}%)."
        qa_html = f" Independently reviewed by the WAI-Test agent — <b>{test['verdict']} · {test['overall_pct']}%</b>."

    plain = f"""Hello,

This week's Women & AI market research report is attached.

Report:  {meta['title']}
Date:    {meta['date']} (Week {meta['week']})
Topic:   {meta['topic']}

It was prepared autonomously by the WAI-Research agent: the topic was selected, statistics
were gathered from named primary sources (each cited with a year and link), and the report
was drafted.{qa_line}

Summary: {meta['summary']}

Attached:
  1. The report (PDF) — a formal report with charts, statistics and references.
  2. The agent operations dashboard (PDF) — the agent's pipeline, quality review and schedule.
The dashboard is also shown in the body of this email for reference.

Researched, written and reviewed by the WAI-Research agent on behalf of {SIGNATORY}.
This inbox is managed by the agent for automated market-research report generation.

Kind regards,
WAI-Research (on behalf of {SIGNATORY})
"""

    blue, navy, ink, muted = "#0a6bff", "#100a45", "#16233a", "#5b6b88"
    html = f"""<!doctype html><html><body style="margin:0;background:#f4f8ff;
  font-family:-apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif;color:{ink};">
  <div style="max-width:640px;margin:0 auto;padding:22px;">
    <div style="background:linear-gradient(120deg,{navy},{blue});border-radius:14px;padding:18px 22px;color:#fff;">
      <div style="font-size:11px;letter-spacing:.12em;text-transform:uppercase;color:#9fc2ff;font-weight:700;">
        Women &amp; AI · Weekly market research</div>
      <div style="font-size:19px;font-weight:800;margin-top:5px;line-height:1.25;">{meta['title']}</div>
      <div style="font-size:12.5px;color:#cfe0ff;margin-top:5px;">{meta['date']} · Week {meta['week']} · {meta['topic']}</div>
    </div>

    <p style="font-size:14px;line-height:1.6;margin:18px 2px 12px;">Hello,</p>
    <p style="font-size:13.5px;line-height:1.65;margin:0 2px 14px;">
      This week's <b>Women &amp; AI</b> market research report is attached. It was prepared autonomously by the
      WAI-Research agent — topic selected, statistics gathered from named primary sources (each cited with a
      year and link), and the report drafted.{qa_html}</p>

    <div style="font-size:13px;font-weight:800;color:{navy};margin:4px 2px 6px;">Summary</div>
    <p style="font-size:13.5px;line-height:1.7;margin:0 2px 16px;">{meta['summary']}</p>

    <div style="font-size:13px;font-weight:800;color:{navy};margin:8px 2px 8px;">Agent operations dashboard</div>
    <img src="cid:dashboard" alt="WAI-Research agent operations dashboard"
      style="width:100%;border:1px solid #dce7fb;border-radius:12px;display:block;margin:0 2px 6px;"/>
    <div style="font-size:11.5px;color:{muted};margin:0 2px 16px;">Attached as a PDF for reference.</div>

    <div style="font-size:13px;font-weight:800;color:{navy};margin:8px 2px 6px;">Attached</div>
    <ol style="font-size:13.5px;line-height:1.6;margin:0 2px 16px;padding-left:18px;">
      <li>The report (PDF) — a formal report with charts, statistics and references.</li>
      <li>The agent operations dashboard (PDF).</li>
    </ol>

    <p style="font-size:12px;line-height:1.6;color:{muted};border-top:1px solid #dce7fb;padding-top:12px;margin:14px 2px 4px;">
      Researched, written and reviewed by the WAI-Research agent on behalf of <b>{SIGNATORY}</b>.
      This inbox is managed by the agent for automated market-research report generation.</p>
    <p style="font-size:13px;color:{ink};margin:6px 2px 0;">Kind regards,<br>
      <b>WAI-Research</b> <span style="color:{muted};">on behalf of {SIGNATORY}</span></p>
  </div>
</body></html>"""
    return plain, html


def main():
    dry_run = "--dry-run" in sys.argv
    preview = "--preview" in sys.argv
    _load_credentials_file()

    sender = os.environ.get("GMAIL_USER", "mugdha.tasgaonkar@gmail.com")
    app_password = os.environ.get("GMAIL_APP_PASSWORD")
    recipients = [r.strip() for r in os.environ.get("EMAIL_TO", "").split(",") if r.strip()] \
        or DEFAULT_RECIPIENTS

    md_path = latest_report_md()
    meta = parse_report(md_path)
    test = load_test()
    plain, html = build_bodies(meta, test)
    subject = f"WAI Market Research Report — {meta['topic']} — {meta['date']} (Week {meta['week']})"

    # Dashboard: refresh screenshot (inline) and a PDF (attachment).
    png_path = refresh_screenshot()
    dash_pdf = png_to_pdf(png_path, DASH_PDF)

    if preview:
        preview_html = html
        if png_path and png_path.exists():
            preview_html = preview_html.replace('src="cid:dashboard"', f'src="{png_path.as_uri()}"')
        PREVIEW.write_text(preview_html, encoding="utf-8")
        print(f"Preview written: {PREVIEW}")
        print(f"Subject: {subject}\nTo: {', '.join(recipients)}")
        webbrowser.open(PREVIEW.as_uri())
        return

    wp_html = ROOT / "whitepapers" / f"{md_path.stem}.html"
    report_pdf = report_to_pdf(wp_html, REPORTS / f"{md_path.stem}.pdf")
    attachments = []
    if report_pdf:
        attachments.append((report_pdf, "application", "pdf",
                            f"WAI Market Research Report - {meta['date']}.pdf"))
    if dash_pdf:
        attachments.append((dash_pdf, "application", "pdf",
                            f"WAI Agent Dashboard - {meta['date']}.pdf"))

    print(f"Report:     {md_path.name}")
    print(f"From:       {sender}  (on behalf of {SIGNATORY})")
    print(f"To:         {', '.join(recipients)}")
    print(f"Subject:    {subject}")
    print(f"Inline:     dashboard screenshot {'(yes)' if png_path else '(MISSING)'}")
    print(f"Attaching:  {', '.join(n for _, _, _, n in attachments) or '(none)'}")

    if dry_run:
        print("\n--dry-run: no email sent.")
        return
    if not app_password:
        sys.exit("ERROR: set GMAIL_APP_PASSWORD (a Gmail App Password) in the environment.")
    if len(attachments) < 2:
        sys.exit("ERROR: expected 2 attachments (report .pdf + dashboard .pdf); one failed to generate. "
                 "Check that Google Chrome and Pillow are available.")

    msg = EmailMessage()
    msg["From"] = f"{SIGNATORY} via WAI-Research <{sender}>"
    msg["To"] = ", ".join(recipients)
    msg["Subject"] = subject
    msg.set_content(plain)
    msg.add_alternative(html, subtype="html")

    # Embed the dashboard inline in the HTML alternative.
    if png_path and png_path.exists():
        html_part = msg.get_payload()[1]
        html_part.add_related(png_path.read_bytes(), maintype="image", subtype="png", cid="<dashboard>")

    for path, maintype, subtype, display_name in attachments:
        msg.add_attachment(path.read_bytes(), maintype=maintype, subtype=subtype, filename=display_name)

    print(f"\nSending to {len(recipients)} recipient(s) with {len(attachments)} attachment(s)...")
    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.starttls()
        smtp.login(sender, app_password)
        smtp.send_message(msg)
    print("Sent successfully.")


if __name__ == "__main__":
    main()
