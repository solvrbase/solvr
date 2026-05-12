---
name: morning-brief
description: Daily morning intelligence brief — news, markets, macro, and priorities.
category: productivity
tier: free
solvr_api: https://api.solvrbot.com
auth: Authorization: Bearer {SOLVR_API_KEY}
source: https://github.com/solvrbase/solvr
---

# Morning Brief

Daily morning intelligence brief — news, markets, macro, and priorities.

## Endpoints
- `GET https://api.solvrbot.com/api/v1/news?category=general&limit=5` — top news
- `GET https://api.solvrbot.com/api/v1/worlddata?query=vix` — market sentiment
- `GET https://api.solvrbot.com/api/v1/worlddata?query=fed+rate` — macro
- `GET https://api.solvrbot.com/api/v1/dex/trending` — crypto pulse

## Instructions
Run all 4 fetches in parallel, then format:

```
☀️ MORNING BRIEF — {date}

📰 TOP STORIES
1. [headline] — [source]
2. [headline] — [source]
3. [headline] — [source]

📊 MARKETS
VIX: {vix} | Fed Rate: {rate}% | Crypto: {trending_top} (+{change}%)

🎯 TODAY'S FOCUS
[1 sentence on most important development]
```
