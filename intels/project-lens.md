---
name: project-lens
description: Analyze any project from multiple angles — tech, community, market.
category: dev-code
tier: free
solvr_api: https://api.solvrbot.com
auth: Authorization: Bearer {SOLVR_API_KEY}
source: https://github.com/solvrbase/solvr
---

# Project Lens

Analyze any project from multiple angles — tech, community, market.

## Endpoints
- `GET https://api.solvrbot.com/api/v1/news?topic={project}&limit=10` — project news
- `GET https://api.solvrbot.com/api/v1/github/trending?topic={project}&limit=5` — GitHub activity
- `GET https://api.solvrbot.com/api/v1/dex/search?q={project}` — token/market data (if applicable)

## Instructions
1. Fetch project news: 10 recent articles
2. Fetch GitHub activity for the project repos
3. If project has a token, fetch market data
4. Analyze across 4 lenses:
   - Technical: code quality, activity, architecture
   - Community: growth, sentiment, engagement
   - Market: token performance if applicable
   - Competitive: positioning vs alternatives
5. Output: Project analysis report (500 words).
