# 🏭 Resume Factory

> **Tailored, ATS-optimised, single-page resumes compiled in seconds — powered by AI and the career-ops pipeline.**

---

## What this is

Resume Factory is a personal AI-powered resume compilation system built on top of the open-source **career-ops** pipeline. It produces per-role, per-company PDFs that are:

- ✅ **100% ATS-keyword matched** (verified with automated scoring)
- 📄 **Exactly one page** (hard constraint, enforced at compile time)
- 🎯 **Dynamically tailored** — skills, summary, and bullets re-prioritised per JD
- 🚫 **Zero gray text** — all copy is solid `#000000` for ATS parsers
- 🔐 **Client-confidential** — no client names appear in resume content

---

## Project Structure

```
Resume_Factory/
├── career-ops/              # Core pipeline (see credits below)
│   ├── batch/               # Per-company CV JSON data files
│   │   ├── cv-yash-rawal-anthropic.json
│   │   ├── cv-yash-rawal-barclays.json
│   │   └── cv-yash-rawal-vodafone.json
│   ├── templates/           # HTML/CSS resume templates
│   │   ├── cv-template.html
│   │   ├── resume-template.html
│   │   └── sections/        # Modular section partials
│   ├── jds/                 # Job description markdown files
│   ├── output/              # Compiled HTML + PDF resumes
│   ├── build-cv-html.mjs    # HTML compilation script
│   └── generate-pdf.mjs     # Puppeteer PDF renderer
├── .agents/
│   └── rules/
│       └── resume_style.md  # House style rules (ATS, layout, content)
└── Career_Info/             # Raw career data (experience, projects, certs)
```

---

## Resume Compilation

```bash
# Build HTML from a batch JSON
node build-cv-html.mjs batch/cv-yash-rawal-vodafone.json output/cv-yash-rawal-vodafone.html

# Render to PDF
node generate-pdf.mjs output/cv-yash-rawal-vodafone.html output/cv-yash-rawal-vodafone.pdf --format=letter
```

---

## House Style Rules

Key enforced constraints:

| Rule | Constraint |
|:---|:---|
| Single column | No two-column layouts — ATS parsers read top-to-bottom |
| No gray text | All text `#000000` — ATS optical parsers reject low-contrast |
| Exact 1 page | Margins and content pruned to fill exactly one page |
| Full page utilisation | Freed space must be filled (extra bullets, 3rd skills row, etc.) |
| Dynamic skills | Skills pruned/added per JD — no static list ever submitted |
| Smart title bridging | Header title matches JD target role for ATS indexing |
| No bold inside bullets | Bold inside bullets breaks ATS token parsing |
| No client names | Past client names never appear in resume copy |

---

## Credits

### career-ops — Original Pipeline

This project is built on top of **[career-ops](https://github.com/santifer/career-ops)**, an open-source AI-powered job search pipeline.

**Original Author:**
**Santiago Fernández de Valderrama**
🌐 [santifer.io](https://santifer.io)
📦 [github.com/santifer/career-ops](https://github.com/santifer/career-ops)

> career-ops is a multi-CLI job-search command center supporting CV generation, ATS scanning, application tracking, interview prep, and outreach automation. Licensed under **MIT**.

All modifications, custom templates, style rules, and batch data in this repository are original work layered on top of the career-ops foundation.

---

## License

The `career-ops/` subdirectory retains its original **MIT License** (see [`career-ops/LICENSE`](career-ops/LICENSE)).

All other files in this repository (`batch/`, `.agents/`, `Career_Info/`, templates) are personal and not for redistribution.
