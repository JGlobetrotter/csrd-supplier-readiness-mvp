import gradio as gr
import sys
import os

# Add project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Imports
from intake.intake_questions import INTAKE_QUESTIONS, QUESTION_TO_KEY
from logic.utils import normalize_answers
from logic.Intake_Tag_DefinitionsAssumptions import derive_tags, SECTOR_BASELINE_ASSUMPTIONS
from logic.scoringnextstepsgenerator import run_screening

# Gradio input components
question_inputs = []
for question, options in INTAKE_QUESTIONS.items():
    question_inputs.append(gr.Radio(label=question, choices=options))

# Main prediction function
def screen_supplier(*responses):
    answers = dict(zip(INTAKE_QUESTIONS.keys(), responses))
    normalized = normalize_answers(answers)
    applied_tags = list(dict.fromkeys(derive_tags(normalized)))
    tags_dict = {tag: True for tag in applied_tags}

    results = run_screening(tags_dict)

    # Adjust for legacy field naming
    if "readiness_level" not in results and "band" in results:
        results["readiness_level"] = results["band"]

    # Format output
    output_lines = []
    output_lines.append(f"\n**Readiness Band:** {results.get('readiness_level', 'N/A')}")
    output_lines.append(f"**Score:** {results.get('score', 'N/A')}")
    if 'reasons' in results:
        output_lines.append("\n**Why:**")
        for reason in results["reasons"]:
            output_lines.append(f"- {reason}")
    if 'next_steps' in results:
        output_lines.append("\n**Suggested Next Steps:**")
        for step in results["next_steps"]:
            output_lines.append(f"- {step}")
    if 'interpretation' in results:
        output_lines.append("\n**Interpretation:**")
        output_lines.append(results["interpretation"])

    return "\n".join(output_lines)

# Launch interface
demo = gr.Interface(
    fn=screen_supplier,
    inputs=question_inputs,
    outputs=gr.Markdown(label="Screening Results"),
    title="Supplier Baseline Screening (CSRD Friendly)",
    description="Decision-support triage for sustainability readiness."
)

demo.launch()
