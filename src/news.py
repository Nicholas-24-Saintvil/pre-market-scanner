import urllib.parse, requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta, timezone

KEYWORDS = {
    "earnings": ["beats", "beat expectations", "tops estimates"],
    "guidance": ["raises guidance", "boosts outlook"],
    "momentum": ["soar", "soars", "surge", "rallies", "jumps"]
}

CATEGORY_WEIGHTS = {"earnings": 10, "guidance": 8, "momentum": 10}

def score_headline(title: str) -> int:
    tl = title.lower()
    score = 0
    for cat, words in KEYWORDS.items():
        if any(w in tl for w in words):
            score += CATEGORY_WEIGHTS.get(cat, 0)
    return score

def get_recent_headlines_for_ticker(ticker: str, window_hours: int):
    query = urllib.parse.quote(f"{ticker} stock news")
    url = f"https://news.google.com/rss/search?q={query}&hl=en"
    cutoff = datetime.now(timezone.utc) - timedelta(hours=window_hours)
    headlines = []
    try:
        resp = requests.get(url, timeout=10)
        soup = BeautifulSoup(resp.content, "xml")
        for item in soup.find_all("item"):
            title = item.title.text.strip()
            link = item.link.text.strip()
            pub_date = item.pubDate.text.strip()
            try:
                dt = datetime.strptime(pub_date, "%a, %d %b %Y %H:%M:%S %Z").replace(tzinfo=timezone.utc)
            except:
                continue
            if dt >= cutoff:
                sc = score_headline(title)
                if sc > 0:
                    headlines.append((title, link, dt, sc))
    except:
        pass
    return headlines
