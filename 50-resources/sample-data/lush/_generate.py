"""
LUSH Korea AX Bootcamp 2차 시연용 더미데이터 생성기.

생성 파일:
- store_sales.csv      매장별 일별 매출 (10개 매장 × 28일)
- channel_sales.csv    온라인 채널별 일별 매출 (자사몰/네이버스토어/카카오선물하기/29CM/올영)
- products_master.csv  제품 마스터 (러쉬 한국 자사몰 인기 라인업 기반)
- campaign_calendar.csv 캠페인 일정/실적
- voc_inflow.csv       VOC·고객문의 (채널톡 + 자사몰 게시판, 매장별·키워드별)

기간: 2026-04-21 ~ 2026-05-18 (4주)
"""
import csv
import random
from datetime import date, timedelta
from pathlib import Path

random.seed(42)

OUT = Path(__file__).parent
START = date(2026, 4, 21)  # 월요일
END = date(2026, 5, 18)    # 일요일 (4주)
DAYS = [(START + timedelta(days=i)) for i in range((END - START).days + 1)]

# ─────────────────────────────────────────────────────────
# 매장 (실제 LUSH 한국 매장 기반 — 명동 본점·강남 학동 본사·홍대·잠실 롯데·여의도 IFC·코엑스·스타필드 하남·신세계 강남·롯데월드몰·현대 판교)
# ─────────────────────────────────────────────────────────
STORES = [
    {"code": "MD01", "name": "명동본점",      "type": "flagship",  "city": "서울", "base_traffic": 850, "base_conv": 0.18, "open_year": 2003},
    {"code": "GN01", "name": "강남신세계",    "type": "dept",       "city": "서울", "base_traffic": 620, "base_conv": 0.22, "open_year": 2015},
    {"code": "HD01", "name": "홍대",          "type": "street",    "city": "서울", "base_traffic": 540, "base_conv": 0.15, "open_year": 2012},
    {"code": "JS01", "name": "잠실롯데",      "type": "dept",      "city": "서울", "base_traffic": 580, "base_conv": 0.20, "open_year": 2014},
    {"code": "YD01", "name": "여의도IFC",     "type": "mall",      "city": "서울", "base_traffic": 410, "base_conv": 0.17, "open_year": 2018},
    {"code": "CE01", "name": "코엑스",        "type": "mall",      "city": "서울", "base_traffic": 480, "base_conv": 0.16, "open_year": 2010},
    {"code": "HN01", "name": "스타필드하남",  "type": "mall",      "city": "경기", "base_traffic": 520, "base_conv": 0.21, "open_year": 2016},
    {"code": "PG01", "name": "현대판교",      "type": "dept",      "city": "경기", "base_traffic": 460, "base_conv": 0.23, "open_year": 2019},
    {"code": "BS01", "name": "신세계센텀",    "type": "dept",      "city": "부산", "base_traffic": 380, "base_conv": 0.19, "open_year": 2017},
    {"code": "DG01", "name": "현대대구",      "type": "dept",      "city": "대구", "base_traffic": 290, "base_conv": 0.18, "open_year": 2021},
]

