from flask import Flask, render_template
from open_interest import get_oi_signals
from price_spike import get_spike_signals

app = Flask(__name__)

@app.route("/")
def home():
    oi_signals = get_oi_signals()
    spike_signals = get_spike_signals()
    return render_template("index.html", oi_signals=oi_signals, spike_signals=spike_signals)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
