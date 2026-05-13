# 프리윌 (Freewill) Design System

> 청소년 기업가정신 · 공교육 디지털전환 · Apple 파트너 연수
> 단일 출처. PDF 보고서 · HTML 대시보드 · 슬라이드 · 워크북 산출물 어디든 이 파일을 참조한다.

---

## Overview

프리윌의 비주얼 표면은 **크림 캔버스 위에 짙은 잉크와 활기색 한 점**으로 정리된다. 청소년 기업가정신 교육 — 청소년이 본인 사업 아이디어를 꺼내고, 워크북을 채우고, 발표하는 과정을 담는 도구다. 너무 가벼우면 학교가 안 따라오고, 너무 무거우면 학생이 멀어진다. 그 사이의 톤이 프리윌 브랜드 보이스다.

캔버스는 따뜻한 크림(`{colors.canvas}` — #FAF7F2)을 기본으로 한다. 종이 워크북에서 시작된 브랜드라 화면 위에서도 종이의 톤을 잃지 않는다. 본문은 짙은 잉크(`{colors.ink}` — #1A1A1A)로 또렷하게 떨어지고, 액션·강조·차시 마커는 **프리윌 오렌지(`{colors.freewill-orange}` — #FF6B35)** 한 점만 사용한다. 청소년이 워크북을 펼쳤을 때 "여기서부터 내 차례야"라고 인식되는 한 점의 색이다.

타입 보이스는 **Pretendard** (한글 본문·헤드라인 공통)와 **Inter** (영문·숫자 라벨)의 페어링이다. 헤드라인은 700 굵게 떨어지되 한국어 자간을 -0.02em으로 살짝 좁혀 "단단한 교과서" 느낌을 낸다. 본문은 400으로 가볍게 흘러 워크북·운영 보고서·이메일 어디든 읽기 부담 없이 적용된다. 숫자(차시·날짜·인원)는 Inter Mono로 떨어뜨려 표 안에서 정렬이 흐트러지지 않게 한다.

**Key Characteristics:**
- 크림 캔버스(`{colors.canvas}` — #FAF7F2) 위에 짙은 잉크 본문(`{colors.ink}` — #1A1A1A). 다크 모드 없음 — 학교 현장은 항상 라이트.
- 프리윌 오렌지(`{colors.freewill-orange}` — #FF6B35)는 액션·강조·차시 마커 전용. 배경 fill 금지. 한 화면에 1~3회 미만.
- 보조 색은 청록 (`{colors.freewill-teal}` — #2C7A7B): 안정·신뢰의 짝색. 통계 카드·운영 상태 라벨에 사용.
- 헤드라인은 Pretendard 700, 자간 -0.02em. 본문은 400. 숫자는 Inter Mono.
- 라운드는 `{rounded.md}` 6px 기본. 워크북·노트의 둥근 모서리에서 가져왔다. 카드·버튼 공통.
- 차시 마커는 모눈 박스 (`{component.session-chip}`) — 1차시·2차시·3차시 식별이 한 눈에 가능하게.
- 간격은 8px 베이스. 섹션 간 `{spacing.section}` 64px, 카드 안쪽 `{spacing.xl}` 24px.

---

## Colors

### Brand & Accent

- **Freewill Orange** (`{colors.freewill-orange}` — #FF6B35): 액션·강조·차시 마커 전용. CTA 버튼 텍스트(흰 배경+오렌지 보더 OR 오렌지 배경+흰 텍스트). 한 화면에 1~3회. 배경 fill로 큰 면적에 사용 금지.
- **Freewill Orange Soft** (`{colors.freewill-orange-soft}` — #FFE4D6): 오렌지의 10% 톤. 차시 마커 배경, 강조 단어 하이라이트.
- **Freewill Teal** (`{colors.freewill-teal}` — #2C7A7B): 운영 상태 라벨, 통계 카드 액센트. 청록 — 오렌지의 보색 안정감.
- **Freewill Teal Soft** (`{colors.freewill-teal-soft}` — #E0F2F1): 청록의 10% 톤. 정상 상태 배경.

### Surface

- **Canvas** (`{colors.canvas}` — #FAF7F2): 페이지 기본 바닥. 크림 — 워크북 종이 톤.
- **Surface** (`{colors.surface}` — #FFFFFF): 카드·테이블 행·모달 표면. 캔버스보다 한 톤 밝아 정보가 떠 보임.
- **Surface Muted** (`{colors.surface-muted}` — #F2EFE8): 캔버스보다 살짝 어두운 톤. 표 헤더·푸터·캡션 배경.
- **Surface Strong** (`{colors.surface-strong}` — #2A2A2A): 다크 강조 카드(예: 헤드라인 통계 카드). 본문 카드 톤 변환용.

### Hairlines & Borders

- **Hairline** (`{colors.hairline}` — #E0DAD0): 1px 디바이더. 카드 보더, 테이블 행 구분.
- **Hairline Strong** (`{colors.hairline-strong}` — #C7BFB0): 강조 보더. 차시 박스·중요 카드 외곽.

### Text

- **Ink** (`{colors.ink}` — #1A1A1A): 본문·헤드라인 기본 색. 순흑보다 살짝 부드러움.
- **Body** (`{colors.body}` — #4A4A4A): 보조 본문·서브 카피.
- **Muted** (`{colors.muted}` — #8C8C8C): 캡션·메타 정보 (날짜·작성자·차시 라벨).
- **Disabled** (`{colors.disabled}` — #BFBFBF): 비활성·플레이스홀더.

### Semantic (운영 상태)

- **Status Success** (`{colors.success}` — #16A34A): 발송완료·배송완료·후기작성완료.
- **Status Warning** (`{colors.warning}` — #F59E0B): 발송준비중·후기 미작성 3일 초과·이슈 미확인 2일 초과.
- **Status Danger** (`{colors.danger}` — #DC2626): 미발송 D-3 이내·심각도 `심` 이슈 미확인.
- **Status Neutral** (`{colors.neutral}` — #6B7280): 예정·정보성 라벨.

---

## Typography

### Font Family

**Pretendard** (한글 본문·헤드라인 공통) + **Inter** (영문·숫자) 페어링. Inter Mono는 표 안의 숫자 정렬용.

폴백 스택: `Pretendard, -apple-system, BlinkMacSystemFont, "Apple SD Gothic Neo", "Noto Sans KR", sans-serif`.

학교·교육청 PC 환경(맥/윈도우 혼재)에서 Pretendard 없는 경우 시스템 폰트로 떨어진다. 자간·행간 토큰은 폴백 시에도 유지.

### Hierarchy

| Token | Size | Weight | Line Height | Letter Spacing | Use |
|---|---|---|---|---|---|
| `{typography.display-xl}` | 40px | 700 | 1.2 | -0.02em | 보고서 표지 제목, 헤로 h1 |
| `{typography.display-lg}` | 32px | 700 | 1.25 | -0.02em | 섹션 헤드 (예: "다음 주 수업 예정") |
| `{typography.display-md}` | 24px | 700 | 1.3 | -0.02em | 서브섹션, 카드 헤드라인 통계 |
| `{typography.title-lg}` | 20px | 700 | 1.4 | -0.01em | 카드 타이틀, 학교명 리스트 헤드 |
| `{typography.title-md}` | 18px | 600 | 1.4 | -0.01em | 본문 안 강조 헤드 |
| `{typography.title-sm}` | 16px | 600 | 1.5 | 0 | 표 헤더, 라벨 |
| `{typography.body-lg}` | 16px | 400 | 1.6 | 0 | 본문 기본 |
| `{typography.body-md}` | 14px | 400 | 1.6 | 0 | 표 본문, 보조 텍스트 |
| `{typography.body-sm}` | 13px | 400 | 1.5 | 0 | 캡션·메타 |
| `{typography.label-uppercase}` | 12px | 700 | 1.3 | 0.08em | 차시 마커, 운영 상태 라벨 ("D-3", "긴급") |
| `{typography.number-mono}` | 14px | 500 | 1.4 | 0 | 표 안 숫자 (Inter Mono) |
| `{typography.button}` | 14px | 600 | 1.0 | 0 | 버튼 라벨 |

### Principles

헤드라인은 Pretendard 700에 자간 -0.02em — 한국어 글자가 살짝 좁아져 "단단한 교과서" 느낌이 난다. 본문은 weight 400을 유지 — 워크북·이메일·보고서가 모두 읽기 부담 없이 흐른다. 라벨(`{typography.label-uppercase}`)만 letter-spacing 0.08em로 떨어져 "이건 메타다" 신호를 준다.

UPPERCASE는 영문 라벨 한정. 한국어 헤드라인은 항상 sentence case — UPPERCASE 한국어는 시각적으로 무너진다.

### Note on Font Substitutes

Pretendard 미설치 환경(일부 학교 PC)에서는 폴백 시스템 폰트로 떨어지되, weight·spacing 토큰은 유지. 폰트 다운로드는 [pretendard.fontworks.kr](https://cactus.tistory.com/306) 기준 v1.3.9.

---

## Layout

### Spacing System

8px 베이스 그리드. 모든 간격 토큰은 8의 배수.

| Token | Value | Use |
|---|---|---|
| `{spacing.xs}` | 4px | 인라인 아이콘과 텍스트 사이 |
| `{spacing.sm}` | 8px | 라벨과 값 사이, 인접 텍스트 |
| `{spacing.md}` | 16px | 카드 안 요소 간격 |
| `{spacing.lg}` | 24px | 카드 안쪽 padding |
| `{spacing.xl}` | 32px | 섹션 안 그룹 간격 |
| `{spacing.xxl}` | 48px | 큰 섹션 간격 |
| `{spacing.section}` | 64px | 페이지 메이저 섹션 |

### Grid & Container

- 보고서 PDF: A4 세로, 좌우 margin 40px, 상하 margin 56px
- 대시보드 HTML: 최대 너비 1280px, 좌우 padding 32px (모바일 16px)
- 카드 그리드: 데스크톱 3-up / 태블릿 2-up / 모바일 1-up. gap `{spacing.md}` 16px

### Whitespace Philosophy

학교 운영 보고서는 정보 밀도가 높다. 그래서 **카드 안쪽 padding(`{spacing.lg}` 24px)을 후하게**, **카드 사이는 짧게(`{spacing.md}` 16px)** 둔다. 카드 안에서 숨 쉬게 하고 카드 사이는 묶어 보이게.

---

## Elevation & Depth

| Level | Shadow | Use |
|---|---|---|
| `{elevation.0}` | none | 캔버스에 누운 평면 표면 |
| `{elevation.1}` | `0 1px 2px rgba(26,26,26,0.06)` | 카드 기본 |
| `{elevation.2}` | `0 4px 12px rgba(26,26,26,0.08)` | 강조 카드 (헤드라인 통계) |
| `{elevation.3}` | `0 12px 32px rgba(26,26,26,0.12)` | 모달·드롭다운 |

### Decorative Depth

그림자는 절제. 카드 elevation은 1~2 사이에서 머문다. 학교 보고서는 종이 워크북의 평면감을 유지해야 한다 — 3D 느낌은 학교 현장에 맞지 않는다.

---

## Shapes

### Border Radius Scale

| Token | Value | Use |
|---|---|---|
| `{rounded.none}` | 0px | 표 셀, 디바이더 |
| `{rounded.sm}` | 4px | 작은 라벨·뱃지 |
| `{rounded.md}` | 6px | 카드·버튼 기본 |
| `{rounded.lg}` | 12px | 큰 카드·모달 |
| `{rounded.full}` | 9999px | 원형 아이콘 버튼, 차시 마커 |

### Photography Geometry

사진은 6px(`{rounded.md}`) 라운드로 떨어진다. 워크북에서 캡처한 학생 사진·교실 풍경 등이 다음 회차 운영 자료에 인용될 때 통일된 톤. 풀블리드 사진은 라운드 없이 0px.

---

## Components

### Top Navigation

- 높이 64px
- 배경 `{colors.surface}` #FFFFFF, 하단 1px `{colors.hairline}` 보더
- 로고 좌측, 메뉴 중앙, 사용자 우측
- 메뉴 항목 `{typography.body-md}` `{colors.body}` — 활성 항목은 `{colors.freewill-orange}` + 하단 2px 보더

### Buttons

**Primary** (`{component.button-primary}`):
- 배경 `{colors.freewill-orange}`, 텍스트 `{colors.surface}` (흰색)
- padding `{spacing.sm}` 8px `{spacing.lg}` 24px
- 라운드 `{rounded.md}` 6px
- 호버: 배경 10% 어둡게

**Secondary** (`{component.button-secondary}`):
- 배경 `{colors.surface}`, 텍스트 `{colors.ink}`, 보더 1px `{colors.hairline-strong}`
- 호버: 보더 `{colors.freewill-orange}`로 전환

**Ghost** (`{component.button-ghost}`):
- 배경 투명, 텍스트 `{colors.body}`
- 호버: 배경 `{colors.surface-muted}`

### Cards & Containers

**Stat Card** (`{component.stat-card}`):
- 배경 `{colors.surface}`, 보더 1px `{colors.hairline}`
- padding `{spacing.lg}` 24px
- 라운드 `{rounded.md}` 6px
- 헤더: 라벨 `{typography.label-uppercase}` `{colors.muted}`
- 메인 숫자: `{typography.display-md}` `{colors.ink}` Inter Mono
- 보조 텍스트: `{typography.body-sm}` `{colors.body}`

**Issue Card** (`{component.issue-card}`):
- 배경 `{colors.surface}`, 좌측 4px 보더 `{colors.danger}` (심각도 `심`) / `{colors.warning}` (심각도 `중`) / `{colors.neutral}` (심각도 `저`)
- padding `{spacing.lg}` 24px
- 헤더: 학교명 `{typography.title-md}` + 차시 chip
- 본문: 후기 텍스트 `{typography.body-md}`
- 푸터: 대응상태 라벨 + 작성일 메타

### Session Chip (`{component.session-chip}`)

차시 마커. 워크북에서 가져온 모눈 박스.
- 배경 `{colors.freewill-orange-soft}` #FFE4D6
- 텍스트 `{colors.freewill-orange}` #FF6B35
- 폰트 `{typography.label-uppercase}`
- padding 2px 8px, 라운드 `{rounded.sm}` 4px
- 표기: "3차시 / 6차시" — "/" 좌우 공백 없이 (Inter Mono 정렬)

### Status Badge (`{component.status-badge}`)

- 라운드 `{rounded.full}` 9999px
- padding 2px 10px
- 폰트 `{typography.label-uppercase}` 11px
- 색상: 운영 상태별 (success / warning / danger / neutral) — 배경은 해당 색의 soft 톤, 텍스트는 진한 톤

### School Row (`{component.school-row}`)

운영 보고서 표 한 행.
- 학교명 `{typography.title-sm}` `{colors.ink}`
- 학년 chip (`{colors.surface-muted}` 배경, `{colors.body}` 텍스트)
- 지역 `{typography.body-sm}` `{colors.muted}`
- 차시 chip
- 발송상태 badge
- 행 사이 1px `{colors.hairline}` 디바이더, 행 padding `{spacing.md}` 16px

### Inputs & Forms

- 입력 필드: 배경 `{colors.surface}`, 보더 1px `{colors.hairline-strong}`, 라운드 `{rounded.md}` 6px
- focus: 보더 2px `{colors.freewill-orange}`
- 라벨: `{typography.title-sm}` `{colors.ink}` 입력 위에 8px 떨어져 배치

### Footer

- 배경 `{colors.surface-muted}` #F2EFE8
- padding `{spacing.section}` 64px 상하
- 텍스트 `{typography.body-sm}` `{colors.muted}`
- 좌측: 프리윌 로고 + "청소년 기업가정신 교육"
- 우측: 본부 연락처·이메일

### Signature Components

**Headline Stat Band**: 보고서 최상단의 "다음 주 N개교 / 발송 미완료 N건 / 긴급 N건" 헤드라인.
- 3-up 그리드, 각 셀 `{component.stat-card}`
- 가장 우려되는 셀(긴급)은 좌측 4px 보더 `{colors.danger}`
- 셀 헤더 라벨 + 큰 숫자 + 한 줄 설명

**Issue Stack**: 미확인 이슈 카드를 심각도 순으로 쌓아 보여주는 컴포넌트.
- 카드 간격 `{spacing.md}` 16px
- 심각도 `심` 카드는 상단 고정 — 스크롤해도 시야 안에 머무름

---

## Do's and Don'ts

### Do's

1. 헤드라인 통계는 Inter Mono 숫자로 떨어뜨려 정렬 흐트러뜨리지 말 것
2. 차시 마커는 항상 모눈 box로 — 텍스트로 "3차시"만 적지 말 것
3. 학교명은 절대 약칭으로 자르지 말 것 ("새빛고" X → "새빛고등학교" O)
4. 운영 상태는 색만 사용 금지 — 항상 텍스트 라벨 동반 (색맹·인쇄 흑백 고려)
5. 보고서는 헤드라인 3줄을 페이지 최상단에 배치 — "그래서 뭐?" 답이 먼저 보이게

### Don'ts

1. 프리윌 오렌지를 큰 면적 배경 fill로 사용 금지 (소프트 톤만 가능)
2. 본문 weight를 500+ 로 올리지 말 것 — 본문은 항상 400
3. 카드 elevation 3 이상 금지 — 종이 톤 깨짐
4. 한국어 헤드라인 UPPERCASE 금지
5. 차시 마커에 보더만 두고 배경 없애지 말 것 — 본문 흐름과 시각적으로 분리되어야 함
6. 다크 모드 만들지 말 것 — 학교·교사·학부모 환경은 항상 라이트

---

## Responsive Behavior

### Breakpoints

| Token | Width | Use |
|---|---|---|
| `{bp.mobile}` | < 640px | 학교·강사 휴대폰 미리보기 |
| `{bp.tablet}` | 640~1024px | iPad (Apple 연수 환경) |
| `{bp.desktop}` | > 1024px | 본부 데스크톱·보고서 |

### Touch Targets

iPad·핸드폰 터치 환경: 최소 44x44px (Apple HIG 기준). 작은 chip·뱃지 외에는 모두 충족.

### Collapsing Strategy

- 모바일: 카드 그리드 3-up → 1-up, 표는 가로 스크롤 대신 카드형으로 재배치
- 헤드라인 통계 카드는 모바일에서도 3-up 유지 (가장 중요한 정보)

### Image Behavior

학교 사진·교실 사진은 모바일에서 16:9 → 4:3으로 비율 변경. 캡션은 항상 사진 아래.

---

## Iteration Guide

1. 새 색이 필요하면 먼저 기존 토큰으로 해결 가능한지 확인
2. 프리윌 오렌지·청록 외 새 액센트 색 추가는 금지 (브랜드 위반)
3. 폰트는 Pretendard·Inter·Inter Mono 외 추가 금지
4. 운영 상태 색은 success/warning/danger/neutral 4단계 유지 — 추가 단계 금지
5. 새 컴포넌트는 기존 토큰으로만 조립. hex 인라인 금지
6. 어두운 surface(`{colors.surface-strong}`)는 헤드라인 카드 1개에만 사용 — 페이지 전체에 흩뿌리지 말 것
7. PDF 산출물은 A4 세로 1장이 기본 — 길어지면 헤드라인을 깎고 본문은 그대로 둠
8. 워크북·강의안은 design.md를 그대로 적용 — 보고서와 톤이 일치해야 학교가 같은 브랜드로 인식함

---

## Known Gaps

- 영상·모션 토큰 미정의 (현재 정적 산출물 중심)
- 다국어(영문 보도자료 등) 폰트 페어링 검증 미완료
- iPad 앱 빌드용 네이티브 토큰 미정의 (Apple 연수 PDF 위주 적용)
- 인쇄 흑백 환경(학교 흑백 프린터)에서 운영 상태 식별 — 색 + 패턴 동시 적용 가이드 추가 필요
