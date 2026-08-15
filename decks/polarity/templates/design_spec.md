---
deck_id: polarity
kind: deck
native_structure_mode: structured
summary: 흑백 극성 반전 개발자 덱 — 기술 발표, 데모데이, 개발자 컨퍼런스, 플랫폼/인프라 소개 (Vercel 계열 모노크롬 + 메시 그라디언트에서 착안)
canvas_format: ppt169
canvas_width: 1280
canvas_height: 720
canvas_viewbox: "0 0 1280 720"
source_canvas_width: 1280
source_canvas_height: 720
source_viewbox: "0 0 1280 720"
replication_mode: standard
page_count: 10
primary_color: "#171717"
keywords: [monochrome, contrast, developer, gradient-mesh, inversion]
defaults:
  mode: showcase
  visual_style: swiss-minimal
  delivery_purpose: balanced
---

# Polarity Mono — Design Specification

> 원저작 템플릿. 개발자 플랫폼 계열에서 널리 쓰이는 **비독점 디자인 원칙** — 흑백 극성 반전, 헤어라인 경계, 단일 메시 그라디언트 오브젝트 — 을 슬라이드 문법으로 새로 설계했다. 어떤 회사의 상표·로고·워드마크·독점 UI도 복제하거나 번들하지 않는다. 브랜드 표기는 `{{BRAND_MARK}}` 텍스트 슬롯으로만 존재한다. 원 브랜드 폰트는 별도 배포 서체이므로 사용하지 않고, 본 저장소의 install-local Pretendard 락을 따른다.

---

## I. Template Overview

| Property | Description |
| --- | --- |
| **Template Name** | polarity |
| **Display Name** | Polarity Mono |
| **Use Cases** | 기술 발표, 데모데이, 개발자 컨퍼런스 세션, 플랫폼·인프라 소개, 오픈소스 프로젝트 발표 |
| **Design Tone** | 명료, 기술적, 자신감 — 설명하지 않고 보여준다 |
| **Theme Mode** | **Dual — 극성 반전.** 콘텐츠는 라이트(`#fafafa`), 챕터·시그니처·클로징은 다크(`#171717`) |

**Anti-mood**: "파스텔 SaaS 마케팅", "일러스트 범벅 랜딩", "다색 카테고리 차트", "라운드 카드 그리드 일변도".

**Litmus test**: 덱을 흑백 인쇄해도 위계가 유지되면 통과. 이 시스템은 애초에 무채색이므로 — **메시 그라디언트를 지웠을 때도 페이지가 성립하는가**를 대신 묻는다. 그라디언트는 분위기이지 구조가 아니다.

---

## II. Canvas Specification

| Property | Value |
| --- | --- |
| **Format** | Standard 16:9 (`ppt169`) |
| **Dimensions** | 1280 × 720 px |
| **viewBox** | `0 0 1280 720` |
| **Side margins** | 72px 고정 — 콘텐츠 폭 1136 (x: 72 → 1208) |
| **Footer chrome** | 좌 `{{BRAND_MARK}}` x=72 / 우 `{{PAGE_LABEL}}` x=1208 anchor end, baseline y=676 |

4px 베이스 스페이싱. 마케팅형 밴드는 64–96px 수직 패딩, 데이터 패널은 32–48px.

---

## III. Color Scheme — LOCKED

이 16개 외의 HEX는 어떤 생성 SVG에도 나타나서는 안 된다.

| Role | HEX | Token | Purpose |
| --- | --- | --- | --- |
| Canvas | `#fafafa` | `--canvas` | 라이트 페이지 배경 |
| Surface | `#ffffff` | `--surface` | 카드·패널 (캔버스보다 밝다) |
| Surface alt | `#f5f5f5` | `--surface-alt` | 2차 서피스, 차트 비강조 |
| Ink | `#171717` | `--ink` | 잉크 · 다크 페이지 배경 · 1차 강조 |
| Ink inverse | `#ffffff` | `--ink-inverse` | 다크 페이지 위 텍스트 |
| Body | `#4d4d4d` | `--body` | 라이트 페이지 본문 |
| Muted | `#888888` | `--muted` | 캡션·축 라벨·비강조 |
| Hairline | `#ebebeb` | `--hairline` | 라이트 1px 경계 |
| Surface dark | `#1f1f1f` | `--surface-dark` | 다크 페이지 위 패널 |
| Hairline dark | `#333333` | `--hairline-dark` | 다크 1px 경계 |
| Mesh A1 | `#007cf0` | `--mesh-a1` | 메시 그라디언트 — 블루 |
| Mesh A2 | `#00dfd8` | `--mesh-a2` | 메시 그라디언트 — 틸 |
| Mesh B1 | `#7928ca` | `--mesh-b1` | 메시 그라디언트 — 바이올렛 |
| Mesh B2 | `#ff0080` | `--mesh-b2` | 메시 그라디언트 — 핑크 |
| Mesh C1 | `#ff4d4d` | `--mesh-c1` | 메시 그라디언트 — 코럴 |
| Mesh C2 | `#f9cb28` | `--mesh-c2` | 메시 그라디언트 — 앰버 |

