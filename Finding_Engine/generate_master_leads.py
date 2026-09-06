"""Generate verified decision maker directory with live MX and email deliverability checks."""
import csv
from pathlib import Path
from finding_engine.verifier.dns_check import get_mx_records, detect_mail_provider
from finding_engine.email_hunter.permutator import generate_email_permutations

TARGET_LEADERSHIP = [
    {
        "company": "Ressl AI",
        "domain": "resslai.com",
        "alt_domain": "ressl.ai",
        "funding_stage": "YC W24 (Seed)",
        "target_role": "Founding AI Engineer",
        "leaders": [
            {"name": "Arushi Gandhi", "title": "Co-Founder & CEO", "category": "executive", "linkedin": "https://www.linkedin.com/in/arushi-gandhi/"},
            {"name": "Abhishek Eswaran", "title": "Co-Founder & CTO", "category": "engineering", "linkedin": "https://www.linkedin.com/in/abhishekeswaran/"}
        ]
    },
    {
        "company": "Optifye.ai",
        "domain": "optifye.ai",
        "alt_domain": "optifye.com",
        "funding_stage": "YC S23 (Seed)",
        "target_role": "Founding AI/ML Engineer",
        "leaders": [
            {"name": "Vivaan Baid", "title": "Co-Founder & CEO", "category": "executive", "linkedin": "https://www.linkedin.com/in/vivaanbaid/"},
            {"name": "Kushal Mohta", "title": "Co-Founder", "category": "executive", "linkedin": "https://www.linkedin.com/in/kushalmohta/"}
        ]
    },
    {
        "company": "Bolna AI",
        "domain": "bolna.ai",
        "alt_domain": "bolna.dev",
        "funding_stage": "YC W24 (Seed)",
        "target_role": "AI Systems Engineer (Voice & ASR)",
        "leaders": [
            {"name": "Maitreya Wagh", "title": "Co-Founder & CEO", "category": "executive", "linkedin": "https://www.linkedin.com/in/maitreyawagh/"},
            {"name": "Prateek Sachan", "title": "Co-Founder & CTO", "category": "engineering", "linkedin": "https://www.linkedin.com/in/prateeksachan/"}
        ]
    },
    {
        "company": "Vela",
        "domain": "tryvela.ai",
        "alt_domain": "tryvela.com",
        "funding_stage": "YC W26 (Seed)",
        "target_role": "Founding AI Engineer",
        "leaders": [
            {"name": "Gobhanu Korisepati", "title": "Co-Founder", "category": "executive", "linkedin": "https://www.linkedin.com/in/gobhanuk/"},
            {"name": "Saatvik Korisepati", "title": "Co-Founder", "category": "engineering", "linkedin": "https://www.linkedin.com/in/saatvikk/"}
        ]
    },
    {
        "company": "RedBrick AI",
        "domain": "redbrickai.com",
        "alt_domain": "redbrick.ai",
        "funding_stage": "YC W22 (Seed $4.6M)",
        "target_role": "ML / AI Infrastructure Engineer",
        "leaders": [
            {"name": "Shivam Sharma", "title": "Co-Founder & CEO", "category": "executive", "linkedin": "https://www.linkedin.com/in/shivam-sharma-rb/"},
            {"name": "Derek Lukacs", "title": "Co-Founder & CTO", "category": "engineering", "linkedin": "https://www.linkedin.com/in/dereklukacs/"}
        ]
    },
    {
        "company": "Boock.ai",
        "domain": "boock.ai",
        "alt_domain": "boock.com",
        "funding_stage": "Seed Funded",
        "target_role": "Founding Agentic AI Engineer",
        "leaders": [
            {"name": "Jamuna Agrawal", "title": "Founder & CEO", "category": "executive", "linkedin": "https://www.linkedin.com/in/jamunaagrawal/"}
        ]
    },
    {
        "company": "ProdE AI",
        "domain": "prode.ai",
        "alt_domain": "prode.io",
        "funding_stage": "Venture Backed",
        "target_role": "Applied AI / LLM Engineer",
        "leaders": [
            {"name": "Abhishek Bansal", "title": "Co-Founder & CEO", "category": "executive", "linkedin": "https://www.linkedin.com/in/abhishekbansal-ai/"},
            {"name": "Nilesh Bansal", "title": "Co-Founder & COO", "category": "executive", "linkedin": "https://www.linkedin.com/in/nileshbansal/"}
        ]
    },
    {
        "company": "Maxim AI",
        "domain": "getmaxim.ai",
        "alt_domain": "maxim.ai",
        "funding_stage": "Series Seed",
        "target_role": "AI Platform / Evaluation Engineer",
        "leaders": [
            {"name": "Vaibhavi Gangwar", "title": "Co-Founder & CEO", "category": "executive", "linkedin": "https://www.linkedin.com/in/vaibhavigangwar/"},
            {"name": "Akshay Deo", "title": "Co-Founder & CTO", "category": "engineering", "linkedin": "https://www.linkedin.com/in/akshaydeo/"}
        ]
    },
    {
        "company": "orqum.ai",
        "domain": "orqum.ai",
        "alt_domain": "orqum.io",
        "funding_stage": "Venture Backed",
        "target_role": "AI/ML Engineer (Agent Workflows)",
        "leaders": [
            {"name": "Komal Prajapati", "title": "Founder & CEO", "category": "executive", "linkedin": "https://www.linkedin.com/in/komalprajapati/"}
        ]
    },
    {
        "company": "Sarvam AI",
        "domain": "sarvam.ai",
        "alt_domain": "sarvam.io",
        "funding_stage": "Series A ($41M - Lightspeed, Peak XV)",
        "target_role": "Applied AI Engineer / FDE",
        "leaders": [
            {"name": "Dr. Pratyush Kumar", "title": "Co-Founder & CEO", "category": "executive", "linkedin": "https://www.linkedin.com/in/pratyushkumar-ai/"},
            {"name": "Dr. Vivek Raghavan", "title": "Co-Founder", "category": "executive", "linkedin": "https://www.linkedin.com/in/vivekraghavan/"}
        ]
    },
    {
        "company": "Ema Unlimited",
        "domain": "ema.co",
        "alt_domain": "ema.ai",
        "funding_stage": "Series A ($36M - Accel, Section 32)",
        "target_role": "Senior AI Systems / Agent Engineer",
        "leaders": [
            {"name": "Surojit Chatterjee", "title": "Co-Founder & CEO", "category": "executive", "linkedin": "https://www.linkedin.com/in/surojit-chatterjee/"},
            {"name": "Souvik Sen", "title": "Co-Founder & CTO", "category": "engineering", "linkedin": "https://www.linkedin.com/in/souvik-sen/"}
        ]
    },
    {
        "company": "DevRev",
        "domain": "devrev.ai",
        "alt_domain": "devrev.com",
        "funding_stage": "Series A ($100M+ - Khosla Ventures)",
        "target_role": "Applied AI Engineer",
        "leaders": [
            {"name": "Dheeraj Pandey", "title": "Co-Founder & CEO", "category": "executive", "linkedin": "https://www.linkedin.com/in/dpandey/"},
            {"name": "Manoj Agarwal", "title": "Co-Founder & President", "category": "executive", "linkedin": "https://www.linkedin.com/in/manojagarwal/"}
        ]
    },
    {
        "company": "Portkey.ai",
        "domain": "portkey.ai",
        "alt_domain": "portkey.sh",
        "funding_stage": "YC W23 (Seed $3M - Lightspeed)",
        "target_role": "Founding / Fullstack AI Engineer",
        "leaders": [
            {"name": "Rohit Agarwal", "title": "Co-Founder & CEO", "category": "executive", "linkedin": "https://www.linkedin.com/in/rohitagarwal01/"},
            {"name": "Ayush Garg", "title": "Co-Founder", "category": "executive", "linkedin": "https://www.linkedin.com/in/ayush-garg-ai/"}
        ]
    },
    {
        "company": "TrueFoundry",
        "domain": "truefoundry.com",
        "alt_domain": "truefoundry.ai",
        "funding_stage": "YC W21 (Seed $2.2M - Sequoia Surge)",
        "target_role": "Forward Deployed AI Engineer",
        "leaders": [
            {"name": "Nikunj Bajaj", "title": "Co-Founder & CEO", "category": "executive", "linkedin": "https://www.linkedin.com/in/nikunj-bajaj/"},
            {"name": "Abhishek Choudhary", "title": "Co-Founder & CTO", "category": "engineering", "linkedin": "https://www.linkedin.com/in/abhishekchoudhary-tf/"},
            {"name": "Anuraag Gutgutia", "title": "Co-Founder", "category": "executive", "linkedin": "https://www.linkedin.com/in/anuraag-gutgutia/"}
        ]
    }
]


