# Job Architecture Generator — Model Training & Deployment

## 1. Project Context

The Job Architecture Generator originated from an operational requirement rather than as a standalone ML experiment.

The initial requirement was to generate a job architecture Excel sheet for a client in a short timeframe. The first implementation used an AI agent powered by a commercial LLM to automate the task.

As the system was explored further, it became clear that repeatedly sending organizational job data to commercial LLM APIs would introduce two significant problems:

- **Data privacy:** Job descriptions, organizational structures, roles, responsibilities, reporting relationships, and workforce information can contain sensitive business information.
- **Inference cost and scalability:** Job architecture exercises can involve thousands of employees and roles. Running a large commercial model for every employee would result in substantial recurring inference costs.

This led to the development of a domain-specific Job Architecture model that could perform the core job-mapping task locally on dedicated GPU infrastructure.

The resulting model became one component of a larger Agentic AI system responsible for job architecture generation, role mapping, and downstream allocation of teams and resources.

---

# 2. Business Problem

Organizations may need to restructure their workforce during:

- Mergers and acquisitions
- Organizational restructuring
- Workforce planning
- Role standardization
- Job architecture redesign
- Resource and team allocation

A major challenge is that different organizations use completely different job titles and organizational structures.

For example:

> **Source organization:** Senior Backend Developer  
> **Target organization:** Software Engineer III

The titles themselves may have little semantic similarity even when the underlying responsibilities are comparable.

Large organizations can make this problem more difficult by using highly granular internal levels and titles such as:

- Software Development Engineer I / II / III
- Staff Engineer
- Principal Engineer
- Business Analyst
- Functional Analyst
- Technical Analyst
- Domain-specific analyst roles

The system therefore needed to reason about the **actual role, responsibilities, seniority, function, skills and organizational context**, rather than simply matching job titles.

---

# 3. System Objective

The objective was to build a specialized model capable of transforming unstructured or semi-structured job information into a standardized Job Architecture representation.

The model needed to perform two tasks simultaneously:

1. **Semantic understanding and job mapping**
   - Understand what a person actually does.
   - Identify the functional area and domain.
   - Determine an appropriate organizational level.
   - Extract responsibilities and required skills.
   - Map roles into the target organization's architecture.

2. **Strict structured generation**
   - Produce predictable machine-readable output.
   - Follow a predefined schema.
   - Maintain consistent field names and value formats.
   - Produce output that could be directly consumed by downstream Agentic AI functions and ultimately transformed into client-specific Excel sheets.

This made output reliability almost as important as semantic correctness.

---

# 4. Model Architecture

The foundation model selected for the project was:

**Qwen2.5-7B**

The model was specialized for the Job Architecture domain using supervised domain-specific training.

The overall training pipeline was:

```text
Real-world Job Architecture Data
             │
             ▼
   Data Preparation / Curation
             │
             ▼
 Claude Sonnet 3.5
 Synthetic Training Data Generation
             │
             ▼
      10K+ Training Examples
             │
             ▼
        Qwen2.5-7B
       Fine-tuning / SFT
             │
             ▼
 Specialized Job Architecture Model
             │
             ▼
 Structured Job Architecture Output
             │
             ▼
       Agentic AI System
             │
             ▼
 Excel / Client-specific Output
```

The training process was implemented using the Python ML ecosystem, including:

- **PyTorch**
- **Hugging Face Transformers**
- **Hugging Face ecosystem**
- **Unsloth**

Training was performed using Google Colab Pro with NVIDIA A100 GPU acceleration.

---

# 5. Training Data Strategy

A major challenge was the limited availability of directly labeled examples pairing real-world job descriptions with the desired Job Architecture representation.

Instead of relying entirely on manually labeled data, a synthetic-data generation pipeline was developed.

Real organizational/job information available from client engagements was used as the basis for constructing representative examples. Claude Sonnet 3.5 was then used to generate additional domain-specific training examples.

More than **10,000 examples** were generated and curated for training.

The approach allowed the dataset to cover a wide variety of:

- Job titles
- Responsibilities
- Seniority levels
- Functions
- Domains
- Skill combinations
- Reporting structures
- Job-description writing styles
- Incomplete or differently structured inputs

The generated examples were reviewed and validated as part of the data preparation process before being used for model training.

