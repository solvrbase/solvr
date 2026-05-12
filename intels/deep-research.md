---
name: deep-research
description: Deep research on any topic using news + world data + context synthesis.
category: research-content
tier: free
solvr_api: https://api.solvrbot.com
auth: Authorization: Bearer {SOLVR_API_KEY}
source: https://github.com/solvrbase/solvr
---

# Deep Research

Deep research on any topic using news + world data + context synthesis.

## Endpoints
- `GET https://api.solvrbot.com/api/v1/news?topic={query}&limit=10` — topic news
- `GET https://api.solvrbot.com/api/v1/worlddata?query={indicator}` — data context

## Instructions
1. Fetch all recent news on topic: `GET https://api.solvrbot.com/api/v1/news?topic=QUERY&limit=10`
2. Identify key themes, claims, and data points from articles
3. For any quantitative claims, verify with worlddata: `GET https://api.solvrbot.com/api/v1/worlddata?query=INDICATOR`
4. Synthesize findings into structured research brief:
   - Background
   - Current state
   - Key developments
   - Data points
   - Outlook
5. Cite sources from article URLs.
