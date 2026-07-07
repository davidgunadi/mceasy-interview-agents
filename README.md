# Interview Agent

**Version:** 2.0.3 — see [CHANGELOG.md](CHANGELOG.md) for what changed and why.

A Claude-powered hiring system for managing end-to-end interviews at McEasy — from job descriptions to hire/no-hire decisions.

## Prerequisites

Must Have:

- [Claude Desktop](https://claude.com/download)
- [Git](https://git-scm.com/install/)
- [Python](https://www.python.org/downloads/)
- [Node](https://nodejs.org/en/download)
- Claude Pro or Max account

- Optional:

- [GitHub Desktop](https://desktop.github.com/download/)
- [VSCode](https://code.visualstudio.com/download)

## How it works

Four Claude agents handle distinct phases of the hiring pipeline:

| Phase          | Agent                                  | What it does                                                                                                                                    |
| -------------- | -------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| Role setup     | `.claude/agents/role-setup.md`         | Reads the JD, selects 5–6 behavioral traits from `roles/_behavioral_question_bank.md`, and generates the role's master `_questions.md` template |
| Pre-interview  | `.claude/agents/question-generator.md` | Reads JD + CV, generates a tailored `questions.md` with technical rubric, green/red flag questions, and soft skill probes                       |
| Post-interview | `.claude/agents/fireflies-reviewer.md` | Pulls the Fireflies transcript and fills in every answer field and outcome checkbox in `questions.md`                                           |
| Decision       | `.claude/agents/create-summary.md`     | Reads the completed `questions.md` and produces `summary.md` with a hire rating (1–10), YES/NO decision, and pros/cons                          |

## Folder structure

```
roles/
  _behavioral_question_bank.md   ← shared master bank of behavioral traits/questions, selected from per role
  [role-name]/                   ← kebab-case, e.g. senior-backend-engineer
    _jd.md                       ← job description (source of truth)
    _questions.md                ← master question template (never edit directly)
    [candidate-name]/            ← kebab-case, e.g. alice-tan
      cv.md or cv.pdf            ← candidate's CV
      questions.md               ← tailored questions; answers filled post-interview
      questions.pdf              ← generated from questions.md after review
      summary.md                 ← hire rating, decision, pros/cons
      summary.pdf                ← generated from summary.md
```

## Workflow

**1. Add a role**

Create `roles/[role-name]/_jd.md` with the job description.

You can generate `_questions.md` now if you want to review the questions first, but this is optional — step 3 (`/setup [candidate-name]`) generates it automatically if it hasn't been done yet.

```
/setup [role-name]
```

**2. Add a candidate**

Create `roles/[role-name]/[candidate-name]/cv.md` or `cv.pdf` with the candidate's CV.

**3. Generate tailored questions**

Run the same skill, this time with just the candidate name. Claude finds which role the candidate belongs to, generates `_questions.md` for the role first if it doesn't exist yet, then reads the JD and CV and produces a question set with a technical rubric specific to this candidate's background. If a candidate with that name exists under more than one role, Claude will ask you to pick which one.

```
/setup [candidate-name]
```

**4. Fill in answers post-interview**

Run the review skill with the candidate name and the Fireflies recording name. Claude pulls the transcript and fills in every answer field and outcome checkbox in `questions.md`, then exports a matching `questions.pdf`. Requires the Fireflies connector to be authorized.

```
/review-interview [candidate-name] [recording-name]
```

**5. Generate the hire summary**

Claude reads the completed `questions.md` and produces `summary.md` in the candidate's folder with a hire rating, YES/NO decision, executive summary, and evidence-backed pros/cons, then exports a matching `summary.pdf`.

```
/summarize [candidate-name]
```

## Rating scale

| Rating | Decision | Meaning                                 |
| ------ | -------- | --------------------------------------- |
| 9–10   | YES      | Exceptional — raise the bar hire        |
| 7–8    | YES      | Solid — meets the bar, risks manageable |
| 5–6    | NO       | Mixed — meaningful gaps                 |
| 3–4    | NO       | Below bar on must-haves                 |
| 1–2    | NO       | Clear mismatch                          |

**7+ = Hire. Below 7 = No Hire. No hedging.**

## File conventions

- Folder names: `kebab-case`
- `_jd.md` and `_questions.md` are prefixed with `_` to distinguish role-level files from candidate folders
- Never write candidate-specific content into `_questions.md` — always work in the candidate's own `questions.md`
- `roles/_behavioral_question_bank.md` is the shared source for behavioral traits/questions across all roles — edit it directly to add/revise traits; `role-setup.md` only selects which traits apply per role
- `questions.pdf` / `summary.pdf` are generated by `scripts/md_to_pdf.py` — regenerate after editing the markdown rather than editing the PDF directly
- Fireflies integration: specify the recording by date or title when running `/review-interview`; requires the Fireflies connector to be authorized
