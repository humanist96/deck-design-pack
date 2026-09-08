---
deck_id: warm-doc
kind: deck
native_structure_mode: structured
summary: 웜 뉴트럴 문서형 덱 — 사내 문서·핸드북, 온보딩, 팀 위키 발표, 프로세스 안내 (Notion 계열 웜그레이 + 파스텔 틴트 카드에서 착안)
canvas_format: ppt169
canvas_width: 1280
canvas_height: 720
canvas_viewbox: "0 0 1280 720"
source_canvas_width: 1280
source_canvas_height: 720
source_viewbox: "0 0 1280 720"
replication_mode: standard
page_count: 10
primary_color: "#5645D4"
keywords: [document, warm-neutral, pastel, handbook, onboarding]
defaults:
  mode: instructional
  visual_style: soft-rounded
  delivery_purpose: text
---

# Warm Document — Design Specification

> 원저작 템플릿. 문서형 협업 도구 계열에서 널리 통용되는 **비독점 디자인 원칙** — 웜그레이 뉴트럴, 1px 헤어라인 아웃라인, 파스텔 틴트 카드, 딥 네이비 히어로 밴드 — 을 슬라이드 문법으로 새로 설계했다. 어떤 회사의 상표·로고·워드마크·독점 UI도 복제하거나 번들하지 않는다. 브랜드 표기는 `{{BRAND_MARK}}` 텍스트 슬롯으로만 존재한다. 원 브랜드 폰트는 커스텀 가변 서체이므로 사용하지 않고, install-local Pretendard 락을 따른다.

---

## I. Template Overview

| Property | Description |
| --- | --- |
| **Template Name** | warm-doc |
| **Display Name** | Warm Document |
| **Use Cases** | 사내 문서·핸드북, 신입 온보딩, 팀 위키 발표, 프로세스·정책 안내, 워크숍 자료 |
| **Design Tone** | 친근하고 정돈됨 — 읽는 문서에 가까운 슬라이드 |
| **Theme Mode** | Light (웜 뉴트럴) — `#ffffff` 캔버스 + `#f6f5f4` 서피스, 히어로만 네이비 |

**Anti-mood**: "차가운 쿨그레이 SaaS", "다크 터미널", "그림자 범벅 카드", "컨설팅 밀도 그리드".

**Litmus test**: 슬라이드를 그대로 문서 페이지로 옮겼을 때 어색하지 않으면 통과. 이 시스템은 **발표용으로 압축한 문서**이지 문서를 흉내 낸 발표가 아니다.

---

## II. Canvas Specification

| Property | Value |
| --- | --- |
| **Format** | Standard 16:9 (`ppt169`) |
| **Dimensions** | 1280 × 720 px |
| **viewBox** | `0 0 1280 720` |
| **Side margins** | 88px — 콘텐츠 폭 1104 (x: 88 → 1192). 다른 템플릿보다 넓다 (문서 여백) |
| **Footer chrome** | 좌 `{{BRAND_MARK}}` x=88 / 우 `{{PAGE_LABEL}}` x=1192 anchor end, baseline y=672 |

4px 베이스 스페이싱. 문서형이라 블록 간 여백을 넉넉히(32–48px) 준다.

---

## III. Color Scheme — LOCKED

이 18개 외의 HEX는 어떤 생성 SVG에도 나타나서는 안 된다.

| Role | HEX | Token | Purpose |
| --- | --- | --- | --- |
| Canvas | `#ffffff` | `--canvas` | 페이지 배경 |
| Surface | `#f6f5f4` | `--surface` | 웜그레이 섹션 서피스 |
| Hairline | `#e5e3df` | `--hairline` | **1px 웜그레이 경계** — 거의 모든 요소를 두른다 |
| Navy | `#0a1530` | `--navy` | 히어로·챕터·클로징 밴드 |
| Purple | `#5645d4` | `--purple` | **주색** — CTA, 강조 1점, 차트 피크 |
| Purple pressed | `#4534b3` | `--purple-2` | 차트 2계열, 눌린 상태 |
| Ink | `#1a1a1a` | `--ink` | 헤드라인 |
| Charcoal | `#37352f` | `--charcoal` | **웜 본문** — 순수 검정이 아닌 따뜻한 먹 |
| Steel | `#787671` | `--steel` | 캡션·축 라벨·푸터 |
| Tint peach | `#ffe8d4` | `--tint-peach` | 카드 틴트 1 |
| Tint rose | `#fde0ec` | `--tint-rose` | 카드 틴트 2 |
| Tint mint | `#d9f3e1` | `--tint-mint` | 카드 틴트 3 |
| Tint lavender | `#e6e0f5` | `--tint-lavender` | 카드 틴트 4 |
| Tint sky | `#dcecfa` | `--tint-sky` | 카드 틴트 5 |
| Accent orange | `#dd5b00` | `--orange` | 주의·강조 라벨 (희소) |
| Accent teal | `#2a9d99` | `--teal` | 차트 3계열 |
| Success | `#1aae39` | `--success` | 양(+) 델타 |
| Error | `#e03131` | `--error` | 음(−) 델타·경고 |

