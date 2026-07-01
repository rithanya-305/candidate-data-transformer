# Candidate Data Transformer

## Overview

The Candidate Data Transformer is a modular data processing pipeline designed to consolidate candidate information originating from multiple heterogeneous sources into a single canonical candidate profile.

Recruitment workflows often involve information arriving from various systems such as recruiter exports, resumes, applicant tracking systems, and external profile sources. These sources frequently contain duplicate records, inconsistent formatting, incomplete information, and conflicting values.

This project addresses these challenges by implementing a deterministic transformation pipeline capable of extracting, normalizing, validating, and merging candidate information while maintaining complete transparency regarding data origin and confidence levels.

The final output is a standardized JSON representation that can be consumed by downstream recruitment systems, applicant tracking platforms, or analytics pipelines.

---

## Problem Statement

Candidate information typically exists across multiple systems and formats.

For example:

- Recruiters maintain spreadsheets containing candidate contact details.
- Candidates submit resumes containing technical skills and experience.
- External platforms contain additional profile information.

Combining this information manually is time consuming and error prone.

The objective of this project is to automate the transformation process while ensuring:

- Consistency
- Explainability
- Traceability
- Configurability
- Data Quality

---

## System Design Philosophy

The implementation follows three fundamental principles:

### Deterministic Processing

The system avoids probabilistic assumptions whenever possible and instead relies on deterministic extraction and merging strategies.

### Explainability

Every generated field includes provenance information describing where the value originated from and how it was generated.

### Configurability

Output schemas are externally configurable without requiring changes to application code.

---

## Multi Source Data Ingestion

The pipeline supports candidate information originating from multiple heterogeneous sources.

### Structured Source

The CSV input represents recruiter-generated candidate information and typically contains highly reliable contact and employment information.

Example fields include:

- Candidate Name
- Email Address
- Phone Number
- Current Company
- Job Title

### Unstructured Source

The Resume PDF represents candidate-generated information and typically contains detailed information regarding:

- Technical Skills
- Education
- Professional Experience
- Certifications
- Project Experience

Supporting both structured and unstructured sources demonstrates the ability of the system to process heterogeneous data inputs.

---

## Extraction Strategy

Each source is processed independently using source-specific extraction logic.

Structured sources use direct field extraction techniques, while unstructured sources use text extraction and pattern matching approaches.

The separation of extraction logic allows additional sources to be integrated into the pipeline without affecting downstream processing stages.

This modular design significantly improves maintainability and extensibility.

---

## Normalization Strategy

Different sources frequently represent the same information using different formats.

Examples include:

| Original Value | Standardized Value |
|---------------|-------------------|
| RITHANYA@MAIL.COM | rithanya@mail.com |
| 9876543210 | +919876543210 |
| nodejs | Node.js |

Normalization improves consistency and reduces duplicate records during candidate profile generation.

---

## Candidate Resolution and Merge Strategy

After extraction and normalization, the pipeline generates a canonical candidate profile.

The merge process performs:

- Duplicate removal
- Missing value completion
- Standardization
- Consolidation of candidate attributes

The final profile represents the best available representation of the candidate across all available sources.

---

## Confidence Scoring

The system assigns confidence values to extracted information to indicate the reliability of each attribute.

Confidence scores provide downstream systems with additional context regarding the trustworthiness of extracted information.

Example confidence scores include:

| Field | Confidence |
|-------|------------|
| Name | 0.99 |
| Email | 1.00 |
| Phone | 0.98 |
| Skills | 0.95 |

---

## Provenance Tracking

Every generated field maintains provenance information describing:

- Source of information
- Extraction mechanism
- Processing stage

This provides complete traceability and enables explainable data transformations.

Example:

| Field | Source |
|-------|--------|
| Name | CSV |
| Emails | CSV + Resume |
| Skills | Resume |

---

## Runtime Configurable Output

The system implements a projection layer that allows output schemas to be dynamically modified using configuration files.

This enables different consumers of the candidate profile to receive only the fields relevant to their use case without requiring code modifications.

The implementation currently supports:

- `default.json`
- `custom.json`

This design improves maintainability and supports future extensibility.

---

## Validation Strategy

Prior to export, all candidate profiles are validated using Pydantic schema models.

Validation ensures:

- Required fields exist.
- Data types are correct.
- Invalid records are rejected.
- Schema consistency is maintained.

This significantly improves data reliability.

---

## Testing Strategy

The project includes automated unit tests implemented using PyTest.

The test suite validates:

- Merge Logic
- Normalization Functions
- Candidate Profile Generation
- Output Consistency

Testing ensures long-term maintainability and reduces regression risk during future development.

---

## Scalability Considerations

The modular architecture allows additional components to be introduced with minimal impact on existing functionality.

Potential future extensions include:

- LinkedIn integration
- GitHub profile ingestion
- OCR support for scanned resumes
- LLM-based skill extraction
- REST API support
- Database persistence

---

## Deliverables

The final submission includes:

- ✅ Source Code
- ✅ README Documentation
- ✅ One Page Design PDF
- ✅ Unit Tests
- ✅ Generated Output Files
- ✅ Demo Video
## Author
Rithanya R
