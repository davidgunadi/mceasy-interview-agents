# Interview Repo

This repo manages the end-to-end hiring process: job descriptions, candidate CVs, interview questions, and post-interview results.

## Folder structure

```
/roles/
  [role-name]/              ← kebab-case, e.g. senior-backend-engineer
    _jd.md                  ← job description (source of truth for the role)
    _questions.md           ← master question template for this role
    [candidate-name]/       ← kebab-case, e.g. alice-tan
      cv.md                 ← candidate's CV
      questions.md          ← tailored copy of _questions.md; answers filled post-interview
```

## File conventions

- Role and candidate folder names: kebab-case
- `_jd.md` and `_questions.md` — prefixed with `_` to distinguish role-level files from candidate folders
- `_questions.md` is the **master template** — never edit it with candidate-specific content; always work in the candidate's own `questions.md`
- `questions.md` per candidate starts as a tailored copy of `_questions.md`, then gets answers populated after the interview via Fireflies transcript review

## Agents

Two reusable agent prompts live in `/agents/`. Load the relevant one before executing each phase.

| Agent | File | When to use |
|-------|------|-------------|
| Question Generator | `agents/question-generator.md` | After adding a candidate's `cv.md` — generates their tailored `questions.md` |
| Interview Reviewer | `agents/interview-reviewer.md` | After the interview — pulls Fireflies transcript and fills in `questions.md` |
| Create Summary | `agents/create-summary.md` | After reviewer fills `questions.md` — produces `summary.md` with rating, decision, and pros/cons |

---

## Workflow

1. Add a role: create `roles/[role-name]/_jd.md` and generate `_questions.md` from it
2. Add a candidate: create `roles/[role-name]/[candidate-name]/cv.md`
3. Generate tailored questions: Claude reads `_questions.md` + `cv.md` and produces `questions.md` for that candidate
4. Post-interview: tell Claude which Fireflies recording maps to which candidate (by date or title), and Claude will pull the transcript and fill in answers in that candidate's `questions.md`
5. Generate summary: Claude reads the completed `questions.md` and produces `summary.md` — hire rating (1–10), YES/NO decision, executive summary, pros and cons
