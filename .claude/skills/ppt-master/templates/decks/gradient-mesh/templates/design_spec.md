---
deck_id: gradient-mesh
kind: deck
native_structure_mode: structured
summary: 그라디언트 메시 핀테크 덱 — 파트너 제안서, 핀테크 IR, 제품 이코노믹스, SaaS 가격 설명 (Stripe 계열 인디고 + 메시 그라디언트에서 착안)
canvas_format: ppt169
canvas_width: 1280
canvas_height: 720
canvas_viewbox: "0 0 1280 720"
source_canvas_width: 1280
source_canvas_height: 720
source_viewbox: "0 0 1280 720"
replication_mode: standard
page_count: 10
primary_color: "#533AFD"
keywords: [fintech, gradient, indigo, pill, tabular]
defaults:
  mode: pyramid
  visual_style: glassmorphism
  delivery_purpose: balanced
---

# Gradient Mesh Fintech — Design Specification

> 원저작 템플릿. 핀테크·개발자 결제 플랫폼 계열에서 널리 통용되는 **비독점 디자인 원칙** — 상단 메시 그라디언트, 풀 필 CTA, 얇은 디스플레이 웨이트, 표 형태 숫자 정렬 — 을 슬라이드 문법으로 새로 설계했다. 어떤 회사의 상표·로고·워드마크·독점 UI도 복제하거나 번들하지 않는다. 브랜드 표기는 `{{BRAND_MARK}}` 텍스트 슬롯으로만 존재한다. 원 브랜드 폰트는 상용 서체이므로 사용하지 않고, install-local Pretendard 락을 따르며 성격은 웨이트·자간으로 재현한다.

---

## I. Template Overview

| Property | Description |
| --- | --- |
| **Template Name** | gradient-mesh |
| **Display Name** | Gradient Mesh Fintech |
| **Use Cases** | 파트너 제안서, 핀테크 IR, 제품 이코노믹스, 가격·수수료 설명, 결제/정산 아키텍처 브리핑 |
| **Design Tone** | 정밀하고 낙관적 — 숫자를 다루되 차갑지 않다 |
| **Theme Mode** | Light — `#ffffff` 캔버스 + 쿨/웜 밴드 교대 |

**Anti-mood**: "다크 터미널", "컨설팅 밀도 그리드", "그림자 범벅 카드", "무지개 카테고리 차트".

**Litmus test**: 메시 그라디언트를 지웠을 때 페이지가 성립하면 통과. 메시는 **분위기**이지 구조가 아니다 — 위계는 얇은 디스플레이 타입과 서피스 밴드가 만든다.

---

## II. Canvas Specification

| Property | Value |
| --- | --- |
| **Format** | Standard 16:9 (`ppt169`) |
| **Dimensions** | 1280 × 720 px |
| **viewBox** | `0 0 1280 720` |
| **Side margins** | 80px — 콘텐츠 폭 1120 (x: 80 → 1200) |
| **Footer chrome** | 좌 `{{BRAND_MARK}}` x=80 / 우 `{{PAGE_LABEL}}` x=1200 anchor end, baseline y=674 |

8px 베이스 스페이싱(8/16/24/32/48/64). 마케팅형 밴드 64–96px, 데이터 패널 32–48px.

---

## III. Color Scheme — LOCKED

이 17개 외의 HEX는 어떤 생성 SVG에도 나타나서는 안 된다.

| Role | HEX | Token | Purpose |
| --- | --- | --- | --- |
| Canvas | `#ffffff` | `--canvas` | 페이지 배경 |
| Surface cool | `#f6f9fc` | `--surface-cool` | 쿨 오프화이트 밴드·카드 |
| Surface warm | `#f5e9d4` | `--surface-warm` | 웜 크림 밴드 (교대 리듬) |
| Hairline | `#e3e8ee` | `--hairline` | 1px 카드·표 경계 |
| Indigo | `#533afd` | `--indigo` | **주색** — CTA 필, 강조 1점, 차트 피크 |
| Indigo deep | `#4434d4` | `--indigo-deep` | 그라디언트 중간 스톱, 눌린 상태 |
| Indigo soft | `#665efd` | `--indigo-soft` | 보조 강조, 차트 2계열 |
| Indigo tint | `#b9b9f9` | `--indigo-tint` | 태그 배경, 차트 비강조 |
| Navy | `#1c1e54` | `--navy` | 다크 카운터패널·강조 지표 카드 |
| Ruby | `#ea2261` | `--ruby` | **차트·그라디언트 전용** — 버튼에 절대 금지 |
| Magenta | `#f96bee` | `--magenta` | 그라디언트 스톱 전용 |
| Sherbet | `#f5a623` | `--sherbet` | 그라디언트 스톱 전용 |
| Ink | `#0d253d` | `--ink` | 헤드라인·본문 1차 |
| Ink secondary | `#273951` | `--ink-2` | 본문 2차 |
| Ink muted | `#64748d` | `--ink-muted` | 캡션·축 라벨·푸터 |
| Ink inverse | `#ffffff` | `--ink-inverse` | 네이비 패널 위 텍스트 |
| Success | `#1e8e5a` | `--success` | 양(+) 델타 전용 |

