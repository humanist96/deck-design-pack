#!/usr/bin/env python3
"""Generate the 10 SVG page prototypes for the `koscom-chevron` deck.

Geometry is authored in the 1280x720 ppt169 canvas the pack uses. Colour and
type values are the ones measured from Koscom's official sample decks
(Black / Blue / Orange, 2026-06-23), re-authored as the pack's SVG grammar.
"""
from pathlib import Path
import math

OUT = Path(__file__).parent / "templates"
OUT.mkdir(parents=True, exist_ok=True)

# ---------------------------------------------------------------- palette
C = dict(
    canvas="#ffffff", surface="#f5f5f7", hairline="#dcdce0", chevron_grey="#ececee",
    orange="#ee6d1d", orange_deep="#f26522", orange_tint="#fad3bb", orange_pale="#fdeee4",
    navy="#00338d", navy_mid="#1f4b9b", navy_soft="#0f499c", blue_tint="#edf4fb",
    black="#000000", wave_dim="#7a3a10", wave_mid="#b85415",
    ink="#2b2b2e", ink2="#6e6e73", grey="#8c8c92", white="#ffffff",
)

# ---------------------------------------------------------------- type
F_BOLD = "'KoPub돋움체 Bold', 'KoPubDotum Bold', Pretendard, 'Malgun Gothic', sans-serif"
F_MED = "'KoPub돋움체 Medium', 'KoPubDotum Medium', Pretendard, 'Malgun Gothic', sans-serif"
F_LIGHT = "'KoPub돋움체 Light', 'KoPubDotum Light', Pretendard, 'Malgun Gothic', sans-serif"

MASTER = 'data-pptx-master="koscom-master" data-pptx-master-name="Koscom Chevron"'


def svg_open(layout_key, layout_name, comment):
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        f'<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="720" viewBox="0 0 1280 720" '
        f'{MASTER} data-pptx-layout="{layout_key}" data-pptx-layout-name="{layout_name}">\n'
        f'  <!-- Koscom Chevron — {comment} -->\n'
    )


def master_bg():
    return (f'  <rect id="master-bg" width="1280" height="720" fill="{C["canvas"]}" '
            'data-pptx-layer="master" data-pptx-editable="false"/>\n')


def layout_rect(id_, x, y, w, h, fill):
    return (f'  <rect id="{id_}" x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" '
            'data-pptx-layer="layout" data-pptx-editable="false"/>\n')


def layout_line(id_, x1, y1, x2, y2, stroke, width=1):
    return (f'  <line id="{id_}" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" '
            f'stroke-width="{width}" data-pptx-layer="layout" data-pptx-editable="false"/>\n')


# Chevron mark: the ">" glyph of the house identity, as pure geometry.
# Unit shape is 565 wide x 760 tall with a 240px arm; scaled by height.
_UNIT = [(0, 0), (240, 0), (565, 380), (240, 760), (0, 760), (295, 380)]


def chevron_points(x, y, h):
    s = h / 760.0
    return " ".join(f"{x + px * s:.0f},{y + py * s:.0f}" for px, py in _UNIT)


def layout_chevron(id_, x, y, h, fill):
    return (f'  <polygon id="{id_}" points="{chevron_points(x, y, h)}" fill="{fill}" '
            'data-pptx-layer="layout" data-pptx-editable="false"/>\n')


def text(x, y, size, family, fill, content, anchor=None, ls=None, extra=""):
    a = f' text-anchor="{anchor}"' if anchor else ""
    l = f' letter-spacing="{ls}"' if ls is not None else ""
    return (f'<text x="{x}" y="{y}"{a} font-family="{family}" font-size="{size}"{l} '
            f'fill="{fill}"{extra}>{content}</text>')


def kicker_bar(x, y, fill=None):
    """The 8x26 vertical bar that precedes every kicker in the house style."""
    return f'<rect x="{x}" y="{y}" width="8" height="26" fill="{fill or C["orange"]}"/>'


