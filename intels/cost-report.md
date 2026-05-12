---
name: cost-report
description: API usage and cost report — track endpoint usage, tier status, and spend.
category: meta-agent
tier: free
solvr_api: https://api.solvrbot.com
auth: Authorization: Bearer {SOLVR_API_KEY}
source: https://github.com/solvrbase/solvr
---

# Cost Report

API usage and cost report — track endpoint usage, tier status, and spend.

## Endpoints
- `GET https://api.solvrbot.com/api/v1/catalog` — tier status and limits

## Instructions
1. Fetch your current tier status: `GET https://api.solvrbot.com/api/v1/catalog`
2. Log all API calls made in this session to memory
3. Calculate:
   - Calls per endpoint
   - Daily usage vs limit
   - Estimated monthly cost at current rate
4. Alert if > 80% of daily limit consumed
5. Output: Usage report with cost estimate and optimization suggestions.
