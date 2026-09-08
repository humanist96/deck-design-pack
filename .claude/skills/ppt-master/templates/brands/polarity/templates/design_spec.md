---
brand_id: polarity
kind: brand
summary: 흑백 극성 반전 개발자 아이덴티티 — 배경 반전이 곧 챕터 구분, 단일 메시 그라디언트 오브젝트
keywords: [monochrome, contrast, developer, gradient-mesh, inversion]
primary_color: "#171717"
---

# Polarity Mono — Brand Specification

> Identity-only preset. 페이지 로스터가 없다 — 이 제약 아래에서 페이지는 자유롭게 구성한다.
>
> **Provenance**: [`templates/decks/polarity/`](../../../decks/polarity/templates/design_spec.md)에서 아이덴티티 세그먼트만 추출했다(덱이 source of truth). 색·타이포·보이스 변경은 덱에서 먼저 고치고 이 파일에 동기화한다. 페이지 구조·크기 램프·마진은 덱 소관이며 여기 기록하지 않는다.
>
> 원저작 아이덴티티. 널리 통용되는 비독점 디자인 원칙에서 새로 설계했으며, 어떤 회사의 상표·로고·워드마크도 복제하거나 번들하지 않는다. 브랜드 표기는 텍스트 슬롯으로만 존재한다.

## I. Brand Overview

| Property | Value |
|---|---|
| Brand Name | Polarity Mono |
| Use Cases | 기술 발표, 데모데이, 개발자 컨퍼런스, 플랫폼·인프라 소개, 오픈소스 발표 |
| Tone | 명료, 기술적, 자신감 — 설명하지 않고 보여준다 |

**Anti-mood**: "파스텔 SaaS 마케팅", "일러스트 랜딩", "다색 카테고리 차트", "라운드 카드 그리드 일변도".

**Companion deck**: 페이지 로스터까지 함께 쓰려면 [`templates/decks/polarity/`](../../../decks/polarity/) — 권장 앵커는 `showcase / swiss-minimal`.

## II. Color Scheme

| Role | HEX | Notes |
|---|---|---|
| canvas | `#fafafa` | 라이트 페이지 배경 |
| surface | `#ffffff` | 카드·패널 (캔버스보다 밝다) |
| surface-alt | `#f5f5f5` | 2차 서피스, 차트 비강조 |
| ink | `#171717` | 잉크 · 다크 배경 · 1차 강조 |
| ink-inverse | `#ffffff` | 다크 위 텍스트 |
| body | `#4d4d4d` | 라이트 본문 |
| muted | `#888888` | 캡션·축 라벨 |
| hairline | `#ebebeb` | 라이트 1px 경계 |
| surface-dark | `#1f1f1f` | 다크 위 패널 |
| hairline-dark | `#333333` | 다크 1px 경계 |
| mesh-a1 | `#007cf0` | 메시 — 블루 |
| mesh-a2 | `#00dfd8` | 메시 — 틸 |
| mesh-b1 | `#7928ca` | 메시 — 바이올렛 |
| mesh-b2 | `#ff0080` | 메시 — 핑크 |
| mesh-c1 | `#ff4d4d` | 메시 — 코럴 |
| mesh-c2 | `#f9cb28` | 메시 — 앰버 |

**극성이 구조다** — 챕터 전환은 색이 아니라 배경 반전(라이트→다크)으로 알리고 구분선·장식을 추가하지 않는다. **메시는 페이지당 1개 오브젝트**이며 세 쌍을 한 덩어리로 배치한다; 텍스트 뒤에 오면 반드시 불투명 서피스를 덧댄다. **유채색은 메시에만 존재한다** — 텍스트·아이콘·차트 강조에 메시 색을 쓰지 않으며 강조는 잉크가 담당한다. 차트는 `#171717` → `#888888` → `#ebebeb` 무채색 래더에 피크 1개만 잉크. 모서리는 인앱 `6`, 카드 `8`–`12`, 마케팅 CTA 풀 필 `100`만 쓴다. 그림자는 시스템 전체에 없다.

## III. Typography

install-local Pretendard lock (see `references/strategist.md` §g). 원 참조 브랜드의 서체는 상용·독점이므로 사용하지 않고, 성격은 웨이트·자간·크기로 재현한다.

| Role | `font-family` | Weight |
|---|---|---|
| body / labels / axis | `Pretendard, 'Malgun Gothic', sans-serif` | 400 |
| emphasis / footer mark | `'Pretendard Medium', Pretendard, 'Malgun Gothic', sans-serif` | 500 |
| headline / card title / kicker | `'Pretendard SemiBold', Pretendard, 'Malgun Gothic', sans-serif` | 600 |

문장 케이스 전면 적용. Title Case와 ALL CAPS 본문은 금지하되 키커는 대문자로 저작한다. 큰 텍스트일수록 자간을 죈다(84px에 -3.0). 한글 비중 ≥50% 런은 자간을 ×0.5로 완화한다.

## IV. Logo

로고 자산을 번들하지 않는다. 브랜드 표기는 텍스트 슬롯(`{{BRAND_MARK}}`)으로만 존재하며, 이미지 로고를 삽입하지 않는다. 사용자가 자기 로고를 넣으려면 프로젝트 `images/`에 배치하고 페이지에서 직접 참조한다.

## V. Voice & Tone

짧고 단정적. 기능을 나열하기보다 결과를 말한다. 감탄부호·이모지 금지, 존대 남용 금지.

## VI. Icon Style

라인 아이콘 최소 사용. 라이트에서 `#171717`, 다크에서 `#ffffff` 단색. 채움·다색 아이콘 금지.
