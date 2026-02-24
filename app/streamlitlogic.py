import streamlit as st


PASSWORD = "betastream"

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    pwd = st.text_input("Enter password", type="password")
    if pwd == PASSWORD:
        st.session_state.authenticated = True
        st.rerun()
    st.stop()

# ---- real app below ----
st.title("Supplier Baseline Screening (CSRD friendly)")


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
        tags.append("EU_EXPOSURE_NON_EU")
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
    if tags_dict.get("EU_EXPOSURE_NON_EU"):
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

    from logic.scoringnextstepsgenerator import run_screening as REAL_RUN_SCREENING
    run_screening = REAL_RUN_SCREENING

    
except Exception as e:
    import_error = e  # shown in Debug expander; app still loads

# ------------------------------------------------------------
# Streamlit UI
# ------------------------------------------------------------
st.title("Notes about the beta version")
st.caption("""
This Sustainability Readiness tool is a fast, decision-grade diagnostic designed to help SME and supplier companies understand whether
they are prepared for current sustainability, human rights, and climate-related reporting expectations — especially under the EU Corporate
Sustainability Reporting Directive (CSRD).

Rather than asking suppliers to "do everything," the tool focuses on what actually matters: data availability, governance maturity, risk exposure, and the ability to meet near-term disclosure and due-[...]

The output is a clear, comparable readiness profile that highlights gaps, flags material risks, and distinguishes between suppliers who need support, monitoring, or escalation.

Built for real supply chains (not idealized ones), the tool is practical, proportionate, and globally usable.

This product can also serve to screen supplier readiness to be onboarded to buyer platforms, identify weak points for triage before risk is metabolized, and prioritize next steps for investment of res[...]  

Additional Notes:
- No legal interpretation required from the supplier  
- Aligned to what buyers actually screen for first under CSRD / HRDD  
- Safe for Global South and SME suppliers  

Disclaimer: This is a decision support tool. It is not meant to be legal advice, or a final compliance/reporting determination.
""")

# Session state init
if "answers" not in st.session_state:
    st.session_state.answers = {}
if "results" not in st.session_state:
    st.session_state.results = None
if "applied_tags" not in st.session_state:
    st.session_state.applied_tags = []
if "normalized" not in st.session_state:
    st.session_state.normalized = {}

