---
name: paper-digest
description: Research paper digest — latest findings from science, AI, and tech.
category: research-content
tier: free
solvr_api: https://api.solvrbot.com
auth: Authorization: Bearer {SOLVR_API_KEY}
source: https://github.com/solvrbase/solvr
---

# Paper Digest

Research paper digest — latest findings from science, AI, and tech.

## Endpoints
- `GET https://api.solvrbot.com/api/v1/news?category=science&limit=10` — science news
- `GET https://api.solvrbot.com/api/v1/news?topic=AI+research+paper&limit=5` — AI research

## Instructions
1. Fetch science news: `GET https://api.solvrbot.com/api/v1/news?category=science&limit=10`
2. Fetch AI research: `GET https://api.solvrbot.com/api/v1/news?topic=AI+research+paper&limit=5`
3. Filter for papers/studies (look for "study", "research", "paper", "findings" keywords)
4. For each paper: extract claim, method, and implication
5. Output: top 5 papers with 2-sentence summary each.
