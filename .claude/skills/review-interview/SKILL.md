---
name: review-interview
description: >
  Reviews a Fireflies recording for a candidate and fills in their questions.md.
  Use this skill whenever the user runs `/review-interview [candidate-name] [recording-name]`,
  or asks to review a Fireflies transcript, fill in interview answers, or populate questions.md
  from a recording. The user must have the Fireflies connector authorized in Claude.
---

# Review Fireflies Transcript

## Overview

This skill pulls a Fireflies transcript by recording name (or date/title) and fills in
the candidate's `questions.md` with answers and assessments.

The user must have the Fireflies connector authorized. If it is not available, stop and
tell the user to connect it via their claude.ai connector settings before proceeding.

---

## Step 1: Identify the candidate

- Extract candidate name and recording name from the skill arguments — if either is missing, ask the user to provide it
- Search all `roles/*/[candidate-name]/` folders for a match:
  - If found under exactly one role, use that role
  - If found under multiple roles, list the matching roles and ask the user which one they mean
  - If not found under any role, tell the user and stop
- Confirm the target file: `roles/[role-name]/[candidate-name]/questions.md`
- Stop if `questions.md` does not exist — tell the user to run `/setup` first

---

## Step 2: Pull the Fireflies transcript

- Use the Fireflies connector to search for the recording matching the provided name/date/title
- If multiple matches are found, list them and ask the user to confirm which one
- Retrieve the full transcript

---

## Step 3: Fill in questions.md

Invoke the Agent tool with `subagent_type: "fireflies-reviewer"` and a self-contained prompt telling it to:

- Read `roles/[role-name]/[candidate-name]/questions.md`
- Search for and retrieve the Fireflies transcript matching [recording-name] (it has direct access to the Fireflies MCP tools)
- Populate every blank field per its own scoring criteria, without overwriting already-filled fields
- Save the updated file in place at `roles/[role-name]/[candidate-name]/questions.md`

---

## Step 4: Export to PDF

Run this to generate a matching `questions.pdf` next to the markdown file:

```
python3 scripts/md_to_pdf.py roles/[role-name]/[candidate-name]/questions.md roles/[role-name]/[candidate-name]/questions.pdf
```

If the script fails (e.g. `reportlab` not installed), tell the user `questions.md` was
still saved successfully and that they can install it with `pip3 install reportlab`
to enable PDF export.

---

## Finishing up

Confirm to the user that `questions.md` and `questions.pdf` have been filled in/saved,
and suggest running `/summarize [candidate-name]` as the next step.
