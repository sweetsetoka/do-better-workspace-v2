# Mac 카톡 오프라인 읽기 — 작동 원리 (교육용)

Mac 카카오톡은 대화를 **암호화된 SQLite(SQLCipher)**로 디스크에 저장한다. 암호화돼 있어 "못 읽는다"고 흔히 생각하지만, **복호화에 필요한 재료(기기 UUID·계정 userId)가 같은 Mac 안에 다 있고, 키 도출식이 공개**돼 있어 본인 데이터는 읽을 수 있다. 핵심은 "정책을 뚫는 것"이 아니라 "내 기기 안의 내 데이터를, 공개된 방식으로" 푸는 것.

전제: 자기 Mac에 로그인된 자기 카톡 데이터만 대상. 읽기 전용. 서버 접속 0.

---

## 전체 그림

```
[기기 UUID]  ─┐
              ├─→ 정해진 포맷으로 엮음 ─→ PBKDF2-HMAC-SHA256(100k,128B) ─┬→ DB 파일명
[계정 userId]─┘                                                          └→ SQLCipher 키
                                                                              │
        암호화 DB 파일  ──(키로 복호화, PRAGMA 순서 주의)──────────────────────┘
                            │
                            └→ NTChatRoom / NTChatMessage / NTUser 테이블을 SQL로 조회
```

재료는 단 둘 — **기기 UUID**와 **계정 userId**. 둘을 정해진 규칙으로 엮어 파일명과 키를 만든다.

---

## 1단계. 기기 UUID

```bash
ioreg -rd1 -c IOPlatformExpertDevice | grep IOPlatformUUID
# "IOPlatformUUID" = "A6B703D0-....-............"
```

맥 하드웨어 고유값. 카톡은 이 UUID를 키 도출의 한 축으로 쓴다. 누구 Mac이든 `ioreg`로 바로 나온다.

> 함정: 출력 줄에서 따옴표로 나뉜 4번째 토큰이 UUID. (openkakao는 이 파싱에 버그가 있어 UUID를 못 읽고 멈춘다 — 아래 "레퍼런스 버그" 참조.)

## 2단계. 계정 userId (이게 사람마다 다르고, 한 번 구하면 됨)

카톡은 **모든 인증 API 요청에 `talk-user-id: <본인 정수ID>` 헤더**를 붙인다. macOS의 HTTP 캐시(CFURLCache = `~/Library/Containers/com.kakao.KakaoTalkMac/Data/Library/Caches/Cache.db`)가 그 **요청 객체를 binary plist로 평문 저장**한다. 그래서 MITM·프록시 없이 디스크에서 바로 읽을 수 있다.

- 위치: `Cache.db`의 `cfurl_cache_blob_data.request_object`
- 구조: `root(dict) → "Array"(배열) → 각 item(dict)=HTTP 헤더 묶음`. `Authorization`이 있는 dict가 인증 요청이고, 같은 dict의 `talk-user-id`가 본인 ID.
- **반드시 `plistlib`로 파싱.** binary plist(bplist00)라 단순 문자열/`strings` grep으로는 안 보인다 (여기서 한참 막혔던 함정).
- 응답 본문(`cfurl_cache_receiver_data`)은 카톡이 암호화 → 못 읽음. 반면 요청 객체는 평문.

> 안 통한 길(기록): plist `FSChatWindowTransparency<숫자>` 공통꼬리 trick은 25.10.0엔 키가 없음(`FSChatWindowFrame_<해시>`로 바뀜). mitmproxy 실시간 캡처는 cert pinning에 막히고 애초에 불필요(헤더가 평문 캐시). → 결국 위 Cache.db talk-user-id가 정답.

## 3단계. 파일명·키 도출 (공개된 공식)

출처: blluv gist(8418e3ef…) → kakaocli `KeyDerivation.swift`(silver-flight-group) → k-skill(NomaDamas). 셋 다 동일.

공통 helper:
```
hashed_device_uuid(uuid) = base64( SHA1(uuid) ‖ SHA256(uuid) )
pbkdf2(password, salt)   = PBKDF2-HMAC-SHA256(password, salt, 100000회, 128바이트)
```

**DB 파일명**:
```
password = ".".join([".", "F", userId, "A", "F", reversed(uuid), ".", "|"])
         = "..F.{userId}.A.F.{reversed_uuid}...|"        ← 점 3개 (정식)
salt     = reversed( hashed_device_uuid(uuid) )
파일명   = pbkdf2(password, salt).hex()[28 : 28+78]       ← 78자 hex
```

**SQLCipher 키**:
```
parts    = ["A", hashed_device_uuid(uuid), "|", "F", uuid[:5], "H", userId, "|", uuid[7:]]
password = reversed( "F".join(parts) )
salt     = uuid[ int(len(uuid)*0.3) : ]                   ← UUID 30% 지점부터 끝까지
키       = pbkdf2(password, salt).hex()                   ← 256자 hex (= passphrase)
```

`"F"`, `"A"`, `"H"`, `"|"`, 점, 문자열 뒤집기, UUID 슬라이싱은 전부 **난독화 장치**다. 의미는 없고, 이 순서를 정확히 재현하는 게 핵심.

## 4단계. 열기 (PRAGMA 순서가 결정적)

