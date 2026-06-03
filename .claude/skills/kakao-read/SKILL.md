---
name: kakao-read
description: Mac 카카오톡 대화·사진·파일을 로컬에서 직접 읽어 요약·할일 추출·검색·내용 파악. "카톡 읽어줘", "카톡 대화 정리", "카톡 요약", "카톡에서 X 찾아줘", "카톡 사진 내용 확인", "그 방 사진 뭐야", "카톡 파일 받아줘", "어제 그 방 대화 정리해줘", "카톡 체크"(지난 체크 이후 새 활동 1:1 방 메뉴형 수집) 등 Mac에서 본인 카톡 내용을 가져올 때 자동 실행. 텍스트는 서버 접속 0·완전 오프라인. 사진/파일은 CDN에서 평문 다운로드(저위험 GET, LOCO 아님)해 비전·텍스트로 내용 파악. 메시지 보내기/온라인 LOCO는 범위 밖. **macOS 전용** — Windows/Linux에선 동작하지 않음.
allowed-tools: Bash, Read
---

# kakao-read — Mac 카톡 오프라인 읽기

> **macOS 전용 스킬.** Mac 카카오톡 데스크톱 앱의 로컬 DB만 지원한다. Windows/Linux에서 트리거되면 스크립트가 "macOS 전용" 안내를 출력하고 종료한다 (다른 스킬엔 영향 없음). 이 환경이 Mac이 아니면 여기서 멈추고 사용자에게 알린다.

Mac 카카오톡 앱이 디스크에 저장하는 암호화 DB(SQLCipher)를 복호화해, **본인 대화를 텍스트로 직접 읽는다.** 화면 캡처 없이, 서버 접속 없이, 데스크톱 앱을 건드리지 않고 전체 히스토리를 읽는다.

## 범위 (중요 — 이 선을 넘지 않는다)

- **읽기 전용 · 본인 기기의 본인 계정만.** 자기 Mac에 로그인된 자기 카톡 데이터를 읽는다.
- **텍스트(chats/read/search)**: 서버 접속 0, 완전 오프라인. 로컬 암호화 DB 직독.
- **사진/파일(media)**: 메시지 메타데이터에 든 카톡 **CDN 서명URL로 평문 다운로드** → 사진은 비전, 텍스트 파일은 그대로 내용 파악. 이 부분만 네트워크(CDN GET)를 쓰지만 **LOCO/로그인이 아니라 단순 파일 GET**이라 세션 충돌·밴 위험 없음. 단 URL에 만료가 있어 **최근 미디어만** 받힌다(오래된 건 링크 만료).
- **하지 않는 것**: 메시지 보내기/삭제/수정, 온라인 LOCO 로그인·watch, 남의 기기·계정. 이것들은 데스크톱 앱 세션을 밀어내거나(로그아웃) 계정 밴 위험이 있어 다루지 않는다.
- 시연·전달할 때도 "각자 본인 Mac·본인 카톡"이 전제다.

## 전제

- **macOS** + 카카오톡 데스크톱 앱(로그인 상태로 한 번 이상 사용)
- `sqlcipher` 설치: `brew install sqlcipher`
- 최초 1회 `setup`으로 본인 userId를 캐시 (`~/.config/kakao-read/config.json` — 워크스페이스 밖 HOME에 저장, git 추적 안 됨)

## 사용법

스크립트: `.claude/skills/kakao-read/scripts/kakao_read.py` (워크스페이스 루트 기준 상대경로)

```bash
python3 .claude/skills/kakao-read/scripts/kakao_read.py setup             # 최초 1회: userId 추출·캐시
python3 .claude/skills/kakao-read/scripts/kakao_read.py chats 20          # 최근 방 20개 (chatId·type·인원·이름)
python3 .claude/skills/kakao-read/scripts/kakao_read.py read <chatId> 50  # 방 메시지 50개 (시간 오름차순)
python3 .claude/skills/kakao-read/scripts/kakao_read.py search "키워드" 30 # 전체 메시지 검색
python3 .claude/skills/kakao-read/scripts/kakao_read.py media <chatId> 5  # 방의 최근 미디어 5개 다운로드(사진/파일)
python3 .claude/skills/kakao-read/scripts/kakao_read.py check             # '지난 체크 이후' 새 활동 1:1 방 목록 (메뉴형 수집)
python3 .claude/skills/kakao-read/scripts/kakao_read.py since <chatId>    # 그 방의 '지난 체크 이후' 메시지만 (창 기준)
python3 .claude/skills/kakao-read/scripts/kakao_read.py mark              # 지금을 '마지막 체크 시각'으로 저장 (창 전진)
python3 .claude/skills/kakao-read/scripts/kakao_read.py tables            # 스키마 확인
```

