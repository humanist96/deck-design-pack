---
deck_id: koscom-chevron
kind: deck
native_structure_mode: structured
summary: 코스콤 공식 PPT 샘플(Black·Blue·Orange, 2026.06)을 pack 문법으로 재작성한 하우스 덱 — 오렌지 셰브론(›) 모티프, KoPub돋움체 Bold/Medium, 화이트 본문 + 네이비 챕터 + 블랙 시그니처
canvas_format: ppt169
canvas_width: 1280
canvas_height: 720
canvas_viewbox: "0 0 1280 720"
source_canvas_width: 1280
source_canvas_height: 720
source_viewbox: "0 0 1280 720"
replication_mode: standard
page_count: 10
primary_color: "#EE6D1D"
keywords: [koscom, chevron, orange, navy, corporate, capital-market, kopub]
defaults:
  mode: briefing
  visual_style: swiss-minimal
  delivery_purpose: balanced
---

# Koscom Chevron — Design Specification

> **하우스 템플릿.** 코스콤(주)의 공식 발표자료 샘플 3종 — `Koscom PPT Sample_Black / Blue / Orange (2026.06.23)` — 에서 색·서체·간격·페이지 골격을 측정해 pack의 SVG 문법으로 다시 그렸다. 세 샘플은 같은 5페이지 골격(표지·목차·챕터·본문·클로징)을 공유하고 **서피스 색만 다르다.** 이 덱은 셋을 하나의 10페이지 스파인으로 합친다: 본문은 화이트(Orange 샘플), 챕터·클로징은 네이비(Blue 샘플), 시그니처는 블랙(Black 샘플).
>
> 코스콤의 명칭과 셰브론 마크는 코스콤(주)의 자산이다. **로고 이미지는 번들하지 않는다** — 브랜드 표기는 `{{BRAND_MARK}}` 텍스트 슬롯이며, 셰브론은 로고가 아니라 기하 모티프(다각형)로만 쓴다. 실제 로고를 넣으려면 프로젝트 `images/`에 배치하고 표지·푸터의 `{{BRAND_MARK}}` 자리에 직접 참조한다. 서체는 샘플과 동일한 **KoPub돋움체**(한국출판인회의 배포, 무료 라이선스)로 잠근다 — `../fonts/` 참고.
>
> 원본 샘플은 A4(1040×720 상당) 캔버스다. pack의 스파인·검사기와 맞추기 위해 **ppt169(1280×720)로 재배치**했으며, 좌우 여백은 pack 규약인 80px을 따른다(샘플 61px 상당).

---

## I. Template Overview

| Property | Description |
| --- | --- |
| **Template Name** | koscom-chevron |
| **Display Name** | Koscom Chevron |
| **Use Cases** | 회사소개서, 사업 브리핑, 경영 보고, 대외 제안서, 채용 설명회 — 코스콤 및 자본시장 IT 문맥의 공식 발표 |
| **Design Tone** | 단정하고 명확한 공기업형 코퍼레이트 — 굵은 KoPub 헤드라인, 넉넉한 여백, 한 방향(›)으로 밀어주는 셰브론 |
| **Theme Mode** | Light 본문 + Navy 앵커 + Black 시그니처 |

**Anti-mood**: "스타트업 그라디언트", "둥근 카드 범벅", "파스텔 다색", "그림자·글로우".

**Litmus test**: 셰브론을 전부 지웠을 때 페이지가 단정한 문서로 성립하면 통과. 셰브론은 앵커 페이지(표지·챕터·클로징)의 **방향 신호**이지 본문의 장식이 아니다.

---

## II. Canvas Specification

| Property | Value |
| --- | --- |
| **Format** | Standard 16:9 (`ppt169`) |
| **Dimensions** | 1280 × 720 px |
| **viewBox** | `0 0 1280 720` |
| **Side margins** | 80px — 콘텐츠 폭 1120 (x: 80 → 1200) |
| **Header zone (본문 페이지)** | 키커 baseline 96 / 페이지 제목 baseline 144 / 리드 baseline 190 |
| **Footer chrome** | 좌 `{{BRAND_MARK}}` x=80 (KoPub Bold 14) / 우 `{{PAGE_LABEL}}` x=1200 anchor end (13), baseline y=674 |

