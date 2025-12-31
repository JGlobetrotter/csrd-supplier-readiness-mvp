
# Intake form questions and responses for (external)


intake = {}

"Intake Form"

"Section A: Supplier Profile"

intake["Where is your company primarily operating?"] = "EU", "Non-EU", "Both"
intake["Do you sell directly or indirectly to EU-based companies or investors?"] = "Yes, directly", "Yes, indirectly", "Not sure"
intake["What best describes your company size?"] = "Micro", "Small", "Medium", "Large"
intake["Which sector best fits your operations?"] = "Manufacturing (components / sub-assemblies)", "Processing / transformation (e.g. food, materials)", "Agriculture / farming", "Forestry / timber", "Fisheries / aquaculture", "Mining / extractives", "Construction / infrastructure", "Logistics / transport (road, sea, air)," "Warehousing / distribution," "Energy production or supply", "Waste management / recycling," "Chemicals / industrial inputs," "Textiles / apparel / footwear," "Electronics / electrical equipment," "Packaging / materials," "IT / digital services," "Professional services," "Facilities management / cleaning / security," "Other services (non-industrial)"
intake["Which best describes your role in the value chain today?"] = "Primarily a supplier to other companies," "Both a supplier and a buyer", "Primarily a buyer (procures from others)"

"Section B: Supply Chain & Labor Context"

intake["How complex is your supply chain?"] = "Highly multi-tiered", "Mostly direct suppliers" "Mix of direct and indirect"
intake["Do your operations or sourcing occur in regions commonly considered higher risk for labor or human-rights issues?"] = "Yes", "Some operations", "No", "Not sure"
intake["Are labor conditions a material issue in your operations or sourcing?"] = "Yes", "Somewhat", "No"
intake["Have buyers or partners asked you about environmental or climate-related topics?"] = "Yes", "Somewhat", "No"
intake["Which environmental topics have buyers mentioned or asked about? (Select all that apply)?"] = "Climate / emissions", "Energy use", "Water use", "Waste / materials", "Biodiversity / land use", "Other issue", "not applicable", "Not specified /unclear"

"Section C: Buyer Pressure"

intake["Have buyers or partners recently requested ESG, sustainability, or human-rights information?"] = "Yes", "No", "Expected soon,"
intake["Have you been asked to complete questionnaires or provide information that feels new or more detailed than in the past?"] = "Yes, significantly more detailed", "Yes, somewhat more detailed", "No change / Not applicable"
intake["What do you think prompted these requests?"] = "CSRD regulations", "Other new regulation or law (not just CSRD)", "Buyer policy update," "Investor requirement," "Unclear / not explained"
intake["Have any buyers or partners mentioned CSRD, EU sustainability reporting, or new EU sustainability laws when requesting information from you?"] = "Yes, explicitly," "Yes, indirectly (e.g. “new EU requirements”)," "No," "Not sure"

"Section D: Governance & Confidence"

intake["Who is primarily responsible for sustainability or social impact topics internally?"] = "Dedicated role/team", "Shared responsibility," "Legal / compliance only", "No clear owner"
intake["Do you have written policies related to the environment, sustainability and labor?"] = "Yes", "Draft / informal", "No"
intake["Do you currently track any sustainability or social data?"] = "Yes, structured", "Informal / ad hoc", "No"
intake["How confident do you feel responding to buyer ESG, sustainability or human rights requests?"] = "Confident", "Somewhat confident", "Not confident"

# Dictionary of Question Tags (internal)

QUESTION_TO_TAG = {
    
    # Section A

    "Where is your company primarily operating?": "operates_in_eu",
    "Do you sell directly or indirectly to EU-based companies or investors?": "sells_to_eu_buyers",
    "What best describes your company size?": "company_size",
    "Which sector best fits your operations?": "sector",
    "Which best describes your role in the value chain today?": "value_chain_role",
    
    #Section B

    "How complex is your supply chain?": "supply_chain_complexity",
    "Do your operations or sourcing occur in regions commonly considered higher risk for labor or human-rights issues?" : "sourcing_risk_H_Rights",
    "Are labor conditions a material issue in your operations or sourcing?" : "sourcing_laborissues",
    "Have buyers or partners asked you about environmental or climate-related topics?" : "partner_ask_abt_climate",
    "Which environmental topics have buyers mentioned or asked about? (Select all that apply)?" : "which_topic_environment",

    #Section C

    "Have buyers or partners recently requested ESG, sustainability, or human-rights information?" : "recent_info_request",
    "Have you been asked to complete questionnaires or provide information that feels new or more detailed than in the past?": "info_request_more_detailed",
    "What do you think prompted these requests?" : "opinion_prompt",
    "Have any buyers or partners mentioned CSRD, EU sustainability reporting, or new EU sustainability laws when requesting information from you?" : "CSRD_reporting_request",

    # Section D

    "Who is primarily responsible for sustainability or social impact topics internally?" : "responsible_for_internal_SI",
    "Do you have written policies related to the environment, sustainability and labor?" : "policy_internal_status",
    "Do you currently track any sustainability or social data?" : "data_tracking",
    "How confident do you feel responding to buyer ESG, sustainability or human rights requests?" : "confidence_level"

}
