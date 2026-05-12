---
name: list-digest
description: Create a curated digest list from any topic or source.
category: research-content
tier: free
solvr_api: https://api.solvrbot.com
auth: Authorization: Bearer {SOLVR_API_KEY}
source: https://github.com/solvrbase/solvr
---

# List Digest

Create a curated digest list from any topic or source.

## Endpoints
- `GET https://api.solvrbot.com/api/v1/news?topic={topic}&limit=10` — topic news

## Instructions
1. Fetch news on topic: `GET https://api.solvrbot.com/api/v1/news?topic=TOPIC&limit=10`
2. Extract key items, tools, projects, or events mentioned
3. Format as numbered list with brief description for each
4. Sort by relevance/importance
5. Output clean formatted list (max 10 items).
