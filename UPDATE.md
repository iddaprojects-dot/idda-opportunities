# Weekly update runbook – IDDA Opportunities

The page https://idda-erasmus.com/opportunities/ loads `data.json` from this repository
(`https://raw.githubusercontent.com/iddaprojects-dot/idda-opportunities/main/data.json`).
If the file is missing or broken, the page falls back to the copy built into the page, so
**never push a file that fails `python3 tools/validate.py`**.

## Each weekly run

1. **Remove** every item whose `deadline` has passed (the page hides them anyway; keep the file clean).
2. **Re-check** items that are `st: upcoming / later / watch` and items closing in the next 30 days:
   if an official page now shows a fixed deadline, set `deadline` (ISO 8601 with offset) and drop `st`/`badge`;
   if a deadline was extended, update it.
3. **Search for new opportunities** (web search, official sources only: funder or programme websites,
   government, EU, Council of Europe, UN, embassies). Aggregators (fundsforNGOs, Opportunity Desk, etc.)
   may be used to *discover* calls, but every fact must be confirmed on the official page.
   - `org` (grants for NGOs): first **Türkiye** (ministries, development agencies e.g. BEBKA/SOGEP,
     TÜBİTAK, EU Delegation / ab.gov.tr / siviltoplumsektoru.ab.gov.tr, STGM, UNDP, Council of Europe Ankara,
     embassies and consulates in Ankara/Istanbul, Turkish foundations), then **Estonia** (KÜSK, HARNO,
     ESTDEV, KIK, Kultuurkapital, Integration Foundation, Nordic Council of Ministers, EEA/Norway Grants,
     CERV via KÜSK), then international/regional programmes open to NGOs in many countries.
   - `youth`: scholarships, leadership programmes and fellowships, startup accelerators,
     volunteering/travel, internships and trainings, open to young people internationally.
   - Prefer opportunities with a deadline at least 2 weeks away. Add at most ~10 new items per run.
4. Set `checked` to today's date (YYYY-MM-DD).
5. Run `python3 tools/validate.py`. Fix every error before committing.
6. Commit to `main` with a message like `Weekly update 2027-01-04: +3 org, +4 youth, -5 expired`
   and push. Then write a short summary for IDDA (what was added/removed, anything urgent this week).

## Item formats

### org (grants for organisations)
```json
{"id":"short-unique-id","c":["TR"],"x":["optional excluded country codes"],
 "type":"eu|intl|regional|national|embassy|bilateral|foundation",
 "title":"…","funder":"…","emoji":"🌍",
 "opens":"2027-01-10 (optional)","deadline":"2027-02-01T23:59:00+01:00 or empty string",
 "st":"upcoming|later|watch|rolling (only when deadline is empty)","badge":"short label, e.g. Next: spring 2027",
 "dlText":"explanation when there is no fixed deadline",
 "amount":"…","who":"…","req":["…","…"],"period":"…","themes":["climate","digital","youth","education","inclusion","democracy","rights","capacity"],
 "how":"…","tip":"one practical idea for IDDA","url":"https://official-page"}
```
`c` takes ISO country codes (`TR`, `EE`, …) or groups: `ALL`, `EU27`, `ERASMUS` (EU + IS LI NO MK RS TR GB CH),
`COE` (Council of Europe members), `NB8` (Nordic–Baltic), `ENL` (EU enlargement countries), `WB6`
(Western Balkans), `EEDC` (EU neighbourhood + Western Balkans + Türkiye), `EUROMED`, `DEV`
(all countries except high-income ones).

### youth
```json
{"id":"…","cat":"scholar|lead|startup|travel|train","title":"…","by":"…","emoji":"🎓",
 "opens":"optional","deadline":"ISO or empty","st":"…","badge":"…","dlText":"…","dlNote":"optional note",
 "get":"what you get","who":"who can apply","url":"https://official-page",
 "el":{"a":[18,30],"lv":["hs","ug","grad","pg","pro"],"nat":{"in":["…"],"x":["…"]},"n":"condition to double-check"}}
```
`el` drives the "Find programmes that fit you" tool: `a` = [min age, max age] (use null for no limit),
`lv` = allowed study levels (hs high school, ug university student, grad bachelor's graduate,
pg master's/PhD, pro working/youth worker), `nat.in` / `nat.x` = allowed / excluded citizenships,
`n` = a condition the visitor must check themselves. Leave out what you don't know.

## Rules
- Write in clear, simple English. No promises on IDDA's behalf.
- Never invent amounts, dates or eligibility. If unsure, leave the field general and add a `dlText`/`n` note.
- Dates: include the time zone offset from the official call; if no time is given use 23:59 local time.
- Keep at least the existing structure; never delete the file or empty a list.
