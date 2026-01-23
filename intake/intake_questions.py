# Intro / Purpose
"""

Introduction:

Sustainability Readiness tool is a fast, decision-grade diagnostic designed to help SME and supplier companies understand whether
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

## Note: This repo is illustrative; commercial use requires agreement

## intake questions


INTAKE_QUESTIONS = {
  "Where is your company primarily operating?": ["EU", "Non-EU", "Both"],
  "Do you sell directly or indirectly to EU-based companies or investors?": ["Yes, directly", "Yes, indirectly", "Not sure"],
  "What best describes your company size?": ["Micro", "Small", "Medium", "Large"],
  "Which sector best fits your operations?": [
      "Manufacturing (components / sub-assemblies)",
      "Processing / transformation (e.g. food, materials)",
      "Agriculture / farming",
      "Forestry / timber",
      "Fisheries / aquaculture",
      "Mining / extractives",
      "Construction / infrastructure",
      "Logistics / transport (road, sea, air)",
      "Warehousing / distribution",
      "Energy production or supply",
      "Waste management / recycling",
      "Chemicals / industrial inputs",
      "Textiles / apparel / footwear",
      "Electronics / electrical equipment",
      "Packaging / materials",
      "IT / digital services",
      "Professional services",
      "Facilities management / cleaning / security",
      "Other services (non-industrial)"
  ],
  "Which best describes your role in the value chain today?": ["Primarily a supplier to other companies", "Both a supplier and a buyer", "Primarily a buyer (procures from others)"],

  "How complex is your supply chain?": ["Mostly direct suppliers", "Mix of direct and indirect", "Highly multi-tiered"],
  "Do your operations or sourcing occur in regions commonly considered higher risk for labor or human-rights issues?": ["Yes", "Some operations", "No", "Not sure"],
  "Are labor conditions a material issue in your operations or sourcing?": ["Yes", "Somewhat", "No"],
  "Have buyers or partners asked you about environmental or climate-related topics?": ["Yes", "Somewhat", "No"],
  "Which environmental topics have buyers mentioned or asked about? (Select all that apply)?": ["Climate / emissions", "Energy use", "Water use", "Waste / materials", "Biodiversity / land use", "Other issue", "Not applicable", "Not specified / unclear"],

  "Have buyers or partners recently requested ESG, sustainability, or human-rights information?": ["Yes", "No", "Expected soon"],
  "Have you been asked to complete questionnaires or provide information that feels new or more detailed than in the past?": ["Yes, significantly more detailed", "Yes, somewhat more detailed", "No change / Not applicable"],
  "What do you think prompted these requests?": ["CSRD regulations", "Other new regulation or law (not just CSRD)", "Buyer policy update", "Investor requirement", "Unclear / not explained"],
  "Have any buyers or partners mentioned CSRD, EU sustainability reporting, or new EU sustainability laws when requesting information from you?": ["Yes, explicitly", "Yes, indirectly (e.g. “new EU requirements”)", "No", "Not sure"],

  "Who is primarily responsible for sustainability or social impact topics internally?": ["Dedicated role/team", "Shared responsibility", "Legal / compliance only", "No clear owner" ],
  "Do you have written policies related to the environment, sustainability and labor?": ["Yes", "Draft / informal", "No"],
  "Do you currently track any sustainability or social data?": ["Yes, structured", "Informal / ad hoc", "No"],
  "How confident do you feel responding to buyer ESG, sustainability or human rights requests?": ["Confident", "Somewhat confident", "Not confident"],
}
