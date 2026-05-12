---
name: monitor-polymarket
description: Track Polymarket prediction markets — prices, volume, top moving markets.
category: crypto-markets
tier: free
solvr_api: https://api.solvrbot.com
auth: Authorization: Bearer {SOLVR_API_KEY}
source: https://github.com/solvrbase/solvr
---

# Monitor Polymarket

Track Polymarket prediction markets — prices, volume, top moving markets.

## Endpoints
- `GET https://api.solvrbot.com/api/v1/polymarket?limit=20` — active markets
- `GET https://api.solvrbot.com/api/v1/polymarket?topic={keyword}` — filtered markets

## Instructions
1. Fetch active markets: `GET https://api.solvrbot.com/api/v1/polymarket?limit=20`
2. Sort by volume descending
3. Identify markets where YES probability moved > 10% (compare to stored state)
4. Alert on significant moves: `📊 POLYMARKET: "Will BTC hit $100k?" YES: 72% (+15% today)`
5. Output: Top 5 markets by volume + any major moves.
