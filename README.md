# Smart Task Planner

Break any goal into a realistic, timeline-respecting action plan — in seconds.

## About

Enter a goal and a timeframe. The planner returns a clean, day-by-day task list that finishes exactly on the deadline — no overruns, no fluff.

Here's the thing: this tool turns vague deadlines into concrete, prioritized work you can act on immediately.

---

## Live demo

Try it yourself: https://huggingface.co/spaces/hemasreeg/Smart_Task_Planner

---

## How it works

1. You give a goal with a timeframe, for example: `Build a website in 10 days`.
2. The planner:

   * Detects the total number of days (for example 3 weeks -> 21 days).
   * Produces 8–15 realistic tasks covering planning, execution, and launch.
   * Enforces the final deadline strictly — no task goes past Day N.
3. You get a numbered plan with due dates (`Due: Day N`), dependencies (`Depends on: Task 3`), and short descriptions.

---

## Tech stack

| Component     |                     Technology | Why we chose it                                                 |
| ------------- | -----------------------------: | --------------------------------------------------------------- |
| Core AI model | Qwen/Qwen2.5-Coder-7B-Instruct | Strong instruction-following and reliable structured output     |
| Backend       |     Python + `huggingface_hub` | Official client for secure, simple LLM calls                    |
| Frontend      |                         Gradio | Fast UI with minimal code, great for demos                      |
| Hosting       |            Hugging Face Spaces | One-click deploy, secrets management                            |
| Prompting     |  Constraint-aware instructions | Ensures timeline compliance without over-constraining the model |

---

## Project structure

```
smart-task-planner/
├── app.py              # Gradio UI and user interaction
├── planner.py          # LLM task generation with timeline enforcement
├── requirements.txt    # Dependencies
└── README.md           # This file
```

---

## Key features

* Timeline-aware: converts "2 weeks" → 14 days, "3 weeks" → 21 days.
* Strict deadline enforcement: tasks never exceed your limit.
* Realistic workflows: supports parallel tracks like marketing during development.
* Zero fluff output: a clean, numbered task list only.
* Lightweight and fast: no DB, no heavy infra.

---

## Example input → output

**Input**: `Launch a mobile app in 2 weeks`

**Output**:

```
1. Define app features and user stories - Due: Day 2 - Depends on: None
   Description: Finalize core functionality and target audience.

2. Design UI wireframes - Due: Day 5 - Depends on: Task 1
   Description: Sketch key screens and navigation flow.

3. Set up development environment - Due: Day 3 - Depends on: None
   Description: Configure tools, repo, and cloud services.

4. Build backend API - Due: Day 8 - Depends on: Task 3
   Description: Implement user auth, data storage, and core logic.

5. Develop frontend - Due: Day 11 - Depends on: Tasks 2 and 4
   Description: Code responsive mobile interface.

6. Test full application - Due: Day 13 - Depends on: Task 5
   Description: Run QA on real devices and fix critical bugs.

7. Launch on app stores - Due: Day 14 - Depends on: Task 6
   Description: Submit to Apple App Store and Google Play.
```

---

## Deploy your own

1. Create a Hugging Face account.
2. Go to Hugging Face Spaces → Create new Space

   * SDK: Gradio
   * Hardware: CPU (inference can run via HF Inference API)
3. Add your HF token as a secret:

   * Key: `HF_TOKEN`
   * Value: your HF token with Inference API role
4. Push the repo to your Space and deploy.

---

## Why this matters

Most AI planners either ignore deadlines or generate unrealistic plans. This tool keeps the timeline real and enforces the end date strictly. If Day 21 is your deadline, Day 22 does not exist.

Built for founders, PMs, students, and anyone who needs to ship on time.

---

## License

MIT License — use, modify, and share freely.

---

Made with ❤️ and Qwen2.5-Coder on Hugging Face

No data stored. No tracking. Just smart planning.
