from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def index():
    # Тимчасові сигнали (замість реальних даних)
    signals = [
        {'symbol': 'BTCUSDT', 'exchange': 'Binance', 'type': 'LONG', 'strength': random.randint(1, 100)},
        {'symbol': 'ETHUSDT', 'exchange': 'Bybit', 'type': 'SHORT', 'strength': random.randint(1, 100)},
        {'symbol': 'SOLUSDT', 'exchange': 'Binance', 'type': 'LONG', 'strength': random.randint(1, 100)}
    ]
    return render_template('index.html', signals=signals)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)