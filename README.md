# Deck Design Pack

**A complete presentation workspace in one clone.** The [ppt-master](https://github.com/hugohe3/ppt-master) SVG-authoring pipeline — the one that turns source documents into *natively editable* PowerPoint, not a deck of pictures — is embedded here, with seven extra 16:9 template systems already installed and registered.

Clone it, install the Python dependencies, open the folder in Claude Code or Codex, and ask for a deck. There is no second repository to fetch and no install step for the templates.

```
11 deck templates · 13 brand identities · 70 hand-authored SVG prototypes from this pack
input: PDF · DOCX · URL · Markdown · XLSX/CSV — or one line of topic
output: projects/<name>/exports/<title>_ver1.pptx — real DrawingML shapes, text and charts
```

---

## Quick start

```bash
git clone https://github.com/humanist96/deck-design-pack.git
cd deck-design-pack
pip install -r requirements.txt
```

Then open the folder in your agent — Claude Code (CLI or IDE extension) is the most-tested environment; Codex works with no extra setup because [`AGENTS.md`](AGENTS.md) and the `.codex/skills/` stubs ship in the repo. Ask for what you want:

> "projects/ 에 넣어둔 3분기 보고서 PDF로 임원 보고용 PPT 만들어줘"

The agent reads the source, opens a browser confirmation page where you pick canvas, page count, colour, font and one of the eleven deck templates, draws each page as SVG, checks it for overlap and overflow, then compiles a native `.pptx`.

Full workflow guide, installation detail for Windows, optional AI-image and narration setup: [`docs/slide-master-README.md`](docs/slide-master-README.md) · [`docs/getting-started.md`](docs/getting-started.md) · [`docs/windows-installation.md`](docs/windows-installation.md) · [`docs/faq.md`](docs/faq.md)

---

## The eleven deck templates

Seven designed for this pack:

| Template | Theme | Primary | Signature move | Best for |
|---|---|---|---|---|
| **[Midnight Panel](.claude/skills/ppt-master/templates/decks/midnight-panel/)** | dark | `#5E6AD2` | Surface stepping instead of shadow; one lavender signal per page | Product roadmaps, sprint reviews, engineering briefings |
| **[Polarity Mono](.claude/skills/ppt-master/templates/decks/polarity/)** | light ↔ dark | `#171717` | Chapter breaks are a **polarity inversion**, not a divider | Tech talks, demo days, developer conferences |
| **[Gradient Mesh Fintech](.claude/skills/ppt-master/templates/decks/gradient-mesh/)** | light | `#533AFD` | Mesh gradient over thin 300-weight display type | Partner proposals, fintech IR, product economics |
| **[Warm Document](.claude/skills/ppt-master/templates/decks/warm-doc/)** | warm light | `#5645D4` | 1px outline grammar, five pastel tint cards | Handbooks, onboarding, team wiki decks |
| **[Open Road](.claude/skills/ppt-master/templates/decks/open-road/)** | light + carbon | `#3E6AE1` | One page, one message; full-bleed photography | Product launches, brand keynotes, vision decks |
| **[Signal Green](.claude/skills/ppt-master/templates/decks/signal-green/)** | black / white | `#76B900` | 12×12 corner-square marker; angular 2px geometry | AI/GPU briefings, benchmarks, developer sessions |
| **[Koscom Chevron](.claude/skills/ppt-master/templates/decks/koscom-chevron/)** | white + navy + black | `#EE6D1D` | Orange chevron (›) cluster on anchor pages; KoPub Dotum Bold headlines | Koscom company profiles, business briefings, capital-market IT proposals |

Four that come with the pipeline:

| Template | Pages | Primary | For |
|---|---|---|---|
| **[apple](.claude/skills/ppt-master/templates/decks/apple/)** | 13 | `#1D1D1F` | 제품 발표, 브랜드 스토리, 디자인 리뷰 |
| **[mckinsey](.claude/skills/ppt-master/templates/decks/mckinsey/)** | 10 | `#0F2A4A` | 전략 보고서, 시장·산업 분석, 실행 로드맵 |
| **[naver_ir](.claude/skills/ppt-master/templates/decks/naver_ir/)** | 7 | `#03C75A` | 분기 실적발표, 재무 보고, 투자자 미팅 |
| **[jangpm](.claude/skills/ppt-master/templates/decks/jangpm/)** | 4 | `#4633E3` | 강의, 워크숍, 분석 리포트 |

And **13 identity-only brand presets** under [`templates/brands/`](.claude/skills/ppt-master/templates/brands/) — colours, typography, voice and icon rules with no page roster, for when you want a look but your own structure.

Both are discovered from the index files the pipeline reads: [`decks_index.json`](.claude/skills/ppt-master/templates/decks/decks_index.json) and [`brands_index.json`](.claude/skills/ppt-master/templates/brands/brands_index.json).

---

## Gallery

| | |
|---|---|
| **Midnight Panel**<br><img src="previews/midnight-panel.png" width="420"> | **Polarity Mono**<br><img src="previews/polarity.png" width="420"> |
| **Gradient Mesh Fintech**<br><img src="previews/gradient-mesh.png" width="420"> | **Warm Document**<br><img src="previews/warm-doc.png" width="420"> |
| **Open Road**<br><img src="previews/open-road.png" width="420"> | **Signal Green**<br><img src="previews/signal-green.png" width="420"> |
| **Koscom Chevron**<br><img src="previews/koscom-chevron.png" width="420"> | |

Full-size contact sheets: [`previews/`](previews/) · per-template detail: [`docs/gallery.md`](docs/gallery.md)

---

## What is where

```
.claude/skills/            the workflow — ppt-master + diagram-design, codex-image,
  ppt-master/                native-enhance-pptx, ppt-template-fill
    scripts/               54 Python entry points: SVG → PPTX, quality checker,
                             confirm UI, image backends, TTS, verification
    templates/
      decks/               11 deck templates + decks_index.json
      brands/              13 brand identities + brands_index.json
      layouts/ charts/ icons/
    assets/fonts/          Pretendard (SIL OFL)
    references/ workflows/
.codex/skills/             Codex discovery stubs
projects/                  your decks and source material (git-ignored)
previews/                  contact sheets for this pack's seven templates
docs/                      workflow guides + this pack's authoring notes
install.py                 export this pack into a *different* ppt-master workspace
```

### What you get per pack template

```
.claude/skills/ppt-master/templates/decks/<id>/templates/
├── design_spec.md          # locked palette, type ramp, page roster, anti-patterns
├── 01_cover.svg            # ─┐
├── 02_agenda.svg           #  │
├── 03_section.svg          #  │
├── 04_<signature>.svg      #  │ 10 page prototypes
├── 05_two_column.svg       #  │ with {{TOKEN}} slots
├── 06_card_grid.svg        #  │
├── 07_metrics.svg          #  │
├── 08_chart_bar.svg        #  │
├── 09_chart_line.svg       #  │
└── 10_closing.svg          # ─┘
```

All seven share the same 10-page spine so the pack reads as one system. **Page 04 is where each template's identity shows** — a product panel, a polarity flip, a gradient statement, a tint-card stack, a full-bleed hero, a black hero, a black wave field.

Each `design_spec.md` locks the things that make a deck look designed rather than assembled: an exhaustive colour list (nothing outside it may appear in a generated SVG), a native body-size baseline that overrides the generic default, a chart grammar, and an anti-pattern checklist written to be rejected at authoring time.

---

## Structural contract

These are not decorative SVGs. Each page declares the PowerPoint structure it compiles to:

- root Master/Layout identity (`data-pptx-master`, `data-pptx-layout`)
- fixed framing as Layout atoms (`data-pptx-layer="layout"`)
- content slots as bounded placeholders with exactly one carrier
- `<!-- chart-plot-area: … -->` markers on chart pages

A 10-page template compiles to **1 Master and 9 Layouts** — the two chart pages share one `chart_linear` layout because their fixed framing and slot contract are identical.

Verified per template:

| Gate | Result |
|---|---|
| `svg_quality_checker --template-mode` | 70/70 pages, 0 errors. 60 pages fully clean; `koscom-chevron`'s 10 pages each raise one expected warning — KoPub Dotum is not on the checker's PPT-safe font list, which is the documented cost of keeping Koscom's type lock |
| `template_preview_pptx.py` read-back | 10 slides · 1 master · 9 layouts |
| End-to-end deck generation (`strict` adherence) | 0 errors, 0 warnings · `verify_deck` PASS |
| Exported package | 1 master · layout picker names preserved · placeholders bound |

The six originals were verified end to end, not just structurally: a 7-page deck was generated from each template under `strict` adherence — cover, agenda, section, the signature page, metrics, a chart with real data, and the closing — and each exported package opens with the template's own layout names in the PowerPoint picker. `koscom-chevron` is structurally clean and has a rendered contact sheet; it has not yet been run through `verify_deck`.

Authoring details: [`docs/authoring.md`](docs/authoring.md) · template data model: [`docs/templates-architecture.md`](docs/templates-architecture.md)

---

## Typography

The six originals are locked to **Pretendard** (SIL OFL), bundled at [`assets/fonts/Pretendard/`](.claude/skills/ppt-master/assets/fonts/Pretendard/). `koscom-chevron` is the exception: it keeps the **KoPub돋움체** lock of Koscom's official material and ships the three weights under [`decks/koscom-chevron/fonts/`](.claude/skills/ppt-master/templates/decks/koscom-chevron/fonts/FONTS.md). Hierarchy comes from weight span, letter-spacing, and size ramp — never from switching families.

Latin letter-spacing values in each spec are the reference; **Korean-dominant runs relax them by ×0.5**, because Korean glyph widths are uniform and the same negative tracking closes the letterforms up.

> PPTX does not embed fonts. Decks exported from these templates need Pretendard — and, for `koscom-chevron`, KoPub Dotum — installed wherever they are opened.

---

## Using the pack in a workspace you already run

If you have your own ppt-master workspace and only want these seven templates, `install.py` copies them across and merges both discovery indexes:

```bash
python3 install.py /path/to/your/ppt-master-workspace
python3 install.py <workspace> --only midnight-panel polarity   # subset
python3 install.py <workspace> --force                          # replace existing ids
python3 install.py <workspace> --dry-run                        # show the plan
```

It has no dependencies beyond the standard library (it uses PyYAML if present). Details and manual steps: [`docs/install.md`](docs/install.md).

> **Why an installer instead of the workspace registrar?** The stock `register_template.py` rebuilds each index entry from scratch and drops the `defaults` block the Confirm UI reads to cascade a deck's mode / visual style / delivery purpose. `install.py` sources that block from each template's own frontmatter, so the anchors survive any number of index rebuilds.

---

## Licence, credits and trademarks

The pack's own material — the seven deck templates, the seven brand presets, the contact sheets and `install.py` — is [MIT](LICENSE) © 2026 humanist96.

The embedded workflow is [MIT](THIRD_PARTY_NOTICES.md) © 2025-2026 Hugo He, vendored from [byungjunjang/slide-master](https://github.com/byungjunjang/slide-master), a Korean-workflow customisation of [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master). Upstream's own README is kept verbatim at [`docs/slide-master-README.md`](docs/slide-master-README.md). Fonts and per-skill licences are listed in [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md).

No third-party trademarks, logos, wordmarks, or photographs are bundled by the six original templates. `koscom-chevron` is a corporate house template built from Koscom's own sample decks: the Koscom name and chevron mark belong to Koscom Co., Ltd., the logo image is not bundled (text `{{BRAND_MARK}}` slot only), and the KoPub fonts it ships are under their own free licence. Where a specification names a company, it identifies a design *idiom* as a reference point — descriptive comparison, not a claim of endorsement or affiliation. See [`TRADEMARKS.md`](TRADEMARKS.md) for the full position.
