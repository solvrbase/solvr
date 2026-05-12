---
name: channel-recap
description: Recap what happened in a topic or community over the past 24 hours.
category: research-content
tier: free
solvr_api: https://api.solvrbot.com
auth: Authorization: Bearer {SOLVR_API_KEY}
source: https://github.com/solvrbase/solvr
---

# Channel Recap

Recap what happened in a topic or community over the past 24 hours.

## Endpoints
- `GET https://api.solvrbot.com/api/v1/news?topic={channel_topic}&limit=10` — recent news
- `GET https://api.solvrbot.com/api/v1/reddit?subreddit={sub}&limit=10` — community posts

## Instructions
1. Fetch relevant news: `GET https://api.solvrbot.com/api/v1/news?topic=TOPIC&limit=10`
2. Fetch community posts: `GET https://api.solvrbot.com/api/v1/reddit?subreddit=SUBREDDIT&limit=10`
3. Synthesize into a "what you missed" recap:
   - Top 3 news stories
   - Top community discussions
   - Key metrics change (if crypto: price/volume)
4. Keep under 200 words, bullet-point format.
