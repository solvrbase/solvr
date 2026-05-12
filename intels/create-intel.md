---
name: create-intel
description: Create a new Solvr intel file for any agent use case.
category: dev-code
tier: free
solvr_api: https://api.solvrbot.com
auth: Authorization: Bearer {SOLVR_API_KEY}
source: https://github.com/solvrbase/solvr
---

# Create Intel

Create a new Solvr intel file for any agent use case.

## Endpoints
- `GET https://api.solvrbot.com/api/v1/catalog` — available Solvr endpoints

## Instructions
1. Fetch endpoint catalog: `GET https://api.solvrbot.com/api/v1/catalog`
2. Given a use case description, design the intel:
   - Select relevant endpoints
   - Define trigger (schedule or event)
   - Define output format
3. Write the INTEL.md using this template:
   ```
   ---
   name: intel-name
   description: one-line description
   category: category
   tier: free|standard|full
   ---
   ## Endpoints
   ## Instructions
   ## Output
   ```
4. Test the intel by executing Step 1 manually.
