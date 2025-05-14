from flask import Flask, render_template
from signals import get_bybit_open_interest, get_price_spike_signals

app = Flask(__name__)

@app.route('/')
def home():
    long_signals = get_bybit_open_interest()
    short_signals = get_price_spike_signals()
    return render_template('index.html', long_signals=long_signals, short_signals=short_signals)

   if name == '__main__':
    app.run(debug=True)
