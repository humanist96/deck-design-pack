# Gallery

Every page of every template, plus the identity each one locks.

Contact sheets are rendered from the template's own review PPTX — what you see is the compiled PowerPoint, not the source SVG.


---

## Midnight Panel

`midnight-panel` · primary `#5E6AD2` · 10 pages

<img src="../previews/midnight-panel.png" width="100%">

| | |
|---|---|
| **Theme** | Dark only — `#010102` 캔버스 고정 |
| **Tone** | 절제, 정밀, 야간 작업실 — 화면이 스스로 빛나되 과시하지 않는다 |
| **Use cases** | 제품 로드맵, 스프린트/분기 리뷰, 엔지니어링 브리핑, 개발자 컨퍼런스 세션, 내부 기술 제안 |
| **Anchors** | [dark, product, engineering, restrained, panel] |

**Signature**

1. **서피스 계단** — 그림자 없이 `#010102` → `#0f1011` → `#141516`로 올려 깊이를 만든다. 카드는 항상 1px `#23252a` 헤어라인을 두른다
2. **단일 라벤더 신호** — `#5e6ad2`는 페이지당 정확히 1곳. 표지 악센트 바, 아젠다 현재 항목, 피크 바, 시그니처 패널의 활성 요소 중 하나만
3. **제품 패널 프레임** — 16px 라운드 + 헤어라인 경계의 surface-1 패널 안에 추상 UI(타이틀바 도트 3개, 사이드바 열, 행 스켈레톤)를 그린다. **실제 제품 스크린샷이 아니라 기하 추상**이다

**Page roster**

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

Full specification: [`decks/midnight-panel/templates/design_spec.md`](../decks/midnight-panel/templates/design_spec.md) · identity-only preset: [`brands/midnight-panel/`](../brands/midnight-panel/)

---

## Polarity Mono

`polarity` · primary `#171717` · 10 pages

<img src="../previews/polarity.png" width="100%">

| | |
|---|---|
| **Theme** | **Dual — 극성 반전.** 콘텐츠는 라이트(`#fafafa`), 챕터·시그니처·클로징은 다크(`#171717`) |
| **Tone** | 명료, 기술적, 자신감 — 설명하지 않고 보여준다 |
| **Use cases** | 기술 발표, 데모데이, 개발자 컨퍼런스 세션, 플랫폼·인프라 소개, 오픈소스 프로젝트 발표 |
| **Anchors** | [monochrome, contrast, developer, gradient-mesh, inversion] |

**Signature**

1. **극성 반전 = 챕터 신호** — `03` / `04` / `10`은 `#171717` 풀블리드. 밝음에서 어둠으로 넘어가는 것 자체가 구분선이며, 별도 장식을 넣지 않는다
2. **단일 메시 오브젝트** — 세 쌍(블루→틸 / 바이올렛→핑크 / 코럴→앰버)을 겹친 하나의 블롭 덩어리. 표지에만 등장하며 본문 페이지에는 없다
3. **2-반경 세계** — 인앱 UI 6px, 카드 8–12px, 마케팅 CTA 풀 필(100). 그 사이 값(15, 20 등)은 쓰지 않는다

**Page roster**

| File | Layout key | Surface | Purpose |
| --- | --- | --- | --- |
| `01_cover.svg` | `01_cover` | light + mesh | 표지 — 메시 그라디언트 백드롭 + 84px 헤드라인 |
| `02_agenda.svg` | `02_agenda` | light | 목차 — 헤어라인 5행 |
| `03_section.svg` | `03_section` | **dark** | 챕터 전환 — 극성 반전, 68px 헤드라인 |
| `04_polarity_flip.svg` | `04_polarity_flip` | **dark** | **시그니처** — 다크 + 터미널 목업 + 진술문 |
| `05_two_column.svg` | `05_two_column` | light | 좌 텍스트 / 우 카드 스택 |
| `06_card_grid.svg` | `06_card_grid` | light | 3-up 카드 그리드 |
| `07_metrics.svg` | `07_metrics` | light | 3-up 지표 밴드 |
| `08_chart_bar.svg` | `chart_linear` | light | 6-바 추이 + 피크 잉크 |
| `09_chart_line.svg` | `chart_linear` | light | 2계열 추이 (실선/점선) |
| `10_closing.svg` | `10_closing` | **dark** | 클로징 — 극성 반전 + 대형 마크 |

Full specification: [`decks/polarity/templates/design_spec.md`](../decks/polarity/templates/design_spec.md) · identity-only preset: [`brands/polarity/`](../brands/polarity/)

