---
name: defi-monitor
description: Track DeFi pool health — TVL, volume, liquidity ratio for watched tokens.
category: crypto-markets
tier: standard
solvr_api: https://api.solvrbot.com
auth: Authorization: Bearer {SOLVR_API_KEY}
source: https://github.com/solvrbase/solvr
---

# Defi Monitor

Track DeFi pool health — TVL, volume, liquidity ratio for watched tokens.

## Endpoints
- `GET https://api.solvrbot.com/api/v1/dex/analytics?q={symbol}` — multi-timeframe analytics
- `GET https://api.solvrbot.com/api/v1/intel/{address}` — token intel with liquidity data

## Instructions
1. For each watched DeFi position, fetch analytics: `GET https://api.solvrbot.com/api/v1/dex/analytics?q=SYMBOL`
2. Fetch token intel for liquidity: `GET https://api.solvrbot.com/api/v1/intel/{address}`
3. Calculate:
   - Liquidity/MCap ratio (healthy: >10%)
   - Volume/Liquidity ratio (active: >5%)
   - 24h volume trend
4. Alert if liquidity ratio < 5% or drops > 15% vs prior check.
5. Output: Pool health table with TVL, APR estimate, risk level.
