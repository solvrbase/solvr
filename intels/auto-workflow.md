---
name: auto-workflow
description: Build automated workflows by combining Solvr intelligence endpoints.
category: dev-code
tier: free
solvr_api: https://api.solvrbot.com
auth: Authorization: Bearer {SOLVR_API_KEY}
source: https://github.com/solvrbase/solvr
---

# Auto Workflow

Build automated workflows by combining Solvr intelligence endpoints.

## Endpoints
- `GET https://api.solvrbot.com/api/v1/catalog` — list available endpoints + your tier

## Instructions
1. Fetch available endpoints: `GET https://api.solvrbot.com/api/v1/catalog`
2. Given a workflow goal (e.g. "alert me when a new safe token launches"), design the chain:
   - Step 1: Which endpoints to call
   - Step 2: What conditions to check
   - Step 3: What output to produce
3. Write the workflow as a sequence of API calls with conditional logic
4. Estimate API cost and rate limits for the workflow cadence.
