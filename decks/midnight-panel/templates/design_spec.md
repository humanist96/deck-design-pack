---
deck_id: midnight-panel
kind: deck
native_structure_mode: structured
summary: 니어블랙 다크 프로덕트 덱 — 제품 로드맵, 스프린트 리뷰, 엔지니어링 브리핑, 개발자 대상 발표 (Linear 계열 절제형 다크 UI에서 착안)
canvas_format: ppt169
canvas_width: 1280
canvas_height: 720
canvas_viewbox: "0 0 1280 720"
source_canvas_width: 1280
source_canvas_height: 720
source_viewbox: "0 0 1280 720"
replication_mode: standard
page_count: 10
primary_color: "#5E6AD2"
keywords: [dark, product, engineering, restrained, panel]
defaults:
  mode: briefing
  visual_style: dark-tech
  delivery_purpose: balanced
---

# Midnight Panel — Design Specification

> 원저작 템플릿. 다크 프로덕트 UI 계열(Linear 등)에서 널리 통용되는 **비독점 디자인 원칙** — 니어블랙 서피스 계단, 헤어라인 경계, 단일 채도 악센트 — 을 슬라이드 문법으로 새로 설계했다. 어떤 회사의 상표·로고·워드마크·독점 UI도 복제하거나 번들하지 않는다. 브랜드 표기는 `{{BRAND_MARK}}` 텍스트 슬롯으로만 존재한다. 원 브랜드 폰트는 독점 서체이므로 사용하지 않고, 본 저장소의 install-local Pretendard 락을 따르며 성격은 웨이트·자간·크기로 재현한다.

---

## I. Template Overview

| Property | Description |
| --- | --- |
| **Template Name** | midnight-panel |
| **Display Name** | Midnight Panel |
| **Use Cases** | 제품 로드맵, 스프린트/분기 리뷰, 엔지니어링 브리핑, 개발자 컨퍼런스 세션, 내부 기술 제안 |
| **Design Tone** | 절제, 정밀, 야간 작업실 — 화면이 스스로 빛나되 과시하지 않는다 |
| **Theme Mode** | Dark only — `#010102` 캔버스 고정 |

**Anti-mood** (작도 시점에 거절): "네온 사이버펑크", "그라디언트 SaaS 히어로", "글로우 범벅 대시보드", "다색 카테고리 팔레트", "무지개 차트".

**Litmus test**: 페이지에서 라벤더 악센트를 지웠을 때 위계가 그대로 서 있으면 통과. 악센트는 위계를 *만드는* 도구가 아니라 이미 선 위계에 *신호 하나*를 얹는 도구다.

---

## II. Canvas Specification

| Property | Value |
| --- | --- |
| **Format** | Standard 16:9 (`ppt169`) |
| **Dimensions** | 1280 × 720 px |
| **viewBox** | `0 0 1280 720` |
| **Side margins** | 72px 고정 — 콘텐츠 폭 1136 (x: 72 → 1208) |
| **Footer chrome** | 좌 `{{BRAND_MARK}}` x=72 / 우 `{{PAGE_LABEL}}` x=1208 anchor end, baseline y=676 |

4px 베이스 스페이싱(4/8/12/16/24/32/48), 섹션 간격 96px. 카드 내부 패딩 24px.

---

## III. Color Scheme — LOCKED

이 15개 외의 HEX는 어떤 생성 SVG에도 나타나서는 안 된다.

| Role | HEX | Token | Purpose |
| --- | --- | --- | --- |
| Canvas | `#010102` | `--canvas` | 전 페이지 지배 배경 |
| Surface 1 | `#0f1011` | `--surface-1` | 카드·패널 기본 서피스 |
| Surface 2 | `#141516` | `--surface-2` | 패널 내부 한 단계 리프트 |
| Surface 3 | `#18191a` | `--surface-3` | 차트 비강조 바, 중첩 서피스 |
| Surface 4 | `#191a1b` | `--surface-4` | 최상단 마이크로스텝 |
| Hairline | `#23252a` | `--hairline` | 1px 카드/패널 경계 — 기본 |
| Hairline strong | `#34343a` | `--hairline-strong` | 구분 강조선, 차트 축 |
| Hairline tertiary | `#3e3e44` | `--hairline-3` | 차트 비강조 바 상단, 최약 경계 |
| Accent | `#5e6ad2` | `--accent` | **페이지당 1곳** — 키커·강조 바·피크 데이터 |
| Accent bright | `#828fff` | `--accent-bright` | 악센트 위 미세 하이라이트 (희소) |
| Ink | `#f7f8f8` | `--ink` | 헤드라인·본문 1차 |
| Ink muted | `#d0d6e0` | `--ink-muted` | 본문 2차, 리드 |
| Ink subtle | `#8a8f98` | `--ink-subtle` | 캡션·축 라벨·설명 |
| Ink tertiary | `#62666d` | `--ink-3` | 푸터·번호·최약 라벨 |
| Success | `#27a644` | `--success` | 양(+) 델타 전용 — 그 외 용도 금지 |

