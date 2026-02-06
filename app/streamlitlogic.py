# ## Connect Streamlit UI
import sys
from pathlib import Path

# Add parent directory to Python path - MUST BE BEFORE OTHER IMPORTS
sys.path.insert(0, str(Path(__file__).parent.parent))

import streamlit as st

from intake.intake_questions import INTAKE_QUESTIONS, QUESTION_TO_KEY
from logic.Intake_Tag_DefinitionsAssumptions import derive_tags, SECTOR_BASELINE_ASSUMPTIONS
from logic.utils import normalize_answers

# Try importing run_screening safely so the app can still load and show the real error
try:
    from logic.scoringnextstepsgenerator import run_screening
except Exception as e:
    run_screening = None
    import_error = e
else:
    import_error = None

st.title("Supplier Baseline Screening (CSRD Friendly)")
st.caption("Decision-support triage for readiness and communication.")

# Initialize session state (prevents KeyErrors on first load)
if "answers" not in st.session_state:
    st.session_state.answers = {}
if "results" not in st.session_state:
    st.session_state.results = None
if "applied_tags" not in st.session_state:
    st.session_state.applied_tags = []
if "normalized" not in st.session_state:
    st.session_state.normalized = {}

# If the import failed, show it and stop (so you see the real underlying issue)
if import_error is not None:
    st.error("Could not import run_screening from logic/scoringnextstepsgenerator.py")
    st.exception(import_error)
    st.stop()

st.header("Section A: Supplier Profile")

# Iterate through questions
for question_text, options in INTAKE_QUESTIONS.items():
    answer = st.selectbox(question_text, options, key=question_text)
    st.session_state.answers[question_text] = answer

    # Show sector assumptions for sector question
    if question_text == "Which sector best fits your operations?" and answer:
        if answer in SECTOR_BASELINE_ASSUMPTIONS:
            st.info(f"**Baseline assumptions for '{answer}':**")
            for assumption in SECTOR_BASELINE_ASSUMPTIONS[answer]:
                st.markdown(f"- {assumption}")

if st.button("Run screening"):
    # Normalize answers to internal keys
    normalized = normalize_answers(st.session_state.answers)
    st.session_state.normalized = normalized

    # Derive tags (always produce a list)
    applied_tags = derive_tags(normalized) or []

    # Dedupe tags while preserving order (prevents repeats in reports)
    applied_tags = list(dict.fromkeys(applied_tags))

    st.session_state.applied_tags = applied_tags

    # Build tags dict
    tags_dict = {t: True for t in applied_tags}

    # Run screening safely (so if the logic file throws, you see the exception)
    try:
        st.session_state.results = run_screening(tags_dict)
    except Exception as e:
        st.session_state.results = None
        st.error("run_screening() crashed.")
        st.exception(e)

# Debug section (safe even before button click)
with st.expander("Debug", expanded=False):
    st.write("normalized keys:", list(st.session_state.normalized.keys()) if st.session_state.normalized else [])
    st.write("applied_tags:", st.session_state.applied_tags)
    st.write("type(applied_tags):", str(type(st.session_state.applied_tags)))

st.subheader("Results")
if st.session_state.results is None:
    st.info("Click **Run screening** to generate results.")
else:
    # Prefer a friendly report view if your run_screening returns these keys
    score = st.session_state.results.get("score")
    band = st.session_state.results.get("band")
    why = st.session_state.results.get("why")

    if score is not None:
        st.metric("Score", score)
    if band:
        st.success(f"Band: {band}")

    if isinstance(why, list) and why:
        st.markdown("**Why:**")
        for item in why:
            st.markdown(f"- {item}")

    # Always show raw JSON too (collapsed)
    with st.expander("Raw results JSON", expanded=False):
        st.json(st.session_state.results)


