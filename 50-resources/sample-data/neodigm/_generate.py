#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
네오다임(Neodigm) AX 데모용 더미데이터 생성기.

회사 맥락 (리서치 2026-06 확인):
- B2B 통합 마케팅 대행사. 글로벌 IT 대기업(Adobe, AWS, Microsoft, HP, Cisco) 전담.
- KPI 퍼널: Impression → CPC/CTR → MQL → SQL → Pipeline → Revenue (B2B 리드 퍼널).
- 서비스: Digital Marketing(Search/Display/Video/Social), Contents Marketing, Marketing Technology(Adobe Marketo).
- 대행 수수료: 국내 매체 약 20%, 해외 매체 마크업 15%+ (리서치 brunch 확인).

데모 페르소나: 유예림(기획2본부) — 매주 광고주 성과 리포트(PPT)를 만든다.
랩사(미디어렙)에서 받은 매체 성과 데이터를 광고주에게 전달할 리포트로 가공.

데이터 3종:
1. ad_performance.csv  — 캠페인×매체×일자 광고 성과 (노출·클릭·광고비·전환=MQL)
2. campaign_master.csv — 캠페인/광고주 마스터 (목표·월예산·대행수수료율·매체수수료율·MQL→SQL전환율)
3. content_performance.csv — 콘텐츠(블로그·백서·SNS) 성과 (게시일·조회·체류·다운로드·연동MQL)

