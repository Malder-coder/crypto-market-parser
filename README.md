# 🚀 Web3 & Crypto Python Automation Suite

A collection of lightweight, production-ready Python scripts designed for crypto data extraction, automated alerting, blockchain interaction, and metadata scanning. 

These tools are built for traders, developers, and analysts looking to automate their Web3 workflows without complex infrastructure.

## 🛠 Included Tools

### 1. 📊 Crypto Market Scraper (`crypto_scraper.py`)
* Extracts real-time 24-hour ticker statistics using the public Binance API.
* Filters and sorts the top 50 highest-volume USDT trading pairs.
* Automatically exports clean data into a timestamped `.csv` format for Excel or Pandas.

### 2. 🚨 Telegram Price Alert Bot (`tg_price_alert.py`)
* Monitors real-time cryptocurrency asset prices via custom intervals.
* Triggers instant automated HTML-formatted Telegram alerts when target thresholds are breached.
* Lightweight and optimized for running 24/7 on background servers.

### 3. ⛓ Ethereum Wallet Tracker (`eth_wallet_tracker.py`)
* Interacts directly with the Ethereum blockchain via public RPC endpoints (Cloudflare RPC).
* Fetches exact live ETH balances of any given on-chain wallet address in real-time.
* Requires zero API keys or centralized platform registrations.

### 4. 🔍 On-Chain Metadata Scanner (`discord_finder.py`)
* Connects to GeckoTerminal API to monitor newly created liquidity pools in real-time.
* Scans raw network metadata structure to filter projects with early embedded social links.
* Optimized for micro-cap research and automated token discovery.

## 💻 Tech Stack
* Python 3.x
* `requests` (API & RPC communication)
* `pandas` (Data structuring and analytical export)

## ⚙️ Quick Start

1. Clone the repository and install required packages:
   ```bash
   pip install requests pandas
   ```

2. Run any specific script based on your requirements:
   ```bash
   python crypto_scraper.py
   python tg_price_alert.py
   python eth_wallet_tracker.py
   python discord_finder.py
   ```

---
*Developed for data automation, blockchain tracking, and automated Web3 market analysis.*
