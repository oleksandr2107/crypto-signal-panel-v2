from flask import Flask, render_template, request
from signals import get_bybit_open_interest, get_price_spike_signals

app = Flask(__name__)

@app.route('/')
def home():
    coins = request.args.get('coins', 'BTCUSDT,ETHUSDT')
    oi_threshold = float(request.args.get('oi_threshold', 3.0))
    spike_threshold = float(request.args.get('spike_threshold', 1.5))

    coin_list = [c.strip().upper() for c in coins.split(',') if c.strip()]
    long_signals = get_bybit_open_interest(coin_list, oi_threshold)
    short_signals = get_price_spike_signals(coin_list, spike_threshold)

    return render_template('index.html',
                           long_signals=long_signals,
                           short_signals=short_signals,
                           coins=coins,
                           oi_threshold=oi_threshold,
                           spike_threshold=spike_threshold)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