### Color Rules

- **극성이 구조다.** 챕터 전환은 색이 아니라 **배경 반전**(라이트→다크)으로 알린다. 구분선·장식을 추가하지 않는다
- **메시는 페이지당 1개 오브젝트.** 세 쌍(A/B/C)을 한 덩어리로 배치하며, 여러 곳에 흩뿌리지 않는다. 텍스트 뒤에 오면 반드시 불투명 서피스를 덧댄다
- **강조는 잉크.** 유채색은 메시 그라디언트에만 존재한다 — 텍스트·아이콘·차트 강조에 메시 색을 쓰지 않는다
- **차트는 무채색 래더**: `#171717` → `#888888` → `#ebebeb`. 피크 1개만 잉크
- **Forbidden**: 메시 이외의 그라디언트, 글로우, 그림자(카드 리프트 제외 없음 — 그림자 자체를 쓰지 않는다), 다색 팔레트

---

## IV. Typography System

install-local Pretendard 락. 문장 케이스 + 타이트 음수 자간.

| Weight | `font-family` attribute |
| --- | --- |
| 400 | `Pretendard, 'Malgun Gothic', sans-serif` |
| 500 | `'Pretendard Medium', Pretendard, 'Malgun Gothic', sans-serif` |
| 600 | `'Pretendard SemiBold', Pretendard, 'Malgun Gothic', sans-serif` |

### 🔒 본문 baseline 락 — `delivery_purpose` 기본값보다 우선

**이 템플릿의 본문 baseline은 `20`이다.** 발표 지향이라 midnight-panel(18)보다 크되, 일반 `balanced` 기본값(24)보다는 작다 — 커버:본문 4.2배 대비가 이 시스템의 성격이다. `presentation` 목적일 때만 본문 24 / 커버 96 / 페이지 제목 48로 동반 상향한다.

| Role | Size | Weight | Letter-spacing (라틴) | Use |
| --- | --- | --- | --- | --- |
| Cover title | 84 | 600 | -3.0 | 표지 헤드라인 |
| Section title | 68 | 600 | -2.4 | 챕터 헤드라인 (다크) |
| Statement | 52 | 600 | -1.7 | 시그니처 진술문 (다크) |
| KPI number | 56 | 600 | -1.8 | 지표 대형 숫자 |
| Page title | 42 | 600 | -1.3 | 표준 페이지 제목 |
| Subtitle | 26 | 400 | -0.5 | 표지 서브카피 |
| Lead | 22 | 400 | -0.3 | 페이지 리드 |
| Subheading | 22 | 600 | -0.3 | 카드 제목, 아젠다 항목 |
| Body | 20 | 400 | -0.1 | 본문 |
| Annotation | 16 | 400 | 0 | 캡션·태그·축 라벨 |
| Kicker | 15 | 600 | +1.5 | 대문자 키커 |
| Footnote | 13 | 400 | 0 | 푸터·페이지 라벨 |

**자간 완화 규칙**: 표의 값은 라틴 기준. 한글 비중 ≥50% 런은 **×0.5**(84px → -1.5, 42px → -0.65). 양수 자간은 유지.

---

## V. Page Roster

| File | Layout key | Surface | Purpose |
| --- | --- | --- | --- |
| `01_cover.svg` | `01_cover` | light + mesh | 표지 — 메시 그라디언트 백드롭 + 84px 헤드라인 |
| `02_agenda.svg` | `02_agenda` | light | 목차 — 헤어라인 5행 |
| `03_section.svg` | `03_section` | **dark** | 챕터 전환 — 극성 반전, 68px 헤드라인 |
| `04_polarity_flip.svg` | `04_polarity_flip` | **dark** | **시그니처** — 다크 + 터미널 목업 + 진술문 |
| `05_two_column.svg` | `05_two_column` | light | 좌 텍스트 / 우 카드 스택 |
| `06_card_grid.svg` | `06_card_grid` | light | 3-up 카드 그리드 |
| `07_metrics.svg` | `07_metrics` | light | 3-up 지표 밴드 |
| `08_chart_bar.svg` | `chart_linear` | light | 6-바 추이 + 피크 잉크 |
| `09_chart_line.svg` | `chart_linear` | light | 2계열 추이 (실선/점선) |
| `10_closing.svg` | `10_closing` | **dark** | 클로징 — 극성 반전 + 대형 마크 |

