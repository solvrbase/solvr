---
name: heartbeat
description: Agent health check — verify all required endpoints are reachable.
category: meta-agent
tier: free
solvr_api: https://api.solvrbot.com
auth: Authorization: Bearer {SOLVR_API_KEY}
source: https://github.com/solvrbase/solvr
---

# Heartbeat

Agent health check — verify all required endpoints are reachable.

## Endpoints
- `GET https://api.solvrbot.com/api/v1/catalog` — connectivity check
- `GET https://api.solvrbot.com/api/v1/news?limit=1` — news endpoint check
- `GET https://api.solvrbot.com/api/v1/dex/trending` — DEX endpoint check

## Instructions
1. Ping each required endpoint with a minimal request
2. Record: status code, response time, any errors
3. Health thresholds:
   - < 500ms: HEALTHY
   - 500ms-2s: DEGRADED
   - > 2s or error: DOWN
4. Alert if any endpoint is DOWN or DEGRADED
5. Output: Health report with status for each endpoint.
