---
brand_id: open-road
kind: brand
summary: 시네마틱 사진 키노트 아이덴티티 — 한 화면 한 메시지, 각진 지오메트리, 카본 다크 구분면
keywords: [cinematic, photography, keynote, gallery, launch]
primary_color: "#3E6AE1"
---

# Open Road — Brand Specification

> Identity-only preset. 페이지 로스터가 없다 — 이 제약 아래에서 페이지는 자유롭게 구성한다.
>
> **Provenance**: [`templates/decks/open-road/`](../../../decks/open-road/templates/design_spec.md)에서 아이덴티티 세그먼트만 추출했다(덱이 source of truth). 색·타이포·보이스 변경은 덱에서 먼저 고치고 이 파일에 동기화한다. 페이지 구조·크기 램프·마진은 덱 소관이며 여기 기록하지 않는다.
>
> 원저작 아이덴티티. 널리 통용되는 비독점 디자인 원칙에서 새로 설계했으며, 어떤 회사의 상표·로고·워드마크도 복제하거나 번들하지 않는다. 브랜드 표기는 텍스트 슬롯으로만 존재한다.

## I. Brand Overview

| Property | Value |
|---|---|
| Brand Name | Open Road |
| Use Cases | 제품 런칭, 브랜드 키노트, 비전 발표, 쇼룸·전시 프레젠테이션 |
| Tone | 확신에 차고 조용함 — 갤러리처럼 한 번에 하나만 보여준다 |

**Anti-mood**: "정보 밀집 컨설팅 그리드", "다색 인포그래픽", "그림자 카드 더미", "라운드 파스텔 SaaS".

**Companion deck**: 페이지 로스터까지 함께 쓰려면 [`templates/decks/open-road/`](../../../decks/open-road/) — 권장 앵커는 `showcase / photo-editorial`.

## II. Color Scheme

| Role | HEX | Notes |
|---|---|---|
| canvas | `#FFFFFF` | 본문 페이지 배경 |
| surface | `#F4F4F4` | 카드·패널 서피스 |
| cloud | `#EEEEEE` | 1px 구분선, 차트 비강조 바 |
| silver | `#8E8E8E` | 플레이스홀더 안내, 차트 2계열 |
| pewter | `#5C5E62` | 캡션·축 라벨·푸터 |
| graphite | `#393C41` | 본문 |
| carbon | `#171A20` | 헤드라인 · 챕터/클로징 풀블리드 배경 · 사진 해칭 전경 |
| electric | `#3E6AE1` | 주색 — CTA, 강조 1점, 차트 피크 |
| ink-inverse | `#FFFFFF` | 다크 위 텍스트 |

**한 페이지 한 강조** — `#3E6AE1`은 CTA 또는 차트 피크 중 하나에만 올린다. 본문은 `#393C41`, 헤드라인은 `#171A20`이며 순수 검정을 쓰지 않는다. **그림자를 쓰지 않는다** — 이 시스템의 깊이는 사진에서 오고, 카드는 `#F4F4F4` 서피스와 `#EEEEEE` 1px 선으로만 구분한다. 차트는 근사 무채색(피크 일렉트릭, 나머지 `#EEEEEE`, 2계열 `#8E8E8E`)이며 세 번째 계열이 필요하면 차트를 나눈다. **모서리 기본은 0**, 버튼 `4`, 카테고리 카드 `12`뿐이다. 사진은 캔버스 가장자리까지 닿고 라운딩·프레임을 두지 않는다.

## III. Typography

install-local Pretendard lock (see `references/strategist.md` §g). 원 참조 브랜드의 서체는 상용·독점이므로 사용하지 않고, 성격은 웨이트·자간·크기로 재현한다.

| Role | `font-family` | Weight |
|---|---|---|
| body / labels / axis | `Pretendard, 'Malgun Gothic', sans-serif` | 400 |
| headline / kicker / card title | `'Pretendard Medium', Pretendard, 'Malgun Gothic', sans-serif` | 500 |
| KPI number | `'Pretendard SemiBold', Pretendard, 'Malgun Gothic', sans-serif` | 600 |

**헤드라인은 500이 기본, 600은 지표 숫자에만.** 700 이상은 없다 — 큰 텍스트를 굵게 만들면 갤러리의 정적이 깨진다. 여백이 정체성이므로 측면 96px 마진과 최소 48px 블록 간격을 줄이지 않는다. 한글 비중 ≥50% 런은 자간을 ×0.5로 완화한다.

## IV. Logo

로고 자산을 번들하지 않는다. 브랜드 표기는 텍스트 슬롯(`{{BRAND_MARK}}`)으로만 존재하며, 이미지 로고를 삽입하지 않는다. 사용자가 자기 로고를 넣으려면 프로젝트 `images/`에 배치하고 페이지에서 직접 참조한다.

## V. Voice & Tone

선언적이고 짧게. 문장을 하나 더 뺄 수 있으면 뺀다. 스펙 나열보다 결과를 말하고, 두 번째 메시지가 필요하면 페이지를 나눈다.

## VI. Icon Style

원칙적으로 아이콘을 쓰지 않는다. 타입과 여백, 그리고 사진이 일한다. 불가피하면 `#5C5E62` 단색 라인 아이콘 1개까지.
