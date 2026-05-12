---
name: token-pick
description: Find low-risk tokens with positive momentum using security + TA filters.
category: crypto-markets
tier: standard
solvr_api: https://api.solvrbot.com
auth: Authorization: Bearer {SOLVR_API_KEY}
source: https://github.com/solvrbase/solvr
---

# Token Pick

Find low-risk tokens with positive momentum using security + TA filters.

## Endpoints
- `GET https://api.solvrbot.com/api/v1/dex/trending` — trending tokens
- `POST https://api.solvrbot.com/api/v1/security/scan` — token security scan
- `POST https://api.solvrbot.com/api/v1/ta/quick` — quick TA

## Instructions
1. Fetch trending tokens: `GET https://api.solvrbot.com/api/v1/dex/trending`
2. For top 10 trending, run security scan: `POST https://api.solvrbot.com/api/v1/security/scan`
3. Filter: only keep tokens with `risk_score` <= 35 (safe)
4. For safe tokens, fetch quick TA: `POST https://api.solvrbot.com/api/v1/ta/quick`
5. Score each: +1 RSI < 65, +1 MACD bullish, +1 price > 0%, +1 volume > avg
6. Output top 3 picks with score and rationale.

```
🎯 TODAY'S PICKS (low-risk + momentum)
1. $TOKEN — Risk: 12/100 | RSI: 58 | MACD: ↑ | Score: 4/4
   Why: Clean contract, accumulation pattern, rising volume
```
