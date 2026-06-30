from models.schema import Candidate


def validate_candidate(candidate):
    try:
        validated = Candidate(**candidate)
        return validated
    except Exception as e:
        print("Validation Error:", e)
        return None