---
name: fork-fleet
description: Fork and customize Solvr skills for a specialized agent fleet.
category: dev-code
tier: free
solvr_api: https://api.solvrbot.com
auth: Authorization: Bearer {SOLVR_API_KEY}
source: https://github.com/solvrbase/solvr
---

# Fork Fleet

Fork and customize Solvr skills for a specialized agent fleet.

## Endpoints
- `GET https://api.solvrbot.com/api/v1/catalog` — available endpoints
- `GET https://api.solvrbot.com/api/v1/github/trending?topic=ai+agent` — agent frameworks

## Instructions
1. Fetch catalog and available skills from GitHub
2. Select base skills to fork
3. Customize for specialized use case:
   - Change API endpoints used
   - Modify alert thresholds
   - Add domain-specific output format
4. Output: Forked skill pack with customization notes.
