import re
import time
import warnings
from typing import List, Optional
warnings.filterwarnings("ignore")
try:
    from ddgs import DDGS
except ImportError:
    from duckduckgo_search import DDGS
from finding_engine.models import Person
from finding_engine.email_hunter.permutator import split_full_name


def parse_linkedin_title(raw_title: str) -> tuple[str, str]:
    """
    Parse LinkedIn result title e.g.:
    "Satya Nadella - Chairman and Chief Executive Officer - Microsoft | LinkedIn"
    Returns (Full Name, Title)
    """
    # Strip suffix like " | LinkedIn" or " - LinkedIn"
    clean = re.sub(r'\s*[-|•]\s*LinkedIn.*$', '', raw_title, flags=re.IGNORECASE).strip()
    
    # Split by hyphen or pipe or colon or ' - '
    parts = re.split(r'\s*[-|–—]\s*', clean)
    if len(parts) >= 2:
        name = parts[0].strip()
        title = parts[1].strip()
        return name, title
    elif len(parts) == 1:
        return parts[0].strip(), "Leader"
    return "", ""


def dork_people_for_company(company_name: str, max_results_per_role: int = 2) -> List[Person]:
    """
    Search for key executives and talent leaders for a company via LinkedIn X-Ray.
    """
    roles_queries = [
        ("executive", f'site:linkedin.com/in "{company_name}" ("CEO" OR "Founder" OR "Co-founder" OR "President")'),
        ("engineering", f'site:linkedin.com/in "{company_name}" ("CTO" OR "VP of Engineering" OR "Head of Engineering" OR "Director of Engineering")'),
        ("talent_hr", f'site:linkedin.com/in "{company_name}" ("Head of Talent" OR "Technical Recruiter" OR "Talent Acquisition" OR "Recruiter")')
    ]

    found_people: List[Person] = []
    seen_names = set()

    with DDGS() as ddgs:
        for category, query in roles_queries:
            try:
                results = list(ddgs.text(query, max_results=max_results_per_role))
                for item in results:
                    title_text = item.get("title", "")
                    href = item.get("href", "")
                    body = item.get("body", "")

                    if "linkedin.com/in/" not in href:
                        continue

                    name, extracted_title = parse_linkedin_title(title_text)
                    first, last = split_full_name(name)

                    if not first or len(first) < 2 or first.lower() in ("linkedin", "profiles", "top"):
                        continue

                    # Filter out if company name is not mentioned in snippet or title
                    combined_text = f"{title_text} {body}".lower()
                    if company_name.lower() not in combined_text:
                        continue

                    name_key = f"{first}_{last}".lower()
                    if name_key in seen_names:
                        continue
                    seen_names.add(name_key)

                    found_people.append(
                        Person(
                            full_name=f"{first} {last}".strip(),
                            first_name=first,
                            last_name=last,
                            title=extracted_title if extracted_title else category.replace("_", " ").title(),
                            role_category=category,
                            linkedin_url=href,
                            source="linkedin_xray"
                        )
                    )
                time.sleep(0.5)  # respectful delay
            except Exception:
                continue

    return found_people
