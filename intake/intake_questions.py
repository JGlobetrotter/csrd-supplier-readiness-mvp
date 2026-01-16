"""Survey questions and mappings"""

INTAKE_QUESTIONS = {
  "Where is your company primarily operating?": ["EU", "Non-EU", "Both"],
  "Do you sell directly or indirectly to EU-based companies or investors?": ["Yes, directly", "Yes, indirectly", "Not sure"],
  "What best describes your company size?": ["Micro", "Small", "Medium", "Large"],
  "Which sector best fits your operations?": [
      "Manufacturing (components / sub-assemblies)",
      "Processing / transformation (e.g. food, materials)",
      # ... rest of sectors
  ],
  # ... rest of your questions
}

QUESTION_TO_KEY = {
  "Where is your company primarily operating?": "operates_in_eu",
  "Do you sell directly or indirectly to EU-based companies or investors?": "sells_to_eu_buyers",
  # ... rest of mappings
}
