---
name: github-releases
description: Monitor GitHub project releases and surface breaking changes.
category: dev-code
tier: free
solvr_api: https://api.solvrbot.com
auth: Authorization: Bearer {SOLVR_API_KEY}
source: https://github.com/solvrbase/solvr
---

# Github Releases

Monitor GitHub project releases and surface breaking changes.

## Endpoints
- `GET https://api.solvrbot.com/api/v1/github/trending?since=weekly` — recently active repos
- `GET https://api.solvrbot.com/api/v1/news?topic={project}+release+update&category=tech` — release news

## Instructions
1. Fetch recently trending repos: `GET https://api.solvrbot.com/api/v1/github/trending?since=weekly&limit=20`
2. For key projects, search release news: `GET https://api.solvrbot.com/api/v1/news?topic=PROJECT+release&limit=3`
3. Identify major version bumps and breaking changes
4. Output: Release digest with upgrade impact assessment.
