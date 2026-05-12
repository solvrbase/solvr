---
name: update-gallery
description: Update the Solvr intel gallery with new intels and usage stats.
category: meta-agent
tier: free
solvr_api: https://api.solvrbot.com
auth: Authorization: Bearer {SOLVR_API_KEY}
source: https://github.com/solvrbase/solvr
---

# Update Gallery

Update the Solvr intel gallery with new intels and usage stats.

## Endpoints
- `GET https://api.solvrbot.com/api/v1/catalog` — current API state
- `GET https://api.solvrbot.com/api/v1/github/trending?topic=solvr&since=weekly` — community intels

## Instructions
1. Fetch current API catalog to ensure all endpoints documented
2. Check GitHub for community-contributed intels
3. Generate gallery update:
   - New intels added this week
   - Updated intels
   - Usage highlights (most-used intels)
4. Output: Gallery update manifest ready for publishing.
