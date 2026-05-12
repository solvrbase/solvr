---
name: monitor-kalshi
description: Track Kalshi prediction markets via Polymarket + macro news proxy.
category: crypto-markets
tier: free
solvr_api: https://api.solvrbot.com
auth: Authorization: Bearer {SOLVR_API_KEY}
source: https://github.com/solvrbase/solvr
---

# Monitor Kalshi

Track Kalshi prediction markets via Polymarket + macro news proxy.

## Endpoints
- `GET https://api.solvrbot.com/api/v1/polymarket?topic=macro` — macro prediction markets
- `GET https://api.solvrbot.com/api/v1/news?topic=prediction+market+Kalshi` — Kalshi news

## Instructions
1. Fetch macro-focused prediction markets: `GET https://api.solvrbot.com/api/v1/polymarket?topic=fed+rate+election`
2. Fetch Kalshi news: `GET https://api.solvrbot.com/api/v1/news?topic=Kalshi+prediction+market&limit=5`
3. Surface key market probabilities: Fed rate, election, economic outcomes
4. Output: Prediction market dashboard with key probabilities.

```
🎲 PREDICTION MARKETS
Fed Cut June:    YES 45% | Vol $2.1M
BTC > $100k EOY: YES 62% | Vol $8.4M
US Recession:    YES 28% | Vol $5.2M
```
