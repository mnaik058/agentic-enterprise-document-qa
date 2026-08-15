# Architecture

## Components
- Streamlit UI
- PDF/TXT/CSV/Excel ingestion
- Chunking
- OpenAI embeddings
- FAISS vector store
- Planner Agent
- Retriever Tool
- Answer Agent
- Validator Agent

## Data flow
1. Upload files.
2. Parse content.
3. Normalize and split content.
4. Generate embeddings.
5. Store vectors and metadata.
6. Receive question.
7. Planner creates retrieval query.
8. Retriever finds top-k chunks.
9. Answer agent generates grounded response.
10. Validator checks support.
11. UI displays answer and sources.
