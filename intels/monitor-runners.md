---
name: monitor-runners
description: Find tokens with unusual volume + momentum — potential runners before they run.
category: crypto-markets
tier: standard
solvr_api: https://api.solvrbot.com
auth: Authorization: Bearer {SOLVR_API_KEY}
source: https://github.com/solvrbase/solvr
---

# Monitor Runners

Find tokens with unusual volume + momentum — potential runners before they run.

## Endpoints
- `GET https://api.solvrbot.com/api/v1/dex/trending` — trending tokens
- `POST https://api.solvrbot.com/api/v1/ta/quick` — RSI/MACD snapshot

## Instructions
1. Fetch trending: `GET https://api.solvrbot.com/api/v1/dex/trending`
2. Filter: volume_24h > $50k, price_change_24h > 5%
3. For filtered tokens, check TA: `POST https://api.solvrbot.com/api/v1/ta/quick`
4. Runner criteria: RSI 40-65 (room to run), MACD bullish cross, volume > 1.5x avg
5. Rank by composite score. Output top 5 potential runners.

```
🏃 POTENTIAL RUNNERS
1. $TOKEN — RSI: 52 | MACD: ↑ cross | Vol: 2.1x avg | Score: HIGH
```
