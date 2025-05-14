import requests

def get_bybit_open_interest():
    url = "https://api.bybit.com/v5/market/open-interest?category=linear&symbol=BTCUSDT&interval=5min"
    try:
        response = requests.get(url)
        data = response.json()
        value = float(data["result"]["list"][0]["openInterest"])

        if value > 100000000:  # поріг Open Interest
            return [{'pair': 'BTCUSDT', 'signal': 'LONG'}]
        else:
            return []
    except Exception as e:
        print("Bybit OI Error:", e)
        return []

def get_price_spike_signals():
    url = 'https://api.binance.com/api/v3/ticker/price'
    try:
        response = requests.get(url)
        prices = response.json()

        result = []
        for p in prices:
            if 'USDT' in p['symbol'] and float(p['price']) > 100:  # умовний сплеск
                result.append({'pair': p['symbol'], 'signal': 'SHORT'})
        return result[:2]
    except Exception as e:
        print("Price Error:", e)
        return []
