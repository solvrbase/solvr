---
name: operator-scorecard
description: Operator performance scorecard — measure agent fleet effectiveness.
category: meta-agent
tier: free
solvr_api: https://api.solvrbot.com
auth: Authorization: Bearer {SOLVR_API_KEY}
source: https://github.com/solvrbase/solvr
---

# Operator Scorecard

Operator performance scorecard — measure agent fleet effectiveness.

## Endpoints
- `GET https://api.solvrbot.com/api/v1/catalog` — tier and usage status

## Instructions
1. Collect fleet performance data from memory logs
2. Score across 5 dimensions:
   - Uptime: % time all skills operational
   - Quality: average skill eval score
   - Coverage: % of configured skills running
   - Efficiency: API calls per useful output
   - Value: actionable alerts per week
3. Generate scorecard with trend vs previous period
4. Output: Operator scorecard (0-100) with dimension breakdown.