def title_slot(bounds, x, y, size, family, fill, token="{{TITLE}}", ls=None, idx=None, name="title"):
    i = f' data-pptx-placeholder-idx="{idx}"' if idx else ""
    l = f' letter-spacing="{ls}"' if ls is not None else ""
    return (
        f'  <g id="{name}-slot" data-pptx-placeholder="{name}"{i} data-pptx-placeholder-bounds="{bounds}">\n'
        f'    <text id="{name}-carrier" data-pptx-placeholder-carrier="true" x="{x}" y="{y}" '
        f'font-family="{family}" font-size="{size}"{l} fill="{fill}">{token}</text>\n'
        '  </g>\n'
    )


def page_foot(color):
    return (
        '  <g id="page-foot">\n'
        f'    {text(80, 674, 14, F_BOLD, color, "{{BRAND_MARK}}")}\n'
        f'    {text(1200, 674, 13, F_MED, color, "{{PAGE_LABEL}}", anchor="end")}\n'
        '  </g>\n'
    )


def num_circle(cx, cy, n, r=12, fill=None, ink=None):
    return (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill or C["orange"]}"/>'
            f'{text(cx, cy + 4.5, 13, F_BOLD, ink or C["white"], str(n), anchor="middle")}')


def body_header(kicker_y=96, title_y=144, lead_y=190, title_w=1120):
    """Kicker / page title / lead used by every light body page."""
    return (
        '  <g id="page-kicker">\n'
        f'    {text(80, kicker_y, 14, F_MED, C["orange"], "{{KICKER}}")}\n'
        '  </g>\n'
        + title_slot(f"80 {title_y - 34} {title_w} 44", 80, title_y, 30, F_BOLD, C["orange"])
        + '  <g id="page-lead">\n'
        f'    {text(80, lead_y, 18, F_MED, C["ink"], "{{LEAD}}")}\n'
        '  </g>\n'
    )


pages = {}

# ================================================================ 01 cover
s = svg_open("01_cover", "Cover", "01 Cover: kicker bar + bold headline + chevron cluster")
s += master_bg()
s += layout_chevron("layout-chevron-grey", 700, 360, 460, C["chevron_grey"])
s += layout_chevron("layout-chevron-pale", 1050, 250, 600, C["orange_pale"])
s += layout_chevron("layout-chevron-orange", 870, -20, 600, C["orange_deep"])
s += ('  <g id="cover-brand">\n'
      f'    {text(80, 118, 28, F_BOLD, C["ink"], "{{BRAND_MARK}}")}\n'
      '  </g>\n')
s += ('  <g id="cover-kicker">\n'
      f'    {kicker_bar(80, 298)}\n'
      f'    {text(100, 318, 15, F_MED, C["orange"], "{{KICKER}}", ls=4)}\n'
      '  </g>\n')
s += title_slot("80 340 700 130", 80, 392, 52, F_BOLD, C["ink"], ls=-0.5)
s += title_slot("80 482 700 34", 80, 508, 18, F_MED, C["ink2"], token="{{SUBTITLE}}", ls=0.5, idx=2, name="subtitle")
s += ('  <g id="cover-meta">\n'
      f'    {text(80, 622, 15, F_MED, C["grey"], "{{META_LINE}}")}\n'
      '  </g>\n')
s += page_foot(C["grey"])
s += "</svg>\n"
pages["01_cover.svg"] = s

# ================================================================ 02 agenda
s = svg_open("02_agenda", "Agenda", "02 Agenda: left title block + 5 numbered rows")
s += master_bg()
s += layout_chevron("layout-chevron-grey", 1080, 430, 420, C["chevron_grey"])
s += layout_line("layout-list-top-rule", 540, 150, 1200, 150, C["ink"], 2)
s += ('  <g id="agenda-kicker">\n'
      f'    {kicker_bar(80, 130)}\n'
      f'    {text(100, 150, 15, F_MED, C["orange"], "{{KICKER}}", ls=4)}\n'
      '  </g>\n')
