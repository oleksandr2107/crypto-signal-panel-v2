import requests
from datetime import datetime, timedelta

def get_bybit_open_interest():
    url = "https://api.bybit.com/v5/market/open-interest?category=linear&symbol=BTCUSDT&interval=5min"
    try:
        response = requests.get(url)
        data = response.json()
        oi_now = float(data["result"]["list"][0]["openInterest"])
        oi_prev = float(data["result"]["list"][1]["openInterest"])
        change_pct = ((oi_now - oi_prev) / oi_prev) * 100

        if change_pct > 3.0:  # Поріг росту OI > 3%
            return [{
                'pair': 'BTCUSDT',
                'signal': f'LONG (+{change_pct:.2f}%)',
                'price': get_price('BTCUSDT'),
                'link': 'https://www.coinglass.com/tv/BTCUSDT'
            }]
        return []
    except Exception as e:
        print("Bybit OI Error:", e)
        return []

def get_price_spike_signals():
    try:
        now = int(datetime.now().timestamp() * 1000)
        five_min_ago = now - 5 * 60 * 1000
        url = "https://api.binance.com/api/v3/klines?symbol=ETHUSDT&interval=1m&limit=5"
        response = requests.get(url)
        data = response.json()

        open_price = float(data[0][1])
        close_price = float(data[-1][4])
        change_pct = ((close_price - open_price) / open_price) * 100

        if abs(change_pct) > 1.5:
            return [{
                'pair': 'ETHUSDT',
                'signal': f'SHORT ({change_pct:+.2f}%)',
                'price': get_price('ETHUSDT'),
                'link': 'https://www.coinglass.com/tv/ETHUSDT'
            }]
        return []
    except Exception as e:
        print("Price Spike Error:", e)
        return []

def get_price(symbol):
    try:
        url = f'https://api.binance.com/api/v3/ticker/price?symbol={symbol}'
        response = requests.get(url)
        data = response.json()
        return f"${float(data['price']):,.2f}"
    except:
        return "?"