8px 베이스 스페이싱. 카드 간격 32, 카드 내부 패딩 28~32. **모서리는 각지게(rx 0)** — 셰브론의 각과 맞춘다. 원형은 번호 원(r=12)에만 허용.

---

## III. Color Scheme — LOCKED

이 19개 외의 HEX는 어떤 생성 SVG에도 나타나서는 안 된다.

| Role | HEX | Token | Purpose |
| --- | --- | --- | --- |
| Canvas | `#ffffff` | `--canvas` | 본문 페이지 배경 |
| Surface | `#f5f5f7` | `--surface` | 카드·패널 연회색 |
| Hairline | `#dcdce0` | `--hairline` | 1px 카드·표·행 경계, 차트 비강조 바 |
| Chevron grey | `#ececee` | `--chevron-grey` | 표지·목차의 뒤쪽 회색 셰브론 전용 |
| Orange | `#ee6d1d` | `--orange` | **주색** — 페이지 제목, 키커, 번호 원, 지표 패널, 차트 피크 |
| Orange deep | `#f26522` | `--orange-deep` | 대형 셰브론 채움 (앵커 페이지 전용) |
| Orange tint | `#fad3bb` | `--orange-tint` | 카드 헤더 밴드, 오렌지 패널 위 보조 텍스트 |
| Orange pale | `#fdeee4` | `--orange-pale` | 표지의 연오렌지 셰브론 전용 |
| Navy | `#00338d` | `--navy` | 챕터·클로징 풀블리드 |
| Navy mid | `#1f4b9b` | `--navy-mid` | 네이비 위 뒤쪽 셰브론 |
| Navy soft | `#0f499c` | `--navy-soft` | 네이비 위 중간 셰브론 |
| Blue tint | `#edf4fb` | `--blue-tint` | 네이비 위 보조 텍스트·푸터 |
| Black | `#000000` | `--black` | 시그니처 페이지 배경 |
| Wave dim | `#7a3a10` | `--wave-dim` | 시그니처 웨이브 라인 (먼 층) |
| Wave mid | `#b85415` | `--wave-mid` | 시그니처 웨이브 라인 (중간 층) |
| Ink | `#2b2b2e` | `--ink` | 헤드라인·본문 1차 |
| Ink secondary | `#6e6e73` | `--ink-2` | 본문 2차·표지 서브카피 |
| Grey | `#8c8c92` | `--grey` | 캡션·태그·축 라벨·푸터 |
| White | `#ffffff` | `--white` | 네이비·블랙·오렌지 위 텍스트 |

### Color Rules

- **오렌지는 구조색이다.** 본문 페이지에서 오렌지는 페이지 제목·키커·번호 원·카드 제목처럼 *위계를 표시하는 자리*에만 쓴다. 본문 페이지에서 번호 원보다 큰 오렌지 면은 `07_metrics`의 강조 패널 하나뿐이다
- **대형 오렌지 면(`#f26522` 셰브론)은 앵커 페이지 전용** — 표지·챕터·클로징. 본문 페이지에 셰브론을 올리지 않는다
- **서피스는 페이지당 하나.** 화이트 / 네이비 / 블랙을 한 페이지에서 섞지 않는다
- **네이비 위 계층은 `#1f4b9b` → `#0f499c` → `#f26522` 순**으로 뒤에서 앞으로 쌓는다 (Blue 샘플의 반투명 셰브론을 사전 합성한 값)
- **그림자·그라디언트 금지.** 리프트는 `#f5f5f7` 서피스와 1px `#dcdce0` 헤어라인으로만
- **차트 래더**: 피크 `#ee6d1d`, 나머지 `#dcdce0`. 비교 계열은 `#8c8c92` 점선. 다색 팔레트 금지
- **성공/위험 색이 없다.** 증가 델타는 오렌지, 감소·중립은 그레이

### 공식 3종 서피스와의 대응

| 샘플 | 이 덱에서의 자리 | 변형 방법 |
| --- | --- | --- |
| Orange (화이트 캔버스 + 오렌지 셰브론) | `01` `02` `05`–`09` | 기본 |
| Blue (네이비 캔버스 + 오렌지 셰브론) | `03` `10` | `layout-bg-navy`를 `#ee6d1d`로 바꾸면 Orange 샘플의 챕터 페이지 |
| Black (블랙 캔버스 + 오렌지 웨이브) | `04` | 표지를 블랙으로 쓰려면 `01`의 셰브론 대신 `04`의 웨이브 원자를 옮긴다 |

