---
brand_id: koscom-chevron
kind: brand
summary: 코스콤 하우스 아이덴티티 — 오렌지 셰브론(›) 모티프, 네이비 앵커, KoPub돋움체 Bold 헤드라인, 각진 기하
keywords: [koscom, chevron, orange, navy, corporate, capital-market, kopub]
primary_color: "#EE6D1D"
---

# Koscom Chevron — Brand Specification

> Identity-only preset. 페이지 로스터가 없다 — 이 제약 아래에서 페이지는 자유롭게 구성한다.
>
> **Provenance**: [`templates/decks/koscom-chevron/`](../../../decks/koscom-chevron/templates/design_spec.md)에서 아이덴티티 세그먼트만 추출했다(덱이 source of truth). 색·타이포·보이스 변경은 덱에서 먼저 고치고 이 파일에 동기화한다. 페이지 구조·크기 램프·마진은 덱 소관이며 여기 기록하지 않는다.
>
> 하우스 아이덴티티. 코스콤(주) 공식 발표자료 샘플(2026.06)에서 측정한 값이며, 코스콤의 명칭과 셰브론 마크는 코스콤(주)의 자산이다. 로고 이미지는 번들하지 않고 브랜드 표기는 텍스트 슬롯으로만 존재한다.

## I. Brand Overview

| Property | Value |
|---|---|
| Brand Name | Koscom Chevron |
| Use Cases | 회사소개서, 사업 브리핑, 경영 보고, 대외 제안서, 채용 설명회 — 코스콤 및 자본시장 IT 문맥 |
| Tone | 단정하고 명확한 공기업형 코퍼레이트 — 굵은 헤드라인, 넉넉한 여백, 한 방향으로 밀어주는 셰브론 |

**Anti-mood**: "스타트업 그라디언트", "둥근 카드 범벅", "파스텔 다색", "그림자·글로우".

**Companion deck**: 페이지 로스터까지 함께 쓰려면 [`templates/decks/koscom-chevron/`](../../../decks/koscom-chevron/) — 권장 앵커는 `briefing / swiss-minimal`.

## II. Color Scheme

| Role | HEX | Notes |
|---|---|---|
| canvas | `#ffffff` | 본문 배경 |
| surface | `#f5f5f7` | 카드·패널 연회색 |
| hairline | `#dcdce0` | 1px 경계, 차트 비강조 바 |
| chevron-grey | `#ececee` | 뒤쪽 회색 셰브론 전용 |
| orange | `#ee6d1d` | 주색 — 제목, 키커, 번호 원, 강조 패널, 차트 피크 |
| orange-deep | `#f26522` | 대형 셰브론 채움 (앵커 페이지 전용) |
| orange-tint | `#fad3bb` | 카드 헤더 밴드, 오렌지 위 보조 텍스트 |
| orange-pale | `#fdeee4` | 표지 연오렌지 셰브론 전용 |
| navy | `#00338d` | 챕터·클로징 풀블리드 |
| navy-mid | `#1f4b9b` | 네이비 위 뒤쪽 셰브론 |
| navy-soft | `#0f499c` | 네이비 위 중간 셰브론 |
| blue-tint | `#edf4fb` | 네이비 위 보조 텍스트·푸터 |
| black | `#000000` | 시그니처 배경 |
| wave-dim | `#7a3a10` | 블랙 위 웨이브 라인 (먼 층) |
| wave-mid | `#b85415` | 블랙 위 웨이브 라인 (중간 층) |
| ink | `#2b2b2e` | 헤드라인·본문 1차 |
| ink-2 | `#6e6e73` | 본문 2차 |
| grey | `#8c8c92` | 캡션·태그·축 라벨·푸터 |
| white | `#ffffff` | 네이비·블랙·오렌지 위 텍스트 |

**오렌지는 구조색이다** — 제목·키커·번호 원처럼 위계를 표시하는 자리에 쓰고, 번호 원보다 큰 오렌지 면은 강조 패널 하나까지만 허용한다. **대형 오렌지 면(셰브론)은 앵커 페이지 전용**이며 본문에 올리지 않는다. 서피스는 페이지당 하나(화이트 / 네이비 / 블랙). 그림자·그라디언트를 쓰지 않고 리프트는 `#f5f5f7` 서피스와 1px `#dcdce0` 헤어라인으로만 만든다. 차트는 피크 `#ee6d1d` + 나머지 `#dcdce0`, 비교 계열은 `#8c8c92` 점선. 성공/위험 색이 없다 — 증가는 오렌지, 감소·중립은 그레이.

## III. Typography

**KoPub돋움체** 락 (덱의 `fonts/` 참고). Bold가 헤드라인과 강조, Medium이 본문·키커. 폴백은 Pretendard → Malgun Gothic.

| Role | `font-family` | Weight |
|---|---|---|
| headline / card title / KPI / brand mark | `'KoPub돋움체 Bold', 'KoPubDotum Bold', Pretendard, 'Malgun Gothic', sans-serif` | Bold |
| body / lead / kicker / caption | `'KoPub돋움체 Medium', 'KoPubDotum Medium', Pretendard, 'Malgun Gothic', sans-serif` | Medium |

**헤드라인은 Bold다.** 위계는 굵기 전환이 아니라 크기 램프로 만든다. 한글 비중 ≥50% 런은 음수 자간을 ×0.5로 완화하고, 헤드라인 음수 자간은 -0.5 이상으로 조이지 않는다. 키커는 대문자 + 자간 +4, 항상 8×26 오렌지 세로 바와 함께 온다.

## IV. Logo

로고 자산을 번들하지 않는다. 브랜드 표기는 텍스트 슬롯(`{{BRAND_MARK}}`)으로만 존재한다. 셰브론(›)은 로고가 아니라 **기하 모티프** — 단위 형상 565×760, 팔 두께 240의 다각형 — 로만 쓰며 항상 오른쪽을 가리키고 캔버스 우측 밖으로 잘려 나간다. 실제 로고를 넣으려면 프로젝트 `images/`에 배치하고 페이지에서 직접 참조한다.

## V. Voice & Tone

공식적이고 간결하게. 영문 키커(`COMPANY PROFILE`, `CHAPTER`, `Our Market Role`) + 한글 본문의 이중 구조를 유지한다. 수치에는 단위와 기준 시점을 붙이고 과장 형용사를 쓰지 않는다.

## VI. Icon Style

라인 아이콘 소량, `#2b2b2e` 단색. 순서 표시는 불릿 대신 오렌지 번호 원(r=12, 흰 숫자). 모서리는 각지게 — 둥근 것은 번호 원뿐.
