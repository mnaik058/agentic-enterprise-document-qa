# Demo Script

1. Run `streamlit run app.py`.
2. Upload `data/sample_documents/company_policy.txt`.
3. Click **Build / update knowledge store**.
4. Ask: **What should employees do with confidential company information?**
5. Show the grounded answer and source chunk.
6. Ask an unrelated question such as **What is the company's stock price?**
7. Demonstrate that unsupported information is not invented.
8. Explain Planner → Retriever → Answer → Validator.
9. Run `pytest -q`.