---

## IV. Typography System

샘플과 동일하게 **KoPub돋움체**로 잠근다. Bold가 헤드라인과 강조, Medium이 본문·키커, Light는 쓰지 않는다(샘플에 없음). 폴백은 Pretendard → Malgun Gothic.

| Weight | `font-family` attribute |
| --- | --- |
| Bold | `'KoPub돋움체 Bold', 'KoPubDotum Bold', Pretendard, 'Malgun Gothic', sans-serif` |
| Medium | `'KoPub돋움체 Medium', 'KoPubDotum Medium', Pretendard, 'Malgun Gothic', sans-serif` |

**헤드라인은 Bold다.** pack의 다른 덱과 달리 이 시스템의 성격은 굵은 KoPub 헤드라인과 넉넉한 여백의 대비에서 나온다. 얇은 디스플레이 웨이트로 바꾸는 순간 코스콤 자료로 읽히지 않는다.

### 🔒 본문 baseline 락 — `delivery_purpose` 기본값보다 우선

**본문 baseline은 `16`이다** (샘플 11pt ≈ 15px). 표지:본문 = 52/16 = 3.25배. `presentation` 목적일 때만 본문 20 / 표지 60 / 페이지 제목 36으로 동반 상향한다.

| Role | Size | Weight | Letter-spacing (라틴) | Use |
| --- | --- | --- | --- | --- |
| Section number | 128 | Bold | -2 | 챕터 번호 (`02`) |
| Brand mark (closing) | 60 | Bold | -0.5 | 클로징 대형 마크 |
| Statement | 56 | Bold | -0.5 | 시그니처 진술문 |
| KPI number | 56 | Bold | -1 | 지표 대형 숫자 |
| Cover title | 52 | Bold | -0.5 | 표지 헤드라인 (2행 허용) |
| Section title | 48 | Bold | -0.5 | 챕터 제목, 목차 제목 |
| Agenda number | 44 | Bold | 0 | 목차 번호 (오렌지) |
| Statement title | 34 | Bold | 0 | 시그니처 페이지 제목 |
| Page title | 30 | Bold | 0 | 본문 페이지 제목 (오렌지) |
| Agenda title | 24 | Bold | 0 | 목차 항목 |
| Closing line | 24 | Bold | 0 | 클로징 카피 |
| Lead | 18 | Medium | 0 | 페이지 리드, 챕터 리드, 표지 서브카피 |
| Card title | 17–18 | Bold | 0 | 카드 제목 |
| Body | 16 | Medium | 0 | 본문·불릿·카드 본문 |
| Kicker | 15 | Medium | +4 (`CHAPTER`는 +5) | 대문자 키커 — 항상 8×26 오렌지 바와 함께 |
| Annotation | 14 | Medium | 0 | 캡션·축 라벨·델타·페이지 키커 |
| Footnote | 13–14 | Medium/Bold | 0 | 푸터 |

**자간 완화 규칙**: 한글 비중 ≥50% 런은 표의 음수 값을 **×0.5**. 양수 자간(키커)은 유지. KoPub돋움체는 기본 자폭이 넓지 않아 헤드라인 음수 자간을 -0.5 이상으로 조이지 않는다.

---

## V. Page Roster

