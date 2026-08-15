---
deck_id: open-road
kind: deck
native_structure_mode: structured
summary: 시네마틱 풀블리드 사진 키노트 덱 — 제품 런칭, 브랜드 키노트, 비전 발표, 쇼룸/전시 프레젠테이션 (Tesla 계열 갤러리형 여백 + 카본 다크 구분면에서 착안)
canvas_format: ppt169
canvas_width: 1280
canvas_height: 720
canvas_viewbox: "0 0 1280 720"
source_canvas_width: 1280
source_canvas_height: 720
source_viewbox: "0 0 1280 720"
replication_mode: standard
page_count: 10
primary_color: "#3E6AE1"
keywords: [cinematic, photography, keynote, gallery, launch]
defaults:
  mode: showcase
  visual_style: photo-editorial
  delivery_purpose: presentation
---

# Open Road — Design Specification

> 원저작 템플릿. 프리미엄 제품 브랜드 계열에서 널리 통용되는 **비독점 디자인 원칙** — 한 화면 한 메시지, 풀블리드 시네마틱 사진, 각진 지오메트리, 카본 다크 구분면 — 을 슬라이드 문법으로 새로 설계했다. 어떤 회사의 상표·로고·워드마크·제품 형상도 복제하거나 번들하지 않는다. **사진 자산을 번들하지 않으며**, 사진 자리는 `ltUpDiag` 패턴 플레이스홀더로 표시한다. 브랜드 표기는 `{{BRAND_MARK}}` 텍스트 슬롯으로만 존재한다. 원 브랜드 폰트는 상용 서체이므로 사용하지 않고, install-local Pretendard 락을 따른다.

---

## I. Template Overview

| Property | Description |
| --- | --- |
| **Template Name** | open-road |
| **Display Name** | Open Road |
| **Use Cases** | 제품 런칭, 브랜드 키노트, 비전 발표, 쇼룸·전시 프레젠테이션, 신사업 소개 |
| **Design Tone** | 확신에 차고 조용함 — 갤러리처럼 한 번에 하나만 보여준다 |
| **Theme Mode** | Light + 카본 다크 구분면 — `#FFFFFF` 본문, `#171A20` 챕터·클로징 |

**Anti-mood**: "정보 밀집 컨설팅 그리드", "다색 인포그래픽", "그림자 카드 더미", "라운드 파스텔 SaaS".

**Litmus test**: 슬라이드에서 문장을 하나 더 빼도 의미가 남으면 **더 빼라.** 이 시스템은 한 페이지 한 메시지다 — 두 번째 메시지가 필요하면 페이지를 나눈다.

---

## II. Canvas Specification

| Property | Value |
| --- | --- |
| **Format** | Standard 16:9 (`ppt169`) |
| **Dimensions** | 1280 × 720 px |
| **viewBox** | `0 0 1280 720` |
| **Side margins** | **96px** — 콘텐츠 폭 1088 (x: 96 → 1184). 팩 중 가장 넓다 (갤러리 여백) |
| **Footer chrome** | 좌 `{{BRAND_MARK}}` x=96 / 우 `{{PAGE_LABEL}}` x=1184 anchor end, baseline y=672 |

8px 베이스 스페이싱(8/16/24/32/48/64/96). 블록 간격은 최소 48px — 채우지 않는다.

---

## III. Color Scheme — LOCKED

이 10개 외의 HEX는 어떤 생성 SVG에도 나타나서는 안 된다.

| Role | HEX | Token | Purpose |
| --- | --- | --- | --- |
| Canvas | `#FFFFFF` | `--canvas` | 본문 페이지 배경 |
| Surface | `#F4F4F4` | `--surface` | 카드·패널 서피스 |
| Cloud gray | `#EEEEEE` | `--cloud` | 1px 구분선, 차트 비강조 바 |
| Silver fog | `#8E8E8E` | `--silver` | 플레이스홀더 안내, 차트 2계열 |
| Pewter | `#5C5E62` | `--pewter` | 캡션·축 라벨·푸터 |
| Graphite | `#393C41` | `--graphite` | **본문** |
| Carbon | `#171A20` | `--carbon` | 헤드라인 · 챕터/클로징 풀블리드 배경 |
| Electric | `#3E6AE1` | `--electric` | **주색** — CTA, 강조 1점, 차트 피크 |
| Ink inverse | `#FFFFFF` | `--ink-inverse` | 다크 서피스 위 텍스트 |
| Hatch fg | `#393C41` | `--hatch-fg` | 사진 플레이스홀더 해칭 전경 |

