#!/usr/bin/env python3
"""
WAI-Research — Agent Operations Dashboard (Streamlit app).

A live application (not a static HTML file) that reads the repo's real data —
the WAI-Test scorecard, report files, metrics — and renders the agent pipeline,
the test-agent review, the Monday 09:00 CST schedule, and the report topics in an
electric-blue Medtronic theme.

Run from the app/ folder:
    python3 -m streamlit run dashboard.py
or use:  ./run.sh
"""
import datetime
import json
from pathlib import Path

import plotly.graph_objects as go
import streamlit as st

ROOT = Path(__file__).resolve().parent.parent
RESULTS = ROOT / "test" / "results"
REPORTS = ROOT / "reports"

# ----- palette (electric blue / Medtronic) -----
NAVY = "#100a45"
BLUE = "#0a6bff"
BLUE_D = "#0048d6"
CYAN = "#00b6f0"
GOOD = "#0bb07b"
WARN = "#e69414"
BAD = "#e5484d"
INK = "#16233a"
MUTED = "#5b6b88"

st.set_page_config(page_title="WAI-Research · Agent Operations",
                   page_icon="💙", layout="wide", initial_sidebar_state="collapsed")

# ----- global CSS -----
st.markdown(f"""
<style>
  .stApp {{ background:
     radial-gradient(1100px 540px at 82% -8%, #e7f1ff 0%, rgba(231,241,255,0) 60%),
     radial-gradient(820px 460px at -8% 0%, #eafaff 0%, rgba(234,250,255,0) 55%), #f4f8ff; }}
  .block-container {{ padding-top: 1.4rem; max-width: 1280px; }}
  #MainMenu, footer, header[data-testid="stHeader"] {{ visibility: hidden; }}
  .hero {{ background:linear-gradient(120deg,{NAVY} 0%,#1d1466 45%,{BLUE_D} 125%);
     color:#fff;border-radius:22px;padding:26px 30px;position:relative;overflow:hidden;
     box-shadow:0 12px 40px rgba(10,107,255,.18);margin-bottom:6px; }}
  .hero h1 {{ font-size:27px;margin:6px 0 6px;font-weight:800;line-height:1.12;color:#fff; }}
  .hero .eyebrow {{ font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:#9fc2ff;font-weight:800; }}
  .hero p {{ color:#cfe0ff;font-size:14px;margin:0;max-width:760px; }}
  .hero .edition {{ position:absolute;top:24px;right:28px;background:rgba(255,255,255,.14);
     border:1px solid rgba(255,255,255,.25);color:#eaf2ff;font-size:11px;font-weight:700;
     padding:5px 12px;border-radius:999px; }}
  .card {{ background:#fff;border:1px solid #dce7fb;border-radius:16px;padding:16px 18px;
     box-shadow:0 1px 2px rgba(16,40,90,.04),0 8px 24px rgba(16,40,90,.06);height:100%; }}
  .kpi .k {{ font-size:11px;text-transform:uppercase;letter-spacing:.07em;color:#8a98b4;font-weight:800; }}
  .kpi .v {{ font-size:25px;font-weight:800;color:{NAVY};line-height:1.1;margin-top:3px; }}
  .kpi .s {{ font-size:12px;color:{MUTED};margin-top:2px; }}
  .stage .num {{ display:inline-flex;width:24px;height:24px;border-radius:50%;background:{BLUE};color:#fff;
     font-size:12px;font-weight:800;align-items:center;justify-content:center;margin-bottom:8px; }}
  .stage .who {{ font-size:10.5px;font-weight:800;color:{BLUE};text-transform:uppercase;letter-spacing:.05em; }}
  .stage h4 {{ margin:2px 0 6px;font-size:14px;color:{NAVY};font-weight:800; }}
  .stage p {{ font-size:12px;color:{MUTED};margin:0 0 8px; }}
  .stage .last {{ font-size:11px;color:#8a98b4;border-top:1px dashed #dce7fb;padding-top:7px; }}
  .pill {{ display:inline-block;font-size:11px;font-weight:800;padding:3px 11px;border-radius:999px; }}
  .pill.ship {{ background:#e4faf2;color:#06794f; }}
  .pill.hold {{ background:#fdecec;color:#b42318; }}
  .pill.blue {{ background:#e8f1ff;color:{BLUE_D}; }}
  .chip {{ display:inline-flex;align-items:center;gap:7px;background:#e8f1ff;border:1px solid #dbe9ff;
     color:{NAVY};border-radius:999px;padding:6px 12px;font-size:12.5px;font-weight:600;margin:4px 6px 0 0; }}
  .chip .av {{ width:20px;height:20px;border-radius:50%;background:{BLUE};color:#fff;font-size:10px;
     font-weight:800;display:inline-flex;align-items:center;justify-content:center; }}
  .topic {{ display:flex;align-items:center;gap:11px;background:#fff;border:1px solid #dce7fb;border-radius:12px;
     padding:10px 13px;margin-bottom:7px; }}
  .topic.active {{ border-color:{BLUE};box-shadow:0 0 0 2px rgba(10,107,255,.15); background:linear-gradient(180deg,#f3f8ff,#fff); }}
  .topic .code {{ font-weight:800;font-size:11.5px;color:#fff;background:{BLUE};border-radius:8px;padding:4px 8px;min-width:32px;text-align:center; }}
  .topic.done .code {{ background:{GOOD}; }} .topic.active .code {{ background:{NAVY}; }}
  .topic .t {{ font-size:13px;font-weight:700;color:{NAVY}; }}
  .topic .l {{ font-size:11px;color:{MUTED}; }}
  .topic .st {{ margin-left:auto;font-size:10.5px;font-weight:800;padding:3px 9px;border-radius:999px; }}
  .st-done {{ background:#e4faf2;color:#06794f; }} .st-now {{ background:#e8f1ff;color:{BLUE_D}; }}
  .st-next {{ background:#fff5e2;color:#9a6406; }} .st-queue {{ background:#eef2f9;color:{MUTED}; }}
  .sec {{ font-size:18px;font-weight:800;color:{NAVY};margin:18px 0 4px; }}
  .secsub {{ font-size:12.5px;color:{MUTED};margin:0 0 12px; }}
  .big-stat {{ background:linear-gradient(135deg,{NAVY},{BLUE_D});color:#fff;border-radius:16px;padding:20px;text-align:center; }}
  .big-stat .n {{ font-size:42px;font-weight:800;line-height:1; }}
  .big-stat .c {{ font-size:12px;color:#cfe0ff;margin-top:8px; }}
</style>
""", unsafe_allow_html=True)


