"""CLI interface for Finding Engine."""
import argparse
from pathlib import Path
from finding_engine.pipeline import process_single_company, run_batch_from_csv


def main():
    parser = argparse.ArgumentParser(description="Finding Engine - Decision Maker & Email Prospecting System")
    parser.add_argument("--company", type=str, help="Target company name (e.g. 'Ressl AI')")
    parser.add_argument("--domain", type=str, help="Target company domain/website (e.g. 'ressl.ai')")
    parser.add_argument("--csv", type=str, help="Path to input CSV file containing companies")
    parser.add_argument("--output", type=str, default="enriched_decision_makers.csv", help="Path to save enriched output CSV")
    parser.add_argument("--limit", type=int, default=None, help="Limit number of companies to process from CSV")
    parser.add_argument("--verify-smtp", action="store_true", help="Perform live SMTP handshake checks")

    args = parser.parse_args()

    if args.csv:
        run_batch_from_csv(args.csv, args.output, max_companies=args.limit)
    elif args.company:
        lead = process_single_company(args.company, website_url=args.domain, verify_smtp=args.verify_smtp)
        print(lead.model_dump_json(indent=2))
    else:
        # Default run on funded_ai_startup_jobs.csv if present
        default_csv = Path("../funded_ai_startup_jobs.csv")
        if default_csv.exists():
            run_batch_from_csv(str(default_csv), args.output, max_companies=5)
        else:
            parser.print_help()


if __name__ == "__main__":
    main()
