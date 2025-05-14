def get_bybit_open_interest(threshold=1.0):
    return [
        {'pair': 'BTCUSDT', 'signal': f'LONG (+{threshold}%)', 'price': '$65,000', 'link': 'https://www.coinglass.com/tv/BTCUSDT'}
    ]

def get_price_spike_signals(threshold=1.2):
    return [
        {'pair': 'ETHUSDT', 'signal': f'SHORT (-{threshold}%)', 'price': '$2,900', 'link': 'https://www.coinglass.com/tv/ETHUSDT'}
    ]
