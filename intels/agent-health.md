---
name: agent-health
description: Full agent fleet health check — connectivity, performance, and cost.
category: meta-agent
tier: free
solvr_api: https://api.solvrbot.com
auth: Authorization: Bearer {SOLVR_API_KEY}
source: https://github.com/solvrbase/solvr
---

# Agent Health

Full agent fleet health check — connectivity, performance, and cost.

## Endpoints
- `GET https://api.solvrbot.com/api/v1/catalog` — API status
- `GET https://api.solvrbot.com/api/v1/news?limit=1` — connectivity
- `GET https://api.solvrbot.com/api/v1/dex/trending` — data freshness

## Instructions
1. Run parallel health checks on all Solvr endpoints
2. Check rate limit status: current usage vs daily limit
3. Calculate fleet cost estimate: calls × price per call × 30 days
4. Check data freshness: are news/market data within expected cache TTL?
5. Output: Full fleet health report with traffic light status (🟢/🟡/🔴).
