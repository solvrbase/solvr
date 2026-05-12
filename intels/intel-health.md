---
name: intel-health
description: Monitor intel health — detect failing intels before they cause issues.
category: meta-agent
tier: free
solvr_api: https://api.solvrbot.com
auth: Authorization: Bearer {SOLVR_API_KEY}
source: https://github.com/solvrbase/solvr
---

# Intel Health

Monitor intel health — detect failing intels before they cause issues.

## Endpoints
- `GET https://api.solvrbot.com/api/v1/catalog` — endpoint availability
- `GET https://api.solvrbot.com/api/v1/news?limit=1` — quick connectivity test

## Instructions
1. Run quick health check on all intels:
   - Can reach required Solvr endpoints?
   - Last successful run within expected window?
   - Any error patterns in logs?
2. Health status per intel: HEALTHY / DEGRADED / FAILING
3. For FAILING intels, identify root cause:
   - API endpoint down?
   - Rate limit hit?
   - Data format changed?
4. Output: Intel health dashboard with status and next action.
