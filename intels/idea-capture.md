---
name: idea-capture
description: Capture and enrich ideas with current data and trend context.
category: productivity
tier: free
solvr_api: https://api.solvrbot.com
auth: Authorization: Bearer {SOLVR_API_KEY}
source: https://github.com/solvrbase/solvr
---

# Idea Capture

Capture and enrich ideas with current data and trend context.

## Endpoints
- `GET https://api.solvrbot.com/api/v1/news?topic={idea_domain}&limit=5` — validate idea with news
- `GET https://api.solvrbot.com/api/v1/github/trending?topic={idea_tech}&limit=5` — tech feasibility

## Instructions
1. Given an idea, fetch news to validate demand: any similar solutions? problems being discussed?
2. Check technical feasibility: fetch trending repos in relevant tech stack
3. Enrich the idea:
   - Problem it solves (from news)
   - Similar existing solutions
   - Tech stack to build it
   - Market signal (growing/declining/emerging)
4. Store enriched idea in memory with timestamp.
