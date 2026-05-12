---
name: reddit-digest
description: Reddit community digest — hot posts from crypto/tech subreddits.
category: research-content
tier: free
solvr_api: https://api.solvrbot.com
auth: Authorization: Bearer {SOLVR_API_KEY}
source: https://github.com/solvrbase/solvr
---

# Reddit Digest

Reddit community digest — hot posts from crypto/tech subreddits.

## Endpoints
- `GET https://api.solvrbot.com/api/v1/reddit?subreddit={sub}&sort=hot&limit=10` — Reddit hot posts

## Instructions
1. Fetch from multiple subreddits in parallel:
   - `GET https://api.solvrbot.com/api/v1/reddit?subreddit=cryptocurrency&limit=5`
   - `GET https://api.solvrbot.com/api/v1/reddit?subreddit=defi&limit=5`
   - `GET https://api.solvrbot.com/api/v1/reddit?subreddit=ethfinance&limit=5`
2. Sort all posts by score descending
3. Filter: score > 100
4. Output top 10 posts with title, score, comment count, link.
