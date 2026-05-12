---
name: github-trending
description: Daily GitHub trending repositories digest by language and topic.
category: dev-code
tier: free
solvr_api: https://api.solvrbot.com
auth: Authorization: Bearer {SOLVR_API_KEY}
source: https://github.com/solvrbase/solvr
---

# Github Trending

Daily GitHub trending repositories digest by language and topic.

## Endpoints
- `GET https://api.solvrbot.com/api/v1/github/trending?since=daily&limit=25` — daily trending repos
- `GET https://api.solvrbot.com/api/v1/github/trending?language={lang}&since=daily` — by language

## Instructions
1. Fetch daily trending: `GET https://api.solvrbot.com/api/v1/github/trending?since=daily&limit=25`
2. Group by language
3. Highlight AI/ML, crypto/Web3, and developer tools categories
4. Format:

```
⭐ GITHUB TRENDING TODAY
🤖 AI/ML
1. org/repo — Python — 342 stars — [description]
...
🔗 WEB3
1. org/repo — TypeScript — 189 stars — [description]
```