---

## Gradient Mesh Fintech

`gradient-mesh` · primary `#533AFD` · 10 pages

<img src="../previews/gradient-mesh.png" width="100%">

| | |
|---|---|
| **Theme** | Light — `#ffffff` 캔버스 + 쿨/웜 밴드 교대 |
| **Tone** | 정밀하고 낙관적 — 숫자를 다루되 차갑지 않다 |
| **Use cases** | 파트너 제안서, 핀테크 IR, 제품 이코노믹스, 가격·수수료 설명, 결제/정산 아키텍처 브리핑 |
| **Anchors** | [fintech, gradient, indigo, pill, tabular] |

**Signature**

1. **상단 메시 그라디언트** — 크림·셔벗·라벤더·인디고·루비 블롭이 상단 1/3을 채우고 아래로 캔버스 색으로 페이드된다. `01`과 `04`에만 등장
2. **풀 필 CTA** — 반경 9999의 인디고 필. 페이지당 최대 1개
3. **얇은 디스플레이** — 76px를 weight 300으로. 굵기가 아니라 크기가 위계다

**Page roster**

| File | Layout key | Surface | Purpose |
| --- | --- | --- | --- |
| `01_cover.svg` | `01_cover` | white + mesh | 표지 — 상단 1/3 메시 + 76px 얇은 헤드라인 + 인디고 필 |
| `02_agenda.svg` | `02_agenda` | white | 목차 — 헤어라인 5행 |
| `03_section.svg` | `03_section` | **navy** | 챕터 전환 — 네이비 카운터패널 |
| `04_gradient_statement.svg` | `04_gradient_statement` | white + mesh | **시그니처** — 메시 블롭 위 진술문 |
| `05_two_column.svg` | `05_two_column` | white | 좌 텍스트 / 우 카드 스택 |
| `06_card_grid.svg` | `06_card_grid` | cool | 3-up 카드 그리드 |
| `07_metrics.svg` | `07_metrics` | white | 3-up 지표 (3번째는 네이비 강조) |
| `08_chart_bar.svg` | `chart_linear` | white | 6-바 추이 + 피크 인디고 |
| `09_chart_line.svg` | `chart_linear` | white | 2계열 추이 |
| `10_closing.svg` | `10_closing` | **navy** | 클로징 — 네이비 + 대형 마크 |

Full specification: [`decks/gradient-mesh/templates/design_spec.md`](../decks/gradient-mesh/templates/design_spec.md) · identity-only preset: [`brands/gradient-mesh/`](../brands/gradient-mesh/)

---

## Warm Document

`warm-doc` · primary `#5645D4` · 10 pages

<img src="../previews/warm-doc.png" width="100%">

| | |
|---|---|
| **Theme** | Light (웜 뉴트럴) — `#ffffff` 캔버스 + `#f6f5f4` 서피스, 히어로만 네이비 |
| **Tone** | 친근하고 정돈됨 — 읽는 문서에 가까운 슬라이드 |
| **Use cases** | 사내 문서·핸드북, 신입 온보딩, 팀 위키 발표, 프로세스·정책 안내, 워크숍 자료 |
| **Anchors** | [document, warm-neutral, pastel, handbook, onboarding] |

**Signature**

1. **웜 뉴트럴 지반** — 본문 `#37352f`, 서피스 `#f6f5f4`, 경계 `#e5e3df`. 쿨그레이를 한 번도 쓰지 않는다
2. **1px 아웃라인 문법** — 모든 카드·패널·표가 헤어라인을 두른다. 그림자는 시스템 전체에 없다
3. **파스텔 틴트 5색 스택** — 시그니처 페이지에서 피치·로즈·민트·라벤더·스카이 카드가 계단식으로 겹친다. 정보 분류가 아니라 **리듬**이다

**Page roster**

| File | Layout key | Surface | Purpose |
| --- | --- | --- | --- |
| `01_cover.svg` | `01_cover` | **navy** | 표지 — 네이비 히어로 밴드 + 72px 헤드라인 |
| `02_agenda.svg` | `02_agenda` | white | 목차 — 헤어라인 5행 |
| `03_section.svg` | `03_section` | **navy** | 챕터 전환 |
| `04_tinted_cards.svg` | `04_tinted_cards` | surface | **시그니처** — 파스텔 틴트 5색 카드 스택 |
| `05_two_column.svg` | `05_two_column` | white | 좌 텍스트 / 우 아웃라인 스택 |
| `06_card_grid.svg` | `06_card_grid` | surface | 3-up 카드 그리드 (흰 카드 + 헤어라인) |
| `07_metrics.svg` | `07_metrics` | white | 3-up 지표 |
| `08_chart_bar.svg` | `chart_linear` | white | 6-바 추이 + 피크 퍼플 |
| `09_chart_line.svg` | `chart_linear` | white | 2계열 추이 |
| `10_closing.svg` | `10_closing` | **navy** | 클로징 |

