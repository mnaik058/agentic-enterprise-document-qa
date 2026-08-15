from openai import OpenAI
from .config import settings
from .prompts import PLANNER_PROMPT, ANSWER_PROMPT, VALIDATOR_PROMPT

def _chat(prompt):
    client = OpenAI()
    response = client.chat.completions.create(model=settings.chat_model, temperature=0, messages=[{"role": "user", "content": prompt}])
    return response.choices[0].message.content.strip()

def _context(results):
    return "\n\n".join(f"[{r['file']}, chunk {r['chunk']}]\n{r['text']}" for r in results)

def run_agentic_qa(question, retriever):
    retrieval_query = _chat(PLANNER_PROMPT.format(question=question))
    results = retriever.search(retrieval_query)
    if not results:
        return {"answer": "I could not find sufficiently relevant evidence in the indexed documents.", "validation": "REVIEW — no supporting evidence was retrieved.", "sources": []}
    context = _context(results)
    answer = _chat(ANSWER_PROMPT.format(question=question, context=context))
    validation = _chat(VALIDATOR_PROMPT.format(answer=answer, context=context))
    return {"answer": answer, "validation": validation, "sources": results}
