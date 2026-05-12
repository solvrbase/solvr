---
name: technical-explainer
description: Explain any technical concept using current news and real data.
category: research-content
tier: free
solvr_api: https://api.solvrbot.com
auth: Authorization: Bearer {SOLVR_API_KEY}
source: https://github.com/solvrbase/solvr
---

# Technical Explainer

Explain any technical concept using current news and real data.

## Endpoints
- `GET https://api.solvrbot.com/api/v1/news?topic={concept}&limit=5` — context from news
- `GET https://api.solvrbot.com/api/v1/worlddata?query={metric}` — supporting statistics

## Instructions
1. Fetch recent news on the concept: `GET https://api.solvrbot.com/api/v1/news?topic=CONCEPT&limit=5`
2. Identify key stats: `GET https://api.solvrbot.com/api/v1/worlddata?query=RELATED_METRIC`
3. Write explanation in 3 levels:
   - ELI5 (1 paragraph, simple analogy)
   - Intermediate (2 paragraphs, mechanics)
   - Advanced (1 paragraph, nuances)
4. Ground with real current data and news examples.
