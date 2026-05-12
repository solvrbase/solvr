---
name: remix-tweets
description: Remix trending news into original tweet formats.
category: social-writing
tier: free
solvr_api: https://api.solvrbot.com
auth: Authorization: Bearer {SOLVR_API_KEY}
source: https://github.com/solvrbase/solvr
---

# Remix Tweets

Remix trending news into original tweet formats.

## Endpoints
- `GET https://api.solvrbot.com/api/v1/news?topic={niche}&limit=10` — source material
- `GET https://api.solvrbot.com/api/v1/worlddata?query={stat}` — supporting data

## Instructions
1. Fetch 10 trending articles in your niche
2. For each article, identify the key insight or data point
3. Remix into tweet formats:
   - Thread hook: controversial take or surprising stat
   - Hot take: contrarian opinion with data backing
   - How-to: actionable steps from news
   - Data drop: stats formatted for maximum impact
4. Output: 5 remixed tweets with engagement score estimate.
