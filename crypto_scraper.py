import requests
import pandas as pd
from datetime import datetime

def fetch_crypto_data():
    """
    Fetches 24hr ticker data from Binance API, filters top 50 USDT pairs by volume, 
    and exports the data to a CSV file.
    """
    print("Fetching data from Binance API...")
    url = "https://api.binance.com/api/v3/ticker/24hr"
    
    try:
        # Added timeout to prevent infinite hanging if the API is unresponsive
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        # Filter for USDT trading pairs only
        usdt_pairs = [item for item in data if item['symbol'].endswith('USDT')]
        
        # Sort by quote volume (descending)
        usdt_pairs = sorted(usdt_pairs, key=lambda x: float(x['quoteVolume']), reverse=True)
        
        # Take the top 50 pairs
        top_50 = usdt_pairs[:50]
        
        processed_data = []
        for coin in top_50:
            processed_data.append({
                "Symbol": coin['symbol'],
                "Last Price (USDT)": float(coin['lastPrice']),
                "Price Change 24h (%)": float(coin['priceChangePercent']),
                "Volume 24h (USDT)": round(float(coin['quoteVolume']), 2)
            })
            
        # Export to CSV
        df = pd.DataFrame(processed_data)
        filename = f"crypto_market_data_{datetime.now().strftime('%Y%m%d')}.csv"
        df.to_csv(filename, index=False)
        print(f"Success! Top 50 markets exported to {filename}")
        
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    fetch_crypto_data()