s += title_slot("80 176 400 70", 80, 232, 48, F_BOLD, C["ink"], ls=-0.5)
s += ('  <g id="agenda-subtitle">\n'
      f'    {text(80, 270, 15, F_MED, C["grey"], "{{SUBTITLE}}")}\n'
      '  </g>\n')
for i in range(5):
    r = 150 + i * 94
    s += (f'  <g id="agenda-item-{i + 1}">\n'
          f'    {text(540, r + 58, 44, F_BOLD, C["orange"], "{{ITEM_%d_NO}}" % (i + 1))}\n'
          f'    {text(660, r + 42, 24, F_BOLD, C["ink"], "{{ITEM_%d_TITLE}}" % (i + 1))}\n'
          f'    {text(660, r + 70, 15, F_MED, C["grey"], "{{ITEM_%d_TAG}}" % (i + 1))}\n'
          f'    <line x1="540" y1="{r + 92}" x2="1200" y2="{r + 92}" stroke="{C["hairline"]}" stroke-width="1"/>\n'
          '  </g>\n')
s += page_foot(C["grey"])
s += "</svg>\n"
pages["02_agenda.svg"] = s

# ================================================================ 03 section
s = svg_open("03_section", "Section", "03 Section: navy counterpanel + chevron cluster")
s += master_bg()
s += layout_rect("layout-bg-navy", 0, 0, 1280, 720, C["navy"])
s += layout_chevron("layout-chevron-back", 1080, -60, 800, C["navy_mid"])
s += layout_chevron("layout-chevron-soft", 880, 210, 400, C["navy_soft"])
s += layout_chevron("layout-chevron-orange", 960, 30, 660, C["orange_deep"])
s += ('  <g id="section-number">\n'
      f'    {text(80, 258, 128, F_BOLD, C["white"], "{{SECTION_NO}}", ls=-2)}\n'
      '  </g>\n')
s += ('  <g id="section-kicker">\n'
      f'    {text(80, 334, 15, F_MED, C["white"], "{{KICKER}}", ls=5)}\n'
      '  </g>\n')
s += title_slot("80 366 760 70", 80, 420, 48, F_BOLD, C["white"], ls=-0.5)
s += ('  <g id="section-lead">\n'
      f'    {text(80, 478, 18, F_MED, C["white"], "{{LEAD}}")}\n'
      '  </g>\n')
s += page_foot(C["blue_tint"])
s += "</svg>\n"
pages["03_section.svg"] = s

# ================================================================ 04 signature: wave statement
s = svg_open("04_wave_statement", "Wave Statement", "04 Signature: black field + orange wave lines")
s += master_bg()
s += layout_rect("layout-bg-black", 0, 0, 1280, 720, C["black"])


def wave_path(phase, amp, base, k=1.0):
    pts = []
    for i in range(0, 1281, 20):
        x = i
        y = base + amp * math.sin(k * x / 140.0 + phase) + 0.45 * amp * math.sin(x / 61.0 + 2 * phase)
        pts.append(f"{x},{y:.1f}")
    return "M " + " L ".join(pts)


waves = []
n = 14
for j in range(n):
    t = j / (n - 1)
    tone = C["wave_dim"] if t < 0.3 else (C["wave_mid"] if t < 0.65 else C["orange"])
    waves.append((wave_path(0.9 + t * 1.6, 44 + 26 * math.sin(t * 3.1), 596 - 90 * t, 1 + 0.25 * t), tone))
for idx, (d, tone) in enumerate(waves, 1):
    s += (f'  <path id="layout-wave-{idx:02d}" d="{d}" fill="none" stroke="{tone}" stroke-width="1" '
          'data-pptx-layer="layout" data-pptx-editable="false"/>\n')
s += ('  <g id="statement-kicker">\n'
      f'    {kicker_bar(80, 196)}\n'
      f'    {text(100, 216, 15, F_MED, C["orange"], "{{KICKER}}", ls=4)}\n'
      '  </g>\n')
