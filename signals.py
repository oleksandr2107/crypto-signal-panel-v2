def get_bybit_open_interest():
    # Тестові LONG сигнали
    return [
        {'pair': 'BTCUSDT', 'signal': 'LONG'},
        {'pair': 'ETHUSDT', 'signal': 'LONG'}
    ]

def get_price_spike_signals():
    # Тестові SHORT сигнали
    return [
        {'pair': 'DOGEUSDT', 'signal': 'SHORT'},
        {'pair': 'SOLUSDT', 'signal': 'SHORT'}
    ]