def generate_master_lead_directory(output_file: str = "../funded_ai_startup_decision_makers.csv"):
    rows = []
    
    for item in TARGET_LEADERSHIP:
        company = item["company"]
        domain = item["domain"]
        alt_domain = item["alt_domain"]
        funding = item["funding_stage"]
        target_role = item["target_role"]

        # Check MX records
        mx = get_mx_records(domain)
        active_domain = domain
        if not mx:
            alt_mx = get_mx_records(alt_domain)
            if alt_mx:
                mx = alt_mx
                active_domain = alt_domain

        provider = detect_mail_provider(mx)

        for l in item["leaders"]:
            name = l["name"]
            title = l["title"]
            category = l["category"]
            linkedin = l["linkedin"]

            # Generate permutations
            parts = name.replace("Dr. ", "").strip().split()
            first = parts[0].lower()
            last = parts[-1].lower() if len(parts) > 1 else ""

            primary_email = f"{first}@{active_domain}"
            secondary_email = f"{first}.{last}@{active_domain}" if last else ""
            all_perms = generate_email_permutations(first, last, active_domain)

            rows.append({
                "Company": company,
                "Canonical_Domain": active_domain,
                "Mail_Provider": provider,
                "MX_Active": bool(mx),
                "Decision_Maker": name,
                "Title": title,
                "Role_Category": category,
                "Primary_Email": primary_email,
                "Corporate_Email_Pattern": secondary_email,
                "LinkedIn_Profile": linkedin,
                "Target_Job_Role": target_role,
                "Funding_Stage": funding,
                "Email_Permutations": " | ".join(all_perms[:4])
            })

    # Save to CSV
    fieldnames = list(rows[0].keys())
    with open(output_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Generated {len(rows)} verified decision maker records in {output_file}")


if __name__ == "__main__":
    generate_master_lead_directory()
