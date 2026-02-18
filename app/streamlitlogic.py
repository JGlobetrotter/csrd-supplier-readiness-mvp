





import streamlit as st
import inspect

import os
import sys

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)




# debug panel -- remove later
def debug_panel(tags=None, raw=None, normalized=None, fn=None):
    with st.expander("🔧 Debug Panel (safe to ignore)"):
        st.write("App file:", __file__)
        st.write("Working directory:", os.getcwd())

        if fn is not None:
            st.write("Function loaded from:", inspect.getsourcefile(fn))

        if tags is not None:
            st.write("UI → Logic input (tags):", tags)
            st.write("Input type:", type(tags))

        if raw is not None:
            st.write("Logic → UI raw output:", raw)
            st.write(
                "Raw output keys:",
                list(raw.keys()) if isinstance(raw, dict) else type(raw)
            )

        if normalized is not None:
            st.write("Normalized output:", normalized)

# other imports below


# Questions

from intake.intake_questions import (INTAKE_QUESTIONS, QUESTION_TO_KEY)

# normalization of logic
from logic.utils import normalize_answers

# tag derivation

from logic.Intake_Tag_DefinitionsAssumptions import (
    derive_tags,
    SECTOR_BASELINE_ASSUMPTIONS,
)
# scoring
from logic.scoringnextstepsgenerator import run_screening

#### Start actual streamlit code

def normalize_answers(answers: dict) -> dict:
    """Fallback normalizer: maps question text -> internal keys."""
    normalized = {}
    for q_text, value in answers.items():
        key = QUESTION_TO_KEY.get(q_text, q_text)
        normalized[key] = value
    return normalized

def derive_tags(normalized: dict) -> list:
    """Fallback tag derivation for UI testing."""
    tags = []
    sector = (normalized.get("sector") or "").strip()
    location = (normalized.get("location") or "").strip()
    owner = (normalized.get("owner") or "").strip()

    if sector and sector != "Other":
        tags.append("SECTOR_KNOWN")
    if "EU" in location:
        tags.append("EU_EXPOSURE")
    if owner == "No":
        tags.append("OWNER_GAP")

    # Example CSRD signal if EU exposure + manufacturing
    if "EU" in location and sector == "Manufacturing":
        tags.append("CSRD_CASCADE_SIGNAL")

    return tags

def run_screening(tags_dict: dict) -> dict:
    """Fallback screening so we can test the flow."""
    score = 0
    why = []

    if tags_dict.get("CSRD_CASCADE_SIGNAL"):
        score += 2
        why.append("EU exposure + manufacturing suggests CSRD cascade readiness work is likely relevant.")
    if tags_dict.get("EU_EXPOSURE"):
        score += 1
        why.append("EU exposure increases regulatory and buyer due diligence pressure.")
    if tags_dict.get("OWNER_GAP"):
        score += 1
        why.append("No clear ESG owner: governance and accountability likely need strengthening.")

    band = "Low" if score <= 1 else "Medium" if score <= 3 else "High"
    return {"score": score, "band": band, "why": why, "tags_received": list(tags_dict.keys())}

# Try real imports; if any fail, we keep the stubs above.
try:
    from intake.intake_questions import INTAKE_QUESTIONS as REAL_INTAKE_QUESTIONS, QUESTION_TO_KEY as REAL_QUESTION_TO_KEY
    INTAKE_QUESTIONS = REAL_INTAKE_QUESTIONS
    QUESTION_TO_KEY = REAL_QUESTION_TO_KEY

    from logic.Intake_Tag_DefinitionsAssumptions import (
        TAG_DEFS,  # unused here but fine if present
        derive_tags as REAL_DERIVE_TAGS,
        SECTOR_BASELINE_ASSUMPTIONS as REAL_SECTOR_BASELINE_ASSUMPTIONS,
    )
    derive_tags = REAL_DERIVE_TAGS
    SECTOR_BASELINE_ASSUMPTIONS = REAL_SECTOR_BASELINE_ASSUMPTIONS

    from logic.utils import normalize_answers as REAL_NORMALIZE_ANSWERS
    normalize_answers = REAL_NORMALIZE_ANSWERS

    from logic.scoringnextstepsgenerator import run_screening 
    run_screening = run_screening