# ----- load live data -----
def load_latest():
    f = RESULTS / "latest.json"
    if f.exists():
        return json.loads(f.read_text())
    return None


report_count = len([p for p in REPORTS.glob("*.md") if p.name != "_template.md"]) if REPORTS.exists() else 0
latest = load_latest()


def next_monday_9am():
    today = datetime.date.today()
    days = (7 - today.weekday()) % 7  # Monday=0
    if days == 0:
        days = 7
    return today + datetime.timedelta(days=days)


nm = next_monday_9am()

# ===== HERO =====
st.markdown(f"""
<div class="hero">
  <span class="edition">💙 Medtronic R&amp;D edition</span>
  <div class="eyebrow">Women and AI · Agent Operations Dashboard</div>
  <h1>How the agent researches, writes, tests &amp; ships the weekly report</h1>
  <p>Live view of the autonomous pipeline — focused on <b>women &amp; AI in healthcare R&amp;D</b>.
  Every Monday 09:00 CST it picks a topic, gathers cited statistics, drafts the report,
  runs an independent QA review, and emails the Medtronic team.</p>
</div>
""", unsafe_allow_html=True)

# ===== KPI ROW =====
verdict = latest["verdict"] if latest else "—"
overall = f"{latest['overall_pct']}%" if latest else "—"
k1, k2, k3, k4 = st.columns(4)
with k1:
    st.markdown(f'<div class="card kpi"><div class="k">Next scheduled run</div>'
                f'<div class="v">{nm.strftime("%a %b %-d")}</div>'
                f'<div class="s">09:00 CST · America/Chicago</div></div>', unsafe_allow_html=True)
with k2:
    st.markdown(f'<div class="card kpi"><div class="k">Reports filed</div>'
                f'<div class="v">{report_count}</div><div class="s">live count from /reports</div></div>',
                unsafe_allow_html=True)
