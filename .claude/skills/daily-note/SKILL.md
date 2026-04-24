---
name: daily-note
description: 오늘 날짜의 Daily Note 생성 또는 열기. gcalcli 설치 시 Google Calendar 일정 포함. "오늘 daily note", "일일 노트", "daily note", "오늘 작성", "하루 기록" 등을 언급하면 자동 실행.
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
---

# daily-note

오늘 날짜의 Daily Note를 생성하거나 여는 스킬.

## 수행 작업

### 1. 오늘 날짜 확인

```bash
TODAY=$(date +%Y-%m-%d)
MONTH=$(date +%Y-%m)
DAY_NUM=$(date +%u)  # 1=월 ~ 7=일

case $DAY_NUM in
  1) WEEKDAY="월요일";;
  2) WEEKDAY="화요일";;
  3) WEEKDAY="수요일";;
  4) WEEKDAY="목요일";;
  5) WEEKDAY="금요일";;
  6) WEEKDAY="토요일";;
  7) WEEKDAY="일요일";;
esac
```

### 2. 파일 경로

```
./40-personal/41-daily/{MONTH}/{TODAY}.md
```

월별 폴더가 없으면 먼저 생성: `mkdir -p ./40-personal/41-daily/{MONTH}`

### 3. 파일이 있으면 → 열기

기존 내용 표시. 업데이트하고 싶은지 물어보기.

### 4. 파일이 없으면 → 템플릿으로 생성

템플릿: `./00-system/01-templates/daily-note-template.md`

변수 치환:
- `YYYY-MM-DD` → `{TODAY}`
- `(요일)` → `{WEEKDAY}`

### 5. (선택) Google Calendar 일정 추가

`gcalcli`가 설치된 경우에만:

```bash
if command -v gcalcli &> /dev/null; then
  EVENTS=$(gcalcli agenda --tsv 2>/dev/null | head -20)
fi
```

결과를 Markdown 리스트로 변환하여 daily note에 "오늘 일정" 섹션 추가.
설치 안 되어 있으면 이 단계 스킵 (에러 메시지 X).

### 6. 결과 보고

```
✅ Daily Note 생성: ./40-personal/41-daily/2026-04/2026-04-24.md
   요일: 목요일
   일정: 3건 (Google Calendar에서 가져옴)
```

## 팁

- 전날/내일 계산 (Mac/Linux 호환):
  ```bash
  # Mac
  YESTERDAY=$(date -v-1d +%Y-%m-%d)
  TOMORROW=$(date -v+1d +%Y-%m-%d)

  # Linux
  YESTERDAY=$(date -d "yesterday" +%Y-%m-%d)
  TOMORROW=$(date -d "tomorrow" +%Y-%m-%d)
  ```
  OS 체크: `[ "$(uname)" = "Darwin" ]`

- 경로는 항상 **상대 경로** (`./40-personal/...`). 워크스페이스 루트에서 실행 전제.
