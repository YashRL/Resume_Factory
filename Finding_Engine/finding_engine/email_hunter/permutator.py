"""Email Hunter permutations generator."""
import re
from typing import List, Tuple


def clean_name_part(text: str) -> str:
    """Normalize names (remove special characters, honorifics, etc.)."""
    text = text.lower().strip()
    # Remove common honorifics/prefixes
    text = re.sub(r'^(dr|mr|ms|mrs|prof)\.?\s+', '', text)
    # Remove emojis, brackets, non-alphanumeric except hyphen
    text = re.sub(r'[^a-z0-9\-]', '', text)
    return text


def split_full_name(full_name: str) -> Tuple[str, str]:
    """Extract first and last name from full name."""
    clean = re.sub(r'\s*[\(\[].*?[\)\]]', '', full_name).strip()  # remove (he/him), etc.
    # Remove credentials like PhD, MBA, etc.
    clean = re.sub(r',.*$', '', clean).strip()
    parts = [clean_name_part(p) for p in clean.split() if clean_name_part(p)]
    
    if not parts:
        return "", ""
    if len(parts) == 1:
        return parts[0], ""
    return parts[0], parts[-1]


def generate_email_permutations(first_name: str, last_name: str, domain: str) -> List[str]:
    """
    Generate standard enterprise and startup email address patterns.
    Returns prioritized list based on startup & enterprise statistical likelihood.
    """
    f = clean_name_part(first_name)
    l = clean_name_part(last_name)
    d = domain.lower().strip().replace("https://", "").replace("http://", "").split("/")[0]

    if not d:
        return []

    permutations = []

    if f and l:
        # Standard corporate & startup prioritized list
        permutations.extend([
            f"{f}@{d}",                 # Top for startups (< 30 people)
            f"{f}.{l}@{d}",              # Top for Series A+ / Enterprise
            f"{f}{l[0]}@{d}",            # e.g. yashr@
            f"{f[0]}{l}@{d}",            # e.g. yrawal@
            f"{f}{l}@{d}",               # e.g. yashrawal@
            f"{f}_{l}@{d}",              # e.g. yash_rawal@
            f"{l}@{d}",                  # e.g. rawal@
            f"{f[0]}.{l}@{d}",           # e.g. y.rawal@
            f"{l}.{f}@{d}",              # e.g. rawal.yash@
        ])
    elif f:
        permutations.append(f"{f}@{d}")
    elif l:
        permutations.append(f"{l}@{d}")

    # Remove duplicates while preserving priority order
    seen = set()
    result = []
    for email in permutations:
        if email not in seen:
            seen.add(email)
            result.append(email)

    return result
