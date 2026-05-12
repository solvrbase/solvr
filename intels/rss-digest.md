---
name: rss-digest
description: Multi-source news aggregator digest powered by Solvr.
category: research-content
tier: free
solvr_api: https://api.solvrbot.com
auth: Authorization: Bearer {SOLVR_API_KEY}
source: https://github.com/solvrbase/solvr
---

# Rss Digest

Multi-source news aggregator digest powered by Solvr.

## Endpoints
- `GET https://api.solvrbot.com/api/v1/news?category={cat}&limit=5` — news by category

## Instructions
1. Fetch from all categories in parallel:
   - general, world, tech, business, science, health, politics
2. Combine all articles (max 35 total)
3. Score by recency (last 6h = +3, last 24h = +2, older = +1)
4. Deduplicate similar stories
5. Output top 15 stories across all categories with sources.
