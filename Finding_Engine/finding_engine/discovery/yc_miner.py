"""Miner for Y Combinator / Work at a Startup companies."""
import re
import httpx
from bs4 import BeautifulSoup
from typing import List, Optional
from finding_engine.models import Person
from finding_engine.email_hunter.permutator import split_full_name


def extract_yc_slug(url: str) -> Optional[str]:
    """Extract company slug from YC / Work at a Startup URL."""
    match = re.search(r'companies/([a-zA-Z0-9\-]+)', url)
    if match:
        return match.group(1)
    return None


def mine_yc_profile(company_slug_or_url: str) -> List[Person]:
    """Scrape founders and team from YC company directory."""
    slug = extract_yc_slug(company_slug_or_url) or company_slug_or_url
    url = f"https://www.ycombinator.com/companies/{slug}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    people: List[Person] = []

    try:
        resp = httpx.get(url, headers=headers, follow_redirects=True, timeout=10.0)
        if resp.status_code != 200:
            return people

        soup = BeautifulSoup(resp.text, "html.parser")
        
        # Look for Active Founders section
        founder_blocks = soup.find_all("div", class_=re.compile(r'founder|leading-tight', re.I))
        
        # Look for headings or bold text that indicate founders
        for div in soup.select("h3, div.font-bold"):
            name_text = div.get_text(strip=True)
            # Find sibling or parent container
            parent = div.find_parent("div")
            if parent:
                parent_text = parent.get_text(" ", strip=True)
                if any(kw in parent_text.lower() for kw in ["founder", "ceo", "cto", "co-founder"]):
                    # Look for linkedin link inside parent
                    linkedin_link = None
                    for a in parent.find_all("a", href=True):
                        if "linkedin.com" in a["href"]:
                            linkedin_link = a["href"]
                            break
                    
                    first, last = split_full_name(name_text)
                    if first and len(first) > 1 and not any(p.full_name == name_text for p in people):
                        people.append(
                            Person(
                                full_name=name_text,
                                first_name=first,
                                last_name=last,
                                title="Founder",
                                role_category="executive",
                                linkedin_url=linkedin_link,
                                source="yc_directory"
                            )
                        )
    except Exception:
        pass

    return people
