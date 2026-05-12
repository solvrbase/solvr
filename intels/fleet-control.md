---
name: fleet-control
description: Coordinate multiple Solvr agents — dispatch, monitor, and aggregate results.
category: dev-code
tier: free
solvr_api: https://api.solvrbot.com
auth: Authorization: Bearer {SOLVR_API_KEY}
source: https://github.com/solvrbase/solvr
---

# Fleet Control

Coordinate multiple Solvr agents — dispatch, monitor, and aggregate results.

## Endpoints
- `GET https://api.solvrbot.com/api/v1/catalog` — available endpoints and your tier status

## Instructions
1. Fetch catalog to confirm available endpoints: `GET https://api.solvrbot.com/api/v1/catalog`
2. Define fleet mission (e.g., monitor 20 tokens simultaneously)
3. Shard work across agents:
   - Agent 1: tokens 1-5
   - Agent 2: tokens 6-10
   - etc.
4. Define aggregation logic for results
5. Output: Fleet dispatch plan with coordination instructions.