# ─────────────────────────────────────────────────────────
# 제품 (러쉬 자사몰 실제 라인업 기반 — 인기 카테고리만 발췌)
# 출처: lush.co.kr 자사몰 카테고리·인기 제품
# ─────────────────────────────────────────────────────────
PRODUCTS = [
    # 배쓰밤 — 가장 시그니처 카테고리
    {"sku": "BB001", "name": "인터갤럭틱 배쓰밤",       "category": "배쓰밤",      "price": 13500, "cost": 4200, "weight_g": 200, "is_vegan": True,  "season": "all"},
    {"sku": "BB002", "name": "트와일라잇 배쓰밤",        "category": "배쓰밤",      "price": 13500, "cost": 4200, "weight_g": 200, "is_vegan": True,  "season": "all"},
    {"sku": "BB003", "name": "더 익스피리먼터 배쓰밤",   "category": "배쓰밤",      "price": 16000, "cost": 5100, "weight_g": 220, "is_vegan": True,  "season": "all"},
    {"sku": "BB004", "name": "베리 베리 체리 배쓰밤",   "category": "배쓰밤",      "price": 11500, "cost": 3700, "weight_g": 180, "is_vegan": True,  "season": "spring"},
    {"sku": "BB005", "name": "어머 사쿠라 배쓰밤",      "category": "배쓰밤",      "price": 14000, "cost": 4400, "weight_g": 200, "is_vegan": True,  "season": "spring"},
    # 샴푸바 — 환경 시그니처 라인
    {"sku": "SB001", "name": "허니 아이 워시드 더 키즈 샴푸바", "category": "샴푸바",  "price": 23000, "cost": 7200, "weight_g": 55,  "is_vegan": False, "season": "all"},
    {"sku": "SB002", "name": "시앤스 샴푸바",             "category": "샴푸바",      "price": 23000, "cost": 7100, "weight_g": 55,  "is_vegan": True,  "season": "all"},
    {"sku": "SB003", "name": "재스민 앤 헤나 풀룬덤 샴푸바", "category": "샴푸바",   "price": 23000, "cost": 7100, "weight_g": 55,  "is_vegan": True,  "season": "all"},
    # 마사지바
    {"sku": "MB001", "name": "씬티앙 마사지바",          "category": "마사지바",    "price": 21000, "cost": 6800, "weight_g": 60,  "is_vegan": True,  "season": "all"},
    {"sku": "MB002", "name": "더 컴포터 마사지바",        "category": "마사지바",    "price": 21000, "cost": 6800, "weight_g": 60,  "is_vegan": True,  "season": "all"},
    {"sku": "MB003", "name": "마사지바 틴 케이스",        "category": "액세서리",    "price": 9000,  "cost": 2400, "weight_g": 80,  "is_vegan": True,  "season": "all"},
    # 페이스 마스크
    {"sku": "FM001", "name": "마스크 오브 매그너민티",   "category": "페이스마스크", "price": 21500, "cost": 6900, "weight_g": 125, "is_vegan": True,  "season": "all"},
    {"sku": "FM002", "name": "쿠퍼톤 페이스 마스크",      "category": "페이스마스크", "price": 21500, "cost": 6900, "weight_g": 125, "is_vegan": True,  "season": "all"},
    {"sku": "FM003", "name": "캐치 어 스타 페이스 마스크","category": "페이스마스크", "price": 21500, "cost": 6900, "weight_g": 125, "is_vegan": False, "season": "all"},
    # 립
    {"sku": "LP001", "name": "립 스크럽 바블검",         "category": "립",          "price": 14500, "cost": 4800, "weight_g": 25,  "is_vegan": False, "season": "all"},
    {"sku": "LP002", "name": "립 스크럽 미스터 펭귄",    "category": "립",          "price": 14500, "cost": 4800, "weight_g": 25,  "is_vegan": False, "season": "winter"},
    {"sku": "LP003", "name": "립 밤 허니 트랩",          "category": "립",          "price": 12000, "cost": 3900, "weight_g": 9,   "is_vegan": False, "season": "all"},
    # 바디 (네이키드 라인)
    {"sku": "BD001", "name": "샤워젤리 위치 어메이징",   "category": "샤워젤",      "price": 19000, "cost": 6100, "weight_g": 240, "is_vegan": True,  "season": "all"},
    {"sku": "BD002", "name": "락 스타 솝",               "category": "비누",        "price": 15500, "cost": 4900, "weight_g": 120, "is_vegan": True,  "season": "all"},
    {"sku": "BD003", "name": "샌드 비누",                 "category": "비누",        "price": 13500, "cost": 4300, "weight_g": 100, "is_vegan": True,  "season": "summer"},
    {"sku": "BD004", "name": "로션 바 더 컴포터",         "category": "바디로션바",  "price": 21000, "cost": 6700, "weight_g": 100, "is_vegan": True,  "season": "all"},
    # 헤어
    {"sku": "HR001", "name": "헨 헤어 헤나 카라멜",       "category": "헤어",        "price": 28000, "cost": 9000, "weight_g": 330, "is_vegan": True,  "season": "all"},
    {"sku": "HR002", "name": "프로 컨디셔너 바 에이브리 후이",  "category": "헤어",   "price": 19000, "cost": 6000, "weight_g": 60,  "is_vegan": True,  "season": "all"},
    # 기프트 세트 (가격대 높음, 4월~5월 어버이날·스승의날 시즌 부스트)
    {"sku": "GS001", "name": "기프트 세트 - 바스타임",   "category": "기프트",      "price": 56000, "cost": 18000,"weight_g": 800, "is_vegan": True,  "season": "all"},
    {"sku": "GS002", "name": "기프트 세트 - 핑크 클라우드", "category": "기프트",    "price": 78000, "cost": 25000,"weight_g": 950, "is_vegan": True,  "season": "all"},
    {"sku": "GS003", "name": "기프트 세트 - 어머니날 한정", "category": "기프트",    "price": 89000, "cost": 28000,"weight_g": 1200,"is_vegan": True,  "season": "spring"},
]

