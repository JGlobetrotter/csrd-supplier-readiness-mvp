# csrd-supplier-readiness-mvp
CSRD Readiness Triage and Governance Logic
The purpose of this product (repository) is to create a lightweight Supplier Baseline Screening Tool that helps suppliers understand buyer-driven sustainability and human-rights expectations, specifically through a CSRD (EU) lens. This product will screen suppliers readiness to be onboarded to buyer platforms, identify weak points for triage before risk is metabolized, and prioritize next steps for investment of resources, if applicable.

## What this does
- Accepts structured supplier intake information
- Applies governance and readiness logic
- Produces a concise readiness assessment highlighting likely buyer expectations

## What this does NOT do
- Provide legal advice
- Certify CSRD compliance
- Replace formal audits or reporting

## Boundaries of this tool
- Decision support only
- Not legal advice
- Not a compliance or reporting determination

## Design principles applied
- multiple choice only
- no legal interpretation required from the supplier
- aligned to what buyers actually screen for first under CSRD / HRDD
- safe for Global South and SME suppliers

## Repository structure
- /intake – supplier intake questions 
- /logic – tagging library, tagging and readiness rules
- /app - scoring logic and streamlit UI
- /outputs – example readiness output (TBD - for later)
- /prompts – system prompt and assumptions (TBD - for later)

## Workflow Description

## Input: supplier intake answers (number of questions)

## Step 1 — Normalize inputs
- Convert answers into consistent keys/values

## Step 2 — Apply rule-based tags

## Step 3 — Generate readiness level
- LOW / MEDIUM / HIGH based on tag counts and CSRD exposure signals

## Step 4 — Generate output brief
- Readiness level
- Tags triggered
- Interpretation (1–2 sentences)
- Top 3 next steps

