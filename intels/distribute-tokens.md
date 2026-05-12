---
name: distribute-tokens
description: Analyze token holder distribution and concentration risk.
category: crypto-markets
tier: standard
solvr_api: https://api.solvrbot.com
auth: Authorization: Bearer {SOLVR_API_KEY}
source: https://github.com/solvrbase/solvr
---

# Distribute Tokens

Analyze token holder distribution and concentration risk.

## Endpoints
- `GET https://api.solvrbot.com/api/v1/intel/{address}` — holder count + security
- `POST https://api.solvrbot.com/api/v1/security/scan` — full security + distribution data

## Instructions
1. Fetch intel: `GET https://api.solvrbot.com/api/v1/intel/{address}`
2. Run security scan: `POST https://api.solvrbot.com/api/v1/security/scan`
3. Analyze distribution:
   - Holder count < 100: EXTREME RISK
   - Holder count 100-500: HIGH RISK
   - Holder count 500-2000: MODERATE
   - Holder count > 2000: HEALTHY
4. Check GoPlus top holder concentration
5. Output: Distribution report with risk rating.
