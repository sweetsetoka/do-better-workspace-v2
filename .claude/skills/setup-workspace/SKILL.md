---
name: setup-workspace
description: 첫 clone 후 워크스페이스 초기 설정. CLAUDE.md의 "내 프로필" 섹션을 대화형으로 채우고 첫 daily note를 생성. "워크스페이스 세팅", "초기 설정", "setup", "setup-workspace" 등을 언급하면 자동 실행.
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
---

# setup-workspace

Do Better Workspace를 처음 clone한 사용자를 위한 초기 설정 스킬.

## 수행 작업

### 1. 환경 체크

```bash
# 현재 폴더가 워크스페이스 루트인지 확인
test -f CLAUDE.md && test -d 40-personal && test -d 30-knowledge/00-wiki && echo "OK: workspace root" || echo "ERROR: CLAUDE.md나 핵심 폴더 없음"
```

루트가 아니면 "워크스페이스 루트에서 실행해주세요" 안내 후 종료.

### 2. 대화형 프로필 질문

순서대로 하나씩 물어본다. 한 번에 하나씩 (일괄 질문 금지).

1. **이름 또는 호칭** — "어떻게 불러드릴까요?"
2. **역할/직업** — "현재 어떤 일을 하고 계세요? (ex: 카페 사장, 마케터, 프리랜서 디자이너)"
3. **주요 관심사** — "요즘 가장 집중하고 있는 것 2~3개만 알려주세요"
4. **이 워크스페이스 용도** — "이 워크스페이스를 어떻게 쓰고 싶으세요? (ex: 일일 기록, 프로젝트 관리, 학습 정리)"

각 답변을 변수로 저장 (`USER_NAME`, `USER_ROLE`, `USER_INTERESTS`, `USER_PURPOSE`).

### 3. CLAUDE.md 업데이트

`CLAUDE.md` 하단의 "내 프로필" 섹션을 찾아 답변으로 채운다.

기존:
```markdown
## 내 프로필

> 이 섹션을 직접 작성하거나 `/setup-workspace` 스킬을 실행하세요.

**이름**:
**역할**:
**관심사**:
**이 워크스페이스 용도**:
```

업데이트 후:
```markdown
## 내 프로필

**이름**: {USER_NAME}
**역할**: {USER_ROLE}
**관심사**: {USER_INTERESTS}
**이 워크스페이스 용도**: {USER_PURPOSE}

_작성일: YYYY-MM-DD_
```

### 4. 첫 Daily Note 생성 제안

"오늘의 첫 Daily Note를 만들까요?"를 묻고 Yes면 `daily-note` 스킬 호출.

### 5. 다음 단계 안내

다음 메시지를 한국어로 출력:

```
워크스페이스 세팅 완료!

다음에 해볼 것:
1. "오늘 daily note 만들어줘" → 매일의 기록 시작
2. "할 일 추가해줘: XXX" → 첫 todo 추가
3. "같이 생각해보자: XXX" → thinking-partner로 문제 탐색
4. "이 아이디어 저장해줘" → idea 스킬로 인사이트 캡처

폴더 구조 힌트:
- 00-inbox/ : 생각나는 즉시 캡처
- 10-projects/ : 시한부 프로젝트
- 20-operations/ : 지속적 운영
- 30-knowledge/00-wiki/ : 지식 복리 축적
- 40-personal/ : Daily/Weekly/Ideas/Todos

자세한 건 README.md 참고!
```

## 원칙

- **일괄 질문 금지**. 하나씩 물어야 인지 부담 낮음.
- **답변은 짧게 유도**. 긴 자기소개 요구하지 말 것.
- **CLAUDE.md 덮어쓰기 금지**. "내 프로필" 섹션만 `Edit` 도구로 부분 수정.
- **이미 채워져 있으면** 덮어쓰기 전 사용자에게 확인.
