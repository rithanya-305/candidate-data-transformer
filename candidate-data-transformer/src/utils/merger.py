from utils.normalizer import (
    normalize_email,
    normalize_phone,
    normalize_skills,
)

from utils.confidence import generate_confidence
from utils.projector import generate_provenance


def merge_candidate(csv_data, resume_data):

    profile = {
        "full_name": csv_data.get("full_name"),
        "emails": normalize_email(
            csv_data.get("emails", []) +
            resume_data.get("emails", [])
        ),
        "phones": normalize_phone(
            csv_data.get("phones", []) +
            resume_data.get("phones", [])
        ),
        "skills": normalize_skills(
            resume_data.get("skills", [])
        ),
        "current_company": csv_data.get("current_company"),
        "title": csv_data.get("title")
    }

    return {
        "candidate": profile,
        "confidence": generate_confidence(),
        "provenance": generate_provenance()
    }