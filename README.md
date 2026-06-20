# 🚀 Crypto Market Scraper

A lightweight and efficient Python script designed to extract real-time market data for cryptocurrency pairs. 

This tool interacts directly with the public Binance API to fetch 24-hour ticker statistics, filters the top 50 most actively traded USDT pairs by volume, and automatically exports the clean data into a CSV format for further analysis or accounting.

## 🛠 Features
* **No API Keys Required:** Uses public endpoints for hassle-free execution.
* **Volume Sorting:** Automatically identifies the highest liquidity markets (Top 50).
* **Automated Export:** Generates a timestamped `.csv` file ready for Excel or Pandas integration.

## 💻 Tech Stack
* Python 3.x
* `requests` (API interaction)
* `pandas` (Data structuring and export)

## ⚙️ How to Use
1. Clone the repository to your local machine.
2. Install the required dependencies:
   ```bash
   pip install requests pandas
   ```
3. Run the script:
   ```bash
   python crypto_scraper.py
   ```
4. Find the generated `crypto_market_data_YYYYMMDD.csv` file in your root folder.

---
*Developed for data automation and Web3 market analysis.*