`08` / `09`는 고정 Layout 원자와 슬롯 계약이 동일하므로 `chart_linear` 키를 공유한다.

---

## VI. Signature Design Elements

1. **극성 반전 = 챕터 신호** — `03` / `04` / `10`은 `#171717` 풀블리드. 밝음에서 어둠으로 넘어가는 것 자체가 구분선이며, 별도 장식을 넣지 않는다
2. **단일 메시 오브젝트** — 세 쌍(블루→틸 / 바이올렛→핑크 / 코럴→앰버)을 겹친 하나의 블롭 덩어리. 표지에만 등장하며 본문 페이지에는 없다
3. **2-반경 세계** — 인앱 UI 6px, 카드 8–12px, 마케팅 CTA 풀 필(100). 그 사이 값(15, 20 등)은 쓰지 않는다
4. **터미널 목업** — 다크 시그니처 페이지의 코드/터미널 프레임. 모노스페이스 행을 기하 추상으로 그린다(실제 코드 텍스트가 아니다)
5. **그림자 없음** — 리프트는 서피스 밝기(`#fafafa` → `#ffffff`)와 1px 헤어라인으로만

---

## VII. Chart Treatment

- 그리드: 가로 헤어라인 5개 `#ebebeb` 1px. 세로 그리드·플롯 프레임 금지
- 축 라벨: 16px `#888888`. y축 anchor end, x축 anchor middle
- 바: 라운드 6, 피크만 `#171717`, 나머지 `#ebebeb`
- 라인: 주 계열 실선 2.5px `#171717` + 데이터 점, 비교 계열 점선 2px `#888888`
- 레전드: 우상단, 스와치 12px rx3(면) / 24px 선(라인)
- 값 라벨: 16px `#888888`, 피크만 `#171717`
- **Forbidden**: 메시 색상을 차트에 사용, 3D, 그림자, 다색 팔레트, 파이

| Page | Marker |
| --- | --- |
| `08_chart_bar` | `<!-- chart-plot-area: 160,250,1208,540 -->` |
| `09_chart_line` | `<!-- chart-plot-area: 160,250,1208,540 -->` |

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
| `{{TERMINAL_LABEL}}` / `{{TERMINAL_CAPTION}}` | 04 | 터미널 패널 라벨·캡션 |
| `{{LEGEND_PEAK}}` / `{{LEGEND_OTHERS}}` | 08 | 바 레전드 |
| `{{LEGEND_SERIES_A}}` / `{{LEGEND_SERIES_B}}` | 09 | 라인 레전드 |
| `{{CLOSING_LINE}}` / `{{CONTACT_LINE}}` | 10 | 클로징 카피 / 연락처 |
| `{{BRAND_MARK}}` | 전 페이지 푸터 + 10 대형 마크 | 브랜드명 **텍스트** — 로고 이미지가 아니다 |
| `{{PAGE_LABEL}}` | 전 페이지 푸터 | 페이지 번호 또는 섹션 라벨 |

---

## IX. Anti-Pattern Checklist

| ✗ 금지 | 대안 |
| --- | --- |
| 메시 색을 텍스트·아이콘·차트에 사용 | 메시는 표지 백드롭 전용. 강조는 잉크 |
| 메시를 여러 페이지에 반복 | 페이지당 1개, 표지에만 |
| 그림자 / 글로우 | 서피스 밝기 + 1px 헤어라인 |
| 중간 라운드 값 (15, 20, 24) | 6 / 8 / 12 / 100 만 |
| 챕터 구분에 선·아이콘 추가 | 극성 반전 자체가 구분 |
| 다크 페이지에 `#4d4d4d` 본문 | 다크 위 본문은 `#888888` 이상 밝기 |
| 실제 코드 텍스트를 터미널에 삽입 | 기하 추상 행 |
| 로고 이미지 번들 | `{{BRAND_MARK}}` 텍스트 슬롯 |
| 한글 런에 라틴 자간 그대로 | §IV 완화 규칙 ×0.5 |