with k3:
    pill = "ship" if verdict == "SHIP" else "hold"
    st.markdown(f'<div class="card kpi"><div class="k">Latest QA verdict</div>'
                f'<div class="v"><span class="pill {pill}">{verdict}</span> {overall}</div>'
                f'<div class="s">WAI-Test · {latest["fails"] if latest else 0} fail / {latest["warns"] if latest else 0} warn</div></div>',
                unsafe_allow_html=True)
with k4:
    st.markdown('<div class="card kpi"><div class="k">Featured track</div>'
                '<div class="v" style="font-size:18px">Healthcare R&amp;D</div>'
                '<div class="s">7-topic priority queue</div></div>', unsafe_allow_html=True)

# ===== PIPELINE =====
st.markdown('<div class="sec">The report pipeline</div>'
            '<div class="secsub">Four agents/stages, every Monday — left to right.</div>', unsafe_allow_html=True)
stages = [
    ("1", "Research Agent", "Pick topic &amp; gather evidence",
     "Reads the brain, selects the topic (featured track first), fans out web searches for cited statistics.",
     f"Last: {latest['source_count'] if latest else '—'} sources, {latest['stat_rows'] if latest else '—'} statistics"),
    ("2", "Report Writer", "Draft report + white paper",
     "Writes the 1,500–3,500-word markdown report and a white paper with inline SVG charts.",
     f"Last: {latest['word_count'] if latest else '—'} words · md + HTML + Word"),
    ("3", "WAI-Test agent", "Review: format · content · data",
     "Scores the report against 18 checks across three dimensions. Never edits — it gates.",
     f"Last: {verdict} · {overall}"),
    ("4", "Scheduler &amp; email", "Send Mon 09:00 CST",
     "On a passing review, emails the Word + white-paper files to the Medtronic list, then logs the run.",
     "To: 3 Medtronic recipients · .docx + .html"),
]
pcols = st.columns(4)
for col, (n, who, h, p, last) in zip(pcols, stages):
    with col:
        st.markdown(f'<div class="card stage"><span class="num">{n}</span>'
                    f'<div class="who">{who}</div><h4>{h}</h4><p>{p}</p>'
                    f'<div class="last"><b>{last}</b></div></div>', unsafe_allow_html=True)

# ===== TEST AGENT + SCHEDULER =====
left, right = st.columns([1.15, 0.85])

