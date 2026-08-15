---
brand_id: warm-doc
kind: brand
summary: 웜 뉴트럴 문서형 아이덴티티 — 1px 아웃라인 문법, 파스텔 틴트 5색, 딥 네이비 히어로 밴드
keywords: [document, warm-neutral, pastel, handbook, onboarding]
primary_color: "#5645D4"
---

# Warm Document — Brand Specification

> Identity-only preset. 페이지 로스터가 없다 — 이 제약 아래에서 페이지는 자유롭게 구성한다.
>
> **Provenance**: [`templates/decks/warm-doc/`](../../../decks/warm-doc/templates/design_spec.md)에서 아이덴티티 세그먼트만 추출했다(덱이 source of truth). 색·타이포·보이스 변경은 덱에서 먼저 고치고 이 파일에 동기화한다. 페이지 구조·크기 램프·마진은 덱 소관이며 여기 기록하지 않는다.
>
> 원저작 아이덴티티. 널리 통용되는 비독점 디자인 원칙에서 새로 설계했으며, 어떤 회사의 상표·로고·워드마크도 복제하거나 번들하지 않는다. 브랜드 표기는 텍스트 슬롯으로만 존재한다.

## I. Brand Overview

| Property | Value |
|---|---|
| Brand Name | Warm Document |
| Use Cases | 사내 문서·핸드북, 신입 온보딩, 팀 위키 발표, 프로세스·정책 안내, 워크숍 |
| Tone | 친근하고 정돈됨 — 읽는 문서에 가까운 슬라이드 |

**Anti-mood**: "차가운 쿨그레이 SaaS", "다크 터미널", "그림자 카드", "컨설팅 밀도 그리드".

**Companion deck**: 페이지 로스터까지 함께 쓰려면 [`templates/decks/warm-doc/`](../../../decks/warm-doc/) — 권장 앵커는 `instructional / soft-rounded`.

## II. Color Scheme

| Role | HEX | Notes |
|---|---|---|
| canvas | `#ffffff` | 페이지 배경 |
| surface | `#f6f5f4` | 웜그레이 섹션 서피스 |
| hairline | `#e5e3df` | 1px 웜그레이 경계 — 거의 모든 요소를 두른다 |
| navy | `#0a1530` | 히어로·챕터·클로징 밴드 |
| purple | `#5645d4` | 주색 — CTA, 강조 1점, 차트 피크 |
| purple-2 | `#4534b3` | 차트 2계열, 눌린 상태 |
| ink | `#1a1a1a` | 헤드라인 |
| charcoal | `#37352f` | 웜 본문 — 순수 검정이 아닌 따뜻한 먹 |
| steel | `#787671` | 캡션·축 라벨·푸터 |
| tint-peach | `#ffe8d4` | 카드 틴트 1 |
| tint-rose | `#fde0ec` | 카드 틴트 2 |
| tint-mint | `#d9f3e1` | 카드 틴트 3 |
| tint-lavender | `#e6e0f5` | 카드 틴트 4 |
| tint-sky | `#dcecfa` | 카드 틴트 5 |
| orange | `#dd5b00` | 주의·강조 라벨 (희소) |
| teal | `#2a9d99` | 차트 3계열 |
| success | `#1aae39` | 양(+) 델타 |
| error | `#e03131` | 음(−) 델타·경고 |

**본문은 `#37352f`이지 검정이 아니다** — 웜 먹이 이 시스템의 체온을 만들며 `#1a1a1a`는 헤드라인 전용이다. **경계는 항상 1px `#e5e3df`**이고 그림자를 쓰지 않는다; 아웃라인이 카드를 정의한다. **파스텔 틴트 5색은 시그니처 용도 전용**이며 본문 카드·차트에 쓰지 않는다. 퍼플은 페이지당 1점(CTA 또는 차트 피크). 네이비는 밴드 배경으로만 쓰고 텍스트 색으로 쓰지 않는다. 차트 래더는 `#5645d4` → `#4534b3` → `#2a9d99` → `#e5e3df`. 모서리는 버튼·입력 `8`, 카드 `12`이며 필은 배지에만 쓴다.

## III. Typography

install-local Pretendard lock (see `references/strategist.md` §g). 원 참조 브랜드의 서체는 상용·독점이므로 사용하지 않고, 성격은 웨이트·자간·크기로 재현한다.

| Role | `font-family` | Weight |
|---|---|---|
| body / labels / axis | `Pretendard, 'Malgun Gothic', sans-serif` | 400 |
| emphasis / footer mark | `'Pretendard Medium', Pretendard, 'Malgun Gothic', sans-serif` | 500 |
| heading / card title / kicker | `'Pretendard SemiBold', Pretendard, 'Malgun Gothic', sans-serif` | 600 |

**모든 헤딩은 600, 강조는 500, 본문은 400.** 300과 700 이상은 이 아이덴티티에 없다. 문서형이라 여백을 넉넉히 두고(측면 88px, 블록 간 32–48px) 밀도로 채우지 않는다. 한글 비중 ≥50% 런은 자간을 ×0.5로 완화한다.

## IV. Logo

로고 자산을 번들하지 않는다. 브랜드 표기는 텍스트 슬롯(`{{BRAND_MARK}}`)으로만 존재하며, 이미지 로고를 삽입하지 않는다. 사용자가 자기 로고를 넣으려면 프로젝트 `images/`에 배치하고 페이지에서 직접 참조한다.

## V. Voice & Tone

설명적이고 친절하게. 독자가 처음 본다고 가정하고 약어는 최초 1회 풀어 쓴다. 명령형보다 설명형을 쓴다.

## VI. Icon Style

라인 아이콘 또는 파스텔 틴트 칩. `#37352f` 또는 `#787671` 단색 스트로크. 다색 아이콘 금지.
