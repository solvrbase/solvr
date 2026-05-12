---
name: changelog
description: Auto-generate changelogs from development activity and news.
category: dev-code
tier: free
solvr_api: https://api.solvrbot.com
auth: Authorization: Bearer {SOLVR_API_KEY}
source: https://github.com/solvrbase/solvr
---

# Changelog

Auto-generate changelogs from development activity and news.

## Endpoints
- `GET https://api.solvrbot.com/api/v1/github/trending?topic={project}` — project activity
- `GET https://api.solvrbot.com/api/v1/news?topic={project}+update+release` — release news

## Instructions
1. Fetch project activity: `GET https://api.solvrbot.com/api/v1/github/trending?topic=PROJECT&since=weekly`
2. Fetch release news: `GET https://api.solvrbot.com/api/v1/news?topic=PROJECT+update&limit=5`
3. Generate changelog structure:
   - ## [Version] - YYYY-MM-DD
   - ### Added
   - ### Changed
   - ### Fixed
4. Write in Keep a Changelog format.