### Color Rules

- **악센트는 페이지당 1곳.** 두 번째 라벤더가 등장하는 순간 신호는 장식이 된다
- **깊이는 서피스 계단으로만.** 그림자·글로우·그라디언트 전면 금지 — canvas → surface-1 → surface-2 순으로 올린다
- **경계는 1px 헤어라인.** 굵은 아웃라인·이중 테두리 금지
- **잉크 4단 위계**: `#f7f8f8`(제목/본문) → `#d0d6e0`(리드) → `#8a8f98`(캡션/축) → `#62666d`(푸터/번호). 4단 안에서만 감쇠한다
- **차트 래더**: 피크 1개만 `#5e6ad2`, 나머지는 `#3e3e44` → `#18191a`. 계열 구분은 색이 아니라 선 스타일(실선/점선)
- **Forbidden**: 그라디언트, 그림자, 글로우, 3D, 채도 있는 2차색, `#27a644` 이외의 유채색

---

## IV. Typography System

install-local Pretendard 락. 다크 캔버스 위 강한 음수 자간이 이 시스템의 성격이다.

| Weight | `font-family` attribute |
| --- | --- |
| 400 | `Pretendard, 'Malgun Gothic', sans-serif` |
| 500 | `'Pretendard Medium', Pretendard, 'Malgun Gothic', sans-serif` |
| 600 | `'Pretendard SemiBold', Pretendard, 'Malgun Gothic', sans-serif` |

**웨이트 래더는 400 / 500 / 600 세 단계뿐이다.** 700 이상은 이 로스터에 없다 — 다크 배경에서 굵은 웨이트는 번져 보인다.

### 🔒 본문 baseline 락 — `delivery_purpose` 기본값보다 우선

**이 템플릿의 본문 baseline은 `18`이다.** Strategist는 확인 단계에서 일반 기본값(`text` 20 / `balanced` 24 / `presentation` 32) 대신 아래 네이티브 램프를 추천값으로 제시한다.

**근거**: 이 시스템의 정체성은 *밀도*다. 제품 패널과 데이터가 페이지를 채우고 타입은 물러선다. 본문을 24로 부풀리면 패널 안의 정보가 밀려 나가고, 커버:본문 대비가 4.9→3.7배로 무너져 "그냥 어두운 덱"이 된다. `presentation` 목적일 때는 본문을 최대 22까지만 올리고 커버를 96·페이지 제목을 52로 동반 상향해 대비를 유지한다.

| Role | Size | Weight | Letter-spacing (라틴) | Use |
| --- | --- | --- | --- | --- |
| Cover title | 88 | 600 | -3.2 | 표지 헤드라인 |
| Section title | 72 | 600 | -2.6 | 챕터 헤드라인 |
| Statement | 56 | 600 | -1.8 | 시그니처 진술문 |
| KPI number | 56 | 600 | -1.8 | 지표 대형 숫자 |
| Page title | 44 | 600 | -1.4 | 표준 페이지 제목 |
| Subtitle | 28 | 400 | -0.6 | 표지 서브카피 |
| Lead | 24 | 400 | -0.4 | 페이지 리드 |
| Subheading | 22 | 600 | -0.3 | 카드 제목, 아젠다 항목 |
| Body | 18 | 400 | -0.1 | 본문·카드 설명 |
| Annotation | 15 | 400 | 0 | 캡션·태그·축 라벨 |
| Kicker | 15 | 600 | +1.5 | 대문자 키커 (SVG에 대문자로 저작) |
| Footnote | 13 | 400 | 0 | 푸터·페이지 라벨·번호 |

**자간 완화 규칙**: 표의 값은 라틴 기준이다. 한글 비중 ≥50% 런에는 **×0.5**를 적용한다(88px → -1.6, 44px → -0.7). 양수 자간(키커 +1.5)은 언어 무관하게 유지한다.

---

## V. Page Roster

| File | Layout key | Page Type | Purpose |
| --- | --- | --- | --- |
| `01_cover.svg` | `01_cover` | Cover | 표지 — 악센트 바 + 88px 헤드라인 + 서브카피 |
| `02_agenda.svg` | `02_agenda` | Agenda | 목차 — 헤어라인 5행, 번호·제목·태그 |
| `03_section.svg` | `03_section` | Section | 챕터 전환 — 거의 빈 캔버스 + 72px 헤드라인 |
| `04_panel_showcase.svg` | `04_panel_showcase` | **Signature** | 제품 패널 쇼케이스 — surface-1 프레임 + 추상 UI 크롬 |
| `05_two_column.svg` | `05_two_column` | Content | 좌 텍스트 / 우 패널 2단 |
| `06_card_grid.svg` | `06_card_grid` | Content | 3-up 카드 그리드 |
| `07_metrics.svg` | `07_metrics` | Stat | 3-up 지표 밴드 + 세로 헤어라인 |
| `08_chart_bar.svg` | `chart_linear` | Chart | 6-바 추이 + 피크 1개 악센트 |
| `09_chart_line.svg` | `chart_linear` | Chart | 2계열 추이 (실선/점선) |
| `10_closing.svg` | `10_closing` | Closing | 대형 브랜드 마크 + 클로징 카피 |

