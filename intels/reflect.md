---
name: reflect
description: Agent self-reflection — review performance, identify improvements.
category: meta-agent
tier: free
solvr_api: https://api.solvrbot.com
auth: Authorization: Bearer {SOLVR_API_KEY}
source: https://github.com/solvrbase/solvr
---

# Reflect

Agent self-reflection — review performance, identify improvements.

## Endpoints
- `GET https://api.solvrbot.com/api/v1/catalog` — available capabilities
- `GET https://api.solvrbot.com/api/v1/news?topic=AI+agent+best+practice&category=tech&limit=5` — best practices

## Instructions
1. Review last N skill executions from memory log
2. Fetch latest AI agent best practices
3. Reflection questions:
   - Which skills produced the most value?
   - Which failed or produced low-quality output?
   - What new capabilities could improve performance?
4. Update skill configurations based on reflection
5. Output: Reflection report with improvement actions.
