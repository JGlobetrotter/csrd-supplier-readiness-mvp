

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


## Cell — Map sentences to stable internal keys

QUESTION_TO_KEY = {
  "Where is your company primarily operating?": "operates_in_eu",
  "Do you sell directly or indirectly to EU-based companies or investors?": "sells_to_eu_buyers",
  "What best describes your company size?": "company_size",
  "Which sector best fits your operations?": "sector",
  "Which best describes your role in the value chain today?": "value_chain_role",

  "How complex is your supply chain?": "supply_chain_complexity",
  "Do your operations or sourcing occur in regions commonly considered higher risk for labor or human-rights issues?": "hr_risk_region",
  "Are labor conditions a material issue in your operations or sourcing?": "labor_material",
  "Have buyers or partners asked you about environmental or climate-related topics?": "env_asked",
  "Which environmental topics have buyers mentioned or asked about? (Select all that apply)?": "env_topics",

  "Have buyers or partners recently requested ESG, sustainability, or human-rights information?": "recent_esg_requests",
  "Have you been asked to complete questionnaires or provide information that feels new or more detailed than in the past?": "more_detailed_requests",
  "What do you think prompted these requests?": "request_driver",
  "Have any buyers or partners mentioned CSRD, EU sustainability reporting, or new EU sustainability laws when requesting information from you?": "csrd_mentioned",

  "Who is primarily responsible for sustainability or social impact topics internally?": "internal_owner",
  "Do you have written policies related to the environment, sustainability and labor?": "policy_status",
  "Do you currently track any sustainability or social data?": "data_tracking",
  "How confident do you feel responding to buyer ESG, sustainability or human rights requests?": "confidence",

}

answers_by_question = {
  "Where is your company primarily operating?": "Non-EU",
  "Do you sell directly or indirectly to EU-based companies or investors?": "Yes, indirectly",
  "What best describes your company size?": "Medium",
  "Which sector best fits your operations?": "Manufacturing (components / sub-assemblies)",
  "Which best describes your role in the value chain today?": "Primarily a supplier to other companies",

  "How complex is your supply chain?": "Highly multi-tiered",
  "Do your operations or sourcing occur in regions commonly considered higher risk for labor or human-rights issues?": "Yes",
  "Are labor conditions a material issue in your operations or sourcing?": "Somewhat",
  "Have buyers or partners asked you about environmental or climate-related topics?": "Yes",
  "Which environmental topics have buyers mentioned or asked about? (Select all that apply)?": "Not specified / unclear",

  "Have buyers or partners recently requested ESG, sustainability, or human-rights information?": "Yes",
  "Have you been asked to complete questionnaires or provide information that feels new or more detailed than in the past?": "Yes, significantly more detailed",
  "What do you think prompted these requests?": "Unclear / not explained",
  "Have any buyers or partners mentioned CSRD, EU sustainability reporting, or new EU sustainability laws when requesting information from you?": "Yes, indirectly (e.g. “new EU requirements”)",

  "Who is primarily responsible for sustainability or social impact topics internally?": "No clear owner",
  "Do you have written policies related to the environment, sustainability and labor?": "No",
  "Do you currently track any sustainability or social data?": "Informal / ad hoc",
  "How confident do you feel responding to buyer ESG, sustainability or human rights requests?": "Not confident",
}