This effectively converted sparse domain-specific knowledge into a substantially larger supervised training corpus.

---

# 6. Training Example Structure

A typical training example followed an instruction-oriented structure:

```text
System:
You are a Job Architecture analyst.
Given role information, generate a structured
Job Architecture representation according to
the required schema.

User:
<job description / role information>

Assistant:
<structured Job Architecture output>
```

The target output contained structured fields representing the organization's job architecture.

A representative schema included:

```text
role_title
level
function
domain
reports_to
team
cost_center
experience_years_min
on_call
key_responsibilities
required_skills
required_skills_levels
required_skills_min_years
nice_to_have
```

The exact production schema was considerably larger and could vary according to client requirements.

The important training principle was that the model learned not only **what information to extract**, but also **how that information needed to be represented for downstream processing**.

---

# 7. Why Domain Fine-tuning Was Required

A general-purpose 7B model could understand job descriptions reasonably well, but the project required more than general language understanding.

The model needed to consistently understand the organization's Job Architecture concepts and reproduce them in a deterministic structure.

The specialization therefore taught the model patterns such as:

```text
Job Description
      ↓
Role Understanding
      ↓
Function / Domain
      ↓
Seniority / Level
      ↓
Responsibilities
      ↓
Skills
      ↓
Organizational Mapping
      ↓
Structured Output
```

This effectively turned the general-purpose foundation model into a **domain-specialized Job Architecture model**.

The model was therefore not intended to become a general-purpose conversational model. Its value came from becoming highly specialized for a narrow business workflow.

---

# 8. Train / Test Strategy

The dataset was divided into training and held-out evaluation data, using approximately a:

**90% training / 10% test split**

The held-out examples were not used during training.

For a production-quality evaluation pass, the following metrics can be used to quantify the historical claim of "near-perfect" performance:

| Metric | What it measures |
|---|---|
| JSON Parse Rate | Whether the model produces machine-readable JSON |
| Schema Compliance | Whether output follows the expected structure |
| Field-level Accuracy / F1 | Correctness of structured fields |
| Skill Recall | Ability to identify required skills |
| Hallucination Rate | Information generated without sufficient support |
| Format Compliance | Consistency of the required output format |

The original implementation was primarily validated through functional testing of the generated Job Architecture outputs rather than through a formal ML benchmark suite. The model reached a point where its results were sufficiently reliable for the intended Job Architecture workflow.

The exact historical benchmark values should be recovered from the original training/evaluation notebook before being presented as official project metrics.

---

# 9. Model Output Requirements

A critical design requirement was that the model's output had to be usable by the rest of the Agentic AI system.

The output therefore needed to be:

- Structurally consistent
- Machine-readable
- Predictable
- Compatible with downstream functions
- Convertible into Excel-compatible tabular data

For example, nested skills could ultimately be transformed into fields such as:

```text
required_skills
required_skills_levels
required_skills_min_years
```

while responsibilities and other list-based fields could be transformed into Excel-compatible representations.

This design allowed the model to sit naturally inside an automated workflow rather than requiring manual cleanup after every inference.

---

# 10. Agentic AI Integration

The trained model was not the complete application.

It served as the specialized intelligence layer inside a broader Agentic AI system.

The overall system could:

```text
Client / User Input
        │
        ▼
   AI Agent Layer
        │
        ├── Job Understanding
        │
        ├── Job Architecture Generation
        │
        ├── Role Mapping
        │
        ├── Team Allocation
        │
        └── Resource Allocation
        │
        ▼
 Specialized Job Architecture Model
        │
        ▼
 Structured Data
        │
        ▼
 Client-specific Excel Output
```

The model was therefore responsible for the specialized language/role-understanding component, while the surrounding agents handled orchestration and business workflow logic.

The model-training component was the portion of this system primarily owned and implemented within the ML engineering workflow.

---

# 11. Inference and Deployment

Training and inference were deliberately separated.

### Training Environment

Training was performed using:

**Google Colab Pro + NVIDIA A100 GPU**

The model was trained for several hours as part of the experimentation and fine-tuning process.

### Production Inference Environment

For inference, the trained model was deployed on an Azure GPU environment using:

**Azure Standard_NC24ads_A100_v4**

with an NVIDIA A100 GPU.

The production model was served using:

**vLLM**

This allowed the specialized model to operate as a dedicated inference service rather than requiring every request to be sent to a commercial LLM provider.

