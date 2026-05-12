---
name: telegram-digest
description: Crypto Telegram community digest via news + on-chain data proxy.
category: research-content
tier: free
solvr_api: https://api.solvrbot.com
auth: Authorization: Bearer {SOLVR_API_KEY}
source: https://github.com/solvrbase/solvr
---

# Telegram Digest

Crypto Telegram community digest via news + on-chain data proxy.

## Endpoints
- `GET https://api.solvrbot.com/api/v1/news?topic=crypto&category=tech&limit=10` — crypto news
- `GET https://api.solvrbot.com/api/v1/dex/trending` — what's being talked about on-chain

## Instructions
1. Fetch top crypto news: `GET https://api.solvrbot.com/api/v1/news?topic=crypto+token+launch&limit=10`
2. Fetch trending tokens for on-chain context
3. Identify top 3 topics being discussed (price action, new launches, narratives)
4. Format: Telegram-style digest with bold headers, concise bullets.