# ─────────────────────────────────────────────────────────
# 채널 (자사몰 + 외부 4채널)
# ─────────────────────────────────────────────────────────
CHANNELS = [
    {"code": "OWN",   "name": "자사몰 (lush.co.kr)",  "commission": 0.000, "base_orders": 280},
    {"code": "NAVER", "name": "네이버 브랜드스토어",   "commission": 0.058, "base_orders": 180},
    {"code": "KAKAO", "name": "카카오 선물하기",      "commission": 0.110, "base_orders": 220},
    {"code": "29CM",  "name": "29CM",                "commission": 0.180, "base_orders":  85},
    {"code": "OY",    "name": "올리브영 온라인",      "commission": 0.150, "base_orders": 140},
]

# ─────────────────────────────────────────────────────────
# 캠페인 (러쉬 실제 진행 캠페인 톤 — 어머니날·바이런(빅뉴스)·핑크리본·어스데이·여름 사쿠라)
# ─────────────────────────────────────────────────────────
CAMPAIGNS = [
    {"id": "CAMP-2026-04-1", "name": "어스데이 네이키드 챌린지",   "start": "2026-04-15", "end": "2026-04-30", "budget": 18_000_000, "target_sku": ["BD001","BD002","BD003","BB003"], "channel_focus": "OWN,NAVER"},
    {"id": "CAMP-2026-05-1", "name": "어버이날 기프트 한정",       "start": "2026-04-25", "end": "2026-05-08", "budget": 32_000_000, "target_sku": ["GS001","GS002","GS003"],         "channel_focus": "OWN,KAKAO,NAVER"},
    {"id": "CAMP-2026-05-2", "name": "사쿠라 봄 한정",            "start": "2026-04-28", "end": "2026-05-15", "budget": 12_000_000, "target_sku": ["BB004","BB005"],                "channel_focus": "OWN,NAVER,29CM"},
    {"id": "CAMP-2026-05-3", "name": "리프레시 5월 매장 이벤트",   "start": "2026-05-04", "end": "2026-05-18", "budget":  8_500_000, "target_sku": ["MB001","MB002","FM001"],         "channel_focus": "OFFLINE"},
]

# ─────────────────────────────────────────────────────────
# 1) products_master.csv
# ─────────────────────────────────────────────────────────
with (OUT / "products_master.csv").open("w", newline="", encoding="utf-8-sig") as f:
    w = csv.writer(f)
    w.writerow(["sku", "product_name", "category", "list_price", "cost", "weight_g", "is_vegan", "season"])
    for p in PRODUCTS:
        w.writerow([p["sku"], p["name"], p["category"], p["price"], p["cost"], p["weight_g"], "Y" if p["is_vegan"] else "N", p["season"]])

# ─────────────────────────────────────────────────────────
# 2) store_sales.csv — 매장 × 일자 × 카테고리 × 매출/객수/객단가
# ─────────────────────────────────────────────────────────
CATEGORIES = sorted({p["category"] for p in PRODUCTS})
CAT_WEIGHT = {"배쓰밤": 0.28, "샴푸바": 0.10, "마사지바": 0.06, "액세서리": 0.03,
              "페이스마스크": 0.12, "립": 0.08, "샤워젤": 0.07, "비누": 0.09,
              "바디로션바": 0.05, "헤어": 0.06, "기프트": 0.06}