s += title_slot("80 240 900 56", 80, 282, 34, F_BOLD, C["white"])
s += ('  <g id="statement-body">\n'
      f'    {text(80, 372, 56, F_BOLD, C["white"], "{{STATEMENT}}", ls=-0.5)}\n'
      f'    {text(80, 418, 18, F_MED, C["grey"], "{{STATEMENT_NOTE}}")}\n'
      '  </g>\n')
s += page_foot(C["grey"])
s += "</svg>\n"
pages["04_wave_statement.svg"] = s

# ================================================================ 05 two column
s = svg_open("05_two_column", "Two Column", "05 Two column: text + numbered points / card stack")
s += master_bg()
s += layout_line("layout-column-divider", 640, 236, 640, 580, C["hairline"])
s += body_header()
s += ('  <g id="column-a">\n'
      f'    {text(80, 246, 16, F_BOLD, C["ink"], "{{COL_A_TITLE}}")}\n'
      f'    <line x1="80" y1="258" x2="600" y2="258" stroke="{C["ink"]}" stroke-width="1"/>\n'
      f'    {text(80, 296, 16, F_MED, C["ink2"], "{{BODY}}")}\n')
for i, y in enumerate((356, 424, 492)):
    s += f'    {num_circle(92, y - 5, i + 1)}\n'
    s += f'    {text(118, y, 16, F_MED, C["ink"], "{{POINT_%d}}" % (i + 1))}\n'
    s += f'    <line x1="80" y1="{y + 24}" x2="600" y2="{y + 24}" stroke="{C["hairline"]}" stroke-width="1"/>\n'
s += '  </g>\n'
s += ('  <g id="column-b">\n'
      f'    {text(680, 246, 16, F_BOLD, C["ink"], "{{COL_B_TITLE}}")}\n'
      f'    <line x1="680" y1="258" x2="1200" y2="258" stroke="{C["ink"]}" stroke-width="1"/>\n')
for i, y in enumerate((280, 384, 488)):
    s += (f'    <rect x="680" y="{y}" width="520" height="88" fill="{C["surface"]}" stroke="{C["hairline"]}" stroke-width="1"/>\n'
          f'    {num_circle(712, y + 44, i + 1)}\n'
          f'    {text(740, y + 38, 17, F_BOLD, C["orange"], "{{CARD_%d_TITLE}}" % (i + 1))}\n'
          f'    {text(740, y + 64, 14, F_MED, C["ink2"], "{{CARD_%d_BODY}}" % (i + 1))}\n')
s += '  </g>\n'
s += page_foot(C["grey"])
s += "</svg>\n"
pages["05_two_column.svg"] = s

# ================================================================ 06 card grid
s = svg_open("06_card_grid", "Card Grid", "06 Card grid: 3-up outlined cards with tint header band")
s += master_bg()
s += layout_line("layout-header-rule", 80, 222, 1200, 222, C["ink"])
s += body_header()
for i in range(3):
    x = 80 + i * 384
    s += (f'  <g id="card-{i + 1}">\n'
          f'    <rect x="{x}" y="256" width="352" height="300" fill="{C["canvas"]}" stroke="{C["hairline"]}" stroke-width="1"/>\n'
          f'    <rect x="{x}" y="256" width="352" height="60" fill="{C["orange_tint"]}"/>\n'
          f'    {num_circle(x + 30, 286, i + 1)}\n'
          f'    {text(x + 56, 292, 18, F_BOLD, C["ink"], "{{CARD_%d_TITLE}}" % (i + 1))}\n'
          f'    {text(x + 28, 358, 16, F_MED, C["ink2"], "{{CARD_%d_BODY}}" % (i + 1))}\n'
          '  </g>\n')
s += page_foot(C["grey"])
s += "</svg>\n"
pages["06_card_grid.svg"] = s

