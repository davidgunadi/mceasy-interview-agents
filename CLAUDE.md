# Interview Repo

This repo manages the end-to-end hiring process: job descriptions, candidate CVs, interview questions, and post-interview results.

## Folder structure

```
/roles/
  [role-name]/              ← kebab-case, e.g. senior-backend-engineer
    _jd.md                  ← job description (source of truth for the role)
    _questions.md           ← master question template for this role
    [candidate-name]/       ← kebab-case, e.g. alice-tan
      cv.md or cv.pdf       ← candidate's CV
      questions.md          ← tailored copy of _questions.md; answers filled post-interview
      summary.md            ← hire rating, decision, pros/cons
```

## File conventions

- Role and candidate folder names: kebab-case
- `_jd.md` and `_questions.md` — prefixed with `_` to distinguish role-level files from candidate folders
- `_questions.md` is the **master template** — never edit it with candidate-specific content; always work in the candidate's own `questions.md`
- `questions.md` per candidate starts as a tailored copy of `_questions.md`, then gets answers populated after the interview via Fireflies transcript review
- Candidate CV can be `cv.md` or `cv.pdf` — agents check for either

## Agents

Four agent prompts live in `.claude/agents/`. Skills invoke these automatically — you don't need to load them manually.

| Agent | File | When to use |
|-------|------|-------------|
| Role Setup | `.claude/agents/role-setup.md` | After adding `_jd.md` — generates the master `_questions.md` template for the role |
| Question Generator | `.claude/agents/question-generator.md` | After adding a candidate's `cv.md` — generates their tailored `questions.md` |
| Fireflies Reviewer | `.claude/agents/fireflies-reviewer.md` | After the interview — pulls Fireflies transcript and fills in `questions.md` |
| Create Summary | `.claude/agents/create-summary.md` | After reviewer fills `questions.md` — produces `summary.md` with rating, decision, and pros/cons |

---

## Workflow

1. Add a role: create `roles/[role-name]/_jd.md`, then run `/setup [role-name]`
2. Add a candidate: create `roles/[role-name]/[candidate-name]/cv.md`
3. Generate tailored questions: run `/setup [role-name] [candidate-name]`
4. Post-interview: run `/review-fireflies [role-name] [candidate-name] [recording-name]` — requires Fireflies connector
5. Generate summary: run `/summarize [role-name] [candidate-name]`
