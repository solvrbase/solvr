---
name: unlock-monitor
description: Monitor upcoming token unlocks and assess sell pressure risk.
category: crypto-markets
tier: standard
solvr_api: https://api.solvrbot.com
auth: Authorization: Bearer {SOLVR_API_KEY}
source: https://github.com/solvrbase/solvr
---

# Unlock Monitor

Monitor upcoming token unlocks and assess sell pressure risk.

## Endpoints
- `GET https://api.solvrbot.com/api/v1/intel/{address}` — token intel
- `GET https://api.solvrbot.com/api/v1/news?topic={token}+unlock` — unlock news

## Instructions
1. For watched tokens, fetch intel: `GET https://api.solvrbot.com/api/v1/intel/{address}`
2. Search for unlock news: `GET https://api.solvrbot.com/api/v1/news?topic=TOKEN+unlock+vesting`
3. Assess unlock risk:
   - Unlock > 10% of supply: HIGH RISK
   - Unlock 5-10%: MODERATE
   - Unlock < 5%: LOW RISK
4. Alert 7 days and 1 day before known unlock dates.
5. Output: Unlock calendar with risk ratings.
