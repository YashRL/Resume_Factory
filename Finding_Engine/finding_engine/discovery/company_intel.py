"""Company Intel and Domain Resolution Module."""
import re
from typing import Optional
from urllib.parse import urlparse
from finding_engine.models import CompanyIntel
from finding_engine.verifier.dns_check import get_mx_records, detect_mail_provider


def clean_domain(url_or_domain: str) -> str:
    """Normalize input URL or domain string to clean domain (e.g. 'bolna.ai')."""
    text = url_or_domain.strip().lower()
    if not text.startswith("http://") and not text.startswith("https://"):
        text = "https://" + text
    
    parsed = urlparse(text)
    netloc = parsed.netloc or parsed.path
    # Strip www. and port
    domain = re.sub(r'^www\.', '', netloc).split('/')[0].split(':')[0]
    return domain


def resolve_domain(company_name: str, website_url: Optional[str] = None) -> str:
    """Intelligently resolve the canonical domain for a startup."""
    # 1. If explicit website URL given and not a job aggregator
    if website_url:
        domain = clean_domain(website_url)
        if domain not in ("workatastartup.com", "wellfound.com", "linkedin.com", "ycombinator.com"):
            return domain
        
        # If it's a YC or Wellfound slug
        slug_match = re.search(r'companies/([a-zA-Z0-9\-]+)|company/([a-zA-Z0-9\-]+)', website_url)
        if slug_match:
            slug = slug_match.group(1) or slug_match.group(2)
            slug_clean = slug.replace("-ai", "").replace("-", "")
            # Try slug.ai, slug.com, etc.
            for ext in [".ai", ".com", ".co", ".io"]:
                d = f"{slug.replace('-', '')}{ext}"
                if get_mx_records(d):
                    return d
                d_orig = f"{slug}{ext}"
                if get_mx_records(d_orig):
                    return d_orig

    # 2. Heuristic check based on company name
    clean_name = re.sub(r'[^a-zA-Z0-9]', '', company_name).lower()
    
    # Check if company name already ends with .ai, .com, etc. (e.g. "Optifye.ai", "Bolna AI", "Boock.ai")
    base_name = re.sub(r'\s*(ai|tech|hq|inc|labs|unlimited)\b', '', company_name, flags=re.IGNORECASE)
    base_clean = re.sub(r'[^a-zA-Z0-9]', '', base_name).lower()

    candidates = [
        f"{clean_name}.com",
        f"{clean_name}.ai",
        f"{clean_name}.co",
        f"{base_clean}.ai",
        f"{base_clean}.com",
        f"{base_clean}.co",
        f"{base_clean}ai.com",
    ]

    for cand in candidates:
        mx = get_mx_records(cand)
        if mx:
            return cand

    return f"{clean_name}.ai"


def gather_company_intel(company_name: str, website_url: Optional[str] = None) -> CompanyIntel:
    """Extract domain and email infrastructure details for a company."""
    domain = resolve_domain(company_name, website_url)
    mx_records = get_mx_records(domain)
    mail_provider = detect_mail_provider(mx_records)

    return CompanyIntel(
        name=company_name,
        domain=domain,
        website_url=f"https://{domain}" if domain else None,
        mx_records=mx_records,
        mail_provider=mail_provider
    )
