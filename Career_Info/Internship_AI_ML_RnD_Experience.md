# Internship — AI/ML R&D: Clinical AI, Indian Speech & Generative Models

## Internship Overview

My internship was my first deep exposure to **end-to-end AI/ML research and engineering in a real AI lab environment**. At the time, many of the capabilities that are relatively accessible today—strong instruction-following LLMs, reliable structured outputs, agent guardrails, multilingual speech models, and inexpensive GPU inference—were considerably less mature and more expensive. This shaped how we approached AI systems: rather than assuming that a single LLM could reliably perform an entire workflow, we combined **deep-learning models, speech systems, classical NLP, rule-based logic, and application-level orchestration**.

The internship consisted of three major R&D tracks: **Clinical Summary Generation**, **Speech-to-Text for Indian/Non-English Languages**, and **Text-to-Speech (TTS)**. Alongside these projects, I studied modern CNN architectures for audio classification, explored the work of **AI4Bharat** in Indian-language speech technology, experimented with open-source speech models, and built POCs around real-time multilingual speech processing.

This period became a foundational stage in my engineering journey because I learned not only how to use AI models, but how to **build systems around models when the model itself cannot be trusted to solve everything**.

---

## 1. Clinical Summary Generation

### Objective

The first major track explored how language models could be used to process structured healthcare information and generate useful **clinical summaries and doctor-facing outputs**.

The work involved structured healthcare data containing approximately **116K+ records** spanning multiple hospitals and doctors. The objective was to investigate how an LLM could progressively understand a dataset rather than simply receiving an entire dataset blindly.

### Approach

The system explored a progressive data-understanding workflow:

**Schema → Dataset Statistics → Row Values → LLM Interpretation → Clinical Summary**

The model was exposed to:

- Column names and schema
- Number of records
- Dataset-level statistics
- Actual row-level values
- Doctor/patient information
- Existing summaries and clinical information

This became an early exploration of using LLMs for **structured-data understanding** rather than conventional conversational question answering.

### Healthcare AI Components

The broader clinical-AI R&D explored areas including:

- Clinical summary generation
- Medical Named Entity Recognition (NER)
- Medical terminology extraction
- Medicine-name identification
- Discharge summaries
- Doctor workflow assistance
- Speech-driven clinical workflows
- Gujarati/Hindi language support
- Speech synthesis

At that stage, the reliability of LLMs for strict structured extraction was much lower than what is commonly expected from modern systems. Consequently, **rule-based processing and specialized NLP models were important parts of the architecture**.

Medical NER, for example, could be used to reliably identify medical entities and medicine names rather than depending entirely on an LLM to extract them correctly.

---

## 2. Healthcare Data Summarization POC

### Model and Pipeline

A dedicated R&D/POC was built using **Llama 3 8B** to understand and summarize the large structured healthcare dataset.

The model pipeline used:

- **PyTorch**
- **Hugging Face Transformers**
- **Llama 3 8B**
- **llama.cpp**
- Local inference
- 4-bit quantization

The project eventually explored running a **4-bit quantized Llama 3 8B locally**, demonstrating how model optimization could make a large language model more practical under constrained compute.

### Key Results

* **116K+ rows** of healthcare data processed
* **8B-parameter** Llama 3 foundation model
* Data spanning **multiple hospitals and doctors**
* Structured-data understanding explored from **schema → statistics → row-level data**
* **4-bit quantization** explored using llama.cpp
* **PyTorch + Hugging Face Transformers** used for the model pipeline
* **Local LLM inference** explored instead of relying exclusively on commercial APIs
* Project remained an **R&D / POC**, not a production deployment
* Complete experimentation path: **data → LLM → inference → quantization → optimized local model**

---

# 3. R&D — Audio Classification with CNNs & Speech Models

A major part of the internship involved understanding how machines process speech and audio before moving toward multilingual speech systems.

This included studying the complete signal-processing pipeline:

**Raw Audio → STFT → Mel-Spectrogram / Log-Mel Spectrogram → Neural Network → Learned Representation → Classification**

This was particularly important because it gave me a strong understanding of how audio moves from a raw time-domain signal into a representation that neural networks can learn from.

## Signal Processing

I explored:

- Raw waveform representation
- Sampling and audio representation
- Short-Time Fourier Transform (STFT)
- Frequency-domain representation
- Mel scale
- Mel-spectrograms
- Log-Mel spectrograms
- MFCCs
- Learned/latent representations
- Convolutional feature extraction

I also developed a strong conceptual understanding of how convolutional layers progressively transform raw representations into increasingly abstract and lower-dimensional feature spaces.

---

## CNN Architecture Study

I studied the evolution of CNN architectures and their applicability to audio classification.

