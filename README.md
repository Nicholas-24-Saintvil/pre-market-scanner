# Market Catalyst Ranking Tool

CLI tool that finds pre-market stock gainers, pulls recent headlines, and ranks them using a keyword-based catalyst score.

## Features
- Scrape pre-market gainers (StockAnalysis)
- Filter out penny stocks (configurable)
- Fetch Google News headlines (RSS, last 16h)
- Score headlines by weighted categories
- Show top results in terminal

## Quickstart
```bash
git clone https://github.com/<your-username>/pre-market-scanner.git
cd pre-market-scanner
pip install -r requirements.txt
python src/cli.py --min-price 5 --top 10
