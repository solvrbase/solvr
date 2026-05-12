---
name: fargester-digest
description: Farcaster community digest — trending casts and channel highlights.
category: social-writing
tier: free
solvr_api: https://api.solvrbot.com
auth: Authorization: Bearer {SOLVR_API_KEY}
source: https://github.com/solvrbase/solvr
---

# Fargester Digest

Farcaster community digest — trending casts and channel highlights.

## Endpoints
- `GET https://api.solvrbot.com/api/v1/farcaster?limit=10` — trending casts
- `GET https://api.solvrbot.com/api/v1/farcaster?channel=crypto&limit=10` — crypto channel

## Instructions
1. Fetch trending casts: `GET https://api.solvrbot.com/api/v1/farcaster?limit=10`
2. Fetch crypto channel: `GET https://api.solvrbot.com/api/v1/farcaster?channel=crypto&limit=10`
3. Identify top themes and viral content
4. Format as Farcaster-style digest with engagement metrics.

```
🟣 FARCASTER DIGEST
🔥 TRENDING
1. @user: "[cast text]" — 234 reactions, 45 recasts
...
```
