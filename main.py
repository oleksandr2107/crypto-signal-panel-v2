from flask import Flask, render_template, request
from signals import get_bybit_open_interest, get_price_spike_signals

app = Flask(__name__)

@app.route('/')
def home():
    oi_threshold = float(request.args.get('oi_threshold', 1.0))
    spike_threshold = float(request.args.get('spike_threshold', 1.2))

    long_signals = get_bybit_open_interest(oi_threshold)
    short_signals = get_price_spike_signals(spike_threshold)

    return render_template('index.html', 
        long_signals=long_signals, 
        short_signals=short_signals, 
        request=request
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