### Color Rules

- **인디고는 페이지당 강조 1점.** CTA 필 또는 차트 피크 중 하나 — 둘 다는 안 된다
- **루비·마젠타·셔벗은 그라디언트와 차트에만.** 버튼·텍스트·아이콘에 쓰지 않는다
- **밴드 교대가 리듬이다** — white → `#f6f9fc` → `#f5e9d4` → `#1c1e54` 순으로 페이지 성격을 나눈다. 페이지 안에서 두 밴드를 섞지 않는다
- **숫자는 표 정렬.** 지표·표의 숫자는 오른쪽 정렬하고 자릿수를 맞춘다
- **그림자 금지.** 리프트는 서피스 대비(white ↔ `#f6f9fc`)와 1px 헤어라인으로만
- **차트 래더**: 피크 `#533afd` → `#665efd` → `#b9b9f9` → `#e3e8ee`. 루비는 리스크/감소 표시에만

---

## IV. Typography System

install-local Pretendard 락. **디스플레이는 얇게(300), 본문은 보통(400)** — 이 대비가 시스템의 성격이다.

| Weight | `font-family` attribute |
| --- | --- |
| 300 | `'Pretendard Light', Pretendard, 'Malgun Gothic', sans-serif` |
| 400 | `Pretendard, 'Malgun Gothic', sans-serif` |
| 500 | `'Pretendard Medium', Pretendard, 'Malgun Gothic', sans-serif` |
| 600 | `'Pretendard SemiBold', Pretendard, 'Malgun Gothic', sans-serif` |

**헤드라인은 300 또는 400이지 600이 아니다.** 600은 카드 제목·라벨 같은 작은 텍스트에만 쓴다 — 큰 텍스트를 굵게 만드는 순간 이 시스템의 우아함이 사라진다.

### 🔒 본문 baseline 락 — `delivery_purpose` 기본값보다 우선

**본문 baseline은 `20`이다.** 커버:본문 = 76/20 = 3.8배. `presentation` 목적일 때만 본문 24 / 커버 88 / 페이지 제목 46으로 동반 상향한다.

| Role | Size | Weight | Letter-spacing (라틴) | Use |
| --- | --- | --- | --- | --- |
| Cover title | 76 | 300 | -2.4 | 표지 헤드라인 |
| Section title | 60 | 300 | -1.8 | 챕터 헤드라인 |
| Statement | 52 | 300 | -1.5 | 시그니처 진술문 |
| KPI number | 54 | 400 | -1.4 | 지표 대형 숫자 |
| Page title | 40 | 400 | -1.1 | 표준 페이지 제목 |
| Subtitle | 26 | 300 | -0.4 | 표지 서브카피 |
| Lead | 22 | 400 | -0.2 | 페이지 리드 |
| Subheading | 22 | 600 | -0.2 | 카드 제목 |
| Body | 20 | 400 | -0.1 | 본문 |
| Annotation | 16 | 400 | 0 | 캡션·태그·축 라벨 |
| Kicker | 15 | 600 | +1.6 | 대문자 키커 |
| Footnote | 13 | 400 | 0 | 푸터 |

**자간 완화 규칙**: 한글 비중 ≥50% 런은 표의 값 **×0.5**(76px → -1.2). 양수 자간은 유지.

---

## V. Page Roster

| File | Layout key | Surface | Purpose |
| --- | --- | --- | --- |
| `01_cover.svg` | `01_cover` | white + mesh | 표지 — 상단 1/3 메시 + 76px 얇은 헤드라인 + 인디고 필 |
| `02_agenda.svg` | `02_agenda` | white | 목차 — 헤어라인 5행 |
| `03_section.svg` | `03_section` | **navy** | 챕터 전환 — 네이비 카운터패널 |
| `04_gradient_statement.svg` | `04_gradient_statement` | white + mesh | **시그니처** — 메시 블롭 위 진술문 |
| `05_two_column.svg` | `05_two_column` | white | 좌 텍스트 / 우 카드 스택 |
| `06_card_grid.svg` | `06_card_grid` | cool | 3-up 카드 그리드 |
| `07_metrics.svg` | `07_metrics` | white | 3-up 지표 (3번째는 네이비 강조) |
| `08_chart_bar.svg` | `chart_linear` | white | 6-바 추이 + 피크 인디고 |
| `09_chart_line.svg` | `chart_linear` | white | 2계열 추이 |
| `10_closing.svg` | `10_closing` | **navy** | 클로징 — 네이비 + 대형 마크 |