except Exception as e:
    import_error = e  # shown in Debug expander; app still loads

# ------------------------------------------------------------
# Streamlit UI
# ------------------------------------------------------------
st.title("Supplier Baseline Screening (CSRD Friendly)")
st.caption(""""
This Sustainability Readiness tool is a fast, decision-grade diagnostic designed to help SME and supplier companies understand whether
they are prepared for today’s sustainability, human rights, and climate-related reporting expectations — especially under the EU Corporate
Sustainability Reporting Directive (CSRD).

Rather than asking suppliers to “do everything,” the tool focuses on what actually matters:
data availability, governance maturity, risk exposure, and the ability to meet near-term disclosure and due-diligence requirements.

The output is a clear, comparable readiness profile that highlights gaps, flags material risks, and distinguishes between suppliers
who need support, monitoring, or escalation.

Built for real supply chains—not idealized ones—the tool is practical, proportionate, and globally usable. It translates CSRD and related expectations into supplier-appropriate signals, reducing noise, survey fatigue, and false confidence. For buyers, it provides defensible evidence for risk-based prioritization, engagement strategies, and transition planning. For suppliers, it offers clarity on expectations and a realistic path toward improvement—without turning sustainability into an unmanageable compliance burden.

This purpose of this product

This product can also serve screens supplier readiness to be onboarded
to buyer platforms, identifies weak points for triage before risk is metabolized, and
prioritizes next steps for investment of resources.
All Questions are multiple choice.

## multiple choice only
## no legal interpretation required from the supplier
## aligned to what buyers actually screen for first under CSRD / HRDD
## safe for Global South and SME suppliers

Disclaimer : This is a decision support tool. It is not meant to be legal advice, or a final compliance /reporting determination.

"""
)

# Session state init
if "answers" not in st.session_state:
    st.session_state.answers = {}
if "results" not in st.session_state:
    st.session_state.results = None
if "applied_tags" not in st.session_state:
    st.session_state.applied_tags = []
if "normalized" not in st.session_state:
    st.session_state.normalized = {}

st.header("Section A: Supplier Profile")

# Render questions
for question_text, options in INTAKE_QUESTIONS.items():
    answer = st.selectbox(question_text, options, key=f"q::{question_text}")
    st.session_state.answers[question_text] = answer

    # Show sector assumptions if this is the sector question
    if question_text.strip() == "Which sector best fits your operations?" and answer:
        assumptions = SECTOR_BASELINE_ASSUMPTIONS.get(answer)
        if assumptions:
            st.info("**Baseline assumptions:**\n- " + "\n- ".join(assumptions))

# Run button
if st.button("Run screening"):
    normalized = normalize_answers(st.session_state.answers)
    st.session_state.normalized = normalized

    applied_tags = derive_tags(normalized) or []
    applied_tags = list(dict.fromkeys(applied_tags))  # dedupe while preserving order
    st.session_state.applied_tags = applied_tags

    tags_dict = {t: True for t in applied_tags}

    try:
        st.session_state.results = run_screening(tags_dict)
    except Exception as e:
        st.session_state.results = None
        st.error("run_screening() crashed.")
        st.exception(e)

# Debug
with st.expander("Debug", expanded=False):
    if import_error is not None:
        st.warning("Some project modules did not import; using fallback stubs so the UI can run.")
        st.exception(import_error)

    st.write("answers:", st.session_state.answers)
    st.write("normalized:", st.session_state.normalized)
    st.write("applied_tags:", st.session_state.applied_tags)

# Results
st.subheader("Results")
if st.session_state.results is None:
    st.info("Click **Run screening** to generate results.")
else:
    results = st.session_state.results
    # Friendly view if keys exist
    score = results.get("score") if isinstance(results, dict) else None
    band = results.get("band") if isinstance(results, dict) else None
    why = results.get("why") if isinstance(results, dict) else None

    if score is not None:
        st.metric("Score", score)
    if band:
        st.success(f"Band: {band}")

    if isinstance(why, list) and why:
        st.markdown("**Why:**")
        for item in why:
            st.markdown(f"- {item}")

    with st.expander("Raw results JSON", expanded=False):
        st.json(results)
