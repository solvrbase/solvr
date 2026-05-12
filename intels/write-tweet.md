---
name: write-tweet
description: Write high-engagement tweets backed by live data and news.
category: social-writing
tier: free
solvr_api: https://api.solvrbot.com
auth: Authorization: Bearer {SOLVR_API_KEY}
source: https://github.com/solvrbase/solvr
---

# Write Tweet

Write high-engagement tweets backed by live data and news.

## Endpoints
- `GET https://api.solvrbot.com/api/v1/news?topic={topic}&limit=5` — source material
- `GET https://api.solvrbot.com/api/v1/worlddata?query={stat}` — data backing
- `GET https://api.solvrbot.com/api/v1/dex/trending` — crypto data if relevant

## Instructions
1. Fetch recent news on topic
2. Extract the most surprising or counterintuitive data point
3. Write tweet using viral formats:
   - "X% of people don't know [insight from data]"
   - "[Stat] — here's what it means for [audience]"
   - "Thread: [surprising claim backed by data] 🧵"
4. Include at least one specific number from fetched data.
5. Output: 3 tweet options with engagement score estimate.