도출한 파일을 복사(WAL/SHM까지 — 최신 메시지 포함)한 뒤:
```sql
PRAGMA key='<256자 hex>';          -- 반드시 먼저
PRAGMA cipher_compatibility=3;     -- 그 다음
SELECT ... FROM NTChatMessage ...;
```

- **순서를 바꾸면**(`cipher_compatibility`를 먼저 주면) 올바른 키로도 `file is not a database`가 난다. ← 이게 한동안 "키가 틀렸다"로 오판하게 만든 함정.
- 256자 hex 키는 raw 키가 아니라 **passphrase**로 들어가, SQLCipher가 파일 첫 16바이트 salt로 한 번 더 PBKDF를 돌려 실제 AES 키를 만든다.

테이블:
- `NTChatRoom` — 방 (chatId, type, chatName, activeMembersCount, lastUpdatedAt, directChatMemberUserId)
- `NTChatMessage` — 메시지 (logId, chatId, authorId, message, type, sentAt[unixepoch])
- `NTUser` — 사람 (userId, displayName, nickName, linkId)

---

## 레퍼런스 버그 — "도출식이 바뀐 줄" 알았던 사건 (2026-05)

처음엔 카톡 25.10.0에서 복호화가 안 돼 "버전이 도출식을 바꿨다"고 결론냈는데, **틀린 진단**이었다. 진짜 원인은 둘:

1. **openkakao(많이 쓰이는 Rust 포팅)의 1글자 버그.** 파일명 password가 정식은 `...|`(점 3개)인데 openkakao가 `..|`(점 2개)로 옮겼다. 이걸 그대로 베낀 재구현이 틀린 파일명을 내놓고 → "마이그레이션됐다/안 맞는다"로 오판. 정식(점 3개)으로 계산하면 실제 파일명과 정확히 일치.
2. **PRAGMA 순서.** `cipher_compatibility`를 `key`보다 먼저 줘서 실패 → "키도 틀렸다"로 오판.

교훈: 작동하는 레퍼런스가 있으면 **재구현으로 결론내지 말고 직접 빌드·실행**하고, **여러 독립 레퍼런스를 교차 대조**하라. "X가 바뀌었다"는 큰 결론 전에 오프바이원·인자 순서 같은 작은 원인부터 의심하라.

(검증: openkakao를 직접 빌드해 UUID 파싱·userId·DB파일 선택 버그를 다 고쳐도 복호화 실패 = 코드 자체가 점 2개. 반면 kakaocli·k-skill 정식 공식 + 올바른 PRAGMA 순서로 복호화 성공 — 방 617·메시지 103,414·유저 11,343 직독.)

---

## 사진·파일은 어떻게 가져오나 (텍스트와 다른 점)

텍스트는 로컬 DB 안에 평문으로 들어있지만, **사진·파일의 실제 바이트는 DB에 없다.** type 2(사진)·18(파일) 메시지의 `attachment`(JSON)에 **메타데이터 + 카톡 CDN 서명URL**만 들어있다:

```json
{ "k":"...", "w":3000, "h":4000, "s":4635558, "cs":"<sha1>", "mt":"image/jpg",
  "url":"https://talk.kakaocdn.net/dna/.../i_xxxx.jpg?credential=..&expires=..&signature=..",
  "name":"...", "expire": 1781411376706 }
```

- 그 **`url`로 GET하면 평문 JPEG/PNG/파일이 그대로** 온다. **복호화 불필요** — CDN이 평문을 준다. (openkakao도 받은 바이트의 magic bytes만 확인하고 복호화 안 함.)
- 받은 사진은 Claude가 **비전으로** 읽어 이미지 속 글자·내용까지 파악. 텍스트 파일은 그대로 읽음.
- **단 둘**: (1) 이 부분만 네트워크(CDN GET)를 쓴다 — 텍스트는 0접속, 미디어는 CDN 1회. LOCO/로그인이 아니라 **단순 파일 GET**이라 세션 충돌·밴 위험 없음. (2) `url`에 **만료(expires)**가 있어 **최근 미디어만** 받힌다. 오래된 건 링크가 죽어 재발급이 필요한데, 재발급은 LOCO(위험군)라 안 한다.
- 로컬 미디어 캐시(`c974a544…` 폴더)는 앱이 디스크 저장 시 **따로 암호화**(file=data)라 거기서 직접 못 읽는다. 하지만 CDN 평문이 있어 그 암호화는 **풀 필요 없다.**

`media` 명령이 이 과정을 자동화: 방의 최근 미디어를 받아 로컬 경로를 내놓고, Claude가 Read로 내용 파악.

## 왜 "온라인(LOCO)"은 안 쓰는가 (시연 때 같이 설명)

같은 도구(openkakao)로 서버에 접속해 읽을 수도 있다(LOCO/REST). 하지만 카톡은 **PC 세션을 기기당 1개만** 허용해서, 도구가 "PC 클라이언트인 척" 로그인하면 **데스크톱 카톡 앱이 로그아웃**된다(읽을 때마다 앱이 튕김). 메시지 전송 같은 쓰기는 계정 밴 위험까지 있다. 그래서 "방해 없이 내 대화만 읽기"는 **오프라인 로컬 DB(이 스킬)**가 유일하게 깔끔한 길이다.
