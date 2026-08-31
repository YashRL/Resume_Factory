# Yash Rawal

Surat, Gujarat, India • +91-9399159685 • yashrawal987@gmail.com • linkedin.com/in/rawal-yash • github.com/YashRL

## Professional Summary

Applied AI & Machine Learning Engineer serving a **1M+ user scale** by architecting enterprise agentic platforms and ERP AI infrastructure across 120+ organizations. Specialized in core model training, embedding optimization, and low-latency agent execution frameworks. Active contributor to Spring AI, bridging machine learning models with high-throughput production systems.

## Technical Skills

- **Languages & Backend**: Python, Java, SQL, Spring Boot, FastAPI, PostgreSQL, SAP HANA, Data Engineering, REST APIs
- **AI & ML Engineering**: Model Training & SFT, Agentic AI, Machine Learning, MCP, Vector Embeddings, Distributed Training, Distributed Inference, KV Caching, Custom BPE Tokenization
- **AI & ML Frameworks**: PyTorch, Triton, CUDA, HIP, Spring AI, LangGraph, LangChain, LlamaIndex, CrewAI, AutoGen, vLLM, n8n, GROBID, pdfplumber, Hugging Face, DataParallel, AdamW
- **Platforms & Models**: Azure OpenAI, SAP AI Core, Amazon Bedrock, Google Vertex AI, Claude, Gemini, Qwen, Meta Llama & Open Weights, SAP Build, SAP Joule, TinyStories
- **Infrastructure & Security**: Docker, Kubernetes, Cloud Foundry, Linux, CI/CD, LLM-as-Judge, Red Teaming, PII Sanitization (BIO NER), WebSockets

## Experience

### TalenTeam Ltd., UK (via Bigscal Technologies)
*AI/ML Engineer* | *Oct 2024 – Present*
- Deployed a production-scale agentic platform and multi-agent systems serving **1M+ active ERP users** across 120+ enterprise tenants.
- Designed a capability contract layer to execute nested profiles inside a single ReAct loop, reducing execution overhead by 3x and token consumption by 70%.
- Trained domain-specific **Qwen2.5-7B** models on A100 GPUs and fine-tuned E5-large-v2 embeddings using PyTorch to optimize query intent mapping.
- Developed the Prompt Lab evaluation control plane to collect reasoning trajectories and human preference annotations, establishing a scalable **Human Feedback (RLHF) Pipeline**.
- Implemented a hierarchical RAG pipeline indexing 10,000+ technical documents using GROBID, pdfplumber, and PostgreSQL/PGVector, achieving a 90%+ Recall@10 retrieval rate.
- Secured agentic workflows against OWASP LLM vulnerabilities using phantom-token context propagation, runtime tool monitoring, and trained token-classification models for automated PII redaction.

### Healthray (Bigscal Technologies)
*AI/ML Engineer Intern* | *Apr 2024 – Sep 2024*
- Engineered clinical summarization pipelines for 116K+ medical records with 4-bit quantized Llama 3, and designed real-time WebSocket audio streaming for Indic ASR (Whisper, Vosk, NeMo).
- Researched audio digital signal processing (STFT, Mel-spectrograms, MFCC feature extraction via librosa/torchaudio) and CNN audio architectures (VGGish, ResNet), compiling custom Indic LJSpeech-format datasets.

## Open Source & Projects

### Mini Language Model (~85M Parameter Architecture)
*Personal Research & Author* | *Jan 2026 – Present*
- Pretrained an ~85M-parameter decoder-only transformer to ~1.43 validation loss on TinyStories dataset, designing FragmentStream Attention (chunked sequence tiling) to eliminate O(T^2) VRAM exhaustion on commodity Tesla P100/T4 GPUs.
- Implemented conversational alignment via multi-corpus dialogue training with asymmetric loss masking and 70/30 pretraining replay; developed custom Triton kernels and KV caching for low-latency inference.

### Spring AI (spring-projects/spring-ai)
*Active Contributor* | *Mar 2026 – Present*
- Resolved streaming and non-streaming API latency mismatches by merging DeepSeek-R1/Qwen reasoningContent metadata propagation (PR #5711) and AWS Bedrock Converse API prompt-caching TTL support.

### Modular Agent Harness & Memory System ("Brain")
*Creator & Core Architect* | *Jan 2026 – Present*
- **Principal Creator & Architect** of an open-source plug-and-play agentic framework designed as modular, composable building blocks for flexible enterprise workflows.
- Implemented a formal Java-based ReAct loop (Thought-Action-Observation) with step budgets, tactical pgvector tool routing, and dynamic MCP settings caching.

### AI Agent Security Red Teaming – OpenAI
*Security Researcher* | *Aug 2026*
- Designed adversarial prompt-injection pipelines targeting observer-based guardrails to evaluate security boundaries across 2,000+ agent test cases.

## Education

### Parul University
*Master of Computer Applications (Artificial Intelligence & Machine Learning)* | *2022 – 2024*

## Certifications

- Microsoft Certified: Azure AI Fundamentals (AI-900)
- Microsoft Certified: Azure Fundamentals (AZ-900)
