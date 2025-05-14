import requests
from datetime import datetime, timedelta

def get_all_binance_symbols():
    url = "https://api.binance.com/api/v3/ticker/price"
    try:
        response = requests.get(url)
        data = response.json()
        return [item['symbol'] for item in data if item['symbol'].endswith('USDT')]
    except Exception as e:
        print("Binance symbols error:", e)
        return []

def get_all_bybit_symbols():
    url = "https://api.bybit.com/v5/market/tickers?category=linear"
    try:
        response = requests.get(url)
        data = response.json()
        return [item['symbol'] for item in data['result']['list'] if item['symbol'].endswith('USDT')]
    except Exception as e:
        print("Bybit symbols error:", e)
        return []

def get_bybit_open_interest():
    symbols = get_all_bybit_symbols()
    signals = []

    for symbol in symbols:
        try:
            url = f"https://api.bybit.com/v5/market/open-interest?category=linear&symbol={symbol}&interval=5min"
            response = requests.get(url)
            data = response.json()
            oi_now = float(data["result"]["list"][0]["openInterest"])
            oi_prev = float(data["result"]["list"][1]["openInterest"])
            change_pct = ((oi_now - oi_prev) / oi_prev) * 100

            if change_pct > 1.0:
                signals.append({
                    'pair': symbol,
                    'signal': f'LONG (+{change_pct:.2f}%)',
                    'price': get_price(symbol),
                    'link': f'https://www.coinglass.com/tv/{symbol}'
                })

        except Exception as e:
            continue

    return signals

def get_price_spike_signals():
    symbols = get_all_binance_symbols()
    signals = []

    for symbol in symbols[:30]:  # обмежено до 30 монет, щоб не перевантажити API
        try:
            url = f"https://api.binance.com/api/v3/klines?symbol={symbol}&interval=1m&limit=5"
            response = requests.get(url)
            data = response.json()

            open_price = float(data[0][1])
            close_price = float(data[-1][4])
            change_pct = ((close_price - open_price) / open_price) * 100

            if abs(change_pct) > 1.2:
                signals.append({
                    'pair': symbol,
                    'signal': f'SHORT ({change_pct:+.2f}%)',
                    'price': get_price(symbol),
                    'link': f'https://www.coinglass.com/tv/{symbol}'
                })

        except Exception:
            continue

    return signals

def get_price(symbol):
    try:
        url = f'https://api.binance.com/api/v3/ticker/price?symbol={symbol}'
        response = requests.get(url)
        data = response.json()
        return f"${float(data['price']):,.2f}"
    except:
        return "?"
