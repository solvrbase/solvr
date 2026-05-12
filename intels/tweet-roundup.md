---
name: tweet-roundup
description: Daily tweet roundup — what happened today, distilled to 5 tweets.
category: social-writing
tier: free
solvr_api: https://api.solvrbot.com
auth: Authorization: Bearer {SOLVR_API_KEY}
source: https://github.com/solvrbase/solvr
---

# Tweet Roundup

Daily tweet roundup — what happened today, distilled to 5 tweets.

## Endpoints
- `GET https://api.solvrbot.com/api/v1/news?category=general&limit=10` — top news
- `GET https://api.solvrbot.com/api/v1/dex/trending` — crypto moves
- `GET https://api.solvrbot.com/api/v1/worlddata?query=vix` — market sentiment

## Instructions
1. Fetch top news across all categories
2. Fetch top crypto movers
3. Fetch VIX for market sentiment
4. Write 5 tweet-length summaries of the day's key events
5. Format as a thread with hooks and data points.
