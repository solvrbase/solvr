---
name: hacker-news-digest
description: Tech community digest — top tech news + trending GitHub repos.
category: research-content
tier: free
solvr_api: https://api.solvrbot.com
auth: Authorization: Bearer {SOLVR_API_KEY}
source: https://github.com/solvrbase/solvr
---

# Hacker News Digest

Tech community digest — top tech news + trending GitHub repos.

## Endpoints
- `GET https://api.solvrbot.com/api/v1/news?category=tech&limit=10` — tech headlines
- `GET https://api.solvrbot.com/api/v1/github/trending?since=daily&limit=10` — trending repos

## Instructions
1. Fetch tech news: `GET https://api.solvrbot.com/api/v1/news?category=tech&limit=10`
2. Fetch trending repos: `GET https://api.solvrbot.com/api/v1/github/trending?since=daily&limit=10`
3. Identify overlap (news stories about trending repos)
4. Format digest:

```
🔧 TECH DIGEST
📰 TOP STORIES
1. [Title] — [Source] — [1-line summary]
...

⭐ TRENDING ON GITHUB
1. repo/name — [language] — [stars] stars — [description]
...
```
