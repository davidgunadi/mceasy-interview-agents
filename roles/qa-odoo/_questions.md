# Interview Template: QA Engineer - Odoo

---

## 1. Technical Interview

### 1.1 Technical Rubric

Score each dimension 1–5 after the interview. Pull evidence from answers.

| Dimension | Weight | Score (1–5) | Evidence / Notes |
|-----------|--------|-------------|------------------|
| Functional / Regression / UAT Testing | High | | |
| API Testing (Postman) | High | | |
| Test Documentation (Scenarios, Cases, Bug Reports) | High | | |
| Git + Agile/Scrum | Med | | |
| Odoo / ERP Business Flow Knowledge (CRM, Sales, Purchase, Inventory, Accounting) | Med | | |

**Scoring guide:** 1 = no signal / wrong answers, 2 = weak, 3 = adequate, 4 = strong, 5 = exceptional

**Weighted average:** ___

---

### 1.2 Core Technical Questions

Standard questions for this role, not tailored to any specific candidate.

### Q1: Walk me through how you design a test suite for a new feature in an ERP system. How do you decide what to test, in what order, and how much is enough?

**What a good answer looks like:**
- Starts from requirements/user stories or business flow before writing test cases
- Distinguishes happy path, edge cases, and negative scenarios
- Considers integration points with other modules (e.g., a sales feature touching inventory and accounting)
- Has a practical stopping criterion — knows when coverage is "enough" rather than aiming for exhaustive testing by default

**Red flags:**
- Jumps straight to execution without mentioning requirement analysis
- No mention of integration risk or cross-module side effects in an ERP context
- Cannot articulate how to scope or prioritize test coverage under time constraints

---

### Q2: A bug slips through to production. Walk me through how you'd reproduce it, document it, and determine what went wrong in your test coverage.

**What a good answer looks like:**
- Systematic reproduction approach: isolate environment, data, and steps
- Bug report includes steps to reproduce, expected vs. actual behavior, severity, and evidence (screenshots/logs)
- Conducts a root-cause review of their own test coverage — not just "it was an edge case"
- Has a concrete idea of how to prevent recurrence (new test case, updated regression scope, etc.)

**Red flags:**
- Blames the developer without reflecting on the testing gap
- Cannot describe what a complete bug report looks like
- No concept of updating test coverage after a production escape

---

### Q3: How do you approach regression testing when a new Odoo module or enhancement is deployed? How do you determine the scope of your regression run?

**What a good answer looks like:**
- Risk-based scoping: identifies which modules/flows are touched by the change and prioritizes accordingly
- Understands that in an ERP, changes in one area (e.g., Purchase) can ripple into Accounting or Inventory
- Has a methodology for maintaining and updating regression suites over time — not just running everything every time
- Mentions time and environment constraints as real factors in scoping decisions

**Red flags:**
- "Run all test cases every time" with no risk-based reasoning
- No awareness of Odoo's module interdependencies
- Regression scope never changes regardless of the change being deployed

---

### Q4: Describe how you use Postman for API testing — what kinds of tests do you write, how do you structure your collections, and how do you handle things like authentication or dynamic data between requests?

**What a good answer looks like:**
- Writes assertions beyond status code (response body fields, data types, business logic validation)
- Uses environment variables and collection variables to handle tokens, IDs, and dynamic values across requests
- Has structured collections that reflect business flows, not just a flat list of endpoints
- Aware of Odoo's JSON-RPC or REST API patterns (bonus: can name specific endpoints or authentication mechanism)

**Red flags:**
- Uses Postman only to manually send requests and inspect responses — no automated assertions
- Cannot explain how to chain requests or pass data between them
- No concept of organizing tests into meaningful, reusable collections

---

### Q5: How do you run UAT with business stakeholders who aren't technical? What documentation do you prepare, and how do you manage defect triage with them?

**What a good answer looks like:**
- Prepares test scripts in plain business language, not technical QA jargon
- Facilitates the session — doesn't just hand over a checklist and wait
- Has a clear process for capturing, classifying, and communicating defects back to the team
- Knows how to distinguish a real defect from a misunderstood requirement or a change request during UAT

**Red flags:**
- UAT described purely as "users test the system" with no facilitation role for QA
- No mention of defect documentation or triage during UAT
- Cannot distinguish a bug from a requirement gap

---

## 2. Behavioral Interview

Not a technical assessment — this section probes a role-specific selection of traits drawn from `roles/_behavioral_question_bank.md`. Evidence for any trait can surface in response to any question below (or even during the Technical Interview) — the rubric is scored from the totality of the transcript, not one-to-one against the question that "belongs" to it.

### 2.1 Behavioral Rubric

| Trait | Assessed Outcome | Evidence / Notes |
|-------|-------------------|------------------|
| Leading (IC) | [ ] Green  [ ] Amber  [ ] Red | |
| Ownership | [ ] Green  [ ] Amber  [ ] Red | |
| Integrity | [ ] Green  [ ] Amber  [ ] Red | |
| Learning From Mistakes | [ ] Green  [ ] Amber  [ ] Red | |
| Conflict / Difficult Conversations | [ ] Green  [ ] Amber  [ ] Red | |
| Receiving Feedback | [ ] Green  [ ] Amber  [ ] Red | |

**Anchors — copied verbatim from `roles/_behavioral_question_bank.md` for each selected trait, do not redesign:**

**Leading (IC)**
- Green — Names specific actions taken to influence or lead, not just "I motivated the team." Acknowledges tradeoffs made. Owns the outcome, good or bad, with concrete detail on how they knew it worked.
- Amber — Describes a leadership/influence moment but stays vague on the specific mechanism — general "I aligned the team" language, unclear what action actually shifted the outcome, or credits authority/title rather than persuasion.
- Red — Vague "we" language with no personal action described. Leadership framed purely as authority ("I told them to..."). No mention of how they knew it worked.

