---
name: market-context-refresh
description: Refresh macro + crypto market context for trading decisions.
category: crypto-markets
tier: free
solvr_api: https://api.solvrbot.com
auth: Authorization: Bearer {SOLVR_API_KEY}
source: https://github.com/solvrbase/solvr
---

# Market Context Refresh

Refresh macro + crypto market context for trading decisions.

## Endpoints
- `GET https://api.solvrbot.com/api/v1/worlddata?query={indicator}` — macro indicators
- `GET https://api.solvrbot.com/api/v1/news?category=business` — market news

## Instructions
1. Fetch key macro indicators in parallel:
   - `GET https://api.solvrbot.com/api/v1/worlddata?query=fed+rate`
   - `GET https://api.solvrbot.com/api/v1/worlddata?query=vix`
   - `GET https://api.solvrbot.com/api/v1/worlddata?query=us+gdp`
   - `GET https://api.solvrbot.com/api/v1/worlddata?query=10y+treasury+yield`
2. Fetch top 5 business/market news headlines
3. Assess macro regime:
   - Rate > 4.5% + VIX > 25 → RISK OFF
   - Rate declining + VIX < 20 → RISK ON
   - Mixed → NEUTRAL
4. Output: 1-paragraph market context + regime label.
