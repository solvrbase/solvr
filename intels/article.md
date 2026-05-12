---
name: article
description: Generate a well-researched article on any topic using live data.
category: research-content
tier: free
solvr_api: https://api.solvrbot.com
auth: Authorization: Bearer {SOLVR_API_KEY}
source: https://github.com/solvrbase/solvr
---

# Article

Generate a well-researched article on any topic using live data.

## Endpoints
- `GET https://api.solvrbot.com/api/v1/news?topic={topic}&limit=10` — source material
- `GET https://api.solvrbot.com/api/v1/worlddata?query={metric}` — supporting statistics

## Instructions
1. Fetch 10 recent articles on topic
2. Extract key facts, quotes, and data points
3. Fetch 2-3 supporting statistics from worlddata
4. Write article structure:
   - Hook (1 paragraph)
   - Background (2 paragraphs)
   - Current developments (3 paragraphs)
   - Analysis (2 paragraphs)
   - Conclusion (1 paragraph)
5. Include inline citations to source articles.
