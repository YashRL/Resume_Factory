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
*AI/ML Engineer (Technical Lead)* | *Oct 2024 – Present*
- Served as AI Lead driving 100% end-to-end ownership across multi-tenant microservices, agent runtimes, and models.
- Deployed enterprise agentic platform serving 1M+ active ERP users across 120+ cloud tenants on Azure and AWS.
- Architected multi-agent A2A routing with LangGraph & SAP Joule 2.0, unifying SAP SuccessFactors, Blend, and MCP APIs.
- Engineered dynamic UI widget rendering contracts and capability layers, boosting throughput 3× and saving $120K+/year.
- Fine-tuned and served Qwen2.5-7B and E5-large-v2 on NVIDIA GPUs using PyTorch, Unsloth, and vLLM inference endpoints.
- Built 4-level hierarchical RAG in Python indexing 10,000+ technical documents via PGVector achieving 90%+ Recall@10.
- Conceived and built Prompt Lab control plane to capture execution traces, enabling human feedback and RLHF pipelines.
- Architected multi-tier zero-trust PII sanitization scrubbing sensitive data at tool and server boundaries before LLMs.
- Mentored and upskilled 5+ interns and junior engineers in PyTorch fine-tuning, agentic workflows, and LLM evaluation.

### Bigscal Technologies Pvt. Ltd.
*AI/ML Engineer Intern* | *Apr 2024 – Sep 2024*
- Engineered clinical summarization pipelines in Python for 116K+ medical records with 4-bit quantized Llama 3, and designed real-time WebSocket audio streaming for Indic ASR with **NeMo RNN-T and CTC decoding**.
- Researched audio digital signal processing (STFT, Mel-spectrograms, MFCC feature extraction via librosa/torchaudio) and CNN audio architectures (VGGish, ResNet), compiling custom Indic LJSpeech-format datasets.

## Open Source & Projects

### vLLM High-Performance Inference Engine (vllm-project/vllm)
*Open Source Contributor* | *2026 – Present*
- Merged **PR #55475** resolving structural XML tool parser silent drops for `tool_choice="required"` on `/v1/chat/completions`, safe Pydantic param indexing in `ChatCompletionRequest`, and streaming parser activation (passed 64/64 Qwen tests and 983+ regression suite).
- Fixed unhandled `OSError` crashes in `torchcodec` multimodal video/audio decoder pipelines (Issue #54097) by engineering resilient system FFmpeg error boundaries and import validation suites (15 import tests, 50 video IO tests passed).

### Job Architecture Generator (Qwen2.5-7B Domain SFT & Serving)
*LLM Training & Serving* | *2025 – Present*
- Fine-tuned **Qwen2.5-7B** on 10K+ curated domain examples using Unsloth & PyTorch on NVIDIA GPUs for role standardization and structured JSON generation; deployed an **OpenAI-compatible endpoint** via vLLM for low-latency enterprise inference.

### E5-large-v2 Job & Skills Embedding Fine-Tuning
*Model Training* | *2025 – Present*
- Fine-tuned **E5-large-v2** (335M parameters) on Lightcast labor-market data using PyTorch and triplet loss (anchor + positive + hard negative), raising semantic retrieval relevance by **18%** over OpenAI `text-embedding-3-small`.

### Modular Agent Harness & Memory System ("Brain")
*Creator & Core Architect* | *Jan 2026 – Present*
- **Principal Creator & Architect** of an open-source plug-and-play Python agentic framework designed as modular, composable building blocks for flexible enterprise workflows, implementing a formal ReAct loop with step budgets, pgvector tool routing, and dynamic MCP settings caching.

## Education

### Parul University
*Master of Computer Applications (Artificial Intelligence & Machine Learning)* | *2022 – 2024*

## Certifications

- Microsoft Certified: Azure AI Fundamentals (AI-900)
- Microsoft Certified: Azure Fundamentals (AZ-900)
