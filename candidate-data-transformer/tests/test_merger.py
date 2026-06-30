import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))

from utils.merger import merge_candidate


def test_merge_candidate():

    csv_data = {
        "full_name": "Rithanya",
        "emails": ["rithanya@example.com"],
        "phones": ["9876543210"],
        "current_company": "OpenAI",
        "title": "Software Engineer"
    }

    resume_data = {
        "emails": ["rithanya@example.com"],
        "phones": ["+919876543210"],
        "skills": ["Python", "React"]
    }

    result = merge_candidate(csv_data, resume_data)

    assert result["candidate"]["full_name"] == "Rithanya"
    assert "Python" in result["candidate"]["skills"]
    assert result["candidate"]["phones"][0] == "+919876543210"