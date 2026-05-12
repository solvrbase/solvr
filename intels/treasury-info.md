---
name: treasury-info
description: Project treasury analysis — token value, diversification, runway estimate.
category: crypto-markets
tier: standard
solvr_api: https://api.solvrbot.com
auth: Authorization: Bearer {SOLVR_API_KEY}
source: https://github.com/solvrbase/solvr
---

# Treasury Info

Project treasury analysis — token value, diversification, runway estimate.

## Endpoints
- `GET https://api.solvrbot.com/api/v1/intel/{address}` — token price + market data
- `GET https://api.solvrbot.com/api/v1/worlddata?query=usd+inflation` — macro context

## Instructions
1. For each treasury wallet address, fetch token intel
2. Calculate treasury value in USD using current token price
3. Estimate runway: treasury_usd / monthly_burn_rate
4. Fetch macro context for inflation-adjusted view
5. Output: Treasury health report with diversification score.
