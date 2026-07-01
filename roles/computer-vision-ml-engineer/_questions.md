# Interview Template: Senior Computer Vision / ML Engineer

---

## 1. Technical Rubric

Score each dimension 1–5 after the interview. Pull evidence from answers.

| Dimension | Weight | Score (1–5) | Evidence / Notes |
|-----------|--------|-------------|------------------|
| CV/DL fundamentals (object detection, video models, architectures) | High | | |
| Model training — hands-on PyTorch/TensorFlow, not just inference | High | | |
| Production deployment track record (real users, real data) | High | | |
| Inference optimization for real-time / resource-constrained environments | High | | |
| Engineering quality (Python, building and shipping services) | High | | |
| Real-world image/video data handling at scale | High | | |
| Edge/embedded deployment (TensorRT, ONNX, Jetson, on-device) | Med | | |
| Annotation pipeline design and data quality ownership | Med | | |
| MLOps (versioning, monitoring, drift detection, retraining) | Med | | |
| Domain familiarity: driver monitoring / ADAS / dashcam | Med | | |

**Scoring guide:** 1 = no signal / wrong answers, 2 = weak, 3 = adequate, 4 = strong, 5 = exceptional

**Weighted average:** ___

---

## 2. Core Technical Questions

Standard questions for this role, not tailored to any specific candidate.

### Q1: Design problem — driver fatigue detection at scale

> "We want to detect driver fatigue and distraction from dashcam video across tens of thousands of vehicles. How would you build it so it actually runs cost-effectively?"

**What a good answer looks like:**
- Proposes edge / on-device inference rather than streaming all video to cloud
- Discusses model size trade-offs — smaller backbone, quantization, distillation
- Mentions triggered / event-based processing instead of 24/7 full inference
- Addresses annotation strategy and handling false positives in a safety context
- Reasons through accuracy vs latency vs cost explicitly

**Red flags:**
- "Stream all video to a large cloud GPU model" with no cost consideration
- Accuracy-only thinking, ignores latency, scale, or deployment constraints
- Cannot sequence an end-to-end approach from data to deployment

---

### Q2: Production failure — model works in training, fails in the field

> "Your fatigue detection model hits 95% accuracy on your validation set but performs poorly after 3 months in production. Walk me through how you diagnose and fix it."

**What a good answer looks like:**
- Immediately identifies data/distribution drift as the likely cause
- Describes a monitoring setup to catch degradation early
- Talks about collecting and labeling field data, retraining, iterating
- Mentions edge cases: lighting, camera angle, seasonal variation, vehicle types

**Red flags:**
- First instinct is "train longer" or "use a bigger model"
- No concept of distribution shift or field monitoring
- Cannot give a concrete example from experience

---

### Q3: Model optimization trade-offs

> "You have a YOLO-class model running acceptably on cloud GPUs. You need to get it running on an edge device with 4 GB RAM and no data center connectivity. What's your optimization strategy and what do you give up?"

**What a good answer looks like:**
- Discusses quantization (INT8/FP16), pruning, knowledge distillation as a toolkit
- Knows which to apply first and why (e.g. quantization for quick wins)
- Articulates the accuracy vs inference speed trade-off explicitly
- Mentions profiling as the starting point, not guessing
- Understands TensorRT, ONNX, or equivalent export paths

**Red flags:**
- Cannot explain how quantization or pruning work mechanically
- Treats "just use a smaller model" as a complete answer without reasoning
- Has never actually done this — only theoretical knowledge

---

### Q4: Annotation pipeline ownership

> "Labeling will be outsourced. How do you design the annotation spec and quality control process so the training data is actually useful?"

**What a good answer looks like:**
- Owns the spec: clear class definitions, edge case guidance, example images
- Designs a QA loop — spot checks, inter-annotator agreement, rejection criteria
- Understands how annotation quality directly drives model behavior
- Has iterated on spec based on model errors (closes the feedback loop)

**Red flags:**
- Treats annotation as someone else's problem
- No concept of QA or iterative spec refinement
- Has only worked with pre-labeled academic datasets

---

### Q5: Architecture selection

> "For a dashcam application detecting driver distraction events (phone use, looking away, drowsiness), would you start with a frame-level classifier, a detection model, or a video-understanding model? Why?"

**What a good answer looks like:**
- Reasons through trade-offs: latency, compute budget, temporal context needed
- Identifies that frame-level classification can work for most events with simpler deployment
- Knows when temporal models (3D CNNs, transformers, LSTM post-processing) add value vs overhead
- Considers the deployment target (edge vs cloud) as a hard constraint that shapes architecture

**Red flags:**
- Jumps to most complex architecture without reasoning
- Cannot explain why temporal context matters for drowsiness vs phone detection
- Unfamiliar with detection/classification trade-offs in video

---

### Q6: Inference cost at fleet scale

> "Assume 10,000 vehicles, each with a dashcam running 8 hours a day. Walk me through how you'd estimate and manage inference cost at that scale."

**What a good answer looks like:**
- Frames cost per camera-hour and aggregates to fleet level
- Proposes triggers (motion, event, schedule) to avoid 24/7 full inference
- Considers cloud vs edge cost models: edge = device cost + power, cloud = GPU hours + bandwidth
- Has a mental model for how model size, batch size, and hardware interact

**Red flags:**
- Cannot estimate at all — no quantitative intuition
- Ignores bandwidth cost of sending video to cloud
- Has never thought about inference economics at scale

---

## 3. Soft Skill Questions

Probe discipline, motivation, initiative, and grit. Use behavioral (STAR) format.

### S1: Shipping under ambiguity

> "Tell me about a time you had to ship an AI feature where the requirements were fuzzy or kept changing. How did you decide what 'good enough' looked like?"

**What to listen for:**
- Shows initiative in defining their own success criteria when stakeholders are vague
- Comfortable making a call and moving, not paralyzed waiting for clarity
- Can articulate what they gave up and why that was the right trade

---

### S2: Pushing back on a bad technical direction

> "Walk me through a time you disagreed with how a project or model was being built. What did you do?"

**What to listen for:**
- Raises concerns early with evidence, not just opinions
- Finds the right moment and right audience — not just complaining
- Can describe the outcome: did they change minds, escalate, or execute under protest and why

---

### S3: Learning from a model that failed in production

> "Tell me about a model you shipped that underperformed in the real world. What happened and what did you learn?"

**What to listen for:**
- Takes ownership rather than blaming data or labelers
- Shows a systematic debug approach
- Demonstrates that the lesson actually changed how they work now

---

### S4: Working with non-ML stakeholders

> "Describe a time when a non-technical stakeholder (product, ops, leadership) had unrealistic expectations about what a model could do. How did you handle it?"

**What to listen for:**
- Translates technical limitations without being condescending
- Sets expectations early, not after a failed demo
- Finds a version of the ask that is actually achievable and proposes it proactively

---

## 4. Candidate-Specific Section

> [This section is left blank in the template. The Question Generator agent fills it with CV-specific questions when generating a candidate's questions.md.]

---

## 5. Post-Interview Summary

**Strongest signals:**
>

**Biggest concerns:**
>

**CV vs reality gap (if any):**
>

**Final notes for Dave:**
>
