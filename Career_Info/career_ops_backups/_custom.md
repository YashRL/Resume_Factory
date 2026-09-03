# Custom Instructions -- career-ops

<!-- ============================================================
     THIS FILE IS YOURS. It will NEVER be auto-updated.

     Put your own house rules, custom workflows, and automations
     here -- anything you want the agent to ALWAYS do (or never do).

     This is for PROCEDURAL rules ("HOW I want things done").
     For WHO you are (archetypes, narrative, comp, negotiation),
     use modes/_profile.md instead. Keeping the two separate keeps
     each one readable.

     The agent reads this file alongside the system instructions;
     your rules here take precedence over the defaults, as long as
     they don't break the Data Contract (your files are never
     touched, and we never auto-submit an application for you).

     Because this is a user-layer file, anything you write here
     survives `node update-system.mjs`. Put customizations HERE,
     not in CLAUDE.md / modes/_shared.md / other system files --
     those get overwritten on update.
     ============================================================ -->

## House Rules

<!-- Rules the agent should always follow. Examples:
     - Always write evaluation summaries in British English.
     - Never include a photo in my CV (US / ATS-first market).
     - Cap each batch run at 20 listings unless I say otherwise.
     - If a report scores below 6, skip the cover letter. -->

(none yet -- add yours above)

- **Strict Company Naming (Pure Bigscal Technologies Pvt. Ltd.)**: Across ALL resumes, cover letters, portals, and application payloads, ALWAYS use **`Bigscal Technologies Pvt. Ltd.`** ONLY for both the current AI/ML Engineer role and the AI/ML Engineer Intern role. NEVER append client names (e.g., `(Client: TalenTeam Ltd., UK)`) or product names (e.g., `(Product: Healthray)`). Zero client references on the employer line.
- **Professional Identity & Title**: Always identify the candidate as an **Applied AI & Machine Learning Engineer** (never use "AI Platform Engineer" or "AI System Engineer").
- **Balanced All-Rounder Profile (50-50 Applied AI & Core ML)**: Always frame the candidate's skills and experience to show a balanced 50-50% mix between Applied AI (agent runtimes, RAG, MCP, n8n, Spring AI) and Core Machine Learning (model fine-tuning, training, GPU optimization, signal processing, ASR/TTS, NER token-classification).
- **Scale-First Professional Summary**: The Professional Summary must lead with enterprise scale metrics (e.g., 1M+ active users, 120+ ERP organizations, enterprise agentic platform) first, followed directly by core model training and machine learning engineering.
- **Strong Engineering Verbs**: Never use weak or passive descriptors like "Built local POCs," "Assisted," "Helped," or "Worked on." Use authoritative engineering verbs such as "Engineered," "Designed," "Optimized," "Architected," and "Trained" to represent internship and project work.
- **Pre-Tuning Applied AI Logic**: If a job post is focused only on Applied AI, frame it to show that the candidate tunes and trains the models first (SFT, triplet contrastive training, quantization), then builds the applied agentic systems on top of them. Do not let the profile look like a simple API-wrapper developer.
- **One Bold Highlight per Experience Bullet**: Each bullet in the work experience section must contain strictly **one** bold highlight to ensure balanced visual hierarchy and maximum scanning readability:
  1. Bullet 1: `**1M+ active ERP users**`
  2. Bullet 2: `**3x**` (do not bold 70%)
  3. Bullet 3: `**Qwen2.5-7B**`
  4. Bullet 4: `**Human Feedback (RLHF) Pipeline**`
  5. Bullet 5: `**90%+ Recall@10**`
  6. Bullet 6: `**automated PII redaction**`
- **No Line Wrap for Long Bold Phrases**: If a highlighted term or phrase is long (e.g., `**Human Feedback (RLHF) Pipeline**`, `**Principal Creator & Architect**`, `**1M+ active ERP users**`), it must not wrap across a line break to a second line. Format the surrounding sentence text or adjust sentence structure to ensure these bold phrases sit cleanly on a single line.
- **Context Loading of Projects.txt**: Always read and incorporate the full project inventory context from [Projects.txt](file:///D:/Yash_Code/Resume_Factory/Career_Info/Projects.txt) during tailoring. Use these granular details (such as n8n routing workflows, pgvector indexing, SpaCy NER models, and model parameters) to match the target JD's requirements with the most relevant and high-signal achievements from your actual career history.
- **Priority-Ordering of Technical Skills**: During CV tailoring, you must reorder items inside the skill category lists (Languages & Backend, AI & ML Engineering, AI & ML Frameworks, Platforms & Models, Infrastructure & Security) to bubble the target company's primary tech stack, programming languages, and tools (e.g., Claude/MCP for Anthropic; AWS Bedrock/SageMaker/Java for Barclays; or Python/LangGraph/CrewAI for Vodafone) to the absolute front of their respective lists. Competitor platforms, models, or clouds must be de-prioritized and moved to the end of the lists. All skills must remain factually matched with the master `cv.md` items to pass fact-checks.
- **Dynamic Skill Optimization (Add/Remove based on JD)**: You must dynamically add relevant technologies/libraries or remove lower-relevance skills from the CV category lists to match the target JD:
  - **Add high-relevance skills**: Selectively include specific tools or frameworks from your projects (e.g., `GROBID`, `pdfplumber`, `vLLM`, `n8n`, `Triton`, `distributed training`) if they are explicitly mentioned or highly relevant to the target role.
  - **Remove low-relevance skills**: Discard irrelevant or secondary technologies (e.g., remove SAP-specific tools, minor backend frameworks, or web scrapers when targeting core ML research roles) to declutter the skills block and fit neatly on a single line per category.
  - **Fact-Check Safeguard**: All skills must be drawn from the validated pool in `cv.md` to ensure they pass automated fact verification checks.
- **Candidate Location / Hometown Address**: Always use the candidate's hometown address: **Ratlam (457001), Madhya Pradesh, India** across all resumes, cover letters, and application profiles. Do not use Surat, Gujarat, India.
- **Company Name Formatting for ATS**: Always format the employers as **Bigscal Technologies Pvt. Ltd. (Client: TalenTeam Ltd., UK)** and **Bigscal Technologies Pvt. Ltd. (Product: Healthray)** across all resumes, JSON payloads, and cover letters. Never lead with "TalenTeam Ltd." or "Healthray" so that ATS scanners properly capture the legal employer as "Bigscal Technologies Pvt. Ltd."
- **Company Folder Organization for Generated Resumes & Artifacts**: Always create and store all generated CVs, cover letters, and application artifacts in a dedicated subfolder named after the company under `Generated_Resumes/<Company_Name>/` (e.g., `Generated_Resumes/Ascendion/`, `Generated_Resumes/Mastercard/`, `Generated_Resumes/American_Express/`). Never place files as a flat list in the root of `Generated_Resumes/`.


## Custom Workflows

<!-- Multi-step routines you run often, given a short name. Examples:
     - "weekly review": scan my saved portals, evaluate the new roles,
       then give me a one-paragraph summary of the top 3.
     - "prep <company>": pull the JD, generate STAR stories from
       article-digest.md, and draft 5 likely interview questions. -->

(none yet -- add yours above)

## Output Preferences

<!-- How you like results formatted. Examples:
     - Reports: lead with the score and the one-line verdict.
     - Show the per-step token breakdown after a batch run.
     - Save PDFs date-first: YYYY-MM-DD-company.pdf -->

(none yet -- add yours above)

## Off-Limits

<!-- Things the agent must never do for you. Examples:
     - Never auto-fill or submit an application without showing me first.
     - Never edit a system file to customize my setup -- put it here. -->

(none yet -- add yours above)