| Architecture | Year | Approx. Params | Key Idea | Audio Relevance |
|---|---:|---:|---|---|
| AlexNet | 2012 | 60M | ReLU, dropout, GPU training | Baseline audio experiments |
| ZFNet | 2013 | 61M | Tuned filters and smaller first convolution | Limited audio usage |
| VGGNet | 2014 | 138–144M | Uniform 3×3 convolutions | VGGish-style audio representations |
| GoogLeNet / Inception | 2014–15 | 5–27M | Multi-scale parallel filters | Audio classification |
| ResNet | 2015 | 26–60M | Residual / skip connections | Strong classical CNN baseline |
| DenseNet | 2016 | 8–22M | Dense feature reuse | Transfer-learning experiments |
| MobileNet | 2017 | ~4M | Depthwise separable convolution | Lightweight inference |
| EfficientNet | 2019 | Varies | Compound scaling | Efficient audio/image architectures |

This work gave me substantial hands-on understanding of **CNNs, feature extraction, transfer learning, and representation learning**, rather than treating neural networks as black-box APIs.

---

## Audio Ecosystem Studied

| Library / Framework | Purpose |
|---|---|
| FFmpeg | Audio/video codecs, conversion and resampling |
| librosa | STFT, Mel spectrograms, MFCC, pitch, tempo and beat analysis |
| soundfile | Audio file reading and writing |
| PyDub | Audio manipulation, slicing, concatenation and export |
| PyAudio | Real-time microphone/speaker I/O |
| sounddevice | Audio recording and playback |
| audioread | Cross-format decoding backend |
| PyTorch | Deep-learning framework |
| torchaudio | Audio I/O, transformations and datasets |

---

# 4. Speech Recognition / ASR Research

The next stage moved from general audio classification into **Automatic Speech Recognition (ASR)**.

I studied and experimented with:

- Whisper
- Vosk
- Kaldi
- SpeechRecognition
- SpeechBrain
- ESPnet
- NVIDIA NeMo
- AI4Bharat IndicConformer

The focus gradually shifted toward **Indian and non-English languages**, especially Gujarati.

---

# 5. AI4Bharat Research

A significant part of the internship involved studying the open-source research coming from **AI4Bharat**, particularly its work around Indian-language speech.

## IndicConformer

I studied **IndicConformer**, an ASR model family designed for speech-to-text across **22 official Indian languages**.

This was particularly relevant to the internship because multilingual Indian speech was one of the primary research directions.

## IndicVoices

I also studied **IndicVoices**, a large multilingual Indian speech dataset containing approximately:

* **12,000 hours** of speech
* **22 Indian languages**
* **22,563 speakers**
* **208 Indian districts**
* Read, extempore and conversational speech
* Approximately **3,200 hours transcribed** at the time of the research

The dataset demonstrated the importance of **language diversity, accents, geography, speakers and spontaneous speech** when building speech systems for India.

## IndicWhisper

I also studied **IndicWhisper** and its evaluation work around Indian-language ASR.

The research explored:

- Fine-tuning Whisper for Indian languages
- Multilingual speech recognition
- Language/domain-specific benchmarks
- Vistaar benchmarks
- WER-based evaluation
- Open-source Indian-language ASR

The work highlighted how a general-purpose speech model could be adapted to significantly improve performance on Indian-language speech.

---

# 6. Multilingual Real-Time Speech-to-Text POC

I built a POC around **real-time multilingual speech processing**.

### High-Level Architecture

**Browser Microphone → WebSocket → FastAPI → Language Identification → Multilingual ASR → Incremental Transcription**

The browser continuously captured audio chunks and transmitted them to a **FastAPI-based WebSocket backend**.

The backend first attempted to identify the spoken language and then routed the audio through an appropriate multilingual ASR pipeline.

### Language Identification

I experimented with **SpeechBrain + VoxLingua107**, including its pretrained ECAPA-based language identification model.

The concept was:

**Audio → Language Identification → Hindi / English / Gujarati / etc. → Appropriate ASR model**

This allowed the speech system to dynamically determine which language was being spoken rather than requiring the user to manually select the language.

### ASR Stack

The multilingual pipeline explored:

- NVIDIA NeMo
- CTC decoding
- RNNT decoding
- IndicConformerASR
- SpeechBrain
- Multilingual speech models

The idea behind **RNNT-based decoding** was particularly interesting for real-time speech because transcription could evolve as additional audio arrived.

Instead of treating every partial transcription as final:

**Audio₁ → Partial hypothesis**

**Audio₁ + Audio₂ → Improved hypothesis**

**Audio₁ + Audio₂ + Audio₃ → Better hypothesis**

This provided a useful mental model for streaming speech recognition and temporal sequence decoding.

---

# 7. Text-to-Speech Research

The third major R&D track explored **Text-to-Speech (TTS)**, especially multilingual and Indian-language speech synthesis.

I researched:

- Coqui TTS
- Bark
- AI4Bharat Indic Parler-TTS
- RASMALAI
- LJSpeech dataset formatting
- Conditional Variational Autoencoders
- Adversarial learning
- Speech datasets
- Accent and intonation modeling

## Coqui TTS

I studied the open-source **Coqui TTS** ecosystem and its model architectures.

This also included research into:

**Conditional Variational Autoencoder with Adversarial Learning for End-to-End Text-to-Speech**

