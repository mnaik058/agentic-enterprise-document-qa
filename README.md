# Agentic Enterprise Document QA

Generative AI & ML Capstone Project — AI-agent-based enterprise document question-answering and decision-support system.

## Objective
Users upload PDF, TXT, CSV or Excel documents, ask natural-language questions, retrieve relevant evidence from a vector knowledge store, and receive grounded LLM answers.

## Architecture
User -> Streamlit UI -> Ingestion -> Chunking -> Embeddings -> FAISS

Question -> Planner Agent -> Retriever -> Answer Agent -> Validator -> Grounded Response

## Features
- PDF/TXT/CSV/Excel ingestion
- Text chunking and semantic retrieval
- OpenAI embeddings
- FAISS vector store
- Planner, Retriever, Answer and Validator agent stages
- Source citations and validation
- Streamlit UI
- Automated tests and GitHub Actions
- Docker deployment

## Quick start
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
# copy .env.example to .env and set OPENAI_API_KEY
streamlit run app.py
```

## Testing
```bash
pytest -q
```

## Docker
```bash
docker build -t agentic-doc-qa .
docker run --rm -p 8501:8501 --env-file .env agentic-doc-qa
```

Do not commit API keys or other secrets.
