---
name: paper-pick
description: Pick the single most important research paper or study of the day.
category: research-content
tier: free
solvr_api: https://api.solvrbot.com
auth: Authorization: Bearer {SOLVR_API_KEY}
source: https://github.com/solvrbase/solvr
---

# Paper Pick

Pick the single most important research paper or study of the day.

## Endpoints
- `GET https://api.solvrbot.com/api/v1/news?category=science&limit=10` — science news
- `GET https://api.solvrbot.com/api/v1/news?topic=breakthrough+discovery&limit=5` — breakthrough news

## Instructions
1. Fetch science/research news from multiple queries
2. Score each paper/study:
   - Impact: Does it change current understanding? (+3)
   - Applicability: Can it be acted on? (+2)
   - Novelty: Is it genuinely new? (+2)
   - Credibility: Peer-reviewed, major institution? (+3)
3. Pick highest-scoring paper
4. Write 200-word explainer: what, why it matters, what to watch next.