The research helped build an understanding of how modern TTS systems can learn mappings between text and acoustic representations.

## Bark

I also explored **Suno AI's Bark** as another generative speech/audio architecture.

This provided exposure to a different approach to generative speech synthesis compared with more conventional TTS pipelines.

---

# 8. Indic Parler-TTS / RASMALAI Research

Another important experiment involved **AI4Bharat's Indic Parler-TTS** and the RASMALAI research:

**Resources for Adaptive Speech Modeling in Indian Languages with Accents and Intonations**

The research focused on the difficulty of representing Indian-language speech across different accents, speakers and speaking styles.

## Gujarati Dataset Creation

For experimentation, I worked on creating a Gujarati speech dataset from available radio data.

The data preparation involved:

**Gujarati Radio Data → Audio Segmentation / Preparation → LJSpeech Format → TTS Training Dataset**

The dataset was prepared in the **LJSpeech-style format** required by the training pipeline.

This was a valuable experience because it exposed me to one of the realities of applied ML: model training is often only one part of the problem. **Dataset construction, formatting, cleaning and preparation can be equally important.**

---

# 9. GPU-Constrained Model Training

The TTS research also introduced me to the practical economics of AI infrastructure.

Unlike some of the smaller experiments, modern TTS models required substantially heavier GPU resources. During the internship, GPUs were rented through **TensorDock** for experiments.

The project was ultimately not completed because the compute requirements became prohibitively expensive relative to the available resources.

That limitation itself became an important engineering lesson:

**Model capability is only one dimension of an AI system — compute availability, inference cost, training cost and dataset size can determine whether an approach is practically viable.**

---

# 10. Engineering Philosophy Learned During the Internship

One of the biggest lessons from this period was that **AI engineering is not simply model engineering**.

At the time, models were less reliable at:

- Strict structured JSON generation
- Consistently following complex guardrails
- Reliable tool execution
- Deterministic extraction
- Domain-specific medical terminology
- Multilingual Indian speech
- Long-running agentic workflows

As a result, practical systems frequently required a combination of:

**Neural Models + Rule-Based Logic + Specialized NLP + Signal Processing + Application Code**

For example, rather than asking an LLM to reliably identify every medical entity, a dedicated **Medical NER** component could extract medical terminology and medicine names, while the LLM handled higher-level language understanding and summarization.

This hybrid approach became an important foundation for how I later approached AI systems.

---

# 11. Technical Stack

### LLM / NLP

- Llama 3 8B
- Hugging Face Transformers
- PyTorch
- Medical NER
- Clinical summarization

### Speech / Audio

- Whisper
- IndicConformer
- SpeechBrain
- VoxLingua107
- NVIDIA NeMo
- Kaldi
- Vosk
- ESPnet
- Coqui TTS
- Bark
- Indic Parler-TTS

### Audio Processing

- FFmpeg
- librosa
- torchaudio
- soundfile
- PyDub
- PyAudio
- sounddevice
- audioread

### Infrastructure / Experimentation

- FastAPI
- WebSockets
- Local LLM inference
- llama.cpp
- GPU-based training
- TensorDock

---

# 12. Key Quantified Work

* **116K+** healthcare records processed in the clinical-data POC
* **8B** parameter Llama 3 model explored for clinical summarization
* **4-bit** Llama 3 quantization explored for local inference
* **22** Indian languages covered by the IndicConformer research studied
* **12,000 hours** of IndicVoices speech dataset studied
* **22,563 speakers** represented in IndicVoices
* **208 Indian districts** represented in the dataset
* **107 languages** available in the VoxLingua107 language-identification model explored
* **3 major R&D tracks:** Clinical AI, Speech-to-Text, and Text-to-Speech
* **Real-time WebSocket** speech-processing architecture prototyped
* **CTC + RNNT** decoding approaches explored
* **Gujarati** speech dataset prepared in LJSpeech format for TTS experimentation
* **Multiple CNN generations** studied from AlexNet through EfficientNet
* **Multiple open-source speech ecosystems** evaluated and integrated into POCs

---

# 13. What This Internship Taught Me

This internship was the point where AI stopped being something I was simply learning from papers or tutorials and became something I had to **engineer under real constraints**.

The biggest lessons were:

* **Models are components, not complete systems.**
* **Reliability often requires deterministic logic around probabilistic models.**
* **Data preparation can be as important as model architecture.**
* **Speech AI requires understanding both signal processing and deep learning.**
* **GPU economics directly influence engineering decisions.**
* **Domain-specific models can be necessary when general models are unreliable.**
* **Real-time AI introduces an entirely different class of engineering problems.**
* **Healthcare AI demands significantly more attention to correctness and workflow design.**
* **Open-source research can be transformed into practical prototypes through experimentation and integration.**
* **Understanding the underlying architecture of a model is far more valuable than treating it as an API.**

Most importantly, this internship gave me my first experience of taking an AI problem from **research → model selection → data preparation → experimentation → system integration → optimization**, and it became the foundation for the much larger AI systems I built later.
