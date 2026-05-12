---
name: narrative-tracker
description: Track emerging crypto narratives by monitoring news + trending tokens.
category: crypto-markets
tier: free
solvr_api: https://api.solvrbot.com
auth: Authorization: Bearer {SOLVR_API_KEY}
source: https://github.com/solvrbase/solvr
---

# Narrative Tracker

Track emerging crypto narratives by monitoring news + trending tokens.

## Endpoints
- `GET https://api.solvrbot.com/api/v1/news?topic={narrative}` — news by topic
- `GET https://api.solvrbot.com/api/v1/dex/trending` — trending tokens

## Instructions
1. Define narratives to track: AI, RWA, DePIN, L2, memecoins, gaming, etc.
2. For each narrative, fetch news: `GET https://api.solvrbot.com/api/v1/news?topic=AI+crypto&limit=5`
3. Fetch trending tokens and tag them by narrative keywords in name/description
4. Score each narrative: news volume + trending token count
5. Output: Narrative heatmap ranked by momentum score.

```
🔥 NARRATIVE TRACKER
1. AI Agents    ██████████ 9/10 (12 news, 8 trending tokens)
2. RWA          ███████░░░ 7/10 (8 news, 5 trending tokens)
3. DePIN        █████░░░░░ 5/10 (6 news, 3 trending tokens)
```
