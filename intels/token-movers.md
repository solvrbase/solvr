---
name: token-movers
description: Top 10 winners and losers today with momentum signal tags.
category: crypto-markets
tier: free
solvr_api: https://api.solvrbot.com
auth: Authorization: Bearer {SOLVR_API_KEY}
source: https://github.com/solvrbase/solvr
---

# Token Movers

Top 10 winners and losers today with momentum signal tags.

## Endpoints
- `GET https://api.solvrbot.com/api/v1/dex/trending` — trending tokens across all chains

## Instructions
1. Fetch trending: `GET https://api.solvrbot.com/api/v1/dex/trending`
2. Sort by `price_change_24h` descending for winners, ascending for losers
3. Tag each token:
   - change > +20%: BREAKOUT
   - change > +10%: RALLYING
   - change < -20%: BREAKDOWN
   - change < -10%: DUMPING
   - volume > 2x avg: HIGH-VOL
4. Output top 5 winners + top 5 losers with tags.

```
🟢 TOP MOVERS TODAY
1. $TOKEN +24.5% [BREAKOUT] [HIGH-VOL]
2. $TOKEN +18.2% [RALLYING]
...
🔴 BOTTOM MOVERS
1. $TOKEN -22.1% [BREAKDOWN]
```
