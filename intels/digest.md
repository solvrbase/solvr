---
name: digest
description: Daily news digest — top headlines across categories with brief summaries.
category: research-content
tier: free
solvr_api: https://api.solvrbot.com
auth: Authorization: Bearer {SOLVR_API_KEY}
source: https://github.com/solvrbase/solvr
---

# Digest

Daily news digest — top headlines across categories with brief summaries.

## Endpoints
- `GET https://api.solvrbot.com/api/v1/news?category={category}&limit=10` — headlines by category

## Instructions
1. Fetch headlines for each category in parallel:
   - `GET https://api.solvrbot.com/api/v1/news?category=general&limit=5`
   - `GET https://api.solvrbot.com/api/v1/news?category=tech&limit=5`
   - `GET https://api.solvrbot.com/api/v1/news?category=business&limit=5`
2. Deduplicate by headline similarity
3. Select top 10 most important stories
4. Write 1-sentence summary for each
5. Output formatted digest with sections by category.
