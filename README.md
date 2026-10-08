# LangChain Ollama AI Chat Assistant

A lightweight local AI chatbot built with **LangChain, Ollama, and Streamlit**. The application provides a simple conversational interface for interacting with locally hosted Large Language Models (LLMs) without requiring an external LLM API.

## Features

- Local LLM inference using Ollama
- LangChain integration for prompt construction and model orchestration
- Interactive chat interface using Streamlit
- Support for locally installed Ollama models
- No external LLM API key required
- Simple and extensible architecture
- Suitable for experimentation with local LLM applications
- Can be extended with RAG, agents, tools, memory, and vector databases

## Architecture

```text
┌─────────────────────────┐
│       Streamlit UI      │
│                         │
│   Chat Input / Output   │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│   LangChain Prompt      │
│   ChatPromptTemplate    │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│       OllamaLLM         │
│                         │
│    Gemma 3 / Llama      │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│      Local LLM          │
│        Response         │
└─────────────────────────┘
```

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Application development |
| LangChain | LLM orchestration |
| Ollama | Local LLM runtime |
| Gemma 3 | Default language model |
| Streamlit | Web-based chat interface |

## Project Structure

```text
Langchain-Ollama-Chatbot/
│
├── LangchainBasicModelUse.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Prerequisites

Before running the application, install:

- Python 3.10 or higher
- Conda
- Ollama
- A compatible Ollama model

Verify the installations:

```bash
python --version
conda --version
ollama --version
```

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/Langchain-Ollama-Chatbot.git
cd Langchain-Ollama-Chatbot
```

Replace `YOUR_USERNAME` with your GitHub username.

### 2. Create a Conda Environment

```bash
conda create -n langchain-ai python=3.11 -y
```

Activate the environment:

```bash
conda activate langchain-ai
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

Example `requirements.txt`:

```text
langchain-core
langchain-ollama
streamlit
```

## Install the Ollama Model

The application currently uses:

```text
gemma3:latest
```

Download the model:

```bash
ollama pull gemma3:latest
```

Verify the installed models:

```bash
ollama list
```

## Run the Application

Start the Ollama service:

```bash
ollama serve
```

Then launch the Streamlit application:

```bash
streamlit run LangchainBasicModelUse.py
```

Open the URL displayed by Streamlit, typically:

```text
http://localhost:8501
```

## How It Works

The application follows a straightforward LangChain pipeline:

```text
User Question
      |
      v
ChatPromptTemplate
      |
      v
OllamaLLM
      |
      v
Gemma 3
      |
      v
Generated Response
      |
      v
Streamlit UI
```

The prompt is constructed using `ChatPromptTemplate`:

```python
prompt = ChatPromptTemplate.from_template(template)
```

The Ollama model is initialized with:

```python
model = OllamaLLM(model="gemma3:latest")
```

The prompt and model are composed into a LangChain chain:

```python
chain = prompt | model
```

The user's question is then passed to the chain:

```python
chain.invoke({"question": question})
```

## Why Local AI?

Running an LLM locally provides several advantages.

### Privacy

Prompts and generated responses can remain on the local machine rather than being sent to a third-party hosted LLM API.

### No API Key

The application does not require an OpenAI, Gemini, or other cloud LLM API key.

### Offline Inference

After downloading the model, the application can operate without continuous internet access.

### Experimentation

Local models provide a practical environment for experimenting with:

- Large Language Models
- Prompt engineering
- LangChain
- Retrieval-Augmented Generation
- AI agents
- Tool calling
- Local inference
- Model evaluation

## Future Improvements

Potential extensions include:

- [ ] Streaming responses
- [ ] Persistent conversation memory
- [ ] Multiple model selection
- [ ] RAG with PDF and document support
- [ ] Vector database integration
- [ ] Embedding models
- [ ] Tool calling
- [ ] LangGraph agents
- [ ] Conversation export
- [ ] Model performance monitoring
- [ ] GPU acceleration
- [ ] Docker deployment
- [ ] Authentication
- [ ] Production deployment

## Potential Future Architecture

```text
                    ┌───────────────┐
                    │  Streamlit UI │
                    └───────┬───────┘
                            │
                            v
                    ┌───────────────┐
                    │   LangChain   │
                    └───────┬───────┘
                            │
                ┌───────────┴───────────┐
                │                       │
                v                       v
          ┌───────────┐           ┌───────────┐
          │    RAG    │           │   Tools   │
          └─────┬─────┘           └─────┬─────┘
                │                       │
                └───────────┬───────────┘
                            v
                    ┌───────────────┐
                    │    Ollama     │
                    └───────┬───────┘
                            │
                            v
                       Local LLM
```

## Example Questions

You can test the assistant with questions such as:

```text
Explain machine learning in simple terms.
```

```text
What is the difference between AI and Generative AI?
```

```text
Explain Python decorators with an example.
```

```text
What is Retrieval-Augmented Generation?
```

```text
Explain Transformers from first principles.
```

## Learning Objectives

This project provides practical exposure to:

- Large Language Models
- Prompt engineering
- LangChain
- Ollama
- Local LLM inference
- Streamlit
- LLM application architecture
- Python-based AI development

## Author

**Saksham Sahu**

B.Tech in Mathematics and Computing

Areas of Interest:

```text
Artificial Intelligence
Machine Learning
Data Science
Generative AI
Agentic AI
LLM Systems
```

## Contributing

Contributions, improvements, and suggestions are welcome.

To contribute:

1. Fork the repository.
2. Create a feature branch.
3. Implement your changes.
4. Commit your changes.
5. Push the branch.
6. Open a Pull Request.

## License

This project is intended for educational and experimental purposes.
