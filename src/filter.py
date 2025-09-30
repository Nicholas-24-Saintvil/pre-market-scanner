import yfinance as yf

def filter_penny_stocks(tickers, min_price=5.0):
    valid = []
    for t in tickers:
        try:
            price = yf.Ticker(t).fast_info.last_price
            if price and price >= min_price:
                valid.append(t)
        except:
            continue
    return valid