# ================================================================ 07 metrics
s = svg_open("07_metrics", "Metrics", "07 Metrics: 3-up band, third panel orange")
s += master_bg()
s += layout_rect("layout-panel-orange", 848, 300, 352, 240, C["orange"])
s += body_header()
for i in range(3):
    x = 80 + i * 384
    dark = i == 2
    if not dark:
        s += (f'  <g id="metric-{i + 1}">\n'
              f'    <rect x="{x}" y="300" width="352" height="240" fill="{C["surface"]}" stroke="{C["hairline"]}" stroke-width="1"/>\n')
    else:
        s += f'  <g id="metric-{i + 1}">\n'
    val_c = C["white"] if dark else C["ink"]
    lab_c = C["white"] if dark else C["ink"]
    del_c = C["orange_tint"] if dark else (C["orange"] if i == 0 else C["grey"])
    s += (f'    {text(x + 320, 404, 56, F_BOLD, val_c, "{{METRIC_%d_VALUE}}" % (i + 1), anchor="end", ls=-1)}\n'
          f'    {text(x + 32, 448, 16, F_MED, lab_c, "{{METRIC_%d_LABEL}}" % (i + 1))}\n'
          f'    {text(x + 32, 484, 14, F_BOLD, del_c, "{{METRIC_%d_DELTA}}" % (i + 1))}\n'
          '  </g>\n')
s += page_foot(C["grey"])
s += "</svg>\n"
pages["07_metrics.svg"] = s

# ================================================================ 08 / 09 charts (shared layout)
GRID_Y = [250, 322, 395, 467, 540]
XS = [226, 409, 592, 775, 958, 1141]


def chart_open(comment):
    s = svg_open("chart_linear", "Chart (Linear)", comment)
    s += master_bg()
    s += layout_line("layout-axis-rule", 168, 540, 1200, 540, C["ink"])
    s += ('  <g id="page-kicker">\n'
          f'    {text(80, 96, 14, F_MED, C["orange"], "{{KICKER}}")}\n'
          '  </g>\n')
    s += title_slot("80 110 690 44", 80, 144, 30, F_BOLD, C["orange"])
    s += ('  <g id="page-lead">\n'
          f'    {text(80, 190, 18, F_MED, C["ink"], "{{LEAD}}")}\n'
          '  </g>\n')
    return s


def chart_axes():
    s = '  <g id="chart-body">\n'
    s += f'    <g id="chart-grid" stroke="{C["hairline"]}" stroke-width="1">\n'
    for y in GRID_Y[:-1]:
        s += f'      <line x1="168" y1="{y}" x2="1200" y2="{y}"/>\n'
    s += '    </g>\n'
    s += f'    <g id="chart-y-axis" text-anchor="end" font-family="{F_MED}" font-size="14" fill="{C["grey"]}">\n'
    for y, v in zip(GRID_Y, ("100", "75", "50", "25", "0")):
        s += f'      <text x="154" y="{y + 5}">{v}</text>\n'
    s += '    </g>\n'
    return s


def chart_x_axis():
    s = f'    <g id="chart-x-axis" text-anchor="middle" font-family="{F_MED}" font-size="14" fill="{C["grey"]}">\n'
    for x, lab in zip(XS, ("01", "02", "03", "04", "05", "06")):
        s += f'      <text x="{x}" y="570">{lab}</text>\n'
    s += '    </g>\n  </g>\n'
    return s


# bar
s = chart_open("08 Bar chart — sample data; regenerated with real data at deck generation")
s += ('  <g id="chart-legend">\n'
      f'    <rect x="880" y="136" width="12" height="12" fill="{C["orange"]}"/>\n'
      f'    {text(900, 147, 14, F_MED, C["grey"], "{{LEGEND_PEAK}}")}\n'
      f'    <rect x="1040" y="136" width="12" height="12" fill="{C["hairline"]}"/>\n'
      f'    {text(1060, 147, 14, F_MED, C["grey"], "{{LEGEND_OTHERS}}")}\n'
      '  </g>\n')
s += '  <!-- chart-plot-area: 168,250,1200,540 -->\n'
s += chart_axes()
vals = [42, 55, 63, 88, 71, 79]
peak = vals.index(max(vals))
s += '    <g id="chart-bars">\n'
for i, (x, v) in enumerate(zip(XS, vals)):
    h = round(290 * v / 100)
    fill = C["orange"] if i == peak else C["hairline"]
    s += f'      <rect x="{x - 58}" y="{540 - h}" width="116" height="{h}" fill="{fill}"/>\n'
