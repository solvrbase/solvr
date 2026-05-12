---
name: token-alert
description: Monitor tracked tokens for price/volume anomalies. Alert when 24h change >10% or volume spikes.
category: crypto-markets
tier: standard
solvr_api: https://api.solvrbot.com
auth: Authorization: Bearer {SOLVR_API_KEY}
source: https://github.com/solvrbase/solvr
---

# Token Alert

Monitor tracked tokens for price/volume anomalies. Alert when 24h change >10% or volume spikes.

## Endpoints
- `GET https://api.solvrbot.com/api/v1/dex/trending` — trending tokens
- `POST https://api.solvrbot.com/api/v1/ta/quick` — quick RSI/MACD/BB snapshot

## Instructions
1. Fetch trending: `GET https://api.solvrbot.com/api/v1/dex/trending`
2. For each tracked token, fetch quick TA: `POST https://api.solvrbot.com/api/v1/ta/quick` with `{"symbol": "SYMBOL"}`
3. Alert conditions:
   - `price_change_24h` > +10% → PUMP ALERT
   - `price_change_24h` < -10% → DUMP ALERT
   - RSI > 70 → OVERBOUGHT
   - RSI < 30 → OVERSOLD
   - Volume spike > 3x 7d average → VOLUME SPIKE
4. Format alert: `⚠️ $SYMBOL: +15.2% in 24h | Vol 4x avg | RSI 74 (overbought)`
