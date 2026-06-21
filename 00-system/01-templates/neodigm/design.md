# 네오다임(Neodigm) Design Guide

> 단일 출처 비주얼 아이덴티티. PDF 보고서·HTML 대시보드·랜딩·슬라이드 어떤 산출물이든
> 이 파일을 참조하면 네오다임 톤이 즉시 적용된다.
> 리서치(neodigm.com·en.neodigm.com, 2026-06)로 확인된 톤만 반영.
> 정확한 브랜드 Hex는 공개 가이드라인이 없어 **시각 근사값**을 사용한다 (Known Gaps 참조).

## Overview

네오다임의 비주얼은 **테크·엔터프라이즈 미니멀**이다. 캔버스는 거의 검정에 가까운 **딥 차콜**(`{colors.canvas}` — 다크 베이스)이고, 그 위에 **흰색 타이포**(`{colors.on-dark}`)가 절제된 산세리프로 얹힌다. 글로벌 IT 대기업(Adobe·AWS·Microsoft·HP·Cisco)을 전담하는 B2B 통합 마케팅 대행사답게, 비주얼은 화려함이 아니라 **신뢰감·정밀함·여백**으로 만들어진다. 장식 요소는 최소화하고, 데이터·로직·결과가 주인공이다.

브랜드의 보이스는 슬로건 "**아이디어를 결과로 만드는 경험을 선사합니다**"(We deliver an experience that turns ideas into results)에 압축돼 있다. 아이디어(추상)를 결과(수치·성과)로 변환하는 회사이므로, 산출물 역시 **막연한 인상이 아니라 측정 가능한 지표**로 말한다. voltage(시각적 긴장)는 다크 캔버스 위 단 하나의 **시그니처 액센트 컬러**(`{colors.accent}`)와 큰 KPI 숫자에서 나온다 — 색을 남발하지 않고 한 점에 집중시킨다.

산출물에 적용할 때 핵심은 **다크 + 단색 액센트 절제**다. 액센트는 강조·핵심 수치·CTA에만 쓰고, 본문은 부드러운 회백색 텍스트(`{colors.body}`)로 다크 면 위에 인쇄된 느낌을 낸다. 그라데이션·드롭섀도는 거의 쓰지 않고, 깊이는 **한 단계씩 밝아지는 차콜 색면**과 1px 헤어라인으로 만든다 — 엔터프라이즈 대시보드의 질감이 네오다임이다.

**Key Characteristics:**
- 캔버스는 딥 차콜 다크 베이스(`{colors.canvas}`) — 순백 배경은 마케팅 표면에서 쓰지 않는다.
- 시그니처는 **단일 액센트 컬러**(`{colors.accent}`). 강조·핵심 KPI·CTA 전용. 본문 텍스트는 회백색(`{colors.body}`).
- 타이포는 **모던 산세리프**. 디스플레이는 묵직하게(700), 본문은 가볍게(400) — 무게 대비가 편집 시그니처.
- 깊이는 그림자가 아니라 **차콜 색면 단계**(canvas → surface-soft → surface-card → surface-elevated)와 헤어라인(`{colors.hairline}`)으로.
- 모서리는 작게(`{rounded.sm}`)거나 직각(`{rounded.none}`). 엔터프라이즈 대시보드처럼 단정하게.
- KPI 숫자는 크게·액센트로 — 데이터가 주인공. "아이디어를 결과로"의 결과 = 수치.
- 여백은 넉넉히: 섹션 간 `{spacing.section}`, 카드 내부 `{spacing.xl}`. 빽빽함보다 정밀함.

## Colors

