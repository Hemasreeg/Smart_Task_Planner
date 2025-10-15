# app.py
import gradio as gr
from planner import generate_task_plan

def process_goal(goal):
    if not goal or not goal.strip():
        return "⚠️ Please enter a valid goal."
    try:
        plan = generate_task_plan(goal.strip())
        return plan
    except Exception as e:
        return f"❌ Error: {str(e)}"

# Build Gradio UI
with gr.Blocks(title="Smart Task Planner") as demo:
    gr.Markdown("# 🧠 Smart Task Planner")
    gr.Markdown("Powered by **Qwen2.5-Coder-7B-Instruct**, breaks your goal into a step-by-step action plan.")
    
    with gr.Row():
        goal_input = gr.Textbox(
            label="🎯 Your Goal",
            placeholder="e.g., Launch a mobile app in 2 weeks",
            lines=2
        )
    submit_btn = gr.Button("🚀 Generate Plan", variant="primary")
    output = gr.Textbox(
        label="📋 Your Action Plan",
        interactive=False,
        lines=18,
        max_lines=30
    )

    submit_btn.click(
        fn=process_goal,
        inputs=goal_input,
        outputs=output
    )

# Launch (HF Spaces handles this automatically)
if __name__ == "__main__":
    demo.launch()