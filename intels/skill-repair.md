---
name: skill-repair
description: Auto-repair broken skills by diagnosing root cause and applying fixes.
category: meta-agent
tier: free
solvr_api: https://api.solvrbot.com
auth: Authorization: Bearer {SOLVR_API_KEY}
source: https://github.com/solvrbase/solvr
---

# Skill Repair

Auto-repair broken skills by diagnosing root cause and applying fixes.

## Endpoints
- `GET https://api.solvrbot.com/api/v1/catalog` — verify endpoint availability
- `GET https://api.solvrbot.com/api/v1/news?topic=API+change+deprecation&category=tech` — API changes

## Instructions
1. For failing skill, fetch error from log
2. Diagnose root cause:
   - `HTTP 404`: endpoint moved — check catalog for new path
   - `HTTP 403`: tier insufficient — check catalog for tier requirement
   - `HTTP 429`: rate limited — add backoff
   - `HTTP 5xx`: upstream issue — add retry with exponential backoff
3. Apply fix and re-test
4. Log repair action to memory.
