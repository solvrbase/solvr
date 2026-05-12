---
name: refresh-x
description: Refresh X/Twitter content strategy with trending topics and real data.
category: social-writing
tier: free
solvr_api: https://api.solvrbot.com
auth: Authorization: Bearer {SOLVR_API_KEY}
source: https://github.com/solvrbase/solvr
---

# Refresh X

Refresh X/Twitter content strategy with trending topics and real data.

## Endpoints
- `GET https://api.solvrbot.com/api/v1/news?category=tech&limit=10` — trending tech topics
- `GET https://api.solvrbot.com/api/v1/dex/trending` — trending tokens for crypto content

## Instructions
1. Fetch trending topics from news
2. Fetch trending tokens for data-backed crypto content
3. Identify content gaps (topics trending in news but underrepresented)
4. Generate 5 tweet ideas with:
   - Hook (first line)
   - Data point or stat
   - Call to action
5. Output: Content calendar for next 24 hours.