## 카톡 체크 워크플로 (on-demand 메뉴형 수집)

"카톡 체크"는 **놓친 1:1 대화를 빠짐없이 훑는** 수집 동선이다. 단톡·오픈챗·채널은 자동 제외하고 1:1만 본다.

1. **`check`** — '지난 체크 이후'(마지막 `mark` 시각, 없으면 최근 2일) 새 활동이 있는 1:1 방을 `chatId | 이름 | 마지막시각 | 마지막메시지 미리보기`로 나열. 며칠 건너뛰어도 그 사이 활동한 1:1이 전부 떠서 빠짐 없음(창 기준).
2. **목록을 사용자에게 메뉴로 제시** — 시스템이 후보를 차려주고 사용자가 고른다(proposal-first). 어떤 방을 읽을지 고르게 한다.
3. **고른 방마다 `since <chatId>`** — 그 방의 '지난 체크 이후' 메시지만 시간순으로. (전체 히스토리가 아니라 새 창만 → 가볍고 빠짐 0). 미디어는 표준 워크플로대로 필요시 `media`.
4. **업무 후보를 `00-inbox/raw/`에 떨군다** (아래 "라우팅 연결고리" 참조). 읽은 창에서 업무 정보(약속·할일·문의)가 보이면 raw 파일로 떨군다. **여기서 직접 todo/캘린더에 쓰지 않는다** — 카톡 체크는 *수집 계층*이고, 분류·라우팅은 inbox-triage 한 곳이 전담한다.
5. **inbox-triage 체이닝** — raw를 하나라도 떨궜으면 이어서 `inbox-triage`를 호출해 라우팅한다. 라우팅 proposal(어디로 보낼지 승인)은 거기서 한 번만 받는다. (step 2의 "어느 방 읽을지"는 수집 proposal, 이건 라우팅 proposal — 서로 다른 게이트.)
6. **`mark`** — 체크가 끝나면 실행해 창을 전진시킨다(다음 `check`의 시작점). **읽기를 마친 뒤에만** 호출.

### 라우팅 연결고리 (카톡 체크 → 업무)

카톡 직독은 raw 파일을 안 만들어서 그냥 두면 inbox-triage의 라우팅(목적지 매핑·이중등록 방지·proposal 게이트)을 못 쓴다. 그래서 카톡 체크가 업무 후보를 **raw 파일**로 떨궈 같은 디스패처를 타게 한다. 라우팅 로직은 inbox-triage 한 곳에만 산다(중복·drift 없음).

**언제 떨구나**: 읽은 창에 *업무 신호*(날짜·시간·장소 약속 / 해야 할 일 / 회사·도입 문의 / 사람이 보낸 회신요망 질문)가 있을 때만. 잡담·안부·이미 끝난 대화는 떨구지 않는다.

**무엇을 떨구나**: **읽은 방(1:1) 1개당 raw 파일 1개.** 한 방에 여러 업무 항목이 섞여 있어도 한 파일에 담는다 — 쪼개기/흡수는 inbox-triage가 한다. 본문에는 (a) 판정 근거가 되도록 *관련 메시지 원문 인용* + (b) 추출한 업무 후보 요약을 같이 넣는다.

**파일명·포맷** (inbox-triage가 읽는 규약):

```
파일명: 00-inbox/raw/{방의_마지막메시지시각 YYYY-MM-DD_HHMMSS}_kakao-{chatId}.md
```
```markdown
---
source: kakao-check
collected: {지금 YYYY-MM-DD HH:MM:SS}
kakao_date: {방 마지막 메시지 시각 YYYY-MM-DD HH:MM:SS}
kakao_chat_id: {chatId}
kakao_room: {방 이름}
direction: in
channel: kakao
processed: false
---

# [미처리] 카톡 체크 — {방 이름}

- 방: {방 이름} (chatId {chatId})
- 창: '지난 체크 이후' 메시지

## 본문
\```
{관련 메시지 원문 — 발신자/시각 포함, 판정 근거로 충분하게}
\```

## 업무 후보 (추출 요약)
- {약속/할일 등 1줄씩}
```

`processed:false`라서 inbox-triage Step 0 스캔(`grep -lZ "processed: false"`)에 그대로 잡힌다. inbox-triage는 `source: kakao-check`를 인식한다. 마킹(routed_to/triaged)·라우팅은 전부 inbox-triage가 한다 — 카톡 체크는 떨구고 손 뗀다.