def _day_factor(d: date) -> float:
    """요일/시즌 가중치"""
    weekday = d.weekday()
    base = {0: 0.85, 1: 0.82, 2: 0.88, 3: 0.95, 4: 1.20, 5: 1.45, 6: 1.30}[weekday]
    # 어버이날 주간 (5/4~5/8) 부스트
    if date(2026, 5, 4) <= d <= date(2026, 5, 8):
        base *= 1.35
    # 어스데이 주간 (4/21~4/25)
    if date(2026, 4, 21) <= d <= date(2026, 4, 25):
        base *= 1.10
    # 5월 둘째주 (어버이날 직후 반동) 살짝 감소
    if date(2026, 5, 11) <= d <= date(2026, 5, 13):
        base *= 0.90
    return base

with (OUT / "store_sales.csv").open("w", newline="", encoding="utf-8-sig") as f:
    w = csv.writer(f)
    w.writerow(["date", "store_code", "store_name", "store_type", "city", "category",
                "traffic", "transactions", "units_sold", "gross_sales", "discount_amt", "net_sales", "avg_ticket"])
    for d in DAYS:
        day_f = _day_factor(d)
        for s in STORES:
            traffic = int(s["base_traffic"] * day_f * random.uniform(0.88, 1.12))
            for cat in CATEGORIES:
                cat_share = CAT_WEIGHT.get(cat, 0.05) * random.uniform(0.75, 1.25)
                # 기프트는 어버이날 주간에 폭증
                if cat == "기프트" and date(2026, 5, 4) <= d <= date(2026, 5, 8):
                    cat_share *= 2.6
                # 매장 타입별 카테고리 편차
                if s["type"] == "flagship" and cat in ("배쓰밤", "기프트"):
                    cat_share *= 1.20
                if s["type"] == "dept" and cat in ("페이스마스크", "기프트"):
                    cat_share *= 1.15
                if s["type"] == "street" and cat in ("립", "비누"):
                    cat_share *= 1.10

                cat_traffic = int(traffic * cat_share)
                conv = s["base_conv"] * random.uniform(0.85, 1.15)
                transactions = max(0, int(cat_traffic * conv))
                if transactions == 0:
                    continue
                # 평균 1.4개/거래
                units_sold = int(transactions * random.uniform(1.2, 1.7))
                # 카테고리별 평균 단가
                cat_prods = [p for p in PRODUCTS if p["category"] == cat]
                avg_price = sum(p["price"] for p in cat_prods) / len(cat_prods)
                gross = int(units_sold * avg_price * random.uniform(0.95, 1.05))
                # 캠페인 할인 (어버이날·어스데이 기간 카테고리 일치 시)
                discount = 0
                if cat == "기프트" and date(2026, 4, 25) <= d <= date(2026, 5, 8):
                    discount = int(gross * random.uniform(0.05, 0.10))
                if cat in ("샤워젤", "비누") and date(2026, 4, 15) <= d <= date(2026, 4, 30):
                    discount = int(gross * random.uniform(0.10, 0.15))
                net = gross - discount
                avg_ticket = int(net / transactions) if transactions else 0
                w.writerow([d.isoformat(), s["code"], s["name"], s["type"], s["city"], cat,
                            traffic, transactions, units_sold, gross, discount, net, avg_ticket])