`08` / `09`는 고정 Layout 원자와 슬롯 계약이 동일하므로 `chart_linear` 키를 공유한다.

---

## VI. Signature Design Elements

1. **서피스 계단** — 그림자 없이 `#010102` → `#0f1011` → `#141516`로 올려 깊이를 만든다. 카드는 항상 1px `#23252a` 헤어라인을 두른다
2. **단일 라벤더 신호** — `#5e6ad2`는 페이지당 정확히 1곳. 표지 악센트 바, 아젠다 현재 항목, 피크 바, 시그니처 패널의 활성 요소 중 하나만
3. **제품 패널 프레임** — 16px 라운드 + 헤어라인 경계의 surface-1 패널 안에 추상 UI(타이틀바 도트 3개, 사이드바 열, 행 스켈레톤)를 그린다. **실제 제품 스크린샷이 아니라 기하 추상**이다
4. **강한 음수 자간** — 크기가 커질수록 자간을 더 죈다. 88px에 -3.2가 이 시스템의 서명
5. **거의 빈 챕터면** — 챕터 페이지는 헤드라인 하나와 짧은 헤어라인만. 여백이 전환을 알린다

---

## VII. Chart Treatment

- 그리드: 가로 헤어라인 4–5개 `#23252a` 1px. 세로 그리드·플롯 배경·프레임 금지
- 축 라벨: 15px `#8a8f98`. y축 anchor end, x축 anchor middle
- 바: 라운드 4, 피크만 `#5e6ad2`, 나머지 `#3e3e44`
- 라인: 주 계열 실선 2.5px `#5e6ad2` + 데이터 점, 비교 계열 점선 2px `#62666d`
- 레전드: 우상단, 스와치 12px rx3(면) / 24px 선(라인)
- 값 라벨: 15px `#d0d6e0`, 피크만 `#f7f8f8`
- **Forbidden**: 3D, 그림자, 그라디언트 필, 다색 팔레트, 파이

차트 페이지는 `<!-- chart-plot-area: ... -->` 마커를 보유한다:

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
| `{{BODY}}` | 05 | 좌측 본문 |
| `{{POINT_n}}` | 05 | 좌측 불릿 (n=1..3) |
| `{{CARD_n_TITLE}}` / `{{CARD_n_BODY}}` | 06 | 카드 (n=1..3) |
| `{{METRIC_n_VALUE}}` / `{{METRIC_n_LABEL}}` / `{{METRIC_n_DELTA}}` | 07 | 지표 (n=1..3) |
| `{{PANEL_LABEL}}` / `{{PANEL_CAPTION}}` | 04 | 패널 라벨·캡션 |
| `{{LEGEND_PEAK}}` / `{{LEGEND_OTHERS}}` | 08 | 바 레전드 |
| `{{LEGEND_SERIES_A}}` / `{{LEGEND_SERIES_B}}` | 09 | 라인 레전드 |
| `{{CLOSING_LINE}}` / `{{CONTACT_LINE}}` | 10 | 클로징 카피 / 연락처 |
| `{{BRAND_MARK}}` | 전 페이지 푸터 + 10 대형 마크 | 브랜드명 **텍스트** — 로고 이미지가 아니다 |
| `{{PAGE_LABEL}}` | 전 페이지 푸터 | 페이지 번호 또는 섹션 라벨 |

---

## IX. Anti-Pattern Checklist

| ✗ 금지 | 대안 |
| --- | --- |
| 라벤더 악센트 2곳 이상 | 페이지당 1곳 — 나머지는 잉크 4단으로 |
| 그림자 / 글로우 / 그라디언트 | 서피스 계단(canvas→s1→s2)으로 깊이 |
| 웨이트 700 이상 | 래더는 400/500/600 |
| 다색 차트 팔레트 | 피크 1개 악센트 + 그레이 래더, 계열은 선 스타일로 |
| 굵은 카드 아웃라인 | 1px `#23252a` 헤어라인 |
| 라운드 반경 혼용 | 허용값 0 / 4 / 8 / 12 / 16 / 9999 |
| 실제 제품 스크린샷 삽입 | 기하 추상 UI 크롬 |
| 로고 이미지 번들 | `{{BRAND_MARK}}` 텍스트 슬롯 |
| 한글 런에 라틴 자간 그대로 | §IV 완화 규칙 ×0.5 |