### 1:1 판별
`NTChatRoom.directChatMemberUserId != 0` 이 1:1 판별자. 모든 방이 이 칸 NOT NULL이고, 단톡(type1)·오픈챗(type4)·채널(type5)은 값이 **0**, 친구(type0)·비즈니스 계정(type2)은 상대 userId가 들어 있다. (`IS NOT NULL`은 전부 참이라 판별 못 함 — `!= 0`이 맞다.)

### 노이즈 정리 (선택)
비즈니스 계정에는 업무 1:1과 마케팅·알림 계정이 섞여 있다. config(`~/.config/kakao-read/config.json`)에 `"check_blocklist": ["토스","알라딘", ...]`(방 이름 부분일치)를 두면 `check` 목록에서 가려진다. 기본은 빈 목록(필터 없음).

## 표준 워크플로 (미디어 처리 판단을 포함한다)

1. `chats`로 chatId 확인.
2. `read <chatId>`로 대화를 가져온다. 사진·파일은 본문 흐름 안에 **`[사진]` · `[파일] 이름` · `[동영상]`** 으로 인라인 표시되고, 미디어가 있으면 출력 끝에 안내가 뜬다.
3. **미디어 처리 필요 판단 (이 단계 생략 금지).** `read` 결과에 `[사진]`/`[파일]`/`[동영상]`이 있으면, 그 내용이 이번 요청에 필요한지 본다:
   - 요약·할일 추출·"무슨 내용/얘기야"처럼 **맥락이 필요하면** → `media <chatId> <N>`으로 받아, 출력된 각 경로를 **Read 도구로 열어** 내용 파악(사진=비전으로 이미지 속 글자까지, 텍스트 파일=본문 그대로). 파악한 내용을 대화 정리에 **녹여서** 제시(예: "[사진]" 자리에 '세미나 WiFi 안내(PW: …)'처럼).
   - 텍스트만으로 충분하거나 미디어가 요청과 무관하면 → 받지 않는다(불필요한 CDN 접속·시간 절약).
   - 애매하면 한 번만 묻는다: "사진 N장·파일 M개도 내용 확인할까요?"
4. **핵심 요약 + 할 일 추출**.

받히는 미디어: 사진(2,27)·동영상(3)·음성(12)·GIF(14)·파일(18). 동영상·대용량은 시간이 걸릴 수 있음. **최근 것만**(서명URL 만료 — "실패(만료)"로 뜨면 오래된 미디어).

## setup 주의 — 분류기에 막히면 사람이 직접

`setup`은 `Cache.db`의 `talk-user-id` 헤더에서 userId를 뽑는다. Claude Code 안전분류기가 이 단계를 credential 탐색으로 보고 막을 수 있다. **막히면 사용자에게 프롬프트에서 `!python3 .claude/skills/kakao-read/scripts/kakao_read.py setup` 로 직접 실행하도록 안내한다.** 한 번 캐시되면 이후 `chats`/`read`/`search`는 바로 실행 가능(복호화 읽기는 막히지 않음).

userId를 이미 아는 환경에선 `KT_USER_ID=<숫자>`를 앞에 붙여도 된다.

## 작동 원리 (교육용)

네 단계. 상세·왜 그런지·흔한 함정은 `reference/how-it-works.md` 참조.

1. **UUID** = `ioreg`의 IOPlatformUUID (기기 고유)
2. **userId** = Cache.db의 `talk-user-id` 헤더 (계정 고유, 평문 캐시됨)
3. **DB 파일명·SQLCipher 키** = UUID+userId를 정해진 포맷으로 엮어 PBKDF2-HMAC-SHA256(100,000회, 128B) 도출
4. **열기** = `PRAGMA key` 먼저 → `PRAGMA cipher_compatibility=3` 나중 (순서가 바뀌면 실패)

테이블: `NTChatRoom`(방) / `NTChatMessage`(메시지) / `NTUser`(사람).

## 자주 막히는 곳

- `kakao-read는 macOS 전용입니다` 출력 후 종료 → 이 환경이 Mac이 아님. 정상 동작(비활성).
- `sqlcipher 미설치` → `brew install sqlcipher`.
- `file is not a database` → PRAGMA 순서(key 먼저) 또는 userId/UUID 불일치. 스크립트는 순서를 지킨다.
- 도출 파일명이 디스크에 없음 → userId가 이 기기 계정과 안 맞음. `setup` 다시.
- 그룹방 이름이 `(이름없음)` → `chatName`이 비고 멤버명 집계가 필요한 방. chatId로 `read`는 정상 동작.
