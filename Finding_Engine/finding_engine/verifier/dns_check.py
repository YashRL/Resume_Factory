import dns.resolver
from typing import List, Tuple


def get_mx_records(domain: str) -> List[str]:
    """Retrieve prioritized MX records for a domain."""
    try:
        answers = dns.resolver.resolve(domain, 'MX')
        # Sort MX records by preference
        sorted_records = sorted(answers, key=lambda r: r.preference)
        return [str(r.exchange).rstrip('.') for r in sorted_records]
    except Exception:
        return []


def detect_mail_provider(mx_records: List[str]) -> str:
    """Identify the email service provider hosting the domain."""
    mx_str = " ".join(mx_records).lower()
    if "google" in mx_str or "aspmx" in mx_str:
        return "google_workspace"
    if "outlook" in mx_str or "microsoft" in mx_str:
        return "microsoft_365"
    if "zoho" in mx_str:
        return "zoho"
    if "protonmail" in mx_str or "proton" in mx_str:
        return "protonmail"
    if "improvmx" in mx_str or "forwardemail" in mx_str:
        return "forwarder"
    if mx_records:
        return "custom_mx"
    return "no_mx"
