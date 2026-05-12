---
name: fetch-tweets
description: Fetch and synthesize crypto Twitter activity via news and trending data.
category: research-content
tier: free
solvr_api: https://api.solvrbot.com
auth: Authorization: Bearer {SOLVR_API_KEY}
source: https://github.com/solvrbase/solvr
---

# Fetch Tweets

Fetch and synthesize crypto Twitter activity via news and trending data.

## Endpoints
- `GET https://api.solvrbot.com/api/v1/news?topic={term}&limit=10` — news mentions
- `GET https://api.solvrbot.com/api/v1/dex/trending` — what's trending on-chain

## Instructions
1. Fetch news mentions of target topic: `GET https://api.solvrbot.com/api/v1/news?topic=TERM&limit=10`
2. Fetch trending tokens to cross-reference on-chain activity
3. Synthesize: what's being discussed in news vs what's moving on-chain
4. Identify discrepancies (narrative vs reality)
5. Output: topic summary + sentiment signal (BULLISH/BEARISH/NEUTRAL).
