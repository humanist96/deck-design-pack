---
deck_id: signal-green
kind: deck
native_structure_mode: structured
summary: 블랙 히어로 + 시그널 그린 기술 키노트 덱 — AI·GPU·인프라 브리핑, 개발자 세션, 기술 컨퍼런스, 벤치마크 발표 (NVIDIA 계열 앵귤러 지오메트리 + 단일 그린 악센트에서 착안)
canvas_format: ppt169
canvas_width: 1280
canvas_height: 720
canvas_viewbox: "0 0 1280 720"
source_canvas_width: 1280
source_canvas_height: 720
source_viewbox: "0 0 1280 720"
replication_mode: standard
page_count: 10
primary_color: "#76B900"
keywords: [tech-keynote, angular, signal-accent, benchmark, dual-theme]
defaults:
  mode: showcase
  visual_style: dark-tech
  delivery_purpose: presentation
---

# Signal Green — Design Specification

> 원저작 템플릿. 기술 하드웨어·플랫폼 계열에서 널리 통용되는 **비독점 디자인 원칙** — 블랙 히어로와 화이트 콘텐츠의 교대, 2px 앵귤러 지오메트리, 단일 시그널 컬러, 코너 스퀘어 장식 — 을 슬라이드 문법으로 새로 설계했다. 어떤 회사의 상표·로고·워드마크·독점 UI도 복제하거나 번들하지 않는다. 브랜드 표기는 `{{BRAND_MARK}}` 텍스트 슬롯으로만 존재한다. 원 브랜드 폰트는 독점 서체이므로 사용하지 않고, install-local Pretendard 락을 따른다.

---

## I. Template Overview

| Property | Description |
| --- | --- |
| **Template Name** | signal-green |
| **Display Name** | Signal Green |
| **Use Cases** | AI·GPU·인프라 브리핑, 개발자 세션, 기술 컨퍼런스 발표, 벤치마크·성능 리포트, 플랫폼 로드맵 |
| **Design Tone** | 단호하고 기술적 — 성능 수치가 주인공이다 |
| **Theme Mode** | **Dual** — 히어로·챕터·클로징은 `#000000`, 콘텐츠·데이터는 `#FFFFFF` |

**Anti-mood**: "파스텔 SaaS", "라운드 카드 그리드", "그라디언트 히어로", "다색 카테고리 팔레트".

**Litmus test**: 그린을 지웠을 때 페이지가 성립하면 통과. 그린은 **신호**이지 장식이 아니다 — 한 페이지에서 그린이 두 번 이상 나오면 신호가 소음이 된다.

---

## II. Canvas Specification

| Property | Value |
| --- | --- |
| **Format** | Standard 16:9 (`ppt169`) |
| **Dimensions** | 1280 × 720 px |
| **viewBox** | `0 0 1280 720` |
| **Side margins** | 80px — 콘텐츠 폭 1120 (x: 80 → 1200) |
| **Footer chrome** | 좌 `{{BRAND_MARK}}` x=80 / 우 `{{PAGE_LABEL}}` x=1200 anchor end, baseline y=674 |

8px 베이스 스페이싱(2/4/8/12/16/24/32), 섹션 간 64px.

---

## III. Color Scheme — LOCKED

이 11개 외의 HEX는 어떤 생성 SVG에도 나타나서는 안 된다.

| Role | HEX | Token | Purpose |
| --- | --- | --- | --- |
| Black | `#000000` | `--black` | 히어로·챕터·클로징 풀블리드 배경 |
| Surface dark | `#1A1A1A` | `--surface-dark` | 다크 페이지 위 패널 |
| Canvas | `#FFFFFF` | `--canvas` | 콘텐츠 페이지 배경 |
| Surface soft | `#F7F7F7` | `--surface-soft` | 카드·패널 서피스 |
| Hairline | `#CCCCCC` | `--hairline` | 1px 카드 경계, 차트 그리드 |
| Ink | `#000000` | `--ink` | 헤드라인 (라이트 페이지) |
| Body | `#333333` | `--body` | 본문 |
| Muted | `#767676` | `--muted` | 캡션·축 라벨·푸터 |
| Green | `#76B900` | `--green` | **시그널** — 강조 1점, 코너 스퀘어, 차트 피크 |
| Green pressed | `#5A8D00` | `--green-2` | 차트 2계열, 눌린 상태 |
| Green pale | `#BFF230` | `--green-pale` | 다크 서피스 위 보조 강조 (희소) |