with left:
    st.markdown('<div class="sec">WAI-Test review</div>'
                '<div class="secsub">How the test agent checks the latest report — three dimensions, 18 checks. '
                'Live from <code>test/results/latest.json</code>.</div>', unsafe_allow_html=True)
    if latest:
        st.markdown(f'**{latest["report"]}** &nbsp; <span class="pill {"ship" if verdict=="SHIP" else "hold"}">{verdict} · {overall}</span>',
                    unsafe_allow_html=True)
        g1, g2, g3 = st.columns(3)
        for col, dim in zip((g1, g2, g3), ("format", "content", "data")):
            d = latest["dimensions"][dim]
            color = GOOD if d["failed"] == 0 and d["warned"] == 0 else (WARN if d["failed"] == 0 else BAD)
            fig = go.Figure(go.Indicator(
                mode="gauge+number", value=d["pct"], number={"suffix": "%", "font": {"size": 26, "color": NAVY}},
                gauge={"axis": {"range": [0, 100], "tickwidth": 0, "tickcolor": "#dce7fb"},
                       "bar": {"color": color, "thickness": 0.32},
                       "bgcolor": "#eef4ff", "borderwidth": 0,
                       "steps": [{"range": [0, 100], "color": "#eef4ff"}]},
                domain={"x": [0, 1], "y": [0, 1]}))
            fig.update_layout(height=150, margin=dict(l=10, r=10, t=18, b=0),
                              paper_bgcolor="rgba(0,0,0,0)",
                              title={"text": f"<b>{dim.title()}</b>", "y": 0.97, "x": 0.5,
                                     "font": {"size": 13, "color": NAVY}})
            col.plotly_chart(fig, width="stretch", config={"displayModeBar": False})
            col.markdown(f'<div style="text-align:center;font-size:11px;color:{MUTED};margin-top:-14px">'
                         f'{d["passed"]}/{d["total"]} pass · {d["warned"]} warn · {d["failed"]} fail</div>',
                         unsafe_allow_html=True)

        with st.expander("See all 18 checks", expanded=False):
            icon = {"PASS": "✅", "WARN": "🟡", "FAIL": "❌"}
            rows = [{"": icon.get(c["status"], "•"), "ID": c["id"], "Check": c["name"],
                     "Dim": c["dimension"], "Detail": c["detail"]} for c in latest["checks"]]
            st.dataframe(rows, hide_index=True, width="stretch")
    else:
        st.info("No review found yet. Run `python3 scripts/test_agent.py` to generate test/results/latest.json.")

    # representation chart
    st.markdown('<div class="sec">Latest finding — women\'s share by layer of health-AI R&amp;D</div>'
                '<div class="secsub">Every layer falls short of parity (50%); the bench is thinnest.</div>',
                unsafe_allow_html=True)
    layers = ["AI researchers", "Engineering/tech R&D", "Biopharma CTOs", "AI faculty",
              "Medtech executives", "AI radiology 1st authors", "AI breast-imaging 1st authors"]
    vals = [12, 12, 14, 16, 21, 22.3, 35.7]
    colors = [BAD if v < 20 else (WARN if v < 30 else BLUE) for v in vals]
    bar = go.Figure(go.Bar(x=vals, y=layers, orientation="h",
                           marker_color=colors, text=[f"{v}%" for v in vals],
                           textposition="outside", textfont={"color": NAVY, "size": 12}))
    bar.add_vline(x=50, line_dash="dash", line_color="#b9c8e6",
                  annotation_text="parity 50%", annotation_font_color=MUTED)
    bar.update_layout(height=300, margin=dict(l=10, r=30, t=6, b=6),
                      paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                      xaxis=dict(range=[0, 60], showgrid=True, gridcolor="#e9f0fb", color=MUTED),
                      yaxis=dict(autorange="reversed", color=INK))
    st.plotly_chart(bar, width="stretch", config={"displayModeBar": False})

with right:
    st.markdown('<div class="sec">Scheduler</div>'
                '<div class="secsub">Weekly cadence. Emails go only after WAI-Test passes.</div>',
                unsafe_allow_html=True)
    st.markdown(f"""<div class="card">
      <div style="font-size:13px;color:{INK};padding:5px 0;border-bottom:1px solid #eef3fc"><b>Every Monday, 09:00 CST</b></div>
      <div style="font-size:13px;padding:5px 0;border-bottom:1px solid #eef3fc">Cron <code>0 9 * * 1</code> · America/Chicago</div>
      <div style="font-size:13px;padding:5px 0;border-bottom:1px solid #eef3fc">Next run: <b>{nm.strftime('%A, %b %-d %Y')} · 09:00</b></div>
      <div style="font-size:13px;padding:5px 0">Attaches: Word (.docx) + white paper (.html)</div>
      <div style="font-size:11px;color:{MUTED};margin:12px 0 6px;font-weight:800;text-transform:uppercase;letter-spacing:.06em">Distribution list</div>
      <span class="chip"><span class="av">M</span>mugdha.v.tasgaonkar@medtronic.com</span>
      <span class="chip"><span class="av">S</span>sue.delfidio@medtronic.com</span>
      <span class="chip"><span class="av">T</span>tyler.w.stigen@medtronic.com</span>
      <span class="chip"><span class="av">K</span>marilise.kassouf1@medtronic.com</span>
      <div style="margin-top:14px;background:#f4f8ff;border:1px solid #dce7fb;border-radius:12px;padding:11px 13px;font-size:12px;color:{MUTED}">
        <b style="color:{NAVY}">Gate:</b> if WAI-Test returns <span class="pill hold">HOLD</span>, the email is withheld until the flagged checks are fixed.
      </div>
    </div>""", unsafe_allow_html=True)

    st.markdown('<div class="sec">Latest report</div>', unsafe_allow_html=True)
    st.markdown(f"""<div class="card">
      <div class="big-stat"><div class="n">12%</div><div class="c">of AI researchers are women — 16% of AI faculty (UNESCO 2024)</div></div>
      <ul style="font-size:12.5px;color:{INK};margin:12px 0 0;padding-left:18px">
        <li>Minority at <b>every layer</b> of health-AI R&amp;D.</li>
        <li>Medical-AI authorship stays <b>under 40%</b>.</li>
        <li>Bias is <b>encoded</b>: chest-X-ray AI underdiagnoses women.</li>
        <li>Capital lags: ~1–2% of US VC to all-female teams.</li>
      </ul>
    </div>""", unsafe_allow_html=True)

