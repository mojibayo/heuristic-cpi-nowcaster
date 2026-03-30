**A lightweight, real-time market-implied CPI nowcaster** built in Python.

It calculates a 30-day weighted performance of inflation-sensitive assets (energy, food, metals, housing, used cars, consumer demand, and the dollar) and compares it against your CPI forecast to generate a directional trading signal.

Created in October 2025 as a fast macro filter for CPI prints.
Not backtested. For proper usage, I recommend backtesting and having the weights based on regression.

---

## Features

- Pulls live 30-day returns via `yfinance`
- Weighted proxy for headline CPI momentum
- Simple signal: **Proxy > Forecast → inflation surprise → USD strength / risk-off**
- One-command run, zero setup beyond Python + yfinance
- Clear terminal output with signal interpretation

---

## Requirements

```bash
pip install yfinance pandas matplotlib
```

---

- "Alpha" can probably be built around it, as seen below:
<img width="820" height="858.5" alt="image" src="https://github.com/user-attachments/assets/1e806cc9-3857-4466-81f2-9b958679e96b" />




