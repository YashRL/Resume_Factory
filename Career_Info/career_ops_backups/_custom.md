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

- **Professional Identity & Title**: Always identify the candidate as an **Applied AI & Machine Learning Engineer** (never use "AI Platform Engineer" or "AI System Engineer").
- **Balanced All-Rounder Profile (50-50 Applied AI & Core ML)**: Always frame the candidate's skills and experience to show a balanced 50-50% mix between Applied AI (agent runtimes, RAG, MCP, n8n, Spring AI) and Core Machine Learning (model fine-tuning, training, GPU optimization, signal processing, ASR/TTS, NER token-classification).
- **Scale-First Professional Summary**: The Professional Summary must lead with enterprise scale metrics (e.g., 1M+ active users, 120+ ERP organizations, enterprise agentic platform) first, followed directly by core model training and machine learning engineering.
- **Strong Engineering Verbs**: Never use weak or passive descriptors like "Built local POCs," "Assisted," "Helped," or "Worked on." Use authoritative engineering verbs such as "Engineered," "Designed," "Optimized," "Architected," and "Trained" to represent internship and project work.
- **Pre-Tuning Applied AI Logic**: If a job post is focused only on Applied AI, frame it to show that the candidate tunes and trains the models first (SFT, triplet contrastive training, quantization), then builds the applied agentic systems on top of them. Do not let the profile look like a simple API-wrapper developer.
- **Mandatory Strategic CV Bold Highlights**: Always preserve and highlight exactly the following five key terms/phrases across every generated CV:
  1. `**1M+ active ERP users**` (or `**1M+ user scale**` in the professional summary)
  2. `**3x**` and `**70%**` (efficiency metrics)
  3. `**Qwen2.5-7B**` (model training proof)
  4. `**Human Feedback (RLHF) Pipeline**` (RLHF alignment/annotations system)
  5. `**90%+ Recall@10**` (retrieval metric)
  6. `**Principal Creator & Architect**` (modular harness leadership role)
- **No Line Wrap for Long Bold Phrases**: If a highlighted term or phrase is long (e.g., `**Human Feedback (RLHF) Pipeline**`, `**Principal Creator & Architect**`, `**1M+ active ERP users**`), it must not wrap across a line break to a second line. Format the surrounding sentence text or adjust sentence structure to ensure these bold phrases sit cleanly on a single line.


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