### Brand & Accent
- **Accent** (`{colors.accent}` — #2D7FF9): 시그니처 단일 액센트(테크 블루). 헤드라인 강조·핵심 KPI 수치·CTA·주요 도식. 다크 캔버스 위에서 가장 도드라지는 한 색. (정확한 브랜드 컬러 미확인 — Known Gaps 참조)
- **Accent Soft** (`{colors.accent-soft}` — #6BA6FB): 액센트의 옅은 변형. 보조 강조·링크 호버·도식 보조선.
- **Accent Deep** (`{colors.accent-deep}` — #1B5FCC): 액센트의 짙은 변형. 버튼 호버·진한 구획.

### Surface
- **Canvas** (`{colors.canvas}` — #0E1116): 기본 페이지 바닥. 딥 차콜 다크 베이스.
- **Surface Soft** (`{colors.surface-soft}` — #151A21): 표 셀·푸터 인접 스트립용 한 단계 밝은 차콜.
- **Surface Card** (`{colors.surface-card}` — #1B2129): 카드 배경. 캔버스보다 밝아 다크 면 위에 떠 보임.
- **Surface Elevated** (`{colors.surface-elevated}` — #232B35): 중첩 카드·강조 카드용 한 단계 더 밝은 면.

### Hairlines & Borders
- **Hairline** (`{colors.hairline}` — #2C3440): 다크 면 위 1px 구분선. 섹션·표 행·카드 외곽.
- **Hairline Strong** (`{colors.hairline-strong}` — #3A4452): 강조 구분선·표 헤더 하단 라인.

### Text
- **On Dark** (`{colors.on-dark}` — #FFFFFF): 헤드라인·핵심 텍스트 기본. 다크 위 순백.
- **Body** (`{colors.body}` — #C2C9D2): 본문 러닝 텍스트. 순백보다 한 톤 부드럽게.
- **Body Strong** (`{colors.body-strong}` — #E4E8ED): 강조 본문·리드 문단.
- **Muted** (`{colors.muted}` — #7C8794): 캡션·메타·푸터 링크. 다크 위 회색.

### Semantic
- **Positive** (`{colors.positive}` — #2FB57E): 목표 달성·성과 상승 등 긍정 지표.
- **Negative** (`{colors.negative}` — #E5564E): 목표 미달·하락·위험 신호.
- **Warning** (`{colors.warning}` — #E0A93C): CPL 급등·저효율 등 주의 신호.

## Typography

### Font Family
모던 산세리프 한 종을 무게로 운용. 네오다임 공식 폰트명은 미공개이므로 시스템 대체 스택을 쓴다.
- 디스플레이/헤드라인: `"Pretendard", "Noto Sans KR", -apple-system, "Segoe UI", sans-serif` — 700 묵직하게.
- 본문/UI: 동일 스택 — 400 가독 위주. (디스플레이/본문 같은 패밀리, 무게로 구분)
- 숫자(KPI): 동일 스택 + `font-variant-numeric: tabular-nums` — 표·대시보드 숫자 정렬.

### Hierarchy
| 토큰 | 용도 | 크기/두께(데스크톱) |
|------|------|---------------------|
| `{typography.display-xl}` | 표지·히어로 타이틀 | 44–52px / 700 |
| `{typography.display-lg}` | 섹션 대제목 | 32px / 700 |
| `{typography.heading}` | 소제목 | 22px / 600 |
| `{typography.label-uppercase}` | 라벨·카테고리 | 12px / 600 / letter-spacing 0.08em / muted |
| `{typography.body-lg}` | 리드 문단 | 18px / 400 |
| `{typography.body-md}` | 기본 본문 | 15px / 400 |
| `{typography.caption}` | 캡션·메타 | 12px / 400 muted |
| `{typography.number}` | KPI 수치 | 30–40px / 700, Accent 강조 가능, tabular-nums |

### Principles
- 한 패밀리 안에서 **무게 대비**로 위계를 만든다 — 디스플레이 700, 본문 400.
- 라벨은 작게·자간 넓게(`{typography.label-uppercase}`) 대시보드 캡션처럼, muted 색으로.
- 숫자(KPI)는 크게·tabular-nums로 정렬, 핵심 지표는 Accent.

### Note on Font Substitutes
네오다임 실제 서체는 비공개. 위 스택은 "모던 산세리프"라는 확인된 무드를 시스템/오픈소스 폰트(Pretendard)로 근사한 것. 실제 사이트 서체와 다를 수 있음.

## Layout

### Spacing System
- `{spacing.section}` — 64px (섹션 간)
- `{spacing.xxl}` — 48px (히어로 밴드 내부)
- `{spacing.xl}` — 32px (카드 내부)
- `{spacing.lg}` — 24px
- `{spacing.md}` — 16px
- `{spacing.sm}` — 8px

### Grid & Container
- 최대 콘텐츠 폭 1080–1200px, 중앙 정렬. 엔터프라이즈 대시보드 느낌의 넓은 단.
- 카드 그리드는 12컬럼 기준, KPI 카드는 3–4열.

### Whitespace Philosophy
다크 면 위에서 여백을 충분히. 빽빽이 채우기보다, 단색 액센트와 큰 숫자가 여백 위에서 도드라지게.

## Elevation & Depth

| Level | 용도 | 처리 |
|-------|------|------|
| 0 | 캔버스 | 그림자 없음 |
| 1 | 카드 | `{colors.surface-card}` 면 + 1px 헤어라인(`{colors.hairline}`), 그림자 거의 없음 |
| 2 | 강조 카드 | `{colors.surface-elevated}` 한 단계 밝은 면으로 구분, 그림자 대신 색면 |

### Decorative Depth
깊이는 **그림자가 아니라 차콜 색면 단계와 헤어라인**으로 만든다. 엔터프라이즈 대시보드 질감 유지. 액센트 컬러의 옅은 글로우(매우 절제)는 핵심 KPI 1곳에만 허용.

## Shapes

### Border Radius Scale
| 토큰 | 값 | 용도 |
|------|----|----|
| `{rounded.none}` | 0px | 표·구획 라인·풀폭 밴드 |
| `{rounded.sm}` | 4px | 버튼·칩·작은 카드 |
| `{rounded.md}` | 8px | 큰 카드 (최대치 — 그 이상 둥글게 X) |
| `{rounded.full}` | 9999px | 아이콘 버튼·상태 점만 |

### Photography Geometry
이미지·차트는 다크 카드 위 직각 또는 4px 라운드. 풀블리드 히어로는 다크 오버레이를 깔아 텍스트 가독 확보. 데이터 시각화(차트)가 사진보다 우선 — B2B 테크 톤.

## Components

### Top Navigation
다크 캔버스 위 흰 텍스트. 로고 좌측, 메뉴 우측. 하단 1px 헤어라인. 그림자 없음. 스크롤 시 surface-soft로 한 톤.

### Buttons
- **Primary** (`{component.button-primary}`): Accent 면 + 흰 텍스트, `{rounded.sm}`. 호버 시 `{colors.accent-deep}`.
- **Secondary**: 투명 배경 + 헤어라인 테두리 1px + 흰 텍스트. 호버 시 surface-card.
- **Ghost**: 텍스트만, 밑줄 호버, Accent 텍스트.

### Cards & Containers
`{colors.surface-card}` 배경 + `{colors.hairline}` 1px 테두리 + `{rounded.sm/md}`. 엔터프라이즈 카드처럼 단정. KPI 카드는 큰 숫자(`{typography.number}`, 핵심은 Accent) + 아래 해석 한 줄(muted).

### Inputs & Forms
surface-soft 배경 + 헤어라인 테두리. 포커스 시 Accent 테두리. `{rounded.sm}`. 흰 텍스트.

### Signature Components
- **KPI Strip** (`{component.kpi-strip}`): 다크 캔버스 위 3–4 KPI 카드 가로 배열. 큰 숫자(Accent) + 라벨(muted uppercase) + 해석 한 줄. 네오다임 보고서의 얼굴.
- **Accent Rule** (`{component.accent-rule}`): Accent 색 굵은 구분선(3px) — 섹션 구획 시그니처. 색 1점 집중.
- **Result Band** (`{component.result-band}`): surface-elevated 반전 밴드 — "아이디어 → 결과" 핵심 인용·헤드라인에 사용, 위에 흰 텍스트 + Accent 숫자.

### Footer
`{colors.surface-soft}` 배경 + 로고 + 주소(서초구 서초대로 346)/연락처 + 헤어라인 상단 구분. muted 텍스트.

## Do's and Don'ts

### Do
- 캔버스는 딥 차콜 다크 베이스로.
- 액센트 한 색만 강조·핵심 KPI·CTA에 절제해서.
- 본문은 회백색 텍스트로 — 다크 면 가독.
- KPI 숫자는 크게, 핵심은 Accent로.
- 깊이는 차콜 색면 단계 + 헤어라인으로.
- objective(인지/리드/ABM)가 다른 지표는 시각적으로도 구분해서 보여주기.

### Don't
- 순백(#FFFFFF) 배경 쓰지 않기 — 다크 톤이 네오다임.
- 액센트를 본문 전체에 남발하지 않기 (강조력 소실). 한 색에 집중.
- 화려한 그라데이션·드롭섀도 쓰지 않기.
- 과하게 둥근 모서리(16px+) 쓰지 않기.
- 색을 두세 개 동시에 강조로 쓰지 않기 — 단색 액센트가 원칙.
- 다른 브랜드 톤(라이트 모드 종이 톤·레트로) 섞지 않기.

## Responsive Behavior

### Breakpoints
| 이름 | 폭 |
|------|----|
| Mobile | < 640px |
| Tablet | 640–1024px |
| Desktop | > 1024px |

### Touch Targets
버튼·링크 최소 44×44px.

### Collapsing Strategy
KPI 4열 → 모바일 1–2열. 표는 가로 스크롤 또는 카드형 전환. 차트는 비율 유지 축소.

### Image Behavior
차트·이미지는 비율 유지, 여백 두고 축소. 풀블리드 히어로는 모바일에서 높이 축소 + 다크 오버레이 유지.

## Iteration Guide
1. 새 산출물은 캔버스(딥 차콜) + 회백색 본문에서 시작.
2. 강조가 필요한 곳에만 Accent 한 색.
3. 구획은 Accent Rule 또는 헤어라인.
4. 표지·핵심 인용엔 Result Band(surface-elevated 반전).
5. 숫자(KPI)는 크게·tabular-nums, 핵심은 Accent.
6. 그림자 대신 차콜 색면 단계로 깊이.
7. "아이디어 → 결과" — 모든 산출물이 측정 가능한 지표로 끝나게.
8. 색을 두 개째 강조로 쓰고 싶으면 멈추고 여백·무게·크기로 먼저 푼다.

## Known Gaps
- **정확한 브랜드 Hex 미확인**: 공개 브랜드 가이드라인 없음. WebFetch로 "어두운 배경 + 흰 텍스트"까지만 확인, CSS/로고 이미지 직접 파싱 불가. 위 Accent(#2D7FF9 테크 블루)는 "엔터프라이즈 테크" 무드의 **시각 근사값** — 실제 브랜드 컬러는 neodigm.com 개발자 도구(F12)로 CSS 직접 확인 후 보정 필요.
- **공식 서체명 미확인**: 시스템/오픈소스 대체 스택(Pretendard) 사용.
- **로고 형태/마크 미확인**: 이미지 접근 불가. 본 가이드는 톤만 정의. 실제 로고 파일 별도 확보 필요.
- 모션/인터랙션 가이드 미스코프(정적 산출물 우선).
