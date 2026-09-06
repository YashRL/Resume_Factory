"""Core Finding Engine pipeline orchestrating discovery, permutations, and verification."""
import csv
import json
from pathlib import Path
from typing import List, Dict, Any, Optional
from rich.console import Console
from rich.table import Table

from finding_engine.models import EnrichedLead, Person, CompanyIntel, EmailStatus
from finding_engine.discovery.company_intel import gather_company_intel
from finding_engine.discovery.prospect_dorker import dork_people_for_company
from finding_engine.discovery.yc_miner import mine_yc_profile
from finding_engine.email_hunter.permutator import generate_email_permutations
from finding_engine.verifier.smtp_verifier import verify_email_smtp

import os
import sys

# Ensure UTF-8 output on Windows
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

console = Console(highlight=False)


def process_single_company(
    company_name: str,
    website_url: Optional[str] = None,
    job_target_role: Optional[str] = None,
    funding_stage: Optional[str] = None,
    job_url: Optional[str] = None,
    verify_smtp: bool = False
) -> EnrichedLead:
    """End-to-end prospecting for a single company."""
    console.print(f"[bold cyan]🔍 Prospecting Company:[/bold cyan] [bold white]{company_name}[/bold white]")

    # 1. Company Intel
    company_intel = gather_company_intel(company_name, website_url=website_url)
    console.print(f"   [dim]Domain: {company_intel.domain} | Mail Provider: {company_intel.mail_provider}[/dim]")

    # 2. People Discovery
    people: List[Person] = []
    
    # Try YC miner if applicable
    if website_url and ("ycombinator.com" in website_url or "workatastartup.com" in website_url):
        yc_people = mine_yc_profile(website_url)
        people.extend(yc_people)

    # Dork LinkedIn X-Ray
    xray_people = dork_people_for_company(company_name)
    for xp in xray_people:
        if not any(p.first_name == xp.first_name and p.last_name == xp.last_name for p in people):
            people.append(xp)

    console.print(f"   [green]Found {len(people)} key decision maker(s) / HR(s)[/green]")

    # 3. Email Permutations & Verification
    for person in people:
        perms = generate_email_permutations(person.first_name, person.last_name, company_intel.domain)
        verified_emails: List[EmailStatus] = []

        for email in perms:
            if verify_smtp:
                status = verify_email_smtp(email, domain=company_intel.domain, mx_records=company_intel.mx_records)
            else:
                status = EmailStatus(
                    email=email,
                    status="unverified",
                    confidence=0.7 if company_intel.mx_records else 0.2,
                    mx_valid=bool(company_intel.mx_records),
                    reason="Generated permutation"
                )
            verified_emails.append(status)
            if status.status == "valid":
                person.primary_email = status.email
                break  # found confirmed valid mailbox!

        person.emails = verified_emails
        if not person.primary_email and verified_emails:
            # Fallback to highest confidence / top permutation
            best = max(verified_emails, key=lambda x: x.confidence)
            person.primary_email = best.email

        console.print(f"     👤 [bold]{person.full_name}[/bold] ({person.title}) -> [yellow]{person.primary_email}[/yellow] [dim]({person.linkedin_url or 'No LI'})[/dim]")

    return EnrichedLead(
        company=company_intel,
        people=people,
        job_target_role=job_target_role,
        job_url=job_url,
        funding_stage=funding_stage
    )


def run_batch_from_csv(input_csv_path: str, output_csv_path: str, max_companies: Optional[int] = None) -> List[EnrichedLead]:
    """Process a list of companies from a CSV file (e.g. funded_ai_startup_jobs.csv)."""
    leads: List[EnrichedLead] = []
    
    with open(input_csv_path, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    if max_companies:
        rows = rows[:max_companies]

    console.print(f"[bold green]🚀 Starting Batch Prospecting for {len(rows)} companies...[/bold green]\n")

    flat_records = []

    for row in rows:
        company_name = row.get("company", "").strip()
        job_url = row.get("job_url", "").strip()
        funding_stage = row.get("funding_stage", "").strip()
        role_title = row.get("role_title", "").strip()

        if not company_name:
            continue

        lead = process_single_company(
            company_name=company_name,
            website_url=job_url,
            job_target_role=role_title,
            funding_stage=funding_stage,
            job_url=job_url
        )
        leads.append(lead)

        # Prepare flat rows for CSV export
        for person in lead.people:
            flat_records.append({
                "Company": lead.company.name,
                "Domain": lead.company.domain,
                "Mail_Provider": lead.company.mail_provider,
                "Person_Name": person.full_name,
                "Role_Title": person.title,
                "Category": person.role_category,
                "Primary_Email": person.primary_email,
                "Email_Status": person.emails[0].status if person.emails else "unknown",
                "Confidence": person.emails[0].confidence if person.emails else 0.0,
                "LinkedIn_URL": person.linkedin_url or "",
                "Target_Job_Role": lead.job_target_role or "",
                "Funding_Stage": lead.funding_stage or "",
                "Job_URL": lead.job_url or ""
            })

    # Save to CSV
    if flat_records:
        keys = flat_records[0].keys()
        with open(output_csv_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            writer.writerows(flat_records)
        console.print(f"\n[bold green]✅ Successfully exported enriched leads to {output_csv_path}[/bold green]")

    return leads
