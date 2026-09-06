from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field


class EmailStatus(BaseModel):
    email: str
    status: str = "unknown"  # valid, invalid, catch_all, risky, unverified
    confidence: float = 0.0  # 0.0 to 1.0
    mx_valid: bool = False
    smtp_check: Optional[bool] = None
    is_catch_all: Optional[bool] = None
    reason: str = ""


class Person(BaseModel):
    full_name: str
    first_name: str = ""
    last_name: str = ""
    title: str = ""  # e.g., Founder & CEO, CTO, Head of Talent
    role_category: str = "other"  # executive, engineering, talent_hr, other
    linkedin_url: Optional[str] = None
    twitter_url: Optional[str] = None
    github_url: Optional[str] = None
    emails: List[EmailStatus] = Field(default_factory=list)
    primary_email: Optional[str] = None
    source: str = "web_dork"


class CompanyIntel(BaseModel):
    name: str
    domain: str
    website_url: Optional[str] = None
    mx_records: List[str] = Field(default_factory=list)
    mail_provider: str = "unknown"  # google_workspace, microsoft_365, etc.
    is_catch_all: Optional[bool] = None
    detected_email_pattern: Optional[str] = None  # e.g. {first}.{last}@domain.com


class EnrichedLead(BaseModel):
    company: CompanyIntel
    people: List[Person] = Field(default_factory=list)
    job_target_role: Optional[str] = None
    job_url: Optional[str] = None
    funding_stage: Optional[str] = None
    notes: Optional[str] = None