**Ownership**
- Green — Uses "I" for failure points, "we" for wins. Proactively expanded scope without being asked. Follows through to resolution, not just identification.
- Amber — Claims some ownership but softens it — acknowledges a failure existed but frames their role ambiguously, or expanded scope once but describes it as an exceptional one-off rather than a pattern.
- Red — Failure is always someone else's fault or "the process." Identifies problems but has no story of actually fixing one outside their lane.

**Integrity**
- Green — Chose transparency even when it was costly (career, relationship, timeline). Specific, not hypothetical.
- Amber — Describes a real ethical or professional tension but the resolution is unclear or was deferred to someone else, or the "cost" of honesty turns out to have been minimal.
- Red — Answer is entirely hypothetical ("I would..." rather than "I did..."). Frames dishonesty-adjacent behavior as clever or resourceful.

**Learning From Mistakes**
- Green — Can state the mistake plainly without over-qualifying it. Describes a concrete behavioral or process change that stuck. Some self-awareness about *why* the mistake happened, not just what happened.
- Amber — Names a real mistake and a change made, but the change is described in general terms ("I'm more careful now") without a concrete mechanism, or self-awareness of the cause is thin.
- Red — "Mistake" is trivially small or not really their fault. No lasting change described — same mistake could recur. Over-rehearsed, generic answer (interview-prep smell).

**Conflict / Difficult Conversations**
- Green — Addresses the conflict directly rather than avoiding or escalating past it. Reflects on the relationship post-conflict, not just the immediate resolution.
- Amber — Describes a real tense disagreement but the resolution is vague, or reflection stops at "it worked out" without detail on how the relationship was maintained.
- Red — Conflict always resolved by them being "right" and the other person coming around. Avoidance dressed up as diplomacy ("I just let it go").

**Receiving Feedback**
- Green — Distinguishes between initial emotional reaction and eventual response — honest that it stung before it was useful. Can describe feedback they *didn't* fully agree with and how they handled that tension productively (not just capitulation).
- Amber — Describes real feedback and an eventual change, but skips the initial reaction/friction, or the disagreement was resolved by simply deferring rather than genuinely working through it.
- Red — Claims to have never received hard feedback, or that all feedback was immediately and gratefully accepted. No example of pushing back on feedback they thought was wrong.

---

### 2.2 Behavioral Questions (STAR)

All questions must be phrased to elicit a STAR response (Situation → Task → Action → Result).

### B1: Tell me about a time you had to push a developer, product owner, or business analyst to act on something — a bug priority, a missing requirement, a testing gap — without having the authority to force it. What did you do, and what happened?

**Primary trait probed:** Leading (IC)

**What to listen for:**
- Specific influence tactics used (evidence, data, business impact framing) rather than "I just kept following up"
- Acknowledgment of the other party's perspective or constraints, not just "I was right"
- Concrete outcome — did the situation actually change, and how do they know?

---

### B2: Describe a time you noticed a quality or process problem that wasn't strictly your responsibility to fix. What did you do?

**Primary trait probed:** Ownership

**What to listen for:**
- Took a concrete action beyond flagging the issue — followed through to some resolution
- "I" language for the action taken, not "we eventually figured it out"
- Pattern of behavior, not a one-off anecdote framed as exceptional

---

### B3: Tell me about a time you had to deliver test results or a quality assessment that someone didn't want to hear — a feature that wasn't ready, a bug count that would delay a release, or a finding that contradicted a stakeholder's assumption.

**Primary trait probed:** Integrity

**What to listen for:**
- Was transparent even when it created friction or pressure to change their findings
- Specific, not hypothetical — describes a real instance with real stakes
- Does not soften the answer by saying the stakeholder "understood immediately"

---

### B4: Walk me through a significant testing mistake you made — something that escaped to production or caused a problem. How did you find out, and what concretely changed in how you work afterward?

**Primary trait probed:** Learning From Mistakes

**What to listen for:**
- States the mistake plainly without deflecting blame to developers or requirements
- Describes a specific process or behavioral change that stuck — not just "I'm more careful now"
- Shows awareness of *why* the mistake happened, not just what it was

---

### B5: Tell me about a disagreement with a developer or product owner that got tense — for example, over a bug's severity, whether something was a defect or a feature, or release readiness. How did you handle it, and how was the relationship afterward?

**Primary trait probed:** Conflict / Difficult Conversations

**What to listen for:**
- Engaged directly with the disagreement rather than escalating immediately or backing down
- Can articulate the other person's position fairly, not just why they themselves were right
- Reflects on the relationship after the conflict, not only the immediate outcome

---

### B6: Tell me about the most critical piece of feedback you've received about your QA work or testing approach. What was your first reaction, and what did you do with it?

**Primary trait probed:** Receiving Feedback

**What to listen for:**
- Honest about the initial reaction — defensiveness, surprise, resistance — before describing the eventual response
- Describes a concrete change in behavior or approach, not just "I took it on board"
- Bonus: can describe a case where they pushed back on feedback they disagreed with and how they navigated that

---

## 3. Additional Information

> [This section is left blank in the template. During review, anything the candidate raises that doesn't fit a predefined question in Section 1 or 2 gets logged here, tagged [Technical] or [Behavioral].]

---

## 4. Candidate's Questions for Us

> [This section is left blank in the template. Filled during post-interview review with whatever the candidate actually asked.]

---

## 5. Post-Interview Summary

**Strongest signals:**
>

**Biggest concerns:**
>

**CV vs reality gap (if any):**
>

**Final notes for the hiring manager:**
>
