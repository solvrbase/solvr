---
name: create-skill
description: Create a new Solvr skill file for any agent use case.
category: dev-code
tier: free
solvr_api: https://api.solvrbot.com
auth: Authorization: Bearer {SOLVR_API_KEY}
source: https://github.com/solvrbase/solvr
---

# Create Skill

Create a new Solvr skill file for any agent use case.

## Endpoints
- `GET https://api.solvrbot.com/api/v1/catalog` — available Solvr endpoints

## Instructions
1. Fetch endpoint catalog: `GET https://api.solvrbot.com/api/v1/catalog`
2. Given a use case description, design the skill:
   - Select relevant endpoints
   - Define trigger (schedule or event)
   - Define output format
3. Write the SKILL.md using this template:
   ```
   ---
   name: skill-name
   description: one-line description
   category: category
   tier: free|standard|full
   ---
   ## Endpoints
   ## Instructions
   ## Output
   ```
4. Test the skill by executing Step 1 manually.
