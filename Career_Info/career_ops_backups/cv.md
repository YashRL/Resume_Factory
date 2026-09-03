# Yash Rawal

Ratlam (457001), Madhya Pradesh, India • +91-9399159685 • yashrawal987@gmail.com • linkedin.com/in/rawal-yash • github.com/YashRL

## Professional Summary

Applied AI & Machine Learning Engineer serving a **1M+ user scale** by architecting enterprise agentic platforms, multi-agent systems, and ERP AI infrastructure across 120+ organizations. Specialized in LLM orchestration (LangGraph, CrewAI, ReAct loops), enterprise RAG, and AgentOps evaluation control planes. Active contributor to Spring AI, bridging generative AI models with high-throughput production systems.

## Technical Skills

- **Languages & Backend**: Python, SQL, Java, C++, Spring Boot, FastAPI, PostgreSQL, SAP HANA, Data Engineering, REST APIs
- **AI & ML Engineering**: Agentic AI, Multi-Agent Systems, MCP Server Development, RAG & Vector Search, Model Training & SFT, Context Graphs, Multimodal AI, Audio Signal Processing (DSP), Computer Vision, Machine Learning, MCP, Vector Embeddings, Distributed Training, Distributed Inference, KV Caching, Custom BPE Tokenization, Tool RAG, A2A Communication
- **AI & ML Frameworks**: LangChain, LangGraph, Spring AI, PyTorch, vLLM, LlamaIndex, AutoGen, Scikit-Learn, OpenCV, torchaudio, librosa, Triton, CUDA, HIP, n8n, GROBID, pdfplumber, Hugging Face, DataParallel, AdamW
- **Platforms & Models**: Azure OpenAI, Amazon Bedrock, Google Vertex AI, GCP, AWS, Azure, Claude, Gemini, Qwen, Meta Llama & Open Weights, SAP AI Core, SAP Build, SAP Joule, Whisper, NeMo RNN-T, CTC decoding, IndicConformer, TinyStories
- **Infrastructure & Security**: Docker, Kubernetes, Linux, CI/CD, LLM-as-Judge, Red Teaming, PII Sanitization (BIO NER), WebSockets, Kaggle, Cloud Foundry, Edge Hardware

## Experience

### Bigscal Technologies Pvt. Ltd.
*AI/ML Engineer* | *Oct 2024 – Present*
- Deployed a production-scale agentic platform and multi-agent systems serving **1M+ active ERP users** across 120+ enterprise tenants on cloud infrastructure (Azure, AWS, GCP).
- Architected and deployed multi-agent workflows with LangChain and LangGraph, utilizing **MCP Server Tool Routing (Tool RAG)** and A2A communication with integrated guardrails.
- Designed a capability contract layer to execute nested profiles inside a single ReAct loop, reducing execution overhead by **3x** and token consumption by 70%.
- Implemented a hierarchical RAG pipeline indexing 10,000+ technical documents using GROBID, pdfplumber, and PostgreSQL/PGVector, achieving a **90%+ Recall@10** retrieval rate.
- Engineered an automated LLM evaluation and red-teaming control plane to log reasoning trajectories, scoring agent behaviors via LLM-as-a-judge and **RLHF preference datasets**.
- Built production guardrails against prompt injections and data leaks, integrating runtime tool validation and **automated PII redaction**.

### Bigscal Technologies Pvt. Ltd.
*AI/ML Engineer Intern* | *Apr 2024 – Sep 2024*
- Engineered clinical summarization pipelines for 116K+ medical records with 4-bit quantized Llama 3, and designed real-time WebSocket audio streaming for Indic ASR with **NeMo RNN-T and CTC decoding**.
- Researched audio digital signal processing (STFT, Mel-spectrograms, MFCC feature extraction via librosa/torchaudio) and CNN audio architectures (VGGish, ResNet), compiling custom Indic LJSpeech-format datasets.

## Open Source & Projects

### Modular Agent Harness & Memory System ("Brain")
*Creator & Core Architect* | *Jan 2026 – Present*
- **Principal Creator & Architect** of an open-source plug-and-play agentic framework designed as modular, composable building blocks for flexible enterprise workflows.
- Implemented a formal Java-based ReAct loop (Thought-Action-Observation) with step budgets, tactical pgvector tool routing, and dynamic MCP settings caching.

### Spring AI (spring-projects/spring-ai)
*Active Contributor* | *Mar 2026 – Present*
- Resolved streaming and non-streaming API latency mismatches by merging DeepSeek-R1/Qwen reasoningContent metadata propagation (PR #5711) and AWS Bedrock Converse API prompt-caching TTL support.

### Mini Language Model (~85M Parameter Architecture)
*Personal Research & Author* | *Jan 2026 – Present*
- Pretrained an ~85M-parameter decoder-only transformer to ~1.43 validation loss on TinyStories dataset targeting **edge hardware deployment**, designing FragmentStream Attention (chunked sequence tiling) to eliminate O(T^2) VRAM exhaustion on commodity Tesla P100/T4 GPUs.
- Implemented conversational alignment via multi-corpus dialogue training with asymmetric loss masking and 70/30 pretraining replay; developed custom Triton kernels and KV caching for low-latency inference.

### AI Agent Security Red Teaming – OpenAI
*Security Researcher* | *Aug 2026*
- Designed adversarial prompt-injection pipelines targeting observer-based guardrails to evaluate security boundaries across 2,000+ agent test cases on Kaggle.

## Education

### Parul University
*Master of Computer Applications (Artificial Intelligence & Machine Learning)* | *2022 – 2024*

## Certifications

- Microsoft Certified: Azure AI Fundamentals (AI-900)
- Microsoft Certified: Azure Fundamentals (AZ-900)
