---
name: dev-digest
description: Daily AI/dev community digest — trending tools, models, and repos.
category: research-content
tier: free
solvr_api: https://api.solvrbot.com
auth: Authorization: Bearer {SOLVR_API_KEY}
source: https://github.com/solvrbase/solvr
---

# Dev Digest

Daily AI/dev community digest — trending tools, models, and repos.

## Endpoints
- `GET https://api.solvrbot.com/api/v1/news?topic=AI+coding+LLM+agent&category=tech&limit=10` — AI dev news
- `GET https://api.solvrbot.com/api/v1/github/trending?topic=ai&since=daily&limit=10` — trending AI repos

## Instructions
1. Fetch AI dev news: `GET https://api.solvrbot.com/api/v1/news?topic=AI+agent+LLM+coding&limit=10`
2. Fetch trending AI repos: `GET https://api.solvrbot.com/api/v1/github/trending?topic=ai&since=daily&limit=10`
3. Highlight: new models, tools, frameworks, or techniques
4. Format: concise bullets with repo links and star counts.
