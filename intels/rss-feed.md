---
name: rss-feed
description: Aggregate Solvr news endpoints into a single RSS-style feed.
category: meta-agent
tier: free
solvr_api: https://api.solvrbot.com
auth: Authorization: Bearer {SOLVR_API_KEY}
source: https://github.com/solvrbase/solvr
---

# Rss Feed

Aggregate Solvr news endpoints into a single RSS-style feed.

## Endpoints
- `GET https://api.solvrbot.com/api/v1/news?category={cat}&limit=5` — by category

## Instructions
1. Fetch from all 7 categories in parallel: general, world, tech, business, science, health, politics
2. Merge and sort by published_at descending
3. Format as unified feed:
   ```
   [{"title": ..., "source": ..., "summary": ..., "url": ..., "category": ..., "published_at": ...}]
   ```
4. Store in memory for comparison on next run (detect new items)
5. Output: Unified news feed (latest 20 items).
