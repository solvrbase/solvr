---
name: research-brief
description: Quick research brief (< 300 words) on any topic.
category: research-content
tier: free
solvr_api: https://api.solvrbot.com
auth: Authorization: Bearer {SOLVR_API_KEY}
source: https://github.com/solvrbase/solvr
---

# Research Brief

Quick research brief (< 300 words) on any topic.

## Endpoints
- `GET https://api.solvrbot.com/api/v1/news?topic={query}&limit=5` — recent news
- `GET https://api.solvrbot.com/api/v1/worlddata?query={metric}` — supporting data

## Instructions
1. Fetch 5 recent articles on topic: `GET https://api.solvrbot.com/api/v1/news?topic=QUERY&limit=5`
2. Extract key facts, numbers, and developments
3. Write 3-paragraph brief:
   - What is it? (context)
   - What's happening now? (news)
   - Why does it matter? (implications)
4. Add 3 key stats from worlddata if relevant.
5. Keep under 300 words.
