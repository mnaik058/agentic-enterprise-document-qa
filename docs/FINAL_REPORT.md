# Generative AI & ML Capstone — Final Project Report

## 1. Introduction
This project implements an agent-based enterprise document question-answering and decision-support application based on the supplied capstone brief.

## 2. Problem Statement
Enterprise information is distributed across PDF, text, CSV and spreadsheet documents. Users need a natural-language interface that retrieves relevant information and produces grounded answers.

## 3. Objectives
- Document upload and processing
- Chunking and semantic search
- Embeddings and vector knowledge store
- Relevant evidence retrieval
- Grounded LLM answers
- Agent planning, retrieval, reasoning and validation
- Reliability controls
- Reproducible deployment

## 4. Technology Stack
| Area | Technology |
|---|---|
| UI | Streamlit |
| LLM | OpenAI Chat Completions |
| Embeddings | OpenAI embeddings |
| Vector store | FAISS |
| PDF | pypdf |
| CSV/Excel | pandas/openpyxl |
| Agent stages | Planner / Retriever / Answer / Validator |
| Deployment | Docker |

## 5. Workflow
Documents are parsed, normalized, chunked, embedded and indexed. At query time, the Planner creates a retrieval query, the Retriever finds evidence, the Answer Agent generates a grounded response, and the Validator checks support.

## 6. Reliability and Safety
File validation, empty-content checks, retrieval thresholds, context-only answering, source metadata and a validation pass reduce hallucination risk. They do not guarantee zero hallucinations.

## 7. Testing
Unit tests cover chunking, metadata preservation, TXT loading and unsupported file handling. Run `pytest -q`.

## 8. Deployment
The application runs with Streamlit or the supplied Dockerfile.

## 9. Limitations
Image-only PDF OCR, enterprise authentication/authorization, audit logging and managed production vector infrastructure are outside the capstone scope.

## 10. Future Enhancements
Add OCR, hybrid search, managed vector DB, authentication, document permissions, evaluation datasets, observability and production deployment.

## 11. Conclusion
The project demonstrates a complete Generative AI and Agentic AI workflow for enterprise document QA, from ingestion and semantic retrieval to grounded generation and validation.
