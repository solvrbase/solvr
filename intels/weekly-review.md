---
name: weekly-review
description: Weekly review — what happened, what changed, and what to prioritize next week.
category: productivity
tier: free
solvr_api: https://api.solvrbot.com
auth: Authorization: Bearer {SOLVR_API_KEY}
source: https://github.com/solvrbase/solvr
---

# Weekly Review

Weekly review — what happened, what changed, and what to prioritize next week.

## Endpoints
- `GET https://api.solvrbot.com/api/v1/news?category=general&limit=10` — week's news
- `GET https://api.solvrbot.com/api/v1/dex/trending` — crypto performance
- `GET https://api.solvrbot.com/api/v1/worlddata?query=s%26p+500` — market performance

## Instructions
1. Fetch week's top news
2. Fetch key market metrics for the week
3. Review structure:
   - Key events this week (top 5)
   - Market performance summary
   - Wins and misses (if tracking positions)
   - Top 3 priorities for next week
4. Output in weekly review template format.
