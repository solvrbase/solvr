---
name: autoresearch
description: Auto-research solutions to technical problems using news and GitHub.
category: dev-code
tier: free
solvr_api: https://api.solvrbot.com
auth: Authorization: Bearer {SOLVR_API_KEY}
source: https://github.com/solvrbase/solvr
---

# Autoresearch

Auto-research solutions to technical problems using news and GitHub.

## Endpoints
- `GET https://api.solvrbot.com/api/v1/news?topic={problem}&category=tech&limit=10` — tech solutions
- `GET https://api.solvrbot.com/api/v1/github/trending?topic={keyword}&limit=10` — relevant repos

## Instructions
1. Parse the technical problem into search keywords
2. Fetch tech news on the problem: `GET https://api.solvrbot.com/api/v1/news?topic=PROBLEM&category=tech&limit=10`
3. Fetch relevant repos: `GET https://api.solvrbot.com/api/v1/github/trending?topic=KEYWORD&limit=10`
4. Synthesize solutions:
   - Top 3 approaches from news/articles
   - Top 3 relevant open-source tools/repos
5. Output: Solution brief with pros/cons of each approach.