# ─────────────────────────────────────────────────────────
# 3) channel_sales.csv — 온라인 채널 × 일자 × 카테고리 × 매출/주문
# ─────────────────────────────────────────────────────────
with (OUT / "channel_sales.csv").open("w", newline="", encoding="utf-8-sig") as f:
    w = csv.writer(f)
    w.writerow(["date", "channel_code", "channel_name", "category",
                "orders", "units_sold", "gross_sales", "commission_amt", "net_sales", "avg_order_value", "return_count"])
    for d in DAYS:
        day_f = _day_factor(d)
        for ch in CHANNELS:
            base_orders = int(ch["base_orders"] * day_f * random.uniform(0.85, 1.15))
            # 카카오선물하기는 어버이날 폭증
            if ch["code"] == "KAKAO" and date(2026, 5, 4) <= d <= date(2026, 5, 8):
                base_orders = int(base_orders * 1.8)
            # 자사몰은 어스데이 주간 부스트
            if ch["code"] == "OWN" and date(2026, 4, 21) <= d <= date(2026, 4, 25):
                base_orders = int(base_orders * 1.25)
            for cat in CATEGORIES:
                cat_share = CAT_WEIGHT.get(cat, 0.05) * random.uniform(0.70, 1.30)
                # 카카오는 기프트 비중 매우 높음
                if ch["code"] == "KAKAO" and cat == "기프트":
                    cat_share *= 3.0
                # 올영은 페이스마스크·립 비중 높음
                if ch["code"] == "OY" and cat in ("페이스마스크", "립"):
                    cat_share *= 1.8
                # 29CM은 기프트·바디로션바 비중 높음
                if ch["code"] == "29CM" and cat in ("기프트", "바디로션바"):
                    cat_share *= 1.5

                orders = max(0, int(base_orders * cat_share))
                if orders == 0:
                    continue
                units = int(orders * random.uniform(1.3, 1.9))
                cat_prods = [p for p in PRODUCTS if p["category"] == cat]
                avg_price = sum(p["price"] for p in cat_prods) / len(cat_prods)
                gross = int(units * avg_price * random.uniform(0.95, 1.05))
                commission = int(gross * ch["commission"])
                net = gross - commission
                aov = int(gross / orders) if orders else 0
                # 환불률 ~1.5% (29CM·올영 살짝 높음)
                ret_rate = 0.015
                if ch["code"] in ("29CM", "OY"):
                    ret_rate = 0.025
                returns = int(orders * ret_rate * random.uniform(0.5, 1.5))
                w.writerow([d.isoformat(), ch["code"], ch["name"], cat,
                            orders, units, gross, commission, net, aov, returns])

# ─────────────────────────────────────────────────────────
# 4) campaign_calendar.csv — 캠페인별 일자 진행/예산소진/매출 attribution
# ─────────────────────────────────────────────────────────
with (OUT / "campaign_calendar.csv").open("w", newline="", encoding="utf-8-sig") as f:
    w = csv.writer(f)
    w.writerow(["campaign_id", "campaign_name", "date", "status", "channel_focus",
                "budget_total", "spend_daily", "spend_cumulative",
                "attributed_orders", "attributed_sales", "target_skus"])
    for c in CAMPAIGNS:
        start = date.fromisoformat(c["start"])
        end = date.fromisoformat(c["end"])
        n_days = (end - start).days + 1
        daily_budget = c["budget"] / n_days
        cum_spend = 0
        for i in range(n_days):
            d = start + timedelta(days=i)
            if d < START or d > END:
                continue
            # 첫 3일·마지막 3일 부스트
            burst = 1.4 if (i < 3 or i >= n_days - 3) else 1.0
            spend = int(daily_budget * burst * random.uniform(0.85, 1.15))
            cum_spend += spend
            # ROAS는 어버이날 캠페인이 가장 높음 (4.5~6.0), 어스데이 (2.8~3.5), 매장 이벤트 (1.5~2.2)
            if "어버이날" in c["name"]:
                roas = random.uniform(4.5, 6.0)
            elif "어스데이" in c["name"]:
                roas = random.uniform(2.8, 3.5)
            elif "사쿠라" in c["name"]:
                roas = random.uniform(3.2, 4.0)
            else:
                roas = random.uniform(1.5, 2.2)
            attr_sales = int(spend * roas)
            # 평균 객단가 32,000원 가정
            attr_orders = int(attr_sales / random.randint(28000, 38000))
            status = "running"
            if d == start:
                status = "kickoff"
            if d == end:
                status = "wrap-up"
            w.writerow([c["id"], c["name"], d.isoformat(), status, c["channel_focus"],
                        c["budget"], spend, cum_spend, attr_orders, attr_sales, ",".join(c["target_sku"])])

