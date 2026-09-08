# Yash Rawal

Ratlam (457001), Madhya Pradesh, India • +91-9399159685 • yashrawal987@gmail.com • linkedin.com/in/rawal-yash • github.com/YashRL

## Professional Summary

Applied AI & Machine Learning Engineer serving a **1M+ user scale** by architecting enterprise agentic platforms, hierarchical RAG architectures, and automated intelligence pipelines across 120+ organizations. Specialized in Python, high-throughput LLM serving internals (vLLM contributor), workflow orchestration (SAP Joule 2.0, LangGraph), and automated testing/evaluation control planes. Bridges generative AI models and fine-tuning with resilient cloud-native infrastructure (Azure, AWS, Docker, Kubernetes).

## Technical Skills

- **Languages & Backend**: Python, SQL, FastAPI, PostgreSQL, Oracle, REST APIs, WebSockets, AsyncIO, Linux
- **AI & ML Engineering**: Agentic AI, Model Context Protocol (MCP), Multi-Agent Systems, Tool RAG, Healthcare NLP, High-Throughput Inference (vLLM), Model Training & SFT, KV Caching, Triton Kernels
- **AI & Workflow Frameworks**: LangChain, LangGraph, vLLM, PyTorch, Hugging Face, SAP Joule 2.0, vLLM Tool Parsers, LlamaIndex, GROBID, pdfplumber, Scikit-Learn
- **Platforms & Models**: Azure OpenAI, Amazon Bedrock, Google Vertex AI, GCP, AWS, Azure, Meta Llama & Open Weights, Qwen, Claude, Whisper, NeMo RNN-T, CTC decoding, E5-large-v2
- **Infrastructure, QA & Security**: Docker, Kubernetes, Linux, CI/CD (GitHub Actions, Jenkins, Git, Gerrit), PyTest, LLM-as-a-Judge, Prompt Lab, Red Teaming, PII Sanitization, BDD & Resiliency Testing

## Experience

### Bigscal Technologies Pvt. Ltd.
*AI/ML Engineer* | *Oct 2024 – Present*
- Deployed a production-scale agentic platform and multi-agent systems serving **1M+ active ERP users** across 120+ enterprise tenants on cloud infrastructure (Azure, AWS).
- Architected multi-agent routing and workflow automation with **LangGraph & SAP Joule 2.0**, implementing hybrid semantic-lexical tool discovery (vector + BM25F/RRF) across 650+ dynamic read/write and generation MCP capabilities.
- Designed a capability contract layer to execute nested profiles inside a single ReAct loop, reducing execution overhead by **3x** and token consumption by 70%.
- Trained domain-specific **E5-large-v2** embedding models on Lightcast labor-market datasets using PyTorch triplet contrastive learning to optimize semantic job-to-skills intent matching.
- Implemented a 4-level hierarchical RAG pipeline in Python indexing 10,000+ technical documents using GROBID, pdfplumber, and PostgreSQL/PGVector, achieving a **90%+ Recall@10** retrieval rate.
- Developed the Prompt Lab evaluation control plane in Python to collect reasoning trajectories and human preference annotations, establishing a scalable **Human Feedback (RLHF) Pipeline** shooting zero regressions.
- Built production guardrails against prompt injections and data leaks, integrating runtime tool validation and **automated PII redaction**.

### Bigscal Technologies Pvt. Ltd.
*AI/ML Engineer Intern* | *Apr 2024 – Sep 2024*
- Engineered clinical summarization pipelines in Python for 116K+ medical records with 4-bit quantized Llama 3, and designed real-time WebSocket audio streaming for Indic ASR with **NeMo RNN-T and CTC decoding**.
- Researched audio digital signal processing (STFT, Mel-spectrograms, MFCC feature extraction via librosa/torchaudio) and CNN audio architectures (VGGish, ResNet), compiling custom Indic LJSpeech-format datasets.

## Open Source & Projects

### vLLM High-Performance Inference Engine (vllm-project/vllm)
*Open Source Contributor* | *2026 – Present*
- Merged **PR #55475** resolving structural XML tool parser silent drops for `tool_choice="required"` on `/v1/chat/completions`, safe Pydantic param indexing in `ChatCompletionRequest`, and streaming parser activation (passed 64/64 Qwen tests and 983+ regression suite).
- Fixed unhandled `OSError` crashes in `torchcodec` multimodal video/audio decoder pipelines (Issue #54097) by engineering resilient system FFmpeg error boundaries and import validation suites (15 import tests, 50 video IO tests passed).

### Job Framework Semantic Embedding Model (e5-finetuned-job-framework)
*Machine Learning Model Training* | *2025 – Present*
- Fine-tuned an ~335M-parameter **E5-large-v2** transformer on Lightcast labor-market data using triplet contrastive learning with hard-negative mining in PyTorch, replacing general-purpose embeddings to optimize semantic job-to-skills retrieval precision.

### Modular Agent Harness & Memory System ("Brain")
*Creator & Core Architect* | *Jan 2026 – Present*
- **Principal Creator & Architect** of an open-source plug-and-play Python agentic framework designed as modular, composable building blocks for flexible enterprise workflows, implementing a formal ReAct loop with step budgets, pgvector tool routing, and dynamic MCP settings caching.

## Education

### Parul University
*Master of Computer Applications (Artificial Intelligence & Machine Learning)* | *2022 – 2024*

## Certifications

- Microsoft Certified: Azure AI Fundamentals (AI-900)
- Microsoft Certified: Azure Fundamentals (AZ-900)
