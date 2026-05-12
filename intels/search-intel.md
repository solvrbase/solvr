---
name: search-intel
description: Find the right Solvr intel for any task from the intel catalog.
category: dev-code
tier: free
solvr_api: https://api.solvrbot.com
auth: Authorization: Bearer {SOLVR_API_KEY}
source: https://github.com/solvrbase/solvr
---

# Search Intel

Find the right Solvr intel for any task from the intel catalog.

## Endpoints
- `GET https://api.solvrbot.com/api/v1/catalog` — available Solvr endpoints

## Instructions
1. Fetch endpoint catalog: `GET https://api.solvrbot.com/api/v1/catalog`
2. Given a task description, identify matching intels from:
   - github.com/solvrbase/solvr (intel files)
   - Endpoint catalog
3. Rank matches by fit:
   - Exact match (intel name matches task)
   - Partial match (intel covers part of task)
   - Buildable (task can be built from available endpoints)
4. Output: Top 3 matching intels with usage notes.
