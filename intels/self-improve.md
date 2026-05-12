---
name: self-improve
description: Agent self-improvement — identify new intels to add and existing ones to tune.
category: meta-agent
tier: free
solvr_api: https://api.solvrbot.com
auth: Authorization: Bearer {SOLVR_API_KEY}
source: https://github.com/solvrbase/solvr
---

# Self Improve

Agent self-improvement — identify new intels to add and existing ones to tune.

## Endpoints
- `GET https://api.solvrbot.com/api/v1/github/trending?topic=ai+agent&since=weekly` — new agent techniques
- `GET https://api.solvrbot.com/api/v1/news?topic=AI+agent+improvement+technique&category=tech` — best practices

## Instructions
1. Fetch latest agent development techniques from GitHub + news
2. Review current intel list from memory
3. Identify gaps:
   - New Solvr API endpoints available (check catalog)
   - Intels with stale endpoints or outdated output formats
   - Performance bottlenecks in current intels
4. Propose 3 improvements ranked by impact
5. Output: Self-improvement report with implementation plan.