st.header("Supplier Intake")

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
            st.markdown(f"- {item


# put here feb 24 --- Convert list -> dict for scoring (True/False flags) ---
tags = {t: True for t in applied_tags}

# --- Scoring + reasons ---
score = 0
reasons = []

if tags.get("CSRD_CASCADE_SIGNAL"):
    score += 2
    reasons.append("CSRD readiness activities strongly recommended.")

if tags.get("EU_EXPOSURE_NON_EU"):
    score+= 2
    reasons.append("EU business links suggestions additional vulnerability to CSRD - action recommended")

if tags.get("BUYER_OPACITY_RISK"):
    score += 2
    reasons.append("Clients or buyers are expressing conflicting or confusing requests.")

if tags.get("HRDD_RELEVANCE_HIGH"):
    score += 1
    reasons.append("Human Rights and Labor activity strengthening recommended")

if tags.get("OWNER_GAP"):
    score += 1
    reasons.append("Strengthen responsibility linkages to reporting and compliance")

if tags.get("ENVIRONMENTAL_BASELINE_GAP"):
    score += 1
    reasons.append("Suggest to draft environmental compliance processes to create a baseline")

if tags.get("POLICY_LIGHT"):
    score += 1
    reasons.append("Draft or strengthen Policy documents")

if tags.get("DUAL_ROLE_PRESSURE"):
    score += 1
    reasons.append("Your organization seems to be dealing with pressures coming from multiple angles.")

if tags.get("SUPPLIER_CONFIDENCE_LOW"):
    score += 1
    reasons.append("You don't have a lot of confidence at present - strongly suggest external advisory or support.")

# --- Band logic ---
if score >= 12:
    band = "HIGH: Sustainability readiness triage recommended"
elif score >= 5:
    band = "MEDIUM: Some Sustainability-driven pressure likely"
else:
    band = "LOW: Limited signal of Sustainability-driven pressure"

# --- Output ---
print("\nScore:", score)
print("Band:", band)
print("Why:")
if reasons:
    for r in reasons:
        print("- ", r)
else:
    print("- (no reasons triggered; check whether applied_tags is empty)")


# Additional tags to be given scores later (note)

# "RISING_BUYER_DEMAND": "Requests are increasing in detail/frequency."


# "ENV_RISK": "Environmental topics are being requested by buyers."

              # Cell: Run screenings


def run_screening(tags: dict) -> dict:
    """
    tags: dict like {"CSRD_CASCADE_SIGNAL": True, "DATA_GAP": False, ...}
    returns: dict with keys: readiness_level, tags, interpretation, next_steps
    """

    # Keep only tags that are True
    active_tags = [k for k, v in tags.items() if v is True]

    # ---- Simple scoring model (edit weights TBD) ----
    weights = {
        "CSRD_CASCADE_SIGNAL": 1,
        "EU_EXPOSURE_NON_EU": 1,

        "POLICY_LIGHT": 2,

        "HRDD_RELEVANCE_HIGH": 2,
        "BUYER_OPACITY_RISK": 1,
        "ENVIRONMENTAL_BASELINE_GAP": 1,
        "DOCUMENTATION_LIGHT": 1,
        "SUPPLIER_CONFIDENCE_LOW": 1,
        "DUAL_ROLE_PRESSURE": 1,
        "OWNER_GAP": 2,
        ## to add later: Rising_buyer_demand and ENV_RISK
    }

    score = sum(weights.get(t, 0) for t in active_tags)

    # ---- Readiness level thresholds ----
    # Lower score = more ready; higher score = more gaps/pressure
    if score <= 2:
        readiness_level = "GREEN — Low risk / early readiness"
        interpretation = (
            "You have limited immediate pressure signals and/or only minor capability gaps. "
            "Focus on documentation hygiene and staying ahead of buyer requests."
        )
    elif score <= 6:
        readiness_level = "AMBER — Moderate risk / needs structuring"
        interpretation = (
            "You’re seeing buyer/regulatory pressure signals and some internal gaps. "
            "Prioritize ownership, policy basics, and minimum viable data tracking."
        )
    else:
        readiness_level = "RED — High risk / likely exposure"
        interpretation = (
            "You have multiple pressure signals and several internal capability gaps. "
            "This is where suppliers often get caught flat-footed during buyer requests, audits, or tender processes. "
            "Move quickly to establish ownership, baseline policies, and auditable evidence."

        )



    # Next steps generator (based on which gaps are active)
    next_steps = []

    if "OWNER_GAP" in active_tags:
        next_steps.append("Assign a single accountable owner for sustainability/compliance requests (name + role).")

    if "POLICY_LIGHT" in active_tags:
        next_steps.append("Review for gaps and draft a minimum policy set (environment + labor/human rights) with approval + version control.")

    if "DOCUMENTATION_LIGHT" in active_tags:
        next_steps.append("Start a basic data baseline and inventory check (may include: energy, emissions scope assumptions, water, waste) in a simple tracker.")

    if "HRDD_RELEVANCE_HIGH" in active_tags:
        next_steps.append("Map human rights and/or labor risk in sourcing (countries/commodities) and set up a lightweight supplier or partner due diligence checklist.")

    if "CSRD_CASCADE_SIGNAL" in active_tags or "RISING_BUYER_DEMAND" in active_tags:
        next_steps.append("Create a buyer-response pack: 1-page overview + evidence folder + standard Q&A.")

    if "EU_EXPOSURE_NON_EU" in active_tags:
        next_steps.append("Identify EU-linked customers and expected reporting asks; align your evidence to what they request most.")

    # Always include an “artifact” step so this becomes reusable IP
    next_steps.append("Package outputs into a reusable 'Readiness Folder' (policies, tracker, evidence, Q&A) for future requests.")

#note : to review / ammend "next steps" list

    return {
        "readiness_level": readiness_level,
        "tags": active_tags,
        "interpretation": interpretation,
        "next_steps": next_steps,
    }

    ## add airtable form that requests feedback for the beta ****


    with st.expander("Raw results JSON", expanded=False):
        st.json(results)

