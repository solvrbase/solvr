---
name: contributor-spotlight
description: Spotlight top contributors to the Solvr ecosystem.
category: meta-agent
tier: free
solvr_api: https://api.solvrbot.com
auth: Authorization: Bearer {SOLVR_API_KEY}
source: https://github.com/solvrbase/solvr
---

# Contributor Spotlight

Spotlight top contributors to the Solvr ecosystem.

## Endpoints
- `GET https://api.solvrbot.com/api/v1/github/trending?topic=solvr+agent+intel&since=weekly` — community contributions
- `GET https://api.solvrbot.com/api/v1/news?topic=Solvr+ecosystem+builder&limit=5` — ecosystem news

## Instructions
1. Fetch GitHub activity for Solvr contributors
2. Fetch ecosystem news mentions
3. Identify top contributors:
   - New intels contributed
   - Issues resolved
   - Community engagement
4. Write spotlight feature for top 3 contributors
5. Output: Contributor spotlight ready for publication.
