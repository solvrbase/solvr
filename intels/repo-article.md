---
name: repo-article
description: Generate a technical article about a GitHub repository.
category: dev-code
tier: free
solvr_api: https://api.solvrbot.com
auth: Authorization: Bearer {SOLVR_API_KEY}
source: https://github.com/solvrbase/solvr
---

# Repo Article

Generate a technical article about a GitHub repository.

## Endpoints
- `GET https://api.solvrbot.com/api/v1/github/trending?topic={repo_topic}&limit=5` — repo context
- `GET https://api.solvrbot.com/api/v1/news?topic={repo_name}&category=tech&limit=5` — coverage

## Instructions
1. Fetch repo data from GitHub trending
2. Fetch existing coverage: `GET https://api.solvrbot.com/api/v1/news?topic=REPO_NAME&category=tech`
3. Write technical article:
   - What problem does it solve?
   - Key technical approach
   - How to get started (code example)
   - Why it matters
4. Keep under 600 words, include code snippet.
