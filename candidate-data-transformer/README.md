# Candidate Data Transformer

## Overview

Candidate Data Transformer is a Python-based application that consolidates candidate information from multiple data sources into a single canonical JSON profile.

The application supports:
- Structured data (CSV)
- Unstructured data (Resume PDF)

It normalizes, merges, validates, and projects candidate information using runtime configuration files.

---

## Features

- Parse candidate information from CSV
- Parse Resume PDF
- Normalize emails, phone numbers, and skills
- Merge multiple data sources
- Generate a canonical candidate profile
- Confidence scoring
- Provenance tracking
- Runtime configurable output
- Pydantic validation
- JSON export
- Command Line Interface (CLI)

---

## Project Structure

```
candidate-data-transformer/

config/
    default.json
    custom.json

data/
    sample.csv
    resume.pdf

output/

src/
    main.py

    parsers/
        csv_parser.py
        resume_parser.py

    utils/
        confidence.py
        merger.py
        normalizer.py
        projector.py
        validator.py

    models/
        schema.py

tests/

README.md
requirements.txt
```

---

## Installation

Create a virtual environment

```bash
python -m venv venv
```

Activate it

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Project

Default configuration

```bash
python src/main.py
```

Custom configuration

```bash
python src/main.py --config-file config/custom.json
```

---

## Sample Output

```json
{
    "full_name": "Rithanya",
    "emails": [
        "rithanya@example.com"
    ],
    "phones": [
        "+919876543210"
    ],
    "skills": [
        "MongoDB",
        "Node.js",
        "Python",
        "React",
        "SQL"
    ],
    "current_company": "OpenAI",
    "title": "Software Engineer"
}
```

---

## Technologies Used

- Python
- Pandas
- PyMuPDF
- Pydantic
- Typer

---

## Future Improvements

- Support LinkedIn API
- Support GitHub API
- AI-based resume parsing
- Database integration
- REST API support

---

## Author

Rithanya R