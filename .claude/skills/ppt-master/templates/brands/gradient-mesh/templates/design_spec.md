---
brand_id: gradient-mesh
kind: brand
summary: 인디고 + 메시 그라디언트 핀테크 아이덴티티 — 얇은 디스플레이 웨이트, 풀 필 CTA, 표 정렬 숫자
keywords: [fintech, gradient, indigo, pill, tabular]
primary_color: "#533AFD"
---

# Gradient Mesh Fintech — Brand Specification

> Identity-only preset. 페이지 로스터가 없다 — 이 제약 아래에서 페이지는 자유롭게 구성한다.
>
> **Provenance**: [`templates/decks/gradient-mesh/`](../../../decks/gradient-mesh/templates/design_spec.md)에서 아이덴티티 세그먼트만 추출했다(덱이 source of truth). 색·타이포·보이스 변경은 덱에서 먼저 고치고 이 파일에 동기화한다. 페이지 구조·크기 램프·마진은 덱 소관이며 여기 기록하지 않는다.
>
> 원저작 아이덴티티. 널리 통용되는 비독점 디자인 원칙에서 새로 설계했으며, 어떤 회사의 상표·로고·워드마크도 복제하거나 번들하지 않는다. 브랜드 표기는 텍스트 슬롯으로만 존재한다.

## I. Brand Overview

| Property | Value |
|---|---|
| Brand Name | Gradient Mesh Fintech |
| Use Cases | 파트너 제안서, 핀테크 IR, 제품 이코노믹스, 가격·수수료 설명, 결제/정산 브리핑 |
| Tone | 정밀하고 낙관적 — 숫자를 다루되 차갑지 않다 |

**Anti-mood**: "다크 터미널", "컨설팅 밀도 그리드", "그림자 카드", "무지개 카테고리 차트".

**Companion deck**: 페이지 로스터까지 함께 쓰려면 [`templates/decks/gradient-mesh/`](../../../decks/gradient-mesh/) — 권장 앵커는 `pyramid / glassmorphism`.

## II. Color Scheme

| Role | HEX | Notes |
|---|---|---|
| canvas | `#ffffff` | 페이지 배경 |
| surface-cool | `#f6f9fc` | 쿨 오프화이트 밴드·카드 |
| surface-warm | `#f5e9d4` | 웜 크림 밴드 (교대 리듬) |
| hairline | `#e3e8ee` | 1px 카드·표 경계 |
| indigo | `#533afd` | 주색 — CTA 필, 강조 1점, 차트 피크 |
| indigo-deep | `#4434d4` | 그라디언트 중간 스톱 |
| indigo-soft | `#665efd` | 보조 강조, 차트 2계열 |
| indigo-tint | `#b9b9f9` | 태그 배경, 차트 비강조 |
| navy | `#1c1e54` | 다크 카운터패널 |
| ruby | `#ea2261` | 차트·그라디언트 전용 — 버튼 금지 |
| magenta | `#f96bee` | 그라디언트 스톱 전용 |
| sherbet | `#f5a623` | 그라디언트 스톱 전용 |
| ink | `#0d253d` | 헤드라인·본문 1차 |
| ink-2 | `#273951` | 본문 2차 |
| ink-muted | `#64748d` | 캡션·축 라벨·푸터 |
| ink-inverse | `#ffffff` | 네이비 위 텍스트 |
| success | `#1e8e5a` | 양(+) 델타 전용 |

**인디고는 페이지당 강조 1점** — CTA 필 또는 차트 피크 중 하나이며 둘 다는 안 된다. **루비·마젠타·셔벗은 그라디언트와 차트에만** 쓰고 버튼·텍스트·아이콘에 올리지 않는다. **밴드 교대가 리듬이다** — white → `#f6f9fc` → `#f5e9d4` → `#1c1e54`로 페이지 성격을 나누되 한 페이지에서 두 밴드를 섞지 않는다. 숫자는 우측 정렬하고 자릿수를 맞춘다. 그림자를 쓰지 않고 리프트는 서피스 대비와 1px 헤어라인으로만 만든다. 차트 래더는 `#533afd` → `#665efd` → `#b9b9f9` → `#e3e8ee`이며 루비는 리스크·감소 표시에만 쓴다.

## III. Typography

install-local Pretendard lock (see `references/strategist.md` §g). 원 참조 브랜드의 서체는 상용·독점이므로 사용하지 않고, 성격은 웨이트·자간·크기로 재현한다.

| Role | `font-family` | Weight |
|---|---|---|
| display / headline | `'Pretendard Light', Pretendard, 'Malgun Gothic', sans-serif` | 300 |
| body / page title / KPI | `Pretendard, 'Malgun Gothic', sans-serif` | 400 |
| emphasis / footer mark | `'Pretendard Medium', Pretendard, 'Malgun Gothic', sans-serif` | 500 |
| card title / kicker | `'Pretendard SemiBold', Pretendard, 'Malgun Gothic', sans-serif` | 600 |

**헤드라인은 300 또는 400이지 600이 아니다.** 600은 카드 제목·라벨 같은 작은 텍스트 전용 — 큰 텍스트를 굵게 만드는 순간 이 시스템의 우아함이 사라진다. 한글 비중 ≥50% 런은 자간을 ×0.5로 완화한다.

## IV. Logo

로고 자산을 번들하지 않는다. 브랜드 표기는 텍스트 슬롯(`{{BRAND_MARK}}`)으로만 존재하며, 이미지 로고를 삽입하지 않는다. 사용자가 자기 로고를 넣으려면 프로젝트 `images/`에 배치하고 페이지에서 직접 참조한다.

## V. Voice & Tone

구체적이고 검증 가능하게. 수치에는 단위와 기준 시점을 붙이고, 과장 형용사를 쓰지 않는다.

## VI. Icon Style

라인 아이콘 소량. `#533afd` 또는 `#64748d` 단색. 그라디언트 아이콘·다색 아이콘 금지.