### Color Rules

- **한 페이지 한 강조.** `#3E6AE1`은 CTA 또는 차트 피크 중 하나에만
- **본문은 `#393C41`, 헤드라인은 `#171A20`.** 순수 검정을 쓰지 않는다
- **그림자 금지.** 이 시스템의 깊이는 **사진**에서 온다. 카드는 `#F4F4F4` 서피스와 `#EEEEEE` 1px 선으로만 구분한다
- **차트는 근사 무채색**: 피크 `#3E6AE1`, 나머지 `#EEEEEE`, 2계열 `#8E8E8E`. 세 번째 계열이 필요하면 차트를 나눈다
- **Forbidden**: 그라디언트, 그림자, 글로우, 유채색 2개 이상

---

## IV. Typography System

install-local Pretendard 락. **미디엄 웨이트 중심** — 굵게 외치지 않는다.

| Weight | `font-family` attribute |
| --- | --- |
| 400 | `Pretendard, 'Malgun Gothic', sans-serif` |
| 500 | `'Pretendard Medium', Pretendard, 'Malgun Gothic', sans-serif` |
| 600 | `'Pretendard SemiBold', Pretendard, 'Malgun Gothic', sans-serif` |

**헤드라인은 500이 기본, 600은 지표 숫자에만.** 700 이상은 이 로스터에 없다 — 큰 텍스트를 굵게 만들면 갤러리의 정적이 깨진다.

### 🔒 본문 baseline 락 — `delivery_purpose` 기본값보다 우선

**본문 baseline은 `20`이다.** 페이지당 텍스트가 적어 20으로 충분하며, 커버:본문 3.6배 대비가 여백을 살린다. `presentation` 목적일 때만 본문 24 / 커버 84 / 페이지 제목 46으로 동반 상향한다.

| Role | Size | Weight | Letter-spacing (라틴) | Use |
| --- | --- | --- | --- | --- |
| Cover title | 72 | 500 | -2 | 표지 헤드라인 (사진 위) |
| Section title | 56 | 500 | -1.5 | 챕터 헤드라인 (카본) |
| Statement | 44 | 500 | -1.1 | 시그니처 한 문장 |
| KPI number | 52 | 600 | -1.4 | 지표 대형 숫자 |
| Page title | 40 | 500 | -1 | 표준 페이지 제목 |
| Subtitle | 24 | 400 | -0.3 | 표지 서브카피 |
| Lead | 22 | 400 | -0.2 | 페이지 리드 |
| Subheading | 22 | 500 | -0.2 | 카드 제목 |
| Body | 20 | 400 | -0.1 | 본문 |
| Annotation | 16 | 400 | 0 | 캡션·축 라벨 |
| Kicker | 14 | 500 | +1.5 | 대문자 키커 |
| Footnote | 13 | 400 | 0 | 푸터·플레이스홀더 안내 |

**자간 완화 규칙**: 한글 비중 ≥50% 런은 표의 값 **×0.5**(72px → -1). 양수 자간은 유지.

---

## V. Page Roster

| File | Layout key | Surface | Purpose |
| --- | --- | --- | --- |
| `01_cover.svg` | `01_cover` | **photo** | 표지 — 풀블리드 사진 + 하단 좌측 타이틀 스택 |
| `02_agenda.svg` | `02_agenda` | white | 목차 — 구분선 5행 |
| `03_section.svg` | `03_section` | **carbon** | 챕터 전환 — 카본 다크 |
| `04_fullbleed_hero.svg` | `04_fullbleed_hero` | **photo** | **시그니처** — 풀블리드 사진 + 중앙 한 문장 |
| `05_two_column.svg` | `05_two_column` | white | 좌 텍스트 / 우 이미지 블록 |
| `06_card_grid.svg` | `06_card_grid` | white | 3-up 카드 그리드 |
| `07_metrics.svg` | `07_metrics` | white | 3-up 지표 밴드 |
| `08_chart_bar.svg` | `chart_linear` | white | 6-바 추이 + 피크 일렉트릭 |
| `09_chart_line.svg` | `chart_linear` | white | 2계열 추이 |
| `10_closing.svg` | `10_closing` | **carbon** | 클로징 — 카본 다크 |

`08` / `09`는 고정 Layout 원자와 슬롯 계약이 동일하므로 `chart_linear` 키를 공유한다.

---

## VI. Signature Design Elements

