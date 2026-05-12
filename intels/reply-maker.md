---
name: reply-maker
description: Generate smart, data-backed replies to trending topics.
category: social-writing
tier: free
solvr_api: https://api.solvrbot.com
auth: Authorization: Bearer {SOLVR_API_KEY}
source: https://github.com/solvrbase/solvr
---

# Reply Maker

Generate smart, data-backed replies to trending topics.

## Endpoints
- `GET https://api.solvrbot.com/api/v1/news?topic={reply_context}&limit=5` — context
- `GET https://api.solvrbot.com/api/v1/worlddata?query={relevant_metric}` — supporting data

## Instructions
1. Given a post/topic to reply to, fetch relevant news context
2. Fetch supporting data from worlddata if applicable
3. Write 3 reply options:
   - Informative: add data or context that enhances the conversation
   - Contrarian: polite pushback with evidence
   - Supportive: reinforce the point with additional evidence
4. Keep each reply under 280 chars.