핵심 "아하": 콘텐츠 게시일에 해당 광고주의 MQL이 일·캠페인 양쪽에서 급등한다.
(백서 다운로드 게이트 → 광고 랜딩 전환율 상승 → MQL 스파이크)
"""

import csv
import random
from datetime import date, timedelta

random.seed(20260622)  # 재현 가능
OUT = "/Users/rhim/Projects/do-better-workspace-v2/50-resources/sample-data/neodigm"

# 분석 대상 월: 2026년 5월 (31일)
YEAR, MONTH = 2026, 5
DAYS = [date(YEAR, MONTH, d) for d in range(1, 32)]

# ---------------------------------------------------------------------------
# 1) 광고주 / 캠페인 마스터
# ---------------------------------------------------------------------------
# 글로벌 IT B2B 광고주 5곳 (네오다임 실제 클라이언트군 반영, 캠페인은 데모용 가상)
# objective: Awareness / Lead Gen / ABM 중 하나
# domestic_media: 국내 매체 비중(수수료 20%) vs 해외 매체(마크업 15%)
ADVERTISERS = [
    # adv_id, 광고주(가상 캠페인명 포함), 산업, objective, 월예산(만원), 대행수수료율, MQL→SQL전환율, 기준CPC, 기준CTR, 기준전환율(MQL/click)
    ("ADV-ADOBE",  "Adobe Creative Cloud B2B",  "Software",     "Lead Gen", 4800, 0.18, 0.24, 920, 0.0090, 0.045),
    ("ADV-AWS",    "AWS Korea Summit 리드젠",    "Cloud",        "Lead Gen", 6200, 0.17, 0.22, 1080, 0.0075, 0.038),
    ("ADV-MS",     "Microsoft 365 ABM",         "Software",     "ABM",      3600, 0.20, 0.30, 1350, 0.0065, 0.052),
    ("ADV-HP",     "HP Workstation 인지",        "Hardware",     "Awareness",2800, 0.19, 0.15, 640, 0.0110, 0.022),
    ("ADV-CISCO",  "Cisco Networking 세미나",    "Network",      "Lead Gen", 3100, 0.18, 0.20, 1150, 0.0070, 0.034),
]

# 매체 채널 (국내/해외 구분 → 수수료 구조). 캠페인마다 채널 믹스가 다름.
# channel, kind(domestic/global), media_fee_rate(매체 수수료/마크업)
CHANNELS = {
    "네이버_검색광고":   ("domestic", 0.20),
    "네이버_GFA":        ("domestic", 0.20),
    "카카오모먼트":      ("domestic", 0.20),
    "구글_검색":         ("global",   0.15),
    "구글_디스플레이":   ("global",   0.15),
    "메타_리드":         ("global",   0.15),
    "링크드인_ABM":      ("global",   0.15),
}

# 채널별 광고그룹(소재 세트) — 랩사 export는 광고그룹 단위로 행이 쪼개진다.
AD_GROUPS = {
    "네이버_검색광고":   ["브랜드_키워드", "일반_키워드", "경쟁사_키워드"],
    "네이버_GFA":        ["리타겟팅", "관심사_타겟"],
    "카카오모먼트":      ["리타겟팅", "데모_타겟"],
    "구글_검색":         ["브랜드_키워드", "솔루션_키워드", "경쟁사_키워드"],
    "구글_디스플레이":   ["리마케팅", "유사잠재고객"],
    "메타_리드":         ["리드폼_A", "리드폼_B"],
    "링크드인_ABM":      ["타겟기업_리스트", "직무_타겟"],
}

# 캠페인별 채널 믹스 (objective에 맞게) + 채널별 예산 가중치
CAMPAIGN_MIX = {
    "ADV-ADOBE":  [("구글_검색", 0.30), ("네이버_검색광고", 0.25), ("메타_리드", 0.25), ("네이버_GFA", 0.20)],
    "ADV-AWS":    [("링크드인_ABM", 0.30), ("구글_검색", 0.30), ("메타_리드", 0.22), ("네이버_검색광고", 0.18)],
    "ADV-MS":     [("링크드인_ABM", 0.45), ("구글_검색", 0.30), ("메타_리드", 0.25)],  # ABM은 링크드인 중심
    "ADV-HP":     [("네이버_GFA", 0.35), ("구글_디스플레이", 0.30), ("카카오모먼트", 0.20), ("메타_리드", 0.15)],  # 인지=디스플레이 중심
    "ADV-CISCO":  [("구글_검색", 0.30), ("네이버_검색광고", 0.25), ("링크드인_ABM", 0.25), ("카카오모먼트", 0.20)],
}

# 콘텐츠 게시 = MQL 급등 트리거. 광고주별 게시일(평일, 5월 중) — 일·캠페인 양쪽 검출 위해 충분한 부스트.
# (백서/케이스스터디 게시 → 게이티드 다운로드 → 랜딩 전환율 급등)
CONTENT_EVENTS = [
    # adv_id, 게시일, 콘텐츠유형, 제목(가상), day_boost(그날 노출·클릭·전환 배수 하한)
    ("ADV-ADOBE",  date(YEAR, MONTH, 8),  "백서",        "디자인팀 생산성 벤치마크 리포트 2026",  2.4),
    ("ADV-AWS",    date(YEAR, MONTH, 13), "케이스스터디", "제조사 클라우드 전환 사례집",            2.2),
    ("ADV-MS",     date(YEAR, MONTH, 20), "백서",        "엔터프라이즈 보안 ABM 가이드",          2.6),
    ("ADV-ADOBE",  date(YEAR, MONTH, 26), "웨비나",      "Creative Cloud B2B 라이브 세션",        2.0),
]
CONTENT_BY_DAY = {}
for adv, d, _, _, boost in CONTENT_EVENTS:
    CONTENT_BY_DAY.setdefault((adv, d), boost)

def weekday_factor(d: date) -> float:
    # B2B는 평일 강세, 주말 약세
    return 0.45 if d.weekday() >= 5 else 1.0

# ---- campaign_master.csv ----
master_rows = []
for adv_id, name, industry, obj, budget, agency_fee, mql_sql, cpc, ctr, cvr in ADVERTISERS:
    master_rows.append({
        "advertiser_id": adv_id,
        "advertiser": name,
        "industry": industry,
        "objective": obj,
        "monthly_budget_krw": budget * 10000,       # 원 단위
        "agency_fee_rate": agency_fee,              # 대행 수수료율(광고비 대비)
        "mql_to_sql_rate": mql_sql,                 # MQL→SQL 전환율
        "target_mql": int(budget * 10000 / cpc * cvr * 0.95),  # 월 목표 MQL(대략): 월예산/CPC=클릭 × 전환율
        "primary_channel": CAMPAIGN_MIX[adv_id][0][0],
        "base_cpc_krw": cpc,
    })

with open(f"{OUT}/campaign_master.csv", "w", newline="", encoding="utf-8-sig") as f:
    w = csv.DictWriter(f, fieldnames=list(master_rows[0].keys()))
    w.writeheader()
    w.writerows(master_rows)

# ---- ad_performance.csv ----
# 캠페인×채널×일자. 캠페인별 일예산을 채널 가중치로 분배 → 노출/클릭/전환 생성.
adv_lookup = {a[0]: a for a in ADVERTISERS}
perf_rows = []
order = 0
for adv_id, name, industry, obj, budget, agency_fee, mql_sql, base_cpc, base_ctr, base_cvr in ADVERTISERS:
    daily_budget = budget * 10000 / 31.0
    for d in DAYS:
        wf = weekday_factor(d)
        boost = CONTENT_BY_DAY.get((adv_id, d), 1.0)
        # 콘텐츠 게시일은 그날 전체를 끌어올린다(노출·클릭·전환율 모두). RNG 변동 흡수 위해 하한 넉넉히.
        day_jitter = random.uniform(0.85, 1.15)
        for channel, ch_weight in CAMPAIGN_MIX[adv_id]:
            kind, media_fee = CHANNELS[channel]
            groups = AD_GROUPS[channel]
            # 채널 예산을 광고그룹들로 분배 (랜덤 가중치, 합=1)
            gw = [random.uniform(0.5, 1.5) for _ in groups]
            gsum = sum(gw)
            for gi, ad_group in enumerate(groups):
                ch_budget = daily_budget * ch_weight * (gw[gi] / gsum) * wf * day_jitter
                # 게시일엔 해당 캠페인 예산을 콘텐츠 연동 채널(검색·리드)로 더 태운다 → 그날 비용도 증가
                ch_spend = ch_budget * (boost if boost > 1.0 else 1.0) * random.uniform(0.92, 1.08)
                cpc = base_cpc * random.uniform(0.88, 1.12) * (0.95 if kind == "domestic" else 1.0)
                clicks = max(0, int(ch_spend / cpc))
                ctr = base_ctr * random.uniform(0.85, 1.15)
                impressions = int(clicks / ctr) if ctr > 0 else 0
                # 전환율: 게시일엔 게이티드 콘텐츠로 랜딩 전환 급등
                cvr = base_cvr * random.uniform(0.8, 1.2) * (boost if boost > 1.0 else 1.0)
                mql = int(clicks * cvr)
                order += 1
                perf_rows.append({
                    "date": d.isoformat(),
                    "advertiser_id": adv_id,
                    "campaign": name,
                    "channel": channel,
                    "channel_kind": kind,
                    "ad_group": ad_group,
                    "impressions": impressions,
                    "clicks": clicks,
                    "spend_krw": int(ch_spend),
                    "mql": mql,
                })

with open(f"{OUT}/ad_performance.csv", "w", newline="", encoding="utf-8-sig") as f:
    w = csv.DictWriter(f, fieldnames=list(perf_rows[0].keys()))
    w.writeheader()
    w.writerows(perf_rows)

# ---- content_performance.csv ----
# 콘텐츠(블로그·백서·케이스스터디·웨비나·SNS). 게이티드 콘텐츠는 다운로드→MQL 연동.
content_rows = []
CONTENT_TYPES = [
    # 유형, 게이티드여부(다운로드 있음), 기준조회, 기준체류(초)
    ("블로그",      False, 1400, 110),
    ("백서",        True,  650,  240),
    ("케이스스터디", True,  520,  210),
    ("웨비나",      True,  380,  900),
    ("SNS_링크드인", False, 2200, 35),
]
# 5월 내 콘텐츠 게시물 ~48건 (광고주별 분산). CONTENT_EVENTS의 4건은 반드시 포함(연동 표시).
cid = 0
# 먼저 연동 이벤트 4건 명시 등록
for adv_id, d, ctype, title, boost in CONTENT_EVENTS:
    cid += 1
    gated = ctype in ("백서", "케이스스터디", "웨비나")
    views = int(random.uniform(0.9, 1.3) * dict((c[0], c[2]) for c in CONTENT_TYPES)[ctype])
    dwell = int(random.uniform(0.9, 1.2) * dict((c[0], c[3]) for c in CONTENT_TYPES)[ctype])
    downloads = int(views * random.uniform(0.28, 0.42)) if gated else 0
    attributed_mql = int(downloads * random.uniform(0.35, 0.5)) if gated else int(views * 0.01)
    content_rows.append({
        "content_id": f"CNT-{cid:03d}",
        "publish_date": d.isoformat(),
        "advertiser_id": adv_id,
        "content_type": ctype,
        "title": title,
        "gated": "Y" if gated else "N",
        "views": views,
        "avg_dwell_sec": dwell,
        "downloads": downloads,
        "attributed_mql": attributed_mql,
        "linked_campaign": "Y",   # 광고 랜딩과 연동된 콘텐츠
    })

# 나머지 일반 콘텐츠 채우기 (연동 약함, MQL 기여 작음)
for _ in range(44):
    cid += 1
    adv_id = random.choice([a[0] for a in ADVERTISERS])
    ctype, gated, base_v, base_dw = random.choice(CONTENT_TYPES)
    d = random.choice([x for x in DAYS if x.weekday() < 5])
    views = int(random.uniform(0.6, 1.4) * base_v)
    dwell = int(random.uniform(0.7, 1.3) * base_dw)
    downloads = int(views * random.uniform(0.12, 0.30)) if gated else 0
    attributed_mql = int(downloads * random.uniform(0.15, 0.3)) if gated else int(views * 0.004)
    content_rows.append({
        "content_id": f"CNT-{cid:03d}",
        "publish_date": d.isoformat(),
        "advertiser_id": adv_id,
        "content_type": ctype,
        "title": f"{ctype} 게시물 #{cid}",
        "gated": "Y" if gated else "N",
        "views": views,
        "avg_dwell_sec": dwell,
        "downloads": downloads,
        "attributed_mql": attributed_mql,
        "linked_campaign": "N",
    })

content_rows.sort(key=lambda r: r["publish_date"])
with open(f"{OUT}/content_performance.csv", "w", newline="", encoding="utf-8-sig") as f:
    w = csv.DictWriter(f, fieldnames=list(content_rows[0].keys()))
    w.writeheader()
    w.writerows(content_rows)

print(f"ad_performance.csv: {len(perf_rows)} rows")
print(f"campaign_master.csv: {len(master_rows)} rows")
print(f"content_performance.csv: {len(content_rows)} rows")

# ---------------------------------------------------------------------------
# 스파이크 검증 (생성 후 즉시) — 콘텐츠 연동일이 일·캠페인 양쪽에서 +30% 넘는지
# ---------------------------------------------------------------------------
print("\n=== 스파이크 검증 ===")
from collections import defaultdict
# 캠페인별 일자별 MQL 합
camp_day_mql = defaultdict(lambda: defaultdict(int))
camp_day_spend = defaultdict(lambda: defaultdict(int))
for r in perf_rows:
    camp_day_mql[r["advertiser_id"]][r["date"]] += r["mql"]
    camp_day_spend[r["advertiser_id"]][r["date"]] += r["spend_krw"]

all_ok = True
for adv_id, d, ctype, title, boost in CONTENT_EVENTS:
    days_mql = camp_day_mql[adv_id]
    avg = sum(days_mql.values()) / len(days_mql)
    day_val = days_mql[d.isoformat()]
    ratio = day_val / avg if avg else 0
    ok = ratio >= 1.30
    all_ok = all_ok and ok
    print(f"  {adv_id} {d.isoformat()} ({ctype}): 일MQL {day_val} vs 평균 {avg:.1f} = {ratio:.2f}x  {'OK' if ok else 'FAIL'}")

print(f"\n전체 스파이크 검증: {'PASS' if all_ok else 'FAIL'}")
