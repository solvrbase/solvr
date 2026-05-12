---
name: on-chain-monitor
description: Monitor token contracts for significant on-chain activity and security changes.
category: crypto-markets
tier: standard
solvr_api: https://api.solvrbot.com
auth: Authorization: Bearer {SOLVR_API_KEY}
source: https://github.com/solvrbase/solvr
---

# On Chain Monitor

Monitor token contracts for significant on-chain activity and security changes.

## Endpoints
- `GET https://api.solvrbot.com/api/v1/intel/{address}` — token intelligence
- `POST https://api.solvrbot.com/api/v1/security/scan` — security scan

## Instructions
1. For each watched address, fetch intel: `GET https://api.solvrbot.com/api/v1/intel/{address}`
2. Run security scan: `POST https://api.solvrbot.com/api/v1/security/scan`
3. Alert on:
   - New security flags added
   - Holder count drop > 10%
   - Liquidity drop > 20%
   - Risk score increase > 15 points since last check
4. Log state to memory for comparison on next run.
5. Format: `🔴 ALERT: $TOKEN — liquidity dropped 35% | New flag: sell_tax_modified`
