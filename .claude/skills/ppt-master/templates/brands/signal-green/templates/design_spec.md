---
brand_id: signal-green
kind: brand
summary: 블랙 히어로 + 시그널 그린 기술 아이덴티티 — 앵귤러 2px, 코너 스퀘어 표식, 극성 교대
keywords: [tech-keynote, angular, signal-accent, benchmark, dual-theme]
primary_color: "#76B900"
---

# Signal Green — Brand Specification

> Identity-only preset. 페이지 로스터가 없다 — 이 제약 아래에서 페이지는 자유롭게 구성한다.
>
> **Provenance**: [`templates/decks/signal-green/`](../../../decks/signal-green/templates/design_spec.md)에서 아이덴티티 세그먼트만 추출했다(덱이 source of truth). 색·타이포·보이스 변경은 덱에서 먼저 고치고 이 파일에 동기화한다. 페이지 구조·크기 램프·마진은 덱 소관이며 여기 기록하지 않는다.
>
> 원저작 아이덴티티. 널리 통용되는 비독점 디자인 원칙에서 새로 설계했으며, 어떤 회사의 상표·로고·워드마크도 복제하거나 번들하지 않는다. 브랜드 표기는 텍스트 슬롯으로만 존재한다.

## I. Brand Overview

| Property | Value |
|---|---|
| Brand Name | Signal Green |
| Use Cases | AI·GPU·인프라 브리핑, 개발자 세션, 기술 컨퍼런스, 벤치마크·성능 리포트 |
| Tone | 단호하고 기술적 — 성능 수치가 주인공이다 |

**Anti-mood**: "파스텔 SaaS", "라운드 카드 그리드", "그라디언트 히어로", "다색 카테고리 팔레트".

**Companion deck**: 페이지 로스터까지 함께 쓰려면 [`templates/decks/signal-green/`](../../../decks/signal-green/) — 권장 앵커는 `showcase / dark-tech`.

## II. Color Scheme

| Role | HEX | Notes |
|---|---|---|
| black | `#000000` | 히어로·챕터·클로징 풀블리드 배경 · 라이트 헤드라인 |
| surface-dark | `#1A1A1A` | 다크 위 패널 |
| canvas | `#FFFFFF` | 콘텐츠 페이지 배경 |
| surface-soft | `#F7F7F7` | 카드·패널 서피스 |
| hairline | `#CCCCCC` | 1px 카드 경계, 차트 그리드 |
| body | `#333333` | 본문 |
| muted | `#767676` | 캡션·축 라벨·푸터 |
| green | `#76B900` | 시그널 — 강조 1점, 코너 스퀘어, 차트 피크 |
| green-2 | `#5A8D00` | 차트 2계열, 눌린 상태 |
| green-pale | `#BFF230` | 다크 위 보조 강조 (희소) |

**그린은 페이지당 정확히 1곳** — 코너 스퀘어·규칙선·차트 피크 중 하나다. **극성이 구조다** — 블랙 히어로와 화이트 콘텐츠의 교대가 챕터 구분이며 별도 장식선을 넣지 않는다. 라이트 본문은 `#333333`이고 순수 검정은 헤드라인 전용, 다크 위 본문은 `#767676` 이상 밝기를 쓴다. 차트 래더는 `#76B900` → `#5A8D00` → `#CCCCCC`이며 세 번째 계열이 필요하면 차트를 나눈다. **모서리는 카드·버튼·바 `2`, 히어로·푸터·풀블리드 `0`**뿐이다. 그라디언트·그림자·글로우를 쓰지 않는다.

## III. Typography

install-local Pretendard lock (see `references/strategist.md` §g). 원 참조 브랜드의 서체는 상용·독점이므로 사용하지 않고, 성격은 웨이트·자간·크기로 재현한다.

| Role | `font-family` | Weight |
|---|---|---|
| body / labels / axis | `Pretendard, 'Malgun Gothic', sans-serif` | 400 |
| footer mark | `'Pretendard Medium', Pretendard, 'Malgun Gothic', sans-serif` | 500 |
| card title / kicker | `'Pretendard SemiBold', Pretendard, 'Malgun Gothic', sans-serif` | 600 |
| headline / KPI number | `Pretendard, 'Malgun Gothic', sans-serif + font-weight="700"` | 700 |

**헤드라인은 700, 카드 제목·라벨은 600, 본문은 400.** 300 이하는 없다. 블랙 위 700 웨이트 흰 텍스트가 최대 대비로 서는 것이 이 아이덴티티의 핵심이다. 한글 비중 ≥50% 런은 자간을 ×0.5로 완화한다.

## IV. Logo

로고 자산을 번들하지 않는다. 브랜드 표기는 텍스트 슬롯(`{{BRAND_MARK}}`)으로만 존재하며, 이미지 로고를 삽입하지 않는다. 사용자가 자기 로고를 넣으려면 프로젝트 `images/`에 배치하고 페이지에서 직접 참조한다.

## V. Voice & Tone

수치 우선. 주장보다 벤치마크를 앞세우고, 비교 기준(하드웨어·버전·조건)을 반드시 명시한다. 과장 형용사를 쓰지 않는다.

## VI. Icon Style

코너 스퀘어(12×12)가 아이콘을 대신한다. 필요 시 `#767676` 단색 라인 아이콘만, 라운드 0–2. 다색·채움 아이콘 금지.