# ─────────────────────────────────────────────────────────
# 5) voc_inflow.csv — 채널톡·자사몰 게시판 인입 VOC (정문혁/지오 담당 업무 시뮬레이션)
# ─────────────────────────────────────────────────────────
VOC_CHANNELS = ["채널톡", "자사몰_게시판", "인스타DM", "카카오톡", "전화"]
VOC_TYPES = [
    {"type": "배송문의",        "keyword": "배송 늦음/오배송/추적 문의", "to_team": "물류팀",         "sla_hours": 4,  "weight": 0.28},
    {"type": "제품문의",        "keyword": "성분/사용법/피부타입",         "to_team": "CE팀_제품지식",   "sla_hours": 6,  "weight": 0.22},
    {"type": "교환환불",        "keyword": "단순변심/하자/사이즈",          "to_team": "CE팀_교환",      "sla_hours": 8,  "weight": 0.18},
    {"type": "매장문의",        "keyword": "재고/매장위치/이벤트 일정",     "to_team": "리테일본부",     "sla_hours": 12, "weight": 0.12},
    {"type": "포장오류",        "keyword": "찌그러짐/누액/구성품 누락",     "to_team": "물류팀",         "sla_hours": 4,  "weight": 0.05},
    {"type": "칭찬",            "keyword": "직원응대/제품만족",            "to_team": "VOC_리워드",     "sla_hours": 24, "weight": 0.10},
    {"type": "불만",            "keyword": "직원불친절/대기시간",          "to_team": "CE팀_매장",      "sla_hours": 6,  "weight": 0.05},
]

with (OUT / "voc_inflow.csv").open("w", newline="", encoding="utf-8-sig") as f:
    w = csv.writer(f)
    w.writerow(["voc_id", "date", "channel", "type", "store_code", "store_name",
                "sku_mentioned", "to_team", "sla_hours", "response_hours", "status", "summary"])
    voc_seq = 1
    for d in DAYS:
        # 일평균 40건 (지오 진술 기반)
        n = int(40 * random.uniform(0.7, 1.4))
        # 어버이날 주간은 1.6배
        if date(2026, 5, 4) <= d <= date(2026, 5, 8):
            n = int(n * 1.6)
        for _ in range(n):
            tp = random.choices(VOC_TYPES, weights=[t["weight"] for t in VOC_TYPES])[0]
            # 매장 관련일 때만 매장 채움
            if tp["type"] in ("매장문의", "칭찬", "불만"):
                s = random.choice(STORES)
                store_code = s["code"]
                store_name = s["name"]
            else:
                store_code = ""
                store_name = ""
            # 제품 멘션 (제품문의·교환환불·칭찬일 때 70% 확률)
            sku = ""
            if tp["type"] in ("제품문의", "교환환불", "칭찬") and random.random() < 0.70:
                sku = random.choice(PRODUCTS)["sku"]
            # 응답 시간 (SLA 내 80%, 초과 20%)
            if random.random() < 0.80:
                resp_hours = round(random.uniform(0.5, tp["sla_hours"] * 0.95), 1)
                status = "완료"
            else:
                resp_hours = round(random.uniform(tp["sla_hours"] * 1.1, tp["sla_hours"] * 2.5), 1)
                status = "지연완료"
            # 미회신 3% (확인 요청 누락 시뮬)
            if random.random() < 0.03:
                resp_hours = ""
                status = "미회신"
            voc_id = f"VOC-{d.strftime('%Y%m%d')}-{voc_seq:04d}"
            voc_seq += 1
            # 요약 (한 줄)
            ch_obj = random.choice(VOC_CHANNELS)
            summary = f"[{tp['type']}] {tp['keyword'].split('/')[random.randint(0, len(tp['keyword'].split('/'))-1)]}"
            if store_name:
                summary += f" - {store_name}"
            if sku:
                p = next((p for p in PRODUCTS if p["sku"] == sku), None)
                if p:
                    summary += f" ({p['name']})"
            w.writerow([voc_id, d.isoformat(), ch_obj, tp["type"], store_code, store_name,
                        sku, tp["to_team"], tp["sla_hours"], resp_hours, status, summary])

print("생성 완료:")
for p in OUT.glob("*.csv"):
    print(f"  {p.name}: {p.stat().st_size:,} bytes")
