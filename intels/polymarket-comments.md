---
name: polymarket-comments
description: Surface top Polymarket prediction markets with commentary context.
category: crypto-markets
tier: free
solvr_api: https://api.solvrbot.com
auth: Authorization: Bearer {SOLVR_API_KEY}
source: https://github.com/solvrbase/solvr
---

# Polymarket Comments

Surface top Polymarket prediction markets with commentary context.

## Endpoints
- `GET https://api.solvrbot.com/api/v1/polymarket?limit=10` — active markets
- `GET https://api.solvrbot.com/api/v1/news?topic={market_topic}` — news context

## Instructions
1. Fetch top markets: `GET https://api.solvrbot.com/api/v1/polymarket?limit=10`
2. For each top market, fetch related news: `GET https://api.solvrbot.com/api/v1/news?topic=KEYWORD&limit=3`
3. Generate commentary linking news context to market probability
4. Output: Market + probability + news catalyst + analysis.

```
📊 "Will Fed cut rates in June?" — YES: 45%
📰 Related: "Fed minutes signal patience on rate cuts" (Reuters)
💡 Analysis: Current pricing implies uncertainty. Watch May CPI.
```
