import json

def generate_provenance():
    return {
        "full_name": "CSV",
        "emails": "CSV + Resume",
        "phones": "CSV + Resume",
        "skills": "Resume",
        "current_company": "CSV",
        "title": "CSV"
    }


def project_output(candidate, config_path):
    with open(config_path, "r") as file:
        config = json.load(file)

    projected = {}

    for field in config["fields"]:
        if field in candidate:
            projected[field] = candidate[field]

    return projected