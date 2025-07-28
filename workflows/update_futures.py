import yfinance as yf
import pandas as pd
from datetime import datetime

# List of futures tickers
tickers = ["GC=F", "SI=F", "PL=F", "HG=F"]

# Fetch data
data = []
for symbol in tickers:
    t = yf.Ticker(symbol)
    info = t.info
    data.append({
        "symbol": symbol,
        "price": info.get("regularMarketPrice", None),
        "change": info.get("regularMarketChange", None),
        "change_percent": info.get("regularMarketChangePercent", None),
        "market_time_utc": datetime.utcfromtimestamp(info.get("regularMarketTime", 0)).strftime("%Y-%m-%d %H:%M:%S")
    })

# Convert to DataFrame and save as CSV
df = pd.DataFrame(data)
df.to_csv("futures.csv", index=False)
