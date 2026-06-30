from pydantic import BaseModel
from typing import List


class Candidate(BaseModel):
    full_name: str
    emails: List[str]
    phones: List[str]
    skills: List[str]
    current_company: str
    title: str