| File | Layout key | Surface | Purpose |
| --- | --- | --- | --- |
| `01_cover.svg` | `01_cover` | white + chevrons | 표지 — 좌상단 브랜드 마크, 키커 바, 52px 헤드라인, 우측 셰브론 3겹 |
| `02_agenda.svg` | `02_agenda` | white | 목차 — 좌 제목 블록 / 우 5행(44px 번호 + 제목 + 태그), 우하단 회색 셰브론 |
| `03_section.svg` | `03_section` | **navy** | 챕터 전환 — 128px 번호 + `CHAPTER` + 제목 + 리드, 우측 셰브론 3겹 |
| `04_wave_statement.svg` | `04_wave_statement` | **black** | **시그니처** — 블랙 필드 위 오렌지 웨이브 라인 14줄 + 56px 진술문 |
| `05_two_column.svg` | `05_two_column` | white | 좌 본문 + 번호 포인트 3 / 우 번호 카드 3 |
| `06_card_grid.svg` | `06_card_grid` | white | 3-up 카드 — 오렌지 틴트 헤더 밴드 + 번호 원 |
| `07_metrics.svg` | `07_metrics` | white | 3-up 지표 — 3번째 패널 오렌지 |
| `08_chart_bar.svg` | `chart_linear` | white | 6-바 추이, 피크 오렌지, 각진 바 |
| `09_chart_line.svg` | `chart_linear` | white | 2계열 추이 — 오렌지 실선 + 그레이 점선 |
| `10_closing.svg` | `10_closing` | **navy** | 클로징 — 60px 브랜드 마크 + 오렌지 룰 + 카피·연락처, 셰브론 1개 |

`08` / `09`는 고정 Layout 원자(축 룰)와 슬롯 계약이 동일하므로 `chart_linear` 키를 공유한다. → **1 Master · 9 Layouts**

### 고정 Layout 원자 (레이아웃 식별 근거)

| Layout | 고정 원자 |
| --- | --- |
| `01_cover` | 셰브론 3개 (grey / pale / orange-deep) |
| `02_agenda` | 목록 상단 2px 잉크 룰 (x 540→1200) + 우하단 회색 셰브론 |
| `03_section` | 네이비 배경 + 셰브론 3개 (navy-mid / navy-soft / orange-deep) |
| `04_wave_statement` | 블랙 배경 + 웨이브 패스 14개 |
| `05_two_column` | 컬럼 디바이더 헤어라인 (x=640) |
| `06_card_grid` | 헤더 1px 잉크 룰 (y=222) |
| `07_metrics` | 오렌지 강조 패널 (848,300 352×240) |
| `chart_linear` | x축 1px 잉크 룰 (y=540) |
| `10_closing` | 네이비 배경 + 셰브론 2개 (navy-mid / orange-deep) |

---

## VI. Signature Design Elements

1. **셰브론(›) 모티프** — 하우스 마크의 꺾쇠를 다각형으로 옮긴 것. 단위 형상은 565×760, 팔 두께 240. 항상 오른쪽을 가리키며 캔버스 우측 밖으로 잘려 나간다. 표지는 grey → pale → orange-deep 3겹, 챕터는 navy-mid → navy-soft → orange-deep 3겹, 클로징은 2겹. **본문 페이지에는 올리지 않는다**
2. **키커 바** — 8×26 오렌지 세로 바 + 대문자 키커(자간 +4). 표지·목차·시그니처에서 키커는 항상 이 바와 함께 온다
3. **굵은 KoPub 헤드라인** — 위계는 굵기가 아니라 크기 램프(128 / 52 / 48 / 30)로 만든다. 헤드라인은 전부 Bold
4. **번호 원** — r=12 오렌지 원 + 13px 흰 숫자. 샘플의 다이어그램 번호(①②③) 문법. 목록·카드·다이어그램의 순서 표시는 불릿 대신 이것을 쓴다
5. **웨이브 필드** — 시그니처 전용. 블랙 위에 1px 오렌지 사인 곡선 14줄을 `#7a3a10` → `#b85415` → `#ee6d1d`로 층을 나눠 깊이를 만든다. 래스터 이미지가 아니라 패스다
6. **각진 기하** — 카드·패널·바 모두 rx 0. 둥근 것은 번호 원뿐

`{{STATEMENT}}` 카피 예산: 56px 기준 **한글 12자 이내**. 더 길면 본문 페이지로 옮긴다.

---

## VII. Chart Treatment

- 그리드: 가로 헤어라인 4개 `#dcdce0` 1px + x축 잉크 룰 1px (Layout 원자). 세로 그리드·플롯 프레임 금지
- 축 라벨: 14px KoPub Medium `#8c8c92`. y축 anchor end, x축 anchor middle
- 바: **각진 사각형**(rx 0), 폭 116, 피크만 `#ee6d1d`, 나머지 `#dcdce0`
- 라인: 주 계열 실선 2.5px `#ee6d1d` + 흰 채움 점(r=4, 마지막 점만 오렌지 채움 r=5), 비교 계열 점선 2px `#8c8c92`
- 레전드: 우상단 y=142, 스와치 12px 각진 사각형 / 24px 선
- 값 라벨: 14px KoPub Bold `#8c8c92`, 피크만 `#2b2b2e`
- **Forbidden**: 그림자, 3D, 다색 팔레트, 파이, 라운드 바

