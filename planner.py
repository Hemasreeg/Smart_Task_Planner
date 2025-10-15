# planner.py
import os
from huggingface_hub import InferenceClient

HF_TOKEN = os.getenv("HF_TOKEN")
client = InferenceClient(
    model="Qwen/Qwen2.5-Coder-7B-Instruct",
    token=HF_TOKEN
)

def generate_task_plan(goal: str) -> str:
    # Simple: tell the model the exact number of days
    # We'll assume user includes "X weeks" or "X days"
    # For reliability, we hard-code the logic for common cases
    goal_lower = goal.lower()
    total_days = 14  # default

    if "1 week" in goal_lower:
        total_days = 7
    elif "2 weeks" in goal_lower:
        total_days = 14
    elif "3 weeks" in goal_lower:
        total_days = 21
    elif "4 weeks" in goal_lower:
        total_days = 28
    elif "5 weeks" in goal_lower:
        total_days = 35
    else:
        # Try to extract number + "days"
        import re
        if match := re.search(r'(\d+)\s*days?', goal_lower):
            total_days = int(match.group(1))

    prompt = f"""You are a senior product manager. Break down this goal into a realistic task plan.
Goal: "{goal}"
You have exactly {total_days} days to complete everything. The final task must be done by Day {total_days}.
Instructions:
- Create 8 to 15 actionable tasks.
- Spread work across all {total_days} days — don’t finish early.
- Include: planning, design, development, testing, marketing, launch, and feedback.
- For each task, write:
    [Number]. [Task name] - Due: Day [N] - Depends on: [Task numbers or "None"]
       Description: [One clear sentence]
Important: 
- NEVER use a day greater than {total_days}.
- Do NOT add introductions, summaries, or extra text.
- Output ONLY the numbered list.
Now generate the plan:"""

    try:
        response = client.chat.completions.create(
            model="Qwen/Qwen2.5-Coder-7B-Instruct",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2048,
            temperature=0.3,
            stream=False
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {str(e)}"