### Color Rules

- **본문은 `#37352f`이지 검정이 아니다.** 웜 먹이 이 시스템의 체온을 만든다. `#1a1a1a`는 헤드라인 전용
- **경계는 항상 1px `#e5e3df`.** 그림자를 쓰지 않는다 — 아웃라인이 카드를 정의한다
- **파스텔 틴트 5색은 시그니처 페이지 전용.** 본문 카드·차트에 쓰지 않는다. 카드 그리드는 흰 배경 + 헤어라인
- **퍼플은 페이지당 1점.** CTA 또는 차트 피크 중 하나
- **네이비는 밴드로만** — 히어로·챕터·클로징 풀블리드. 텍스트 색으로 쓰지 않는다
- **차트 래더**: 피크 `#5645d4` → `#4534b3` → `#2a9d99` → `#e5e3df`

---

## IV. Typography System

install-local Pretendard 락. **한 패밀리, 세 웨이트** — 문서형답게 단순하다.

| Weight | `font-family` attribute |
| --- | --- |
| 400 | `Pretendard, 'Malgun Gothic', sans-serif` |
| 500 | `'Pretendard Medium', Pretendard, 'Malgun Gothic', sans-serif` |
| 600 | `'Pretendard SemiBold', Pretendard, 'Malgun Gothic', sans-serif` |

**모든 헤딩은 600, 강조는 500, 본문은 400.** 300과 700 이상은 이 로스터에 없다.

### 🔒 본문 baseline 락 — `delivery_purpose` 기본값보다 우선

**본문 baseline은 `20`이다.** 문서형이라 읽는 텍스트가 많다 — 커버:본문 3.6배로 대비를 억제해 "문서" 느낌을 유지한다. `presentation` 목적일 때만 본문 24 / 커버 84로 동반 상향한다.

| Role | Size | Weight | Letter-spacing (라틴) | Use |
| --- | --- | --- | --- | --- |
| Cover title | 72 | 600 | -2.2 | 표지 헤드라인 |
| Section title | 56 | 600 | -1.6 | 챕터 헤드라인 |
| Statement | 44 | 600 | -1.2 | 시그니처 진술문 |
| KPI number | 52 | 600 | -1.4 | 지표 대형 숫자 |
| Page title | 38 | 600 | -1 | 표준 페이지 제목 |
| Subtitle | 24 | 400 | -0.3 | 표지 서브카피 |
| Lead | 22 | 400 | -0.2 | 페이지 리드 |
| Subheading | 22 | 600 | -0.2 | 카드 제목 |
| Body | 20 | 400 | -0.1 | 본문 |
| Annotation | 16 | 400 | 0 | 캡션·태그·축 라벨 |
| Kicker | 14 | 600 | +1 | 대문자 마이크로 라벨 |
| Footnote | 13 | 400 | 0 | 푸터 |

**자간 완화 규칙**: 한글 비중 ≥50% 런은 표의 값 **×0.5**(72px → -1.1). 양수 자간은 유지.

---

## V. Page Roster

| File | Layout key | Surface | Purpose |
| --- | --- | --- | --- |
| `01_cover.svg` | `01_cover` | **navy** | 표지 — 네이비 히어로 밴드 + 72px 헤드라인 |
| `02_agenda.svg` | `02_agenda` | white | 목차 — 헤어라인 5행 |
| `03_section.svg` | `03_section` | **navy** | 챕터 전환 |
| `04_tinted_cards.svg` | `04_tinted_cards` | surface | **시그니처** — 파스텔 틴트 5색 카드 스택 |
| `05_two_column.svg` | `05_two_column` | white | 좌 텍스트 / 우 아웃라인 스택 |
| `06_card_grid.svg` | `06_card_grid` | surface | 3-up 카드 그리드 (흰 카드 + 헤어라인) |
| `07_metrics.svg` | `07_metrics` | white | 3-up 지표 |
| `08_chart_bar.svg` | `chart_linear` | white | 6-바 추이 + 피크 퍼플 |
| `09_chart_line.svg` | `chart_linear` | white | 2계열 추이 |
| `10_closing.svg` | `10_closing` | **navy** | 클로징 |

