---
name: github-monitor
description: Monitor specific GitHub repositories for new activity — stars, issues, releases.
category: dev-code
tier: free
solvr_api: https://api.solvrbot.com
auth: Authorization: Bearer {SOLVR_API_KEY}
source: https://github.com/solvrbase/solvr
---

# Github Monitor

Monitor specific GitHub repositories for new activity — stars, issues, releases.

## Endpoints
- `GET https://api.solvrbot.com/api/v1/github/trending?topic={repo_topic}&limit=10` — repo activity

## Instructions
1. Fetch repos matching watched topics: `GET https://api.solvrbot.com/api/v1/github/trending?topic=TOPIC&since=daily`
2. For watched repos, check if they appear in trending (indicates new activity)
3. Alert on: new appearance in trending, star spike (> 100 new stars)
4. Cross-reference with tech news: `GET https://api.solvrbot.com/api/v1/news?topic=REPO_NAME&limit=3`
5. Output: Monitor report with activity summary for each watched repo.
