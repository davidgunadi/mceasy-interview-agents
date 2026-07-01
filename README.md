# Interview Agent

A Claude-powered hiring system for managing end-to-end interviews at McEasy — from job descriptions to hire/no-hire decisions.

## How it works

Three Claude agents handle distinct phases of the hiring pipeline:

| Phase | Agent | What it does |
|-------|-------|--------------|
| Pre-interview | `agents/question-generator.md` | Reads JD + CV, generates a tailored `questions.md` with technical rubric, green/red flag questions, and soft skill probes |
| Post-interview | `agents/interview-reviewer.md` | Pulls the Fireflies transcript and fills in every answer field and outcome checkbox in `questions.md` |
| Decision | `agents/create-summary.md` | Reads the completed `questions.md` and produces `summary.md` with a hire rating (1–10), YES/NO decision, and pros/cons |

## Folder structure

```
roles/
  [role-name]/                   ← kebab-case, e.g. senior-backend-engineer
    _jd.md                       ← job description (source of truth)
    _questions.md                ← master question template (never edit directly)
    [candidate-name]/            ← kebab-case, e.g. alice-tan
      cv.md                      ← candidate's CV
      questions.md               ← tailored questions; answers filled post-interview
      summary.md                 ← hire rating, decision, pros/cons
```

## Workflow

**1. Add a role**

Create `roles/[role-name]/_jd.md` with the job description, then ask Claude to generate `_questions.md` from it.

**2. Add a candidate**

Create `roles/[role-name]/[candidate-name]/cv.md` with the candidate's CV.

**3. Generate tailored questions**

Load `agents/question-generator.md` and tell Claude to generate `questions.md` for the candidate. Claude reads the JD and CV and produces a question set with a technical rubric specific to this candidate's background.

**4. Fill in answers post-interview**

Load `agents/interview-reviewer.md` and tell Claude which Fireflies recording maps to this candidate (by date or title). Claude pulls the transcript and fills in every answer field and outcome checkbox in `questions.md`.

**5. Generate the hire summary**

Load `agents/create-summary.md` and tell Claude to produce `summary.md`. Claude reads the completed `questions.md` and outputs a hire rating, YES/NO decision, executive summary, and evidence-backed pros/cons.

## Rating scale

| Rating | Decision | Meaning |
|--------|----------|---------|
| 9–10 | YES | Exceptional — raise the bar hire |
| 7–8 | YES | Solid — meets the bar, risks manageable |
| 5–6 | NO | Mixed — meaningful gaps |
| 3–4 | NO | Below bar on must-haves |
| 1–2 | NO | Clear mismatch |

**7+ = Hire. Below 7 = No Hire. No hedging.**

## File conventions

- Folder names: `kebab-case`
- `_jd.md` and `_questions.md` are prefixed with `_` to distinguish role-level files from candidate folders
- Never write candidate-specific content into `_questions.md` — always work in the candidate's own `questions.md`
- Fireflies integration: specify the recording by date or title when invoking the Interview Reviewer agent