`08` / `09`는 고정 Layout 원자와 슬롯 계약이 동일하므로 `chart_linear` 키를 공유한다.

---

## VI. Signature Design Elements

1. **웜 뉴트럴 지반** — 본문 `#37352f`, 서피스 `#f6f5f4`, 경계 `#e5e3df`. 쿨그레이를 한 번도 쓰지 않는다
2. **1px 아웃라인 문법** — 모든 카드·패널·표가 헤어라인을 두른다. 그림자는 시스템 전체에 없다
3. **파스텔 틴트 5색 스택** — 시그니처 페이지에서 피치·로즈·민트·라벤더·스카이 카드가 계단식으로 겹친다. 정보 분류가 아니라 **리듬**이다
4. **네이비 히어로 밴드** — 표지·챕터·클로징만 `#0a1530` 풀블리드. 문서 사이의 표지지 강조가 아니다
5. **넓은 여백** — 88px 측면 마진과 32–48px 블록 간격. 읽는 속도를 늦춘다

---

## VII. Chart Treatment

- 그리드: 가로 헤어라인 5개 `#e5e3df` 1px. 세로 그리드·플롯 프레임 금지
- 축 라벨: 16px `#787671`. y축 anchor end, x축 anchor middle
- 바: 라운드 8, 피크만 `#5645d4`, 나머지 `#e5e3df`
- 라인: 주 계열 실선 2.5px `#5645d4` + 점, 비교 계열 점선 2px `#787671`
- 레전드: 우상단, 스와치 12px rx4 / 24px 선
- 값 라벨: 16px `#787671`, 피크만 `#1a1a1a`
- **Forbidden**: 파스텔 틴트를 차트에 사용, 그림자, 3D, 파이

| Page | Marker |
| --- | --- |
| `08_chart_bar` | `<!-- chart-plot-area: 176,250,1192,540 -->` |
| `09_chart_line` | `<!-- chart-plot-area: 176,250,1192,540 -->` |

---

## VIII. Placeholder Vocabulary

| Token | Pages | Content |
| --- | --- | --- |
| `{{TITLE}}` | 01–09 | 페이지 헤드라인 |
| `{{KICKER}}` | 01/03/04/07 | 대문자 마이크로 라벨 |
| `{{SUBTITLE}}` | 01 | 표지 서브카피 |
| `{{LEAD}}` | 04/05/06/07 | 페이지 리드 1행 |
| `{{ITEM_n_NO}}` / `{{ITEM_n_TITLE}}` / `{{ITEM_n_TAG}}` | 02 | 아젠다 (n=1..5) |
| `{{BODY}}` / `{{POINT_n}}` | 05 | 좌측 본문 / 불릿 (n=1..3) |
| `{{CARD_n_TITLE}}` / `{{CARD_n_BODY}}` | 06 | 카드 (n=1..3) |
| `{{TINT_n_LABEL}}` / `{{TINT_n_BODY}}` | 04 | 틴트 카드 (n=1..5) |
| `{{METRIC_n_VALUE}}` / `{{METRIC_n_LABEL}}` / `{{METRIC_n_DELTA}}` | 07 | 지표 (n=1..3) |
| `{{LEGEND_PEAK}}` / `{{LEGEND_OTHERS}}` | 08 | 바 레전드 |
| `{{LEGEND_SERIES_A}}` / `{{LEGEND_SERIES_B}}` | 09 | 라인 레전드 |
| `{{CLOSING_LINE}}` / `{{CONTACT_LINE}}` | 10 | 클로징 카피 / 연락처 |
| `{{BRAND_MARK}}` | 전 페이지 푸터 + 10 대형 마크 | 브랜드명 **텍스트** |
| `{{PAGE_LABEL}}` | 전 페이지 푸터 | 페이지 번호 |

---

## IX. Anti-Pattern Checklist

| ✗ 금지 | 대안 |
| --- | --- |
| 본문에 순수 검정 `#000` 또는 쿨그레이 | 웜 먹 `#37352f` |
| 그림자 | 1px `#e5e3df` 아웃라인 |
| 파스텔 틴트를 본문 카드·차트에 사용 | 시그니처 페이지 전용 |
| 퍼플 강조 2곳 이상 | 페이지당 1점 |
| 네이비를 텍스트 색으로 사용 | 밴드 배경으로만 |
| 헤딩 weight 700 이상 | 래더는 400/500/600 |
| 좁은 여백으로 밀도 올리기 | 88px 마진 + 32–48px 블록 간격 유지 |
| 로고 이미지 번들 | `{{BRAND_MARK}}` 텍스트 슬롯 |
| 한글 런에 라틴 자간 그대로 | §IV 완화 규칙 ×0.5 |
