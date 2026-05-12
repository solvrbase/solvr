---
name: evening-recap
description: End-of-day recap — what moved, what mattered, what to watch tomorrow.
category: productivity
tier: free
solvr_api: https://api.solvrbot.com
auth: Authorization: Bearer {SOLVR_API_KEY}
source: https://github.com/solvrbase/solvr
---

# Evening Recap

End-of-day recap — what moved, what mattered, what to watch tomorrow.

## Endpoints
- `GET https://api.solvrbot.com/api/v1/news?category=general&limit=10` — day's news
- `GET https://api.solvrbot.com/api/v1/dex/trending` — crypto close

## Instructions
1. Fetch day's top news
2. Fetch crypto movers for the day
3. Structure recap:
   - What moved: top price movers, key market moves
   - What mattered: most impactful news story
   - What to watch: setup for tomorrow based on today's signals
4. Keep under 150 words.
