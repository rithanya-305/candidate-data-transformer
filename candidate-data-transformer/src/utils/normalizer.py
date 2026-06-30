import re


def normalize_email(emails):
    if not emails:
        return []

    return list(set(email.strip().lower() for email in emails))


def normalize_phone(phones):
    normalized = []

    for phone in phones:
        digits = re.sub(r"\D", "", phone)

        if len(digits) == 10:
            digits = "91" + digits

        normalized.append("+" + digits)

    return list(set(normalized))


def normalize_skills(skills):
    mapping = {
        "python": "Python",
        "node": "Node.js",
        "nodejs": "Node.js",
        "node.js": "Node.js",
        "react": "React",
        "mongodb": "MongoDB",
        "sql": "SQL",
        "javascript": "JavaScript"
    }

    normalized = []

    for skill in skills:
        key = skill.strip().lower()
        normalized.append(mapping.get(key, skill))

    return sorted(list(set(normalized)))