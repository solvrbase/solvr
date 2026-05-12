---
name: repo-pulse
description: Repository health pulse — activity, community, and momentum check.
category: dev-code
tier: free
solvr_api: https://api.solvrbot.com
auth: Authorization: Bearer {SOLVR_API_KEY}
source: https://github.com/solvrbase/solvr
---

# Repo Pulse

Repository health pulse — activity, community, and momentum check.

## Endpoints
- `GET https://api.solvrbot.com/api/v1/github/trending?topic={repo_topic}&since=weekly` — weekly pulse
- `GET https://api.solvrbot.com/api/v1/news?topic={repo_name}&limit=5` — community signal

## Instructions
1. Check if repo appears in weekly trending (strong signal)
2. Fetch news mentions for community activity
3. Pulse metrics:
   - Code activity: in trending? star velocity?
   - Community: news mentions, discussions
   - Momentum: weekly vs monthly trending comparison
4. Output: HEALTHY / GROWING / STABLE / DECLINING with evidence.
