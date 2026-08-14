# Resume Layout and Style Guidelines

This rule enforces the formatting and layout constraints for generating the candidate's resume (CV/Resume) in this workspace. Any AI agent or script modifying the templates or generating new resumes must strictly adhere to these rules.

## Core Rules

1. **Grayscale Aesthetic**: 
   - The resume must be completely black and white. 
   - No color gradients, HSL color definitions, or cyan/purple accents.
   - All text and borders must use pure black (`#000000`) or charcoal (`#333333`).

2. **Typography**:
   - Use a clean, standard sans-serif font stack: `"Liberation Sans", Arial, Helvetica, sans-serif`.
   - Font sizes must stay within `10.5px` to `11px` for the body, and `12px` for section headings.

3. **Centered Section Headings**:
   - All section titles (e.g., `Professional Summary`, `Skills`, `Work Experience`, `Projects`, `Education`, `Certifications`) must be **centered** on the page.
   - Do **NOT** place horizontal lines or borders underneath the section titles.

4. **Section Order**:
   - Resumes must follow this exact section order:
     1. Header (Centered Name and Contact Info row)
     2. Professional Summary
     3. Skills (Technical Skills)
     4. Work Experience
     5. Projects (Open Source & Security Research)
     6. Education
     7. Certifications
   - The `Core Competencies` section must be omitted. All competency keywords must be grouped under the `Skills` block instead.

5. **Experience Entries Alignment**:
   - **Company name**: Bold, left-aligned, on its own line.
   - **Job role and Period**: Job title (bold, left-aligned) and date range (regular, right-aligned) must be on the same horizontal line directly below the company name.
   - **Location**: Displayed below the job role line.
   - **Bullets**: Round black bullets (`●` or standard HTML `disc`).

6. **Education Entries Alignment**:
   - **Institution and Year**: School/University name (bold, left-aligned) and graduation years (regular, right-aligned) must be on the same horizontal line.
   - **Degree**: Left-aligned directly below the school name.

7. **Page Limits & Full Page Utilization**:
   - Tighten padding and margins so the CV fits neatly on exactly **one page**.
   - **Full Page Utilization (Compulsory)**: The resume must use the entire page. If space is freed (e.g., by collapsing education or removing a section), the reclaimed space must be filled intelligently by:
     - Adding a meaningful extra bullet to the most recent experience role.
     - Expanding a project description with an additional line of technical detail or outcome.
     - Adding a third skill category row if the JD warrants it.
     - Restoring previously pruned bullets that are still relevant.
   - Never leave more than half a line of whitespace at the bottom of the page. An empty bottom signals a wasted opportunity.

