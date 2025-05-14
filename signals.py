import requests

# ВСТАВ СВІЙ API-КЛЮЧ ВНИЗУ:
COINGLASS_API_KEY = 'ВСТАВ_СЮДИ_ТВІЙ_API_КЛЮЧ'

def get_bybit_open_interest():
    url = "https://api.bybit.com/v5/market/open-interest?category=linear&symbol=BTCUSDT&interval=5min"
    try:
        response = requests.get(url)
        data = response.json()
        value = float(data["result"]["list"][0]["openInterest"])

        if value > 100000000:
            return [{'pair': 'BTCUSDT', 'signal': 'LONG'}]
        else:
            return []
    except Exception as e:
        print("OI Error:", e)
        return []

def get_binance_open_interest():
    url = 'https://open-api.coinglass.com/api/pro/v1/futures/openInterest'
    headers = {
        'coinglassSecret': COINGLASS_API_KEY
    }
    try:
        response = requests.get(url, headers=headers)
        data = response.json()

        signals = []
        for item in data['data']:
            if item['exchangeName'] == 'Binance' and float(item['openInterestValue']) > 100000000:
                signals.append({'pair': item['symbol'], 'signal': 'LONG'})
        return signals[:3]
    except Exception as e:
        print("Coinglass Binance OI Error:", e)
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