### Color Rules

- **그린은 페이지당 정확히 1곳.** 코너 스퀘어 · 규칙선 · 차트 피크 중 하나
- **극성이 구조다** — 블랙 히어로와 화이트 콘텐츠의 교대가 챕터 구분이다. 별도 장식선을 넣지 않는다
- **본문은 `#333333`.** 라이트 페이지에서 순수 검정은 헤드라인 전용
- **다크 페이지 위 본문은 `#767676` 이상 밝기.** `#333333`을 다크 배경에 쓰지 않는다
- **차트 래더**: 피크 `#76B900` → `#5A8D00` → `#CCCCCC`. 세 번째 계열이 필요하면 차트를 나눈다
- **Forbidden**: 그라디언트, 그림자, 글로우, 그린 외 유채색

---

## IV. Typography System

install-local Pretendard 락. **볼드 헤드라인** — 이 시스템은 단호하게 말한다.

| Weight | `font-family` attribute |
| --- | --- |
| 400 | `Pretendard, 'Malgun Gothic', sans-serif` |
| 500 | `'Pretendard Medium', Pretendard, 'Malgun Gothic', sans-serif` |
| 600 | `'Pretendard SemiBold', Pretendard, 'Malgun Gothic', sans-serif` |
| 700 | `Pretendard, 'Malgun Gothic', sans-serif` + `font-weight="700"` |

**헤드라인은 700, 카드 제목·라벨은 600, 본문은 400.** 300 이하는 이 로스터에 없다.

### 🔒 본문 baseline 락 — `delivery_purpose` 기본값보다 우선

**본문 baseline은 `20`이다.** 커버:본문 3.6배. `presentation` 목적일 때만 본문 24 / 커버 84 / 페이지 제목 46으로 동반 상향한다.

| Role | Size | Weight | Letter-spacing (라틴) | Use |
| --- | --- | --- | --- | --- |
| Cover title | 72 | 700 | -2.2 | 표지 헤드라인 (블랙) |
| Section title | 56 | 700 | -1.6 | 챕터 헤드라인 (블랙) |
| Statement | 48 | 700 | -1.4 | 시그니처 진술문 |
| KPI number | 52 | 700 | -1.4 | 지표 대형 숫자 |
| Page title | 40 | 700 | -1.1 | 표준 페이지 제목 |
| Subtitle | 24 | 400 | -0.3 | 표지 서브카피 |
| Lead | 22 | 400 | -0.2 | 페이지 리드 |
| Subheading | 22 | 600 | -0.2 | 카드 제목 |
| Body | 20 | 400 | -0.1 | 본문 |
| Annotation | 16 | 400 | 0 | 캡션·축 라벨 |
| Kicker | 14 | 600 | +1.5 | 대문자 키커 |
| Footnote | 13 | 400 | 0 | 푸터 |

**자간 완화 규칙**: 한글 비중 ≥50% 런은 표의 값 **×0.5**(72px → -1.1). 양수 자간은 유지.

---

## V. Page Roster