---

# 12. vLLM Serving

vLLM was used as the model inference engine for the deployed Qwen2.5-7B model.

The serving layer provided an API interface through which the Agentic AI backend could submit requests to the specialized model.

Conceptually:

```text
Agentic AI Backend
        │
        │ API Request
        ▼
 Azure GPU Infrastructure
        │
        ▼
       vLLM
        │
        ▼
 Qwen2.5-7B Job Architecture Model
        │
        ▼
 Structured Job Architecture Response
```

The deployment was configurable so that model-serving parameters could be adjusted according to the workload and infrastructure requirements.

Structured output constraints were also important at inference time because downstream components expected predictable machine-readable results.

---

# 13. Commercial LLM vs Specialized Model

The architecture created a practical separation between general-purpose AI capabilities and specialized business inference.

### Initial approach

```text
Agent
  ↓
Commercial LLM API
  ↓
Job Architecture
```

This was easy to prototype but introduced:

- Recurring API costs
- Data privacy considerations
- Dependence on an external model provider
- Scaling costs for thousands of employee records

### Specialized approach

```text
Agent
  ↓
Private inference infrastructure
  ↓
Fine-tuned Qwen2.5-7B
  ↓
Job Architecture
```

This allowed the organization to keep the specialized inference workload under its own infrastructure while reducing dependence on per-request commercial LLM inference.

---

# 14. Supporting Prototype

Before the specialized model was operational, a temporary Claude-powered Job Architecture Agent was also developed and deployed on Cloud Foundry.

The purpose was practical:

- Allow the functional team to generate Job Architectures themselves.
- Allow users to update and regenerate outputs interactively.
- Remove repetitive manual work from the engineering team.
- Provide an immediately usable interface while the specialized model was being developed.

In other words, the temporary solution became a useful bridge between the original manual Excel workflow and the eventual specialized ML system.

It also eliminated the recurring need for engineering intervention whenever the functional team needed another Job Architecture generated.

---

# 15. End-to-End Technical Contribution

The project can therefore be understood as an end-to-end ML engineering workflow:

```text
Business Problem
      ↓
AI Agent Prototype
      ↓
Privacy + Cost Analysis
      ↓
Domain Data Collection
      ↓
Synthetic Data Generation
      ↓
10K+ Domain Examples
      ↓
Dataset Curation / Validation
      ↓
Qwen2.5-7B Fine-tuning
      ↓
Evaluation
      ↓
Specialized Job Architecture Model
      ↓
vLLM Deployment
      ↓
Azure A100 GPU
      ↓
Agentic AI Integration
      ↓
Structured Job Architecture
      ↓
Excel / Business Workflow
```

The key engineering contribution was therefore not simply training an LLM.

It was taking a previously manual business process, identifying where a general-purpose LLM became impractical, creating a domain-specific training corpus, specializing an open-weight foundation model, and integrating that model into an agentic production workflow capable of generating structured business outputs.

---

# 16. Technology Stack

| Area | Technology |
|---|---|
| Foundation Model | Qwen2.5-7B |
| Training | PyTorch |
| Model Fine-tuning | Unsloth |
| NLP / Model Framework | Hugging Face Transformers |
| Synthetic Data Generation | Claude Sonnet 3.5 |
| Training Infrastructure | Google Colab Pro |
| Training GPU | NVIDIA A100 |
| Production GPU | NVIDIA A100 |
| Cloud Infrastructure | Microsoft Azure |
| Model Serving | vLLM |
| Application / Agent Layer | Agentic AI system |
| Temporary Prototype Deployment | Cloud Foundry |
| Output | Structured Job Architecture / Excel |

---

# 17. Project Impact

The system transformed Job Architecture generation from a repetitive manual process into an automated AI-assisted workflow.

The architecture provided:

- Automated role understanding and mapping
- Standardized Job Architecture generation
- Structured machine-readable output
- Integration with downstream AI agents
- Reduced dependence on manual Excel preparation
- A path away from high-volume commercial LLM API inference
- Private GPU-based inference for sensitive organizational data
- Reusable model infrastructure for large-scale Job Architecture workloads

Most importantly, the project demonstrated the progression from **AI prototyping → domain-specific model development → model serving → Agentic AI integration**, rather than treating model training as an isolated experiment.