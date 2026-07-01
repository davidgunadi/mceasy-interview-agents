---
name: setup
description: >
  Generates interview question files for a role or candidate in this repo. Use this skill
  whenever the user runs `/setup [role-name]` or `/setup [candidate-name]`, or asks to
  generate, create, or produce interview questions for a role or candidate. Also trigger
  when the user says things like "generate questions for Alice", "prep questions for the
  backend role", "create questions.md for [candidate]", or "set up questions for [role]".
---

# Generate Interview Questions

## Overview

This skill handles two related tasks:

1. **Role template** — if `_questions.md` does not exist for the role yet, generate it first using `agents/role-setup.md`
2. **Candidate questions** — for each candidate under the role who has a `cv.md` but no `questions.md`, generate their tailored file using `agents/question-generator.md`

When run with a role name, do step 1 before step 2, even if candidates already exist.
When run with a candidate name, skip straight to step 2 for that candidate (running step 1 first if the role's `_questions.md` is still missing).

---

## Step 0: Resolve the target

The skill takes a single name argument, which can be either a role or a candidate:

- If `roles/[argument]/` exists as a directory, treat it as a **role name** — proceed to Step 1 for that role, covering all its candidates.
- Otherwise, treat the argument as a **candidate name** — search all `roles/*/[argument]/` folders:
  - If found under exactly one role, proceed to Step 1 (if `_questions.md` is missing for that role) then Step 2 for that candidate only.
  - If found under multiple roles, list the matching roles and ask the user which one they mean before continuing.
  - If not found under any role, tell the user and stop.

---

## Step 1: Generate `_questions.md` (if missing)

Read `.claude/agents/role-setup.md` — it contains your persona, output format, and instructions.

- Check if `roles/[role-name]/_questions.md` exists
- If it does **not** exist:
  - Read `roles/[role-name]/_jd.md` (stop and tell the user if it's missing)
  - Follow `.claude/agents/role-setup.md` to generate the master template
  - Save to `roles/[role-name]/_questions.md`
  - Confirm to the user
- If it already exists, skip this step silently and move on

---

## Step 2: Generate candidate `questions.md` files

Read `.claude/agents/question-generator.md` — it contains your persona, output format, and instructions for candidate-tailored questions.

- If resolving a single candidate (Step 0 found one match), process only that candidate
- Otherwise, list all subdirectories of `roles/[role-name]/` that contain a `cv.md`
- Skip any candidate folder that already has a `questions.md` — unless the user explicitly asked to regenerate
- If no candidates are found (or all already have `questions.md`), tell the user
- For each candidate to process:
  - Read `roles/[role-name]/[candidate-name]/cv.md`
  - Read `roles/[role-name]/_jd.md` and `roles/[role-name]/_questions.md` for context
  - Follow `.claude/agents/question-generator.md` to generate the tailored question file
  - Save to `roles/[role-name]/[candidate-name]/questions.md`
  - Confirm to the user when done

---

## Finishing up

Summarise what was created:
- Whether `_questions.md` was generated or already existed
- Which candidate `questions.md` files were created
- Which candidates were skipped (already had `questions.md`) — mention them so the user can ask to regenerate if needed