| File | Layout key | Surface | Purpose |
| --- | --- | --- | --- |
| `01_cover.svg` | `01_cover` | **black** | 표지 — 블랙 + 72px 볼드 + 그린 규칙선 |
| `02_agenda.svg` | `02_agenda` | white | 목차 — 헤어라인 5행 |
| `03_section.svg` | `03_section` | **black** | 챕터 전환 — 극성 반전 |
| `04_black_hero.svg` | `04_black_hero` | **black** | **시그니처** — 12×12 그린 코너 스퀘어 + 진술문 |
| `05_two_column.svg` | `05_two_column` | white | 좌 텍스트 / 우 패널 스택 |
| `06_card_grid.svg` | `06_card_grid` | white | **4-up** 카드 그리드 (코너 스퀘어 장식) |
| `07_metrics.svg` | `07_metrics` | white | 3-up 지표 밴드 |
| `08_chart_bar.svg` | `chart_linear` | white | 6-바 추이 + 피크 그린 |
| `09_chart_line.svg` | `chart_linear` | white | 2계열 추이 |
| `10_closing.svg` | `10_closing` | **black** | 클로징 — 극성 반전 |

`06`은 팩의 다른 템플릿(3-up)과 달리 **4-up**이다 — 이 시스템의 카드 그리드 문법이 4열이기 때문이다.
`08` / `09`는 고정 Layout 원자와 슬롯 계약이 동일하므로 `chart_linear` 키를 공유한다.

---

## VI. Signature Design Elements

1. **12×12px 그린 코너 스퀘어** — 카드·패널의 좌상단에 놓이는 이 시스템의 서명. 아이콘도 불릿도 아닌 **위치 표식**이다
2. **극성 교대** — 블랙(`01`/`03`/`04`/`10`)과 화이트(`02`/`05`–`09`)가 번갈아 나온다. 어두움이 챕터를 연다
3. **앵귤러 2px** — 카드·버튼·바는 반경 **2px**. 히어로·푸터·풀블리드는 0. 그 사이 값은 쓰지 않는다
4. **단일 시그널** — `#76B900`이 페이지당 1곳. 두 번째 그린은 신호를 소음으로 만든다
5. **볼드 헤드라인 on 블랙** — 700 웨이트 흰 텍스트가 검정 위에서 최대 대비로 선다

---

## VII. Chart Treatment

- 그리드: 가로 헤어라인 5개 `#CCCCCC` 1px. 세로 그리드·플롯 프레임 금지
- 축 라벨: 16px `#767676`. y축 anchor end, x축 anchor middle
- 바: **라운드 2**, 피크만 `#76B900`, 나머지 `#CCCCCC`
- 라인: 주 계열 실선 2.5px `#76B900` + 점, 비교 계열 점선 2px `#767676`
- 레전드: 우상단, 스와치 12px rx2 / 24px 선
- 값 라벨: 16px `#767676`, 피크만 `#000000`
- **Forbidden**: 그림자, 3D, 그라디언트 필, 다색 팔레트, 파이

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
| `{{STATEMENT}}` / `{{STATEMENT_NOTE}}` | 04 | 시그니처 진술문 / 보조 |
| `{{ITEM_n_NO}}` / `{{ITEM_n_TITLE}}` / `{{ITEM_n_TAG}}` | 02 | 아젠다 (n=1..5) |
| `{{BODY}}` / `{{POINT_n}}` | 05 | 좌측 본문 / 불릿 (n=1..3) |
| `{{CARD_n_TITLE}}` / `{{CARD_n_BODY}}` | 06 | 카드 (n=1..**4**) |
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
| 그린 2곳 이상 | 페이지당 1곳 |
| 그린 외 유채색 | 무채색 + 그린 |
| 라운드 8 이상 | 카드·바 2px, 풀블리드 0 |
| 그라디언트 / 그림자 / 글로우 | 평면. 색 대비가 깊이 |
| 다크 배경에 `#333333` 본문 | `#767676` 이상 밝기 |
| 챕터 구분에 선·아이콘 추가 | 블랙/화이트 극성 반전 |
| 코너 스퀘어를 아이콘처럼 사용 | 위치 표식 — 의미를 담지 않는다 |
| 로고 이미지 번들 | `{{BRAND_MARK}}` 텍스트 슬롯 |
| 한글 런에 라틴 자간 그대로 | §IV 완화 규칙 ×0.5 |
