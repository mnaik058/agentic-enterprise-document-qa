import os
import tempfile
from pathlib import Path
import streamlit as st
from dotenv import load_dotenv
from src.ingest import ingest_files
from src.graph import run_agentic_qa
from src.retriever import LocalRetriever

load_dotenv()
st.set_page_config(page_title="Agentic Enterprise Document QA", page_icon="📚", layout="wide")
st.title("📚 Agentic Enterprise Document QA")
st.caption("Generative AI + RAG + Agentic AI capstone implementation")

with st.sidebar:
    st.header("Configuration")
    top_k = st.slider("Retrieved chunks", 2, 10, int(os.getenv("TOP_K", "5")))
    st.info("Upload documents, index them, then ask a natural-language question.")

uploads = st.file_uploader("Upload PDF, TXT, CSV or Excel files", type=["pdf", "txt", "csv", "xlsx", "xls"], accept_multiple_files=True)

if uploads and st.button("Build / update knowledge store", type="primary"):
    if not os.getenv("OPENAI_API_KEY"):
        st.error("OPENAI_API_KEY is not configured.")
    else:
        with tempfile.TemporaryDirectory() as tmp:
            paths = []
            for upload in uploads:
                target = Path(tmp) / upload.name
                target.write_bytes(upload.getvalue())
                paths.append(target)
            with st.spinner("Parsing, chunking, embedding and indexing documents..."):
                result = ingest_files(paths)
            st.success(f"Indexed {result['chunks']} chunks from {result['documents']} document(s).")

st.divider()
question = st.text_area("Ask a question about the uploaded documents", placeholder="Example: What are the main risks described in the policy?")

if st.button("Ask the agents", type="secondary"):
    if not question.strip():
        st.warning("Enter a question first.")
    elif not os.getenv("OPENAI_API_KEY"):
        st.error("OPENAI_API_KEY is not configured.")
    else:
        try:
            retriever = LocalRetriever(top_k=top_k)
            if not retriever.exists():
                st.warning("Please upload and index documents first.")
            else:
                with st.spinner("Planner → Retriever → Answerer → Validator..."):
                    result = run_agentic_qa(question, retriever)
                st.subheader("Answer")
                st.write(result["answer"])
                st.subheader("Validation")
                st.write(result["validation"])
                st.subheader("Sources")
                for source in result.get("sources", []):
                    st.markdown(f"- **{source['file']}** — chunk {source['chunk']} — similarity `{source['score']:.3f}`")
        except Exception as exc:
            st.error(f"Application error: {exc}")

st.divider()
st.markdown("**Workflow:** Plan → Retrieve → Generate → Validate")
