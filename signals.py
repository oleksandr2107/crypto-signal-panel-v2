import requests

def get_bybit_open_interest():
    # LONG сигнали зі скринера відкритого інтересу
    pairs = ['BTCUSDT', 'ETHUSDT']
    signals = []
    for symbol in pairs:
        price = get_price(symbol)
        signals.append({
            'pair': symbol,
            'signal': 'LONG',
            'price': price,
            'link': f'https://www.coinglass.com/tv/{symbol}'
        })
    return signals

def get_price_spike_signals():
    # SHORT сигнали зі скринера цінових сплесків
    pairs = ['DOGEUSDT', 'SOLUSDT']
    signals = []
    for symbol in pairs:
        price = get_price(symbol)
        signals.append({
            'pair': symbol,
            'signal': 'SHORT',
            'price': price,
            'link': f'https://www.coinglass.com/tv/{symbol}'
        })
    return signals

def get_price(symbol):
    try:
        url = f'https://api.binance.com/api/v3/ticker/price?symbol={symbol}'
        response = requests.get(url)
        data = response.json()
        return f"${float(data['price']):,.2f}"
    except:
        return "?"
