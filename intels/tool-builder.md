---
name: tool-builder
description: Build new agent tools by combining Solvr endpoints.
category: productivity
tier: free
solvr_api: https://api.solvrbot.com
auth: Authorization: Bearer {SOLVR_API_KEY}
source: https://github.com/solvrbase/solvr
---

# Tool Builder

Build new agent tools by combining Solvr endpoints.

## Endpoints
- `GET https://api.solvrbot.com/api/v1/catalog` — available endpoints

## Instructions
1. Fetch catalog to understand available building blocks
2. Given a tool goal, design the implementation:
   - Input: what the user/agent provides
   - Processing: which endpoints to call and how to combine
   - Output: what to return
3. Write the tool as a Python function using the Solvr SDK
4. Include error handling and rate limit awareness
5. Output: Tool code + usage example.
