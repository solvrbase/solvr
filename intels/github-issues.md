---
name: github-issues
description: Surface high-priority open issues from tracked repositories.
category: dev-code
tier: free
solvr_api: https://api.solvrbot.com
auth: Authorization: Bearer {SOLVR_API_KEY}
source: https://github.com/solvrbase/solvr
---

# Github Issues

Surface high-priority open issues from tracked repositories.

## Endpoints
- `GET https://api.solvrbot.com/api/v1/github/trending?topic={repo_topic}` — find repos
- `GET https://api.solvrbot.com/api/v1/news?topic={repo_name}+issue+bug` — issue news

## Instructions
1. Fetch trending repos in target domain: `GET https://api.solvrbot.com/api/v1/github/trending?topic=DOMAIN`
2. For each repo, search for news about known issues: `GET https://api.solvrbot.com/api/v1/news?topic=REPO+issue`
3. Identify high-visibility issues (mentioned in news, affecting users)
4. Output: Issue triage list with severity and context.
