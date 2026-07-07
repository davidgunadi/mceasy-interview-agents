# Changelog

All notable functional changes to the interview pipeline (agents, skills, question bank, workflow) are logged here.

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/); versions follow [SemVer](https://semver.org/) (MAJOR.MINOR.PATCH — MAJOR for workflow-breaking changes, MINOR for new capabilities, PATCH for fixes/tweaks).

Adding a new role, candidate, JD, or CV is not a functional change to the tool and is not logged here.

## [2.0.3] - 2026-07-07

### Changed
- Moved `scripts/` out from under `.claude/` to the repo root, parallel to `.claude/`, matching layout conventions used in other repos. `md_to_pdf.py` is now invoked as `scripts/md_to_pdf.py`.

## [2.0.2] - 2026-07-07

### Fixed
- `md_to_pdf.py` rendered both checked and unchecked checkboxes (`[x]` / `[ ]`) as identical solid black squares in exported PDFs, since the Unicode ballot-box glyphs (☐/☑) it substituted them with aren't supported by the base Helvetica font. Checkboxes now render as plain `[ ]` / bold `[X]` text instead, which is font-safe and visually distinguishable.

## [2.0.1] - 2026-07-06

### Changed
- Agent prompts and role templates (`role-setup`, `question-generator`, `fireflies-reviewer`, `create-summary`) no longer hardcode "Dave" as the hiring manager's name, so the pipeline is generic and replicable across interviewers/companies.

## [2.0.0] - 2026-07-06

### Changed
- **Breaking:** `questions.md` and `summary.md` now carry two fully independent assessments — Technical Interview and Behavioral Interview — each with its own rubric, recommendation, rating, and hire decision, instead of one blended score. Existing candidate files in the old single-track format are not compatible with the new agents.
- `role-setup` now selects 5–6 behavioral traits per role from the new shared `roles/_behavioral_question_bank.md`, replacing the old free-form "Soft Skill Questions" section.
- `question-generator` carries the Behavioral Rubric over verbatim from `_questions.md` rather than tailoring it per candidate.
- `create-summary` produces two independent verdicts (Technical + Behavioral); a front with no interview data yet is reported as "not enough context" instead of a fabricated rating.
- `fireflies-reviewer` supports incremental review across two separate interview rounds (or one combined recording) without overwriting fields already filled by a prior pass, and logs uncategorized topics per front (`[Technical]` / `[Behavioral]`).

### Added
- `roles/_behavioral_question_bank.md` — shared master bank of behavioral traits, questions, and Green/Amber/Red anchors.
- `roles/qa-engineering/`, `roles/qa-odoo/` — new role folders.
- Versioning: this `CHANGELOG.md`, a version line in `README.md`, and a versioning policy in `CLAUDE.md`.

## [1.0.0] - 2026-07-06

Baseline version at the time versioning was introduced.

### Added
- PDF export for `questions.md` and `summary.md` via `.claude/scripts/md_to_pdf.py`
- Additional behavioral topics in `roles/_behavioral_question_bank.md`

### Changed
- Pinned models per agent in `.claude/agents/*.md`