| Page | Marker |
| --- | --- |
| `08_chart_bar` | `<!-- chart-plot-area: 168,250,1200,540 -->` |
| `09_chart_line` | `<!-- chart-plot-area: 168,250,1200,540 -->` |

---

## VIII. Placeholder Vocabulary

| Token | Pages | Content |
| --- | --- | --- |
| `{{TITLE}}` | 01–09 | 페이지 헤드라인 (title 슬롯) |
| `{{KICKER}}` | 01–09 | 대문자 키커 (`2026 COMPANY PROFILE`, `CONTENTS`, `CHAPTER`, `02. Our Market Role` …) |
| `{{SUBTITLE}}` | 01 / 02 | 표지 서브카피 (subtitle 슬롯) / 목차 영문 부제 |
| `{{META_LINE}}` | 01 | 날짜 · 부서 (`2026. 6. 23 ｜ 경영기획부`) |
| `{{SECTION_NO}}` | 03 | 챕터 번호 (`02`) |
| `{{LEAD}}` | 03 / 05–09 | 페이지 리드 1행 |
| `{{ITEM_n_NO}}` / `{{ITEM_n_TITLE}}` / `{{ITEM_n_TAG}}` | 02 | 목차 (n=1..5) |
| `{{STATEMENT}}` / `{{STATEMENT_NOTE}}` | 04 | 시그니처 진술문 / 보조 |
| `{{COL_A_TITLE}}` / `{{COL_B_TITLE}}` | 05 | 좌·우 컬럼 헤더 |
| `{{BODY}}` / `{{POINT_n}}` | 05 | 좌측 본문 / 번호 포인트 (n=1..3) |
| `{{CARD_n_TITLE}}` / `{{CARD_n_BODY}}` | 05 / 06 | 카드 (n=1..3) |
| `{{METRIC_n_VALUE}}` / `{{METRIC_n_LABEL}}` / `{{METRIC_n_DELTA}}` | 07 | 지표 (n=1..3) |
| `{{LEGEND_PEAK}}` / `{{LEGEND_OTHERS}}` | 08 | 바 레전드 |
| `{{LEGEND_SERIES_A}}` / `{{LEGEND_SERIES_B}}` | 09 | 라인 레전드 |
| `{{CLOSING_LINE}}` / `{{CONTACT_LINE}}` | 10 | 클로징 카피 / 연락처 |
| `{{BRAND_MARK}}` | 전 페이지 푸터 + 01 좌상단 + 10 대형 마크 | 브랜드명 **텍스트** (`koscom`) |
| `{{PAGE_LABEL}}` | 전 페이지 푸터 | 페이지 번호 |

---

## IX. Anti-Pattern Checklist

| ✗ 금지 | 대안 |
| --- | --- |
| 본문 페이지에 셰브론 | 셰브론은 `01` `02` `03` `10`에만 |
| 헤드라인을 Light/Regular로 | 헤드라인은 Bold — 위계는 크기 램프로 |
| 둥근 카드(rx>0)·둥근 바 | rx 0. 둥근 것은 번호 원뿐 |
| 한 페이지에 서피스 두 가지 | 화이트 / 네이비 / 블랙 중 하나 |
| 오렌지 대형 면을 본문에 | 본문의 오렌지는 제목·번호 원·`07` 패널까지 |
| 그림자·그라디언트·글로우 | 서피스 대비 + 1px 헤어라인 |
| 녹색/빨강 델타 | 증가 오렌지, 감소·중립 그레이 |
| 로고 이미지 번들 | `{{BRAND_MARK}}` 텍스트 슬롯 — 실제 로고는 프로젝트 `images/`에서 참조 |
| 웨이브를 래스터 이미지로 | `04`의 패스 원자를 그대로 쓴다 |
| 한글 런에 라틴 자간 그대로 | §IV 완화 규칙 ×0.5 |