`08` / `09`는 고정 Layout 원자와 슬롯 계약이 동일하므로 `chart_linear` 키를 공유한다.

---

## VI. Signature Design Elements

1. **상단 메시 그라디언트** — 크림·셔벗·라벤더·인디고·루비 블롭이 상단 1/3을 채우고 아래로 캔버스 색으로 페이드된다. `01`과 `04`에만 등장
2. **풀 필 CTA** — 반경 9999의 인디고 필. 페이지당 최대 1개
3. **얇은 디스플레이** — 76px를 weight 300으로. 굵기가 아니라 크기가 위계다
   - `{{STATEMENT}}` 카피 예산: 52px 기준 **한글 10자 이내**(x=80에서 시작해 메시 존 x=640 전에 끝나야 한다). 더 길면 시그니처 페이지가 아니라 본문 페이지로 옮긴다
4. **네이비 카운터패널** — 챕터·클로징은 `#1c1e54` 풀블리드. 밝은 본문 사이의 쉼표
5. **표 정렬 숫자** — 지표·표의 숫자는 우측 정렬 + 자릿수 일치

---

## VII. Chart Treatment

- 그리드: 가로 헤어라인 5개 `#e3e8ee` 1px. 세로 그리드·플롯 프레임 금지
- 축 라벨: 16px `#64748d`. y축 anchor end, x축 anchor middle
- 바: 라운드 8, 피크만 `#533afd`, 나머지 `#e3e8ee`
- 라인: 주 계열 실선 2.5px `#533afd` + 점, 비교 계열 점선 2px `#b9b9f9`
- 레전드: 우상단, 스와치 12px rx4 / 24px 선
- 값 라벨: 16px `#64748d`, 피크만 `#0d253d`
- **Forbidden**: 그림자, 3D, 다색 팔레트, 파이. 루비는 리스크 표시에만

| Page | Marker |
| --- | --- |
| `08_chart_bar` | `<!-- chart-plot-area: 168,250,1200,540 -->` |
| `09_chart_line` | `<!-- chart-plot-area: 168,250,1200,540 -->` |

---

## VIII. Placeholder Vocabulary

| Token | Pages | Content |
| --- | --- | --- |
| `{{TITLE}}` | 01–09 | 페이지 헤드라인 |
| `{{KICKER}}` | 01/03/04/07 | 대문자 키커 |
| `{{SUBTITLE}}` | 01 | 표지 서브카피 |
| `{{LEAD}}` | 04/05/06/07 | 페이지 리드 1행 |
| `{{ITEM_n_NO}}` / `{{ITEM_n_TITLE}}` / `{{ITEM_n_TAG}}` | 02 | 아젠다 (n=1..5) |
| `{{BODY}}` / `{{POINT_n}}` | 05 | 좌측 본문 / 불릿 (n=1..3) |
| `{{CARD_n_TITLE}}` / `{{CARD_n_BODY}}` | 06 | 카드 (n=1..3) |
| `{{METRIC_n_VALUE}}` / `{{METRIC_n_LABEL}}` / `{{METRIC_n_DELTA}}` | 07 | 지표 (n=1..3) |
| `{{STATEMENT}}` / `{{STATEMENT_NOTE}}` | 04 | 시그니처 진술문 / 보조 |
| `{{CTA_LABEL}}` | 01 | 인디고 필 라벨 |
| `{{LEGEND_PEAK}}` / `{{LEGEND_OTHERS}}` | 08 | 바 레전드 |
| `{{LEGEND_SERIES_A}}` / `{{LEGEND_SERIES_B}}` | 09 | 라인 레전드 |
| `{{CLOSING_LINE}}` / `{{CONTACT_LINE}}` | 10 | 클로징 카피 / 연락처 |
| `{{BRAND_MARK}}` | 전 페이지 푸터 + 10 대형 마크 | 브랜드명 **텍스트** |
| `{{PAGE_LABEL}}` | 전 페이지 푸터 | 페이지 번호 |

---

## IX. Anti-Pattern Checklist

| ✗ 금지 | 대안 |
| --- | --- |
| 헤드라인 weight 600 이상 | 디스플레이는 300 / 400 |
| 루비·마젠타·셔벗을 버튼·텍스트에 사용 | 그라디언트·차트 전용 |
| 인디고 강조 2곳 이상 | 페이지당 1점 |
| 메시를 본문 페이지에 반복 | `01` / `04`에만 |
| 한 페이지에서 밴드 두 가지 혼용 | 페이지당 서피스 1개 |
| 그림자 | 서피스 대비 + 헤어라인 |
| 숫자 좌측 정렬 | 우측 정렬 + 자릿수 일치 |
| 로고 이미지 번들 | `{{BRAND_MARK}}` 텍스트 슬롯 |
| 한글 런에 라틴 자간 그대로 | §IV 완화 규칙 ×0.5 |
