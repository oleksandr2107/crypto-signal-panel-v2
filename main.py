from flask import Flask, render_template_string
import random

app = Flask(__name__)

TEMPLATE = open("index.html", encoding="utf-8").read()

def get_mock_data():
    symbols = ["BTCUSDT", "ETHUSDT", "SOLUSDT", "AVAXUSDT", "DOGEUSDT"]
    rows = []
    for sym in symbols:
        for ex in ["Binance", "Bybit"]:
            signal_type = random.choice(["long", "short", "normal"])
            value = round(random.uniform(-5, 5), 2)
            row = f"<tr class='{signal_type}'><td>{sym}</td><td>{ex}</td><td>{signal_type.upper()}</td><td>{value}%</td><td><a href='https://www.coinglass.com/longShortChart/{sym.replace('USDT','')}' target='_blank'>Coinglass</a></td></tr>"
            rows.append(row)
    return rows

@app.route("/")
def index():
    data_rows = get_mock_data()
    html = TEMPLATE.replace("<!-- SIGNAL_ROWS -->", "\n".join(data_rows))
    return html

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
