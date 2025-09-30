import argparse
from sources import get_premarket_movers
from filter import filter_penny_stocks
from news import get_recent_headlines_for_ticker

def main():
    parser = argparse.ArgumentParser(description="Pre-market stock scanner")
    parser.add_argument("--min-price", type=float, default=5.0)
    parser.add_argument("--window-hours", type=int, default=16)
    parser.add_argument("--top", type=int, default=10)
    args = parser.parse_args()

    movers = get_premarket_movers()
    movers = filter_penny_stocks(movers, min_price=args.min_price)

    ranked = []
    for t in movers:
        news = get_recent_headlines_for_ticker(t, window_hours=args.window_hours)
        if news:
            top_story = max(news, key=lambda x: x[3])
            ranked.append((t, top_story[3], top_story[0], top_story[1]))

    ranked.sort(key=lambda x: -x[1])
    for i, (ticker, score, title, link) in enumerate(ranked[:args.top], 1):
        print(f"{i}. ${ticker} — Score: {score}\n   📰 {title}\n   🔗 {link}\n")

if __name__ == "__main__":
    main()
