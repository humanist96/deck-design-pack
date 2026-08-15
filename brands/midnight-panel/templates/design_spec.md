---
brand_id: midnight-panel
kind: brand
summary: 니어블랙 다크 프로덕트 아이덴티티 — 서피스 계단 깊이, 단일 라벤더 시그널, 4단 잉크 위계
keywords: [dark, product, engineering, restrained, panel]
primary_color: "#5E6AD2"
---

# Midnight Panel — Brand Specification

> Identity-only preset. 페이지 로스터가 없다 — 이 제약 아래에서 페이지는 자유롭게 구성한다.
>
> **Provenance**: [`templates/decks/midnight-panel/`](../../../decks/midnight-panel/templates/design_spec.md)에서 아이덴티티 세그먼트만 추출했다(덱이 source of truth). 색·타이포·보이스 변경은 덱에서 먼저 고치고 이 파일에 동기화한다. 페이지 구조·크기 램프·마진은 덱 소관이며 여기 기록하지 않는다.
>
> 원저작 아이덴티티. 널리 통용되는 비독점 디자인 원칙에서 새로 설계했으며, 어떤 회사의 상표·로고·워드마크도 복제하거나 번들하지 않는다. 브랜드 표기는 텍스트 슬롯으로만 존재한다.

## I. Brand Overview

| Property | Value |
|---|---|
| Brand Name | Midnight Panel |
| Use Cases | 제품 로드맵, 스프린트/분기 리뷰, 엔지니어링 브리핑, 개발자 세션 |
| Tone | 절제, 정밀, 야간 작업실 — 화면이 스스로 빛나되 과시하지 않는다 |

**Anti-mood**: "네온 사이버펑크", "그라디언트 SaaS 히어로", "글로우 대시보드", "다색 카테고리 팔레트".

**Companion deck**: 페이지 로스터까지 함께 쓰려면 [`templates/decks/midnight-panel/`](../../../decks/midnight-panel/) — 권장 앵커는 `briefing / dark-tech`.

## II. Color Scheme

| Role | HEX | Notes |
|---|---|---|
| canvas | `#010102` | 전 페이지 지배 배경 |
| surface-1 | `#0f1011` | 카드·패널 기본 |
| surface-2 | `#141516` | 패널 내부 한 단계 리프트 |
| surface-3 | `#18191a` | 차트 비강조, 중첩 서피스 |
| surface-4 | `#191a1b` | 최상단 마이크로스텝 |
| hairline | `#23252a` | 1px 경계 기본 |
| hairline-strong | `#34343a` | 구분 강조선, 차트 축 |
| hairline-3 | `#3e3e44` | 차트 비강조 바 |
| accent | `#5e6ad2` | 페이지당 1곳 — 유일한 채도 |
| accent-bright | `#828fff` | 악센트 위 미세 하이라이트 (희소) |
| ink | `#f7f8f8` | 헤드라인·본문 1차 |
| ink-muted | `#d0d6e0` | 본문 2차, 리드 |
| ink-subtle | `#8a8f98` | 캡션·축 라벨 |
| ink-3 | `#62666d` | 푸터·번호 |
| success | `#27a644` | 양(+) 델타 전용 |

**악센트는 페이지당 1곳** — 두 번째 라벤더가 등장하는 순간 신호는 장식이 된다. **깊이는 서피스 계단으로만** (canvas → surface-1 → surface-2); 그림자·글로우·그라디언트 전면 금지. 경계는 1px 헤어라인이며 굵은 아웃라인·이중 테두리를 쓰지 않는다. 잉크는 4단(`#f7f8f8` → `#d0d6e0` → `#8a8f98` → `#62666d`) 안에서만 감쇠한다. 차트는 피크 1개만 악센트, 나머지는 `#3e3e44` → `#18191a`이며 계열 구분은 색이 아니라 선 스타일(실선/점선)이다. 모서리는 `0` / `4` / `8` / `12` / `16` / `9999`만 쓴다.

## III. Typography

install-local Pretendard lock (see `references/strategist.md` §g). 원 참조 브랜드의 서체는 상용·독점이므로 사용하지 않고, 성격은 웨이트·자간·크기로 재현한다.

| Role | `font-family` | Weight |
|---|---|---|
| body / labels / axis | `Pretendard, 'Malgun Gothic', sans-serif` | 400 |
| emphasis / footer mark | `'Pretendard Medium', Pretendard, 'Malgun Gothic', sans-serif` | 500 |
| headline / card title / kicker | `'Pretendard SemiBold', Pretendard, 'Malgun Gothic', sans-serif` | 600 |

**웨이트 래더는 400 / 500 / 600 세 단계뿐이다.** 700 이상은 없다 — 다크 배경에서 굵은 웨이트는 번져 보인다. 크기가 커질수록 자간을 더 죈다(88px에 -3.2가 이 시스템의 서명). 한글 비중 ≥50% 런은 자간을 ×0.5로 완화한다.

## IV. Logo

로고 자산을 번들하지 않는다. 브랜드 표기는 텍스트 슬롯(`{{BRAND_MARK}}`)으로만 존재하며, 이미지 로고를 삽입하지 않는다. 사용자가 자기 로고를 넣으려면 프로젝트 `images/`에 배치하고 페이지에서 직접 참조한다.

## V. Voice & Tone

기술적이고 사실 위주. 마케팅 수사·감탄부호·이모지를 쓰지 않는다. 제목은 명사구 또는 짧은 평서문이며, 수치는 장식이 아니라 근거로만 올린다.

## VI. Icon Style

희소한 라인 아이콘만. 다크 서피스 위에서 `#8a8f98` 단색 스트로크, 채움 아이콘·다색 아이콘 금지. 아이콘이 없어도 의미가 유지되면 넣지 않는다.
