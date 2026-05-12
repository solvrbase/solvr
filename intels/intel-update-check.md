---
name: intel-update-check
description: Check for intel updates from the Solvr repository.
category: meta-agent
tier: free
solvr_api: https://api.solvrbot.com
auth: Authorization: Bearer {SOLVR_API_KEY}
source: https://github.com/solvrbase/solvr
---

# Intel Update Check

Check for intel updates from the Solvr repository.

## Endpoints
- `GET https://api.solvrbot.com/api/v1/github/trending?topic=solvr+intel+agent&since=weekly` — repo updates
- `GET https://api.solvrbot.com/api/v1/news?topic=Solvr+Intelligence+API+update&limit=5` — API updates

## Instructions
1. Check GitHub for Solvr repo activity (new intels, updates)
2. Check news for Solvr API updates (new endpoints, breaking changes)
3. Compare installed intels vs available intels
4. Identify: new intels to install, intels with updates, deprecated intels
5. Output: Update manifest with available upgrades.
