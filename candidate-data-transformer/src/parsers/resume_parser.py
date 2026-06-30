import fitz
import re

def parse_resume(file_path):
    try:
        doc = fitz.open(file_path)

        text = ""

        for page in doc:
            text += page.get_text()

        emails = re.findall(r'[\w\.-]+@[\w\.-]+', text)

        phones = re.findall(r'(?:\+91[\s-]?)?[6-9]\d{9}', text)

        known_skills = [
            "Python",
            "React",
            "Node.js",
            "MongoDB",
            "SQL",
            "Java",
            "JavaScript",
            "C++"
        ]

        skills = []

        for skill in known_skills:
            if skill.lower() in text.lower():
                skills.append(skill)

        return {
            "text": text,
            "emails": emails,
            "phones": phones,
            "skills": skills
        }

    except Exception as e:
        print(e)