# ===== TOPICS =====
st.markdown('<div class="sec">Topics for report generation</div>'
            '<div class="secsub">Featured Healthcare R&amp;D track runs first; the standard rotation fills the gaps.</div>',
            unsafe_allow_html=True)
tcol1, tcol2 = st.columns(2)

featured = [
    ("H1", "State of representation in health-AI R&D", "Workforce · authorship · leadership", "done", "Filed · Wk 8"),
    ("H2", "Gender bias inside medical AI", "Male-skewed training data, trial gaps", "active", "Up next"),
    ("H3", "Women in medical-device & diagnostics AI", "Medtech engineering & research", "", "Queued"),
    ("H4", "Women and AI drug discovery & comp. biology", "Biotech / pharma AI", "", "Queued"),
    ("H5", "Women founders in health-AI & femtech", "VC deal & dollar share", "", "Queued"),
    ("H6", "Women leading clinical AI deployment", "Who decides what reaches the bedside", "", "Queued"),
    ("H7", "What works: moving women into health-AI", "Interventions with measured outcomes", "", "Queued"),
]
rotation = [
    ("W7", "Women and AI research: paper authorship", "NeurIPS, ICML, ICLR, ACL", "Rotation"),
    ("W9", "Women and AI leadership at large tech firms", "C-suite, VP, director", "Rotation"),
    ("W10", "Women and AI ethics, governance & policy", "Over/under-representation", "Rotation"),
    ("W11", "Intersectional view: Black women in AI", "Representation, funding, citations", "Rotation"),
]
done = [("W1", "Workforce representation"), ("W2", "Undergraduate pipeline"), ("W3", "PhD programs"),
        ("W4", "Entry-level AI roles"), ("W5", "Pay gap in AI/ML"), ("W6", "The broken rung")]

with tcol1:
    st.markdown(f'<div style="font-size:12px;font-weight:800;color:{BLUE_D};text-transform:uppercase;'
                'letter-spacing:.05em;margin-bottom:8px">⭐ Featured — Women &amp; AI in healthcare R&amp;D</div>',
                unsafe_allow_html=True)
    stmap = {"done": "st-done", "active": "st-now", "": "st-queue"}
    for code, t, l, cls, badge in featured:
        bcls = "st-done" if cls == "done" else ("st-next" if cls == "active" else "st-queue")
        st.markdown(f'<div class="topic {cls}"><span class="code">{code}</span>'
                    f'<div><div class="t">{t}</div><div class="l">{l}</div></div>'
                    f'<span class="st {bcls}">{badge}</span></div>', unsafe_allow_html=True)

with tcol2:
    st.markdown(f'<div style="font-size:12px;font-weight:800;color:{MUTED};text-transform:uppercase;'
                'letter-spacing:.05em;margin-bottom:8px">Standard rotation — next up</div>', unsafe_allow_html=True)
    for code, t, l, badge in rotation:
        st.markdown(f'<div class="topic"><span class="code">{code}</span>'
                    f'<div><div class="t">{t}</div><div class="l">{l}</div></div>'
                    f'<span class="st st-queue">{badge}</span></div>', unsafe_allow_html=True)
    st.markdown(f'<div style="font-size:12px;font-weight:800;color:{GOOD};text-transform:uppercase;'
                'letter-spacing:.05em;margin:14px 0 8px">Already covered</div>', unsafe_allow_html=True)
    for code, t in done:
        st.markdown(f'<div class="topic done"><span class="code">{code}</span>'
                    f'<div><div class="t">{t}</div></div>'
                    f'<span class="st st-done">Done</span></div>', unsafe_allow_html=True)

st.markdown(f'<div style="margin-top:26px;color:#8a98b4;font-size:11.5px">WAI-Research · Agent Operations '
            f'Dashboard (Streamlit app) · Medtronic R&amp;D edition · data read live from the repository · '
            f'rendered {datetime.date.today().isoformat()}</div>', unsafe_allow_html=True)
