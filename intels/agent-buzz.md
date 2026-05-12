---
name: agent-buzz
description: Track buzz around AI agent ecosystem — what agents and protocols are trending.
category: social-writing
tier: free
solvr_api: https://api.solvrbot.com
auth: Authorization: Bearer {SOLVR_API_KEY}
source: https://github.com/solvrbase/solvr
---

# Agent Buzz

Track buzz around AI agent ecosystem — what agents and protocols are trending.

## Endpoints
- `GET https://api.solvrbot.com/api/v1/news?topic=AI+agent+autonomous&category=tech&limit=10` — agent news
- `GET https://api.solvrbot.com/api/v1/dex/trending` — agent tokens on-chain
- `GET https://api.solvrbot.com/api/v1/github/trending?topic=ai-agent&since=daily&limit=10` — agent repos

## Instructions
1. Fetch agent ecosystem news
2. Fetch trending agent tokens on-chain
3. Fetch trending agent GitHub repos
4. Synthesize: what agent projects/protocols are gaining momentum?
5. Output: Agent buzz report with heat scores (1-10) per project.
