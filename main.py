import yfinance as yf
import pandas as pd
import os
import matplotlib.pyplot as plt

tickers = ['XHB', 'USO', 'CORN', 'WEAT', 'CPER', 'SLX', 'XLY', 'DX-Y.NYB', 'VNQ', 'BZ=F', 'NG=F', 'KMX']
data = yf.download(tickers, start='2025-10-24')['Close']
#data = yf.download(tickers, period='30d')['Close']

forecast = float(input('Enter CPI Forecast [%]: '))

data = data.ffill().dropna()
returns = data.pct_change().dropna()
perf = (data.iloc[-1] / data.iloc[0] - 1) * 100
perf2sf = perf.round(2)

print(perf2sf)

weighting = {
    'XHB'       : 0.22,   # housing / building activity (reduced, add VNQ)
    'USO'       : 0.12,   # crude/energy (WTI proxy)
    'CORN'      : 0.06,   # food
    'WEAT'      : 0.05,   # food
    'CPER'      : 0.05,   # base-metals
    'SLX'       : 0.04,   # steel / industrial metals
    'XLY'       : 0.08,   # consumer demand / discretionary
    'DX-Y.NYB'  : 0.15,   # dollar (important driver) 
    'VNQ'       : 0.10,   # shelter/OER proxy (new)
    'BZ=F'      : 0.05,   # Brent (new)
    'NG=F'      : 0.03,   # natural gas (new)
    'KMX'       : 0.05    # used-car retail proxy (new)
}

cpiProxy = sum(weighting[t] * perf.get(t, 0) for t in weighting)

os.system('clear' if os.name == 'nt' else 'clear')
print(f"Nowcast [30d]: {cpiProxy:.2f}%")
signal = cpiProxy - forecast
print(f'Computing Signal: {signal:.2f}%')

if signal > 0:
    print('\n\n\nusd ↑\nmetals ↑↓\nindices ↓\n\nbuy xxx/usd\nsell usd/xxx')

elif signal < 0:
    print('\n\n\nusd ↓\nmetals ↓\nindices ↑\n\nsell xxx/usd\nbuy usd/xxx')