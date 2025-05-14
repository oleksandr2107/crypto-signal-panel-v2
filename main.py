try:
    oi_threshold = float(request.args.get('oi_threshold', 1.0) or 1.0)
    spike_threshold = float(request.args.get('spike_threshold', 1.2) or 1.2)
except:
    oi_threshold = 1.0
    spike_threshold = 1.2