8. **Bullet Point Structure & Impact (Engineering Resumes Standard)**:
   - **Candidate's Writing Principle (What it is -> What I did -> What value it brings)**: Every bullet point must clearly outline:
     1. *What it is* (the context, problem, or technologies used).
     2. *What I did* (your specific action, design choice, or implementation).
     3. *What value it brings* (the qualitative and quantitative business or technical outcomes).
   - **Action-Result-Context (XYZ Formula)**: Bullet points under experience and projects must focus on outcomes and impact, not just daily tasks, structured using the format: *Accomplished [X], as measured by [Y], by doing [Z]* (e.g., specifying latency percentages, cost savings, user scale).
   - **Technical Trade-Offs**: Highlight specific engineering trade-offs (e.g., choosing a memory-mapped RAM-based router over database queries to avoid latency).
   - **Scope and Scale**: Clearly state the scale of responsibility (e.g., number of users, database sizes, or system throughput).
   - **No Rating Bars/Graphics**: Skills must be listed solely as comma-separated text categorized cleanly. Do **not** use visual progress bars, percentages, or rating tags to score candidate expertise.
   - **Open-Source Contributions**: Directly reference the repository name, role (e.g., Active Contributor), and specific issue or PR descriptions (e.g., PR #5711).

9. **Compulsory Competitive Differentiators (To Stand Out)**:
   - **Architectural Trade-Offs**: The resume must explicitly document system trade-offs (e.g., explaining why a custom architecture was built over off-the-shelf databases to solve resource/latency constraints).
   - **Evaluation & Infrastructure**: Do not focus on basic AI wrappers. High-impact bullets must show how you built evaluation control planes, testing harnesses, or dataset pipelines (e.g., Prompt Lab) to prove reliability at scale.
   - **Open-Source Contributions**: Highlight contributions to mainstream codebases (like Spring AI) with exact PR numbers, proving code quality meets global maintainer standards.
   - **Zero-to-One Scope & User Discovery**: Highlight direct involvement in user research, usability testing, and field discovery to bridge code execution with actual business workflows.

10. **Dynamic Skills Tailoring (Compulsory)**:
    - Do not list a static, generic set of skills.
    - **Pruning**: Remove skills, languages, or tools that are completely irrelevant to the job description (e.g., if a role is purely Python-based, reduce prominence of Java/SAP HANA or remove them if space is needed, unless they establish strong background).
    - **Targeted Addition**: Scan the JD and add the exact tools, databases, or frameworks requested (e.g., PySpark, AWS SageMaker, or CI/CD pipelines) provided the candidate has adjacent competency or if they are industry-standard for that role's archetype.
    - **Custom Categorization**: Group skills dynamically into context-specific categories matching the JD (e.g., separating "Data Engineering" or "Cloud & DevOps" into their own lines if the JD places high emphasis on them).

## Do's and Don'ts

### Do:
- **Keep it to one page**: Tighten line heights, margins, and padding to force all sections onto a single page.
- **Quantify impact**: Always include metrics (latency improvements, user scale, cost reductions, percentages).
- **Smart Job Title & Professional Identity Bridging (Compulsory)**: The first sentence of the Professional Summary must lead with the exact target job title from the JD, immediately followed by your core specialization (AI Platform/LLM Infrastructure Engineering). E.g., *"AI Engineer specialized in AI Platform Engineering and enterprise LLM infrastructure..."* to optimize ATS database indexing while preserving your true engineering identity.
- **Reference open-source PRs**: Provide repository name, role, and the specific PR number and context.
- **Maintain a clean typography hierarchy**: Use font weights (bold vs. regular) to distinguish companies, roles, and dates.
- **Follow the Writing Principle**: Structure every bullet point as: *What it is* -> *What I did* -> *What value it brings*.
- **Emphasize competitive differentiators**: Document architectural trade-offs, AI testing pipelines, user research, and open-source contributions.

### Don't:
- **Never use colors**: No colored text, colored borders, or background gradients.
- **Never add competency grids or rating bars**: Avoid rating candidate skills with dots, percentages, or stars.
- **Never include horizontal lines**: Do not place lines under section headings.
- **Never run multiple ReAct loops**: In description blocks, show how you optimized latency by consolidating agent executions.
- **Never list vague responsibilities**: Avoid "Responsible for writing backend APIs"—always explain *what* the API built and *why* it mattered.
- **Never mention confidential client names**: Never print client names like Lockheed Martin, Vodafone, European Patent Office, or EPO in the resume. Always use generic descriptions (e.g., *"a major aerospace client"*, *"a tier-1 telecom provider"*, or *"an international patent authority"*).
- **Never use inline bolding inside bullets**: Do not bold keywords, technologies, numbers, or phrases in the middle of bullet sentences to prevent visual clutter and maintain readability.
- **Never use multi-column layouts or text boxes**: Enforce a strict single-column document structure to ensure ATS parsing compatibility.

## Compulsory Pre-Compile Checklist
Every tailored resume must pass this verification list before compilation:
- [ ] Is the entire document strictly **black and white**?
- [ ] Are all section headers **centered** and **borderless**?
- [ ] Does the resume fit on **exactly one page** in the PDF output?
- [ ] Does the professional summary use **Smart Job Title & Identity Bridging** (exact target title + AI platform/infrastructure specialization)?
- [ ] Are technical skills listed purely as **comma-separated text** (no graphics)?
- [ ] Is the **Skills section dynamically tailored** (irrelevant skills pruned, JD-specific skills added, and grouped by role context)?
- [ ] Does the experience section use the **Company on line 1, Role + Date on line 2** format?
- [ ] Does every bullet point follow the **"What it is -> What I did -> What value it brings"** structure (with qualitative/quantitative value)?
- [ ] Does the resume highlight specific **architectural trade-offs** rather than just tool listings?
- [ ] Does the resume feature **AI evaluation/infrastructure work** rather than simple API wraps?
- [ ] Are **open-source contributions** mapped with exact PR/issue context?
- [ ] Is there proof of **zero-to-one user-centric delivery** (user research, usability testing)?
- [ ] Is there **zero inline bolding** inside the bullet points (plain text only)?
- [ ] Is the document layout strictly a **single-column format** (no text boxes or sidebars)?
- [ ] Are all **confidential client names** (Lockheed Martin, Vodafone, EPO, etc.) replaced with generic descriptors?
- [ ] Does the resume contain **zero placeholder text**?
