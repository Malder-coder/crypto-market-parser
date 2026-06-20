import time
import requests

# Configuration (The user will fill in their own data)
TELEGRAM_BOT_TOKEN = "YOUR_TELEGRAM_TOKEN_HERE"
TELEGRAM_CHAT_ID = "YOUR_CHAT_ID_HERE"
SYMBOL = "BTCUSDT"
PRICE_THRESHOLD = 60000.0  # Alert price level

def get_price(symbol):
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
    try:
        # Added timeout to ensure the loop doesn't block
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return float(response.json()['price'])
    except Exception as e:
        print(f"API Error: {e}")
        return None

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "parse_mode": "HTML"
    }
    try:
        requests.post(url, json=payload, timeout=10)
        print("Alert sent to Telegram!")
    except Exception as e:
        print(f"Telegram Error: {e}")

def monitor_price():
    print(f"Started monitoring {SYMBOL}. Target alert: ${PRICE_THRESHOLD}")
    while True:
        current_price = get_price(SYMBOL)
        if current_price:
            print(f"Current {SYMBOL} price: ${current_price}")
            if current_price < PRICE_THRESHOLD:
                msg = f"🚨 <b>ALERT:</b> {SYMBOL} dropped below ${PRICE_THRESHOLD}!\nCurrent price: <b>${current_price}</b>"
                send_telegram_message(msg)
                break # Stops after first alert
        time.sleep(30) # Checks every 30 seconds

if __name__ == "__main__":
    # monitor_price() # Commented out for safe initial execution on GitHub
    print("Telegram Alert Bot initialized. Ready to run.")
