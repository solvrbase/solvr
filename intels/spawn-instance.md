---
name: spawn-instance
description: Spawn a new agent instance with specific intels and configuration.
category: dev-code
tier: free
solvr_api: https://api.solvrbot.com
auth: Authorization: Bearer {SOLVR_API_KEY}
source: https://github.com/solvrbase/solvr
---

# Spawn Instance

Spawn a new agent instance with specific intels and configuration.

## Endpoints
- `GET https://api.solvrbot.com/api/v1/catalog` — verify endpoint availability

## Instructions
1. Define agent role and required intels
2. Fetch catalog to verify all required endpoints are available for target tier
3. Generate agent configuration:
   - Intel list
   - API key (from Solvr registration)
   - Schedule/triggers
   - Notification channels
4. Output: Agent config file ready for deployment.
