# Define enums
TRADE_OF_SERVICE_ENUM = [
    "Information Technology",
    "Design",
    "Administrative/Assistant",
    "Customer Service",
    "Human Resources",
    "Finance",
    "Accounting",
    "Sales",
    "Marketing",
    "Engineering/Project Management",
]
YEARS_OF_EXPERIENCE_ENUM = [
    "Not Specified",
    "0-3 Years",
    "3-6 Years",
    "6-9 Years",
    "9+ Years",
]
ENGLISH_LEVEL_ENUM = ["Not Specified", "A1", "A2", "B1", "B2", "C1", "C2"]

# Define the JSON Schemas
job_description_schema = {
    "title": "job_description",
    "description": "Data inferred from the job description input provided by the user. The inference is performed with a temperature setting of 0 for accuracy.",
    "type": "object",
    "properties": {
        "trade_of_service": {
            "type": "array",
            "items": {"type": "string", "enum": TRADE_OF_SERVICE_ENUM},
            "description": "The trade or industry in which the candidate have experience.",
        },
        "desired_roles": {
            "type": "array",
            "items": {"type": "string"},
            "description": "The specific roles or job titles desired for the candidate.",
        },
        "technologies": {
            "type": "array",
            "items": {"type": "string"},
            "description": "The technologies or tools the candidate should be proficient in.",
        },
        "years_of_experience": {
            "type": "object",
            "properties": {
                "min": {
                    "oneOf": [
                        {"type": "number"},
                        {"type": "string", "enum": ["Not Specified"]},
                    ],
                    "default": "Not Specified",
                    "description": "The minimum number of years of experience",
                },
                "max": {
                    "oneOf": [
                        {"type": "number"},
                        {"type": "string", "enum": ["Not Specified"]},
                    ],
                    "default": "Not Specified",
                    "description": "The maximum number of years of experience",
                },
            },
            "required": ["min", "max"],
        },
        "english_level": {
            "type": "array",
            "items": {
                "type": "string",
                "enum": ENGLISH_LEVEL_ENUM,
                "description": "The level of English proficiency required for the candidate.",
            },
        },
    },
    "required": [
        "trade_of_service",
        "desired_roles",
        "technologies",
        "years_of_experience",
        "english_level",
    ],
}

job_description_additional_options_schema = {
    "title": "job_description_additional_options",
    "description": "Your task is to recommend options similar to the job description but NOT THE SAME. These recommendations are generated with a higher temperature to provide a wider variety of options.",
    "type": "object",
    "properties": {
        "desired_roles": {
            "type": "array",
            "items": {"type": "string"},
            "minItems": 12,
            "maxItems": 30,
            "description": "Additional recommended roles or job titles for the candidate.",
        },
        "technologies": {
            "type": "array",
            "items": {"type": "string"},
            "minItems": 25,
            "maxItems": 50,
            "description": "Additional recommended technologies or tools for the candidate.",
        },
    },
    "required": [
        "desired_role",
        "technologies",
    ],
}