1. **한 페이지 한 메시지** — 시그니처 페이지(`04`)는 사진 한 장과 문장 하나뿐이다. 불릿·카드·아이콘을 얹지 않는다
2. **풀블리드 사진 = 페이지 자체** — `01`/`04`는 사진이 캔버스 가장자리까지 닿는다. 라운딩 0, 프레임 없음
3. **각진 지오메트리** — 기본 반경 0. 버튼 4, 카테고리 카드 12. 그 사이 값은 쓰지 않는다
4. **카본 구분면** — 챕터·클로징은 `#171A20` 풀블리드. 밝은 본문 사이의 정지 화면
5. **96px 여백** — 팩에서 가장 넓은 마진. 채우고 싶은 충동을 규율로 막는다

### 사진 플레이스홀더 계약

사진 자산은 **번들하지 않는다.** 자리는 `ltUpDiag` 프리셋 패턴으로 표시한다:

```xml
<pattern id="photo-hatch" patternUnits="userSpaceOnUse" width="20" height="20"
         patternTransform="rotate(45)" data-pptx-pattern="ltUpDiag">
  <rect width="20" height="20" fill="#171A20"/>
  <rect width="10" height="20" fill="#393C41"/>
</pattern>
```

- 사용: `<rect ... fill="url(#photo-hatch)"/>`
- 안내 라벨은 13px `#8E8E8E` 중앙 — 리터럴 안내문
- **실사진으로 교체할 때 해칭 rect를 `<image href="../images/...">`로 대체한다.** 사진은 저채도 시네마틱 그레이드, 헤비 그레인 금지

---

## VII. Chart Treatment

- 그리드: 가로 구분선 5개 `#EEEEEE` 1px. 세로 그리드·플롯 프레임 금지
- 축 라벨: 16px `#5C5E62`. y축 anchor end, x축 anchor middle
- 바: **라운드 0** (각진 시스템), 피크만 `#3E6AE1`, 나머지 `#EEEEEE`
- 라인: 주 계열 실선 2.5px `#3E6AE1` + 점, 비교 계열 점선 2px `#8E8E8E`
- 레전드: 우상단, 스와치 12px rx0 / 24px 선
- 값 라벨: 16px `#5C5E62`, 피크만 `#171A20`
- **Forbidden**: 그림자, 3D, 그라디언트 필, 다색 팔레트, 파이

| Page | Marker |
| --- | --- |
| `08_chart_bar` | `<!-- chart-plot-area: 184,250,1184,540 -->` |
| `09_chart_line` | `<!-- chart-plot-area: 184,250,1184,540 -->` |

---

## VIII. Placeholder Vocabulary

| Token | Pages | Content |
| --- | --- | --- |
| `{{TITLE}}` | 01–09 | 페이지 헤드라인 |
| `{{KICKER}}` | 01/03/04/07 | 대문자 키커 |
| `{{SUBTITLE}}` | 01 | 표지 서브카피 |
| `{{LEAD}}` | 05/06/07 | 페이지 리드 1행 |
| `{{STATEMENT}}` | 04 | 시그니처 한 문장 |
| `{{ITEM_n_NO}}` / `{{ITEM_n_TITLE}}` / `{{ITEM_n_TAG}}` | 02 | 아젠다 (n=1..5) |
| `{{BODY}}` / `{{POINT_n}}` | 05 | 좌측 본문 / 불릿 (n=1..3) |
| `{{CAPTION}}` | 05 | 우측 이미지 캡션 |
| `{{CARD_n_TITLE}}` / `{{CARD_n_BODY}}` | 06 | 카드 (n=1..3) |
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
| 시그니처 페이지에 두 번째 메시지 | 페이지를 나눈다 |
| 헤드라인 weight 600 이상 | 500 (지표 숫자만 600) |
| 그림자 / 그라디언트 | 사진이 깊이를 만든다 |
| 중간 라운드 값 (6, 8, 16) | 0 / 4 / 12 만 |
| 사진 위 라운드 프레임 | 풀블리드, 라운딩 0 |
| 유채색 2개 이상 | 일렉트릭 1점 |
| 사진 자산 번들 | `ltUpDiag` 패턴 플레이스홀더 |
| 로고 이미지 번들 | `{{BRAND_MARK}}` 텍스트 슬롯 |
| 96px 마진 축소해 밀도 올리기 | 여백이 이 시스템의 정체성 |
| 한글 런에 라틴 자간 그대로 | §IV 완화 규칙 ×0.5 |
