---
name: push-recap
description: Generate a push recap — what changed, why it matters.
category: dev-code
tier: free
solvr_api: https://api.solvrbot.com
auth: Authorization: Bearer {SOLVR_API_KEY}
source: https://github.com/solvrbase/solvr
---

# Push Recap

Generate a push recap — what changed, why it matters.

## Endpoints
- `GET https://api.solvrbot.com/api/v1/github/trending?topic={project}&since=daily` — activity check
- `GET https://api.solvrbot.com/api/v1/news?topic={project}+update&limit=3` — announcement context

## Instructions
1. Summarize the changes in this push (provided as input)
2. Fetch context: is this part of a bigger initiative? Check news.
3. Assess impact:
   - User-facing changes
   - Performance impact
   - Security impact
   - Breaking changes
4. Output: Push recap in 3 bullet points + impact rating.