s += '    </g>\n'
s += f'    <g id="chart-values" text-anchor="middle" font-family="{F_BOLD}" font-size="14" fill="{C["grey"]}">\n'
for i, (x, v) in enumerate(zip(XS, vals)):
    h = round(290 * v / 100)
    extra = f' fill="{C["ink"]}"' if i == peak else ""
    s += f'      <text x="{x}" y="{540 - h - 10}"{extra}>{v}</text>\n'
s += '    </g>\n'
s += chart_x_axis()
s += page_foot(C["grey"])
s += "</svg>\n"
pages["08_chart_bar.svg"] = s

# line
s = chart_open("09 Line chart — sample data; regenerated with real data at deck generation")
s += ('  <g id="chart-legend">\n'
      f'    <line x1="880" y1="142" x2="904" y2="142" stroke="{C["orange"]}" stroke-width="2.5"/>\n'
      f'    {text(914, 147, 14, F_MED, C["grey"], "{{LEGEND_SERIES_A}}")}\n'
      f'    <line x1="1040" y1="142" x2="1064" y2="142" stroke="{C["grey"]}" stroke-width="2" stroke-dasharray="4 4"/>\n'
      f'    {text(1074, 147, 14, F_MED, C["grey"], "{{LEGEND_SERIES_B}}")}\n'
      '  </g>\n')
s += '  <!-- chart-plot-area: 168,250,1200,540 -->\n'
s += chart_axes()
ya = [470, 440, 400, 350, 320, 290]
yb = [500, 490, 470, 455, 440, 430]
s += ('    <g id="chart-series-b">\n'
      f'      <path d="M {" L ".join(f"{x} {y}" for x, y in zip(XS, yb))}" fill="none" stroke="{C["grey"]}" '
      'stroke-width="2" stroke-dasharray="5 5" stroke-linecap="round" stroke-linejoin="round"/>\n'
      '    </g>\n')
s += ('    <g id="chart-series-a">\n'
      f'      <path d="M {" L ".join(f"{x} {y}" for x, y in zip(XS, ya))}" fill="none" stroke="{C["orange"]}" '
      'stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>\n')
for i, (x, y) in enumerate(zip(XS, ya)):
    if i == len(XS) - 1:
        s += f'      <circle cx="{x}" cy="{y}" r="5" fill="{C["orange"]}"/>\n'
    else:
        s += f'      <circle cx="{x}" cy="{y}" r="4" fill="{C["white"]}" stroke="{C["orange"]}" stroke-width="2.5"/>\n'
s += '    </g>\n'
s += chart_x_axis()
s += page_foot(C["grey"])
s += "</svg>\n"
pages["09_chart_line.svg"] = s

# ================================================================ 10 closing
s = svg_open("10_closing", "Closing", "10 Closing: navy + brand mark + single chevron")
s += master_bg()
s += layout_rect("layout-bg-navy", 0, 0, 1280, 720, C["navy"])
s += layout_chevron("layout-chevron-back", 1120, -20, 760, C["navy_mid"])
s += layout_chevron("layout-chevron-orange", 1000, 100, 520, C["orange_deep"])
s += title_slot("80 280 760 80", 80, 344, 60, F_BOLD, C["white"], token="{{BRAND_MARK}}", ls=-0.5)
s += ('  <g id="closing-copy">\n'
      f'    <rect x="80" y="376" width="60" height="4" fill="{C["orange"]}"/>\n'
      f'    {text(80, 434, 24, F_BOLD, C["white"], "{{CLOSING_LINE}}")}\n'
      f'    {text(80, 474, 16, F_MED, C["blue_tint"], "{{CONTACT_LINE}}")}\n'
      '  </g>\n')
s += page_foot(C["blue_tint"])
s += "</svg>\n"
pages["10_closing.svg"] = s

for name, body in pages.items():
    (OUT / name).write_text(body, encoding="utf-8")
    print("wrote", OUT / name)