Full specification: [`decks/warm-doc/templates/design_spec.md`](../decks/warm-doc/templates/design_spec.md) · identity-only preset: [`brands/warm-doc/`](../brands/warm-doc/)

---

## Open Road

`open-road` · primary `#3E6AE1` · 10 pages

<img src="../previews/open-road.png" width="100%">

| | |
|---|---|
| **Theme** | Light + 카본 다크 구분면 — `#FFFFFF` 본문, `#171A20` 챕터·클로징 |
| **Tone** | 확신에 차고 조용함 — 갤러리처럼 한 번에 하나만 보여준다 |
| **Use cases** | 제품 런칭, 브랜드 키노트, 비전 발표, 쇼룸·전시 프레젠테이션, 신사업 소개 |
| **Anchors** | [cinematic, photography, keynote, gallery, launch] |

**Signature**

1. **한 페이지 한 메시지** — 시그니처 페이지(`04`)는 사진 한 장과 문장 하나뿐이다. 불릿·카드·아이콘을 얹지 않는다
2. **풀블리드 사진 = 페이지 자체** — `01`/`04`는 사진이 캔버스 가장자리까지 닿는다. 라운딩 0, 프레임 없음
3. **각진 지오메트리** — 기본 반경 0. 버튼 4, 카테고리 카드 12. 그 사이 값은 쓰지 않는다

**Page roster**

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

Full specification: [`decks/open-road/templates/design_spec.md`](../decks/open-road/templates/design_spec.md) · identity-only preset: [`brands/open-road/`](../brands/open-road/)

---

## Signal Green

`signal-green` · primary `#76B900` · 10 pages

<img src="../previews/signal-green.png" width="100%">

| | |
|---|---|
| **Theme** | **Dual** — 히어로·챕터·클로징은 `#000000`, 콘텐츠·데이터는 `#FFFFFF` |
| **Tone** | 단호하고 기술적 — 성능 수치가 주인공이다 |
| **Use cases** | AI·GPU·인프라 브리핑, 개발자 세션, 기술 컨퍼런스 발표, 벤치마크·성능 리포트, 플랫폼 로드맵 |
| **Anchors** | [tech-keynote, angular, signal-accent, benchmark, dual-theme] |

**Signature**

1. **12×12px 그린 코너 스퀘어** — 카드·패널의 좌상단에 놓이는 이 시스템의 서명. 아이콘도 불릿도 아닌 **위치 표식**이다
2. **극성 교대** — 블랙(`01`/`03`/`04`/`10`)과 화이트(`02`/`05`–`09`)가 번갈아 나온다. 어두움이 챕터를 연다
3. **앵귤러 2px** — 카드·버튼·바는 반경 **2px**. 히어로·푸터·풀블리드는 0. 그 사이 값은 쓰지 않는다

**Page roster**

| File | Layout key | Surface | Purpose |
| --- | --- | --- | --- |
| `01_cover.svg` | `01_cover` | **black** | 표지 — 블랙 + 72px 볼드 + 그린 규칙선 |
| `02_agenda.svg` | `02_agenda` | white | 목차 — 헤어라인 5행 |
| `03_section.svg` | `03_section` | **black** | 챕터 전환 — 극성 반전 |
| `04_black_hero.svg` | `04_black_hero` | **black** | **시그니처** — 12×12 그린 코너 스퀘어 + 진술문 |
| `05_two_column.svg` | `05_two_column` | white | 좌 텍스트 / 우 패널 스택 |
| `06_card_grid.svg` | `06_card_grid` | white | **4-up** 카드 그리드 (코너 스퀘어 장식) |
| `07_metrics.svg` | `07_metrics` | white | 3-up 지표 밴드 |
| `08_chart_bar.svg` | `chart_linear` | white | 6-바 추이 + 피크 그린 |
| `09_chart_line.svg` | `chart_linear` | white | 2계열 추이 |
| `10_closing.svg` | `10_closing` | **black** | 클로징 — 극성 반전 |

Full specification: [`decks/signal-green/templates/design_spec.md`](../decks/signal-green/templates/design_spec.md) · identity-only preset: [`brands/signal-green/`](../brands/signal-green/)

---
