---
name: defi-overview
description: Global DeFi market snapshot — top pools, TVL trends, macro context.
category: crypto-markets
tier: free
solvr_api: https://api.solvrbot.com
auth: Authorization: Bearer {SOLVR_API_KEY}
source: https://github.com/solvrbase/solvr
---

# Defi Overview

Global DeFi market snapshot — top pools, TVL trends, macro context.

## Endpoints
- `GET https://api.solvrbot.com/api/v1/dex/trending` — trending DeFi tokens
- `GET https://api.solvrbot.com/api/v1/worlddata?query=crypto+market` — macro context
- `GET https://api.solvrbot.com/api/v1/news?topic=DeFi&category=business` — DeFi news

## Instructions
1. Fetch trending: `GET https://api.solvrbot.com/api/v1/dex/trending`
2. Fetch DeFi news: `GET https://api.solvrbot.com/api/v1/news?topic=DeFi&limit=5`
3. Fetch macro: `GET https://api.solvrbot.com/api/v1/worlddata?query=fed+rate`
4. Summarize:
   - Top 5 DeFi tokens by volume
   - Key news headline
   - Macro signal (rate environment)
5. Output DeFi overview brief (< 200 words).
