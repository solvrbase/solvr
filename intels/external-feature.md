---
name: external-feature
description: Research and integrate external APIs or features into your agent.
category: dev-code
tier: free
solvr_api: https://api.solvrbot.com
auth: Authorization: Bearer {SOLVR_API_KEY}
source: https://github.com/solvrbase/solvr
---

# External Feature

Research and integrate external APIs or features into your agent.

## Endpoints
- `GET https://api.solvrbot.com/api/v1/news?topic={api_name}+API&category=tech` — API news
- `GET https://api.solvrbot.com/api/v1/github/trending?topic={api_name}&limit=5` — API libraries

## Instructions
1. Research the external API: fetch news + GitHub libraries
2. Identify best integration approach:
   - Official SDK vs direct HTTP
   - Authentication method
   - Rate limits
3. Check for known issues: `GET https://api.solvrbot.com/api/v1/news?topic=API_NAME+outage+bug`
4. Output: Integration guide with code examples.
