# Authoring

How these templates are built, and what to preserve if you fork or extend one.

## The 10-page spine

All six templates share one roster so the pack reads as a single system:

| # | File | Type | Rhythm |
|---|---|---|---|
| 01 | `01_cover.svg` | Cover | anchor |
| 02 | `02_agenda.svg` | Agenda — 5 hairline rows | dense |
| 03 | `03_section.svg` | Section divider | anchor |
| 04 | `04_<signature>.svg` | **Signature** — the template's identity move | breathing |
| 05 | `05_two_column.svg` | Text column + visual column | dense |
| 06 | `06_card_grid.svg` | Card grid (3-up; 4-up on `signal-green`) | dense |
| 07 | `07_metrics.svg` | 3-up metrics band | dense |
| 08 | `08_chart_bar.svg` | Bar chart, single peak | dense |
| 09 | `09_chart_line.svg` | Two-series line chart | dense |
| 10 | `10_closing.svg` | Closing | anchor |

Page 04 is the only slot that differs by template:

| Template | Signature page |
|---|---|
| `midnight-panel` | `04_panel_showcase` — abstract product UI inside a surface-1 frame |
| `polarity` | `04_polarity_flip` — inverted canvas with a terminal mockup |
| `gradient-mesh` | `04_gradient_statement` — mesh blob behind a 300-weight sentence |
| `warm-doc` | `04_tinted_cards` — five pastel tint cards |
| `open-road` | `04_fullbleed_hero` — one photograph, one sentence |
| `signal-green` | `04_black_hero` — black field with green corner squares |

## Structural contract

Every page declares the PowerPoint structure it compiles to.

```xml
<svg viewBox="0 0 1280 720"
     data-pptx-master="<master-key>"  data-pptx-master-name="<Master picker name>"
     data-pptx-layout="<layout-key>"  data-pptx-layout-name="<Layout picker name>">

  <rect id="master-bg" width="1280" height="720" fill="…"
        data-pptx-layer="master" data-pptx-editable="false"/>

  <line id="layout-column-divider" …
        data-pptx-layer="layout" data-pptx-editable="false"/>

  <g id="title-slot" data-pptx-placeholder="title"
     data-pptx-placeholder-bounds="x y w h">
    <text id="title-carrier" data-pptx-placeholder-carrier="true" …>{{TITLE}}</text>
  </g>

  <g id="content-block">…</g>
</svg>
```

Rules that matter:

- **Paint order is fixed**: Master background atoms → Layout background atoms → remaining Master atoms → remaining Layout atoms → slots and Slide-local content groups. Interleaving fails export.
- **Master and Layout atoms are direct root children.** A `<g data-pptx-layer="…">` is rejected — push transforms and paint into atomic elements.
- **A slot is a direct root `<g id>`** with positive `data-pptx-placeholder-bounds` and exactly one compatible carrier child. Bounds come from the intended design zone, never from the sample text's ink extents.
- **Layout keys must be distinguishable.** Two layouts with identical fixed atoms and identical slot ids/types/bounds compile to duplicate Layouts and the checker rejects it. Each template gives its list, two-column, and grid pages a real fixed-framing atom (a list rule, a column divider, a header rule) so the difference is genuine rather than cosmetic.
- **Chart pages carry a plot-area marker** — `<!-- chart-plot-area: x_min,y_min,x_max,y_max -->` — placed after the axis group and before the first data element.

### Why 9 layouts for 10 pages

`08_chart_bar` and `09_chart_line` share the `chart_linear` key. Their fixed Layout atoms and slot contracts are identical; only Slide-local content differs, and Slide-local geometry does not define Layout identity.

## Colour discipline

Each `design_spec.md` §III lists the **complete** palette and states that no other hex may appear in a generated SVG. This is what keeps a 20-page deck coherent — the Executor draws only from that list and never invents a tone mid-deck.

Two conventions recur across the pack:

- **One accent per page.** Every template restricts its signal colour to a single element per page. A second occurrence turns signal into decoration.
- **Depth without shadow.** None of the six use drop shadows. Lift comes from surface stepping (`midnight-panel`), hairline outlines (`warm-doc`), surface brightness (`polarity`), or photography (`open-road`).

## Typography

Locked to **Pretendard**; hierarchy is weight span + letter-spacing + size, never a family switch.

Each spec declares a **native body baseline** that overrides the generic `delivery_purpose` default (20 / 24 / 32). This is deliberate: a template's identity lives in the *ratio* between display and body, and inflating body alone collapses that contrast. Each spec states its baseline, the ratio it protects, and what to raise alongside it if the deck is projected.

Letter-spacing values in the tables are **Latin reference values**. Korean-dominant runs (≥50% Hangul) relax them by ×0.5 — Korean glyph widths are uniform, so identical negative tracking closes the letterforms up. Positive tracking (kickers) is language-independent.

## Placeholder vocabulary

Text uses `{{TOKEN}}` slots, listed per template in §VIII of its spec. Shared across the pack:

`{{TITLE}}` · `{{KICKER}}` · `{{SUBTITLE}}` · `{{LEAD}}` · `{{ITEM_n_NO}}` / `{{ITEM_n_TITLE}}` / `{{ITEM_n_TAG}}` · `{{BODY}}` / `{{POINT_n}}` · `{{CARD_n_TITLE}}` / `{{CARD_n_BODY}}` · `{{METRIC_n_VALUE}}` / `{{METRIC_n_LABEL}}` / `{{METRIC_n_DELTA}}` · `{{LEGEND_*}}` · `{{CLOSING_LINE}}` / `{{CONTACT_LINE}}` · `{{BRAND_MARK}}` · `{{PAGE_LABEL}}`

`{{BRAND_MARK}}` is always **text**, never an image — no logo assets are bundled.

## Images

Only `open-road` reserves photographic regions, and it does so with a preset pattern rather than a bundled file:

```xml
<pattern id="photo-hatch" patternUnits="userSpaceOnUse" width="20" height="20"
         patternTransform="rotate(45)" data-pptx-pattern="ltUpDiag">
  <rect width="20" height="20" fill="#171A20"/>
  <rect width="10" height="20" fill="#393C41"/>
</pattern>
```

`data-pptx-pattern` must be a value from the OOXML `ST_PresetPatternVal` enum — anything outside it makes PowerPoint report a repair. To use a real photograph, replace the hatched `<rect>` with `<image href="../images/…">`.

## Sample chart data

The chart pages ship plausible sample values so the prototype reads as a chart. They are demonstration data, labelled as such in each file's comment. At deck generation the Executor replaces them with real values while inheriting the template's chart grammar.

## Verifying a change

```bash
# structural contract
python3 <ws>/.claude/skills/ppt-master/scripts/svg_quality_checker.py \
        <template>/templates --template-mode --format ppt169

# compiles to the declared Master/Layout structure
python3 <ws>/.claude/skills/ppt-master/scripts/template_preview_pptx.py <template> --force
```

The first must report 0 errors **and** 0 warnings. The second must report the expected slide/master/layout counts; a duplicate-layout warning from the first means two layout keys need genuinely different fixed framing, not a renamed key.
