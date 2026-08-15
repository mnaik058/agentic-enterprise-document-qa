from openai import OpenAI
from .config import settings

def embed_texts(texts):
    client = OpenAI()
    response = client.embeddings.create(model=settings.embedding_model, input=texts)
    return [item.embedding for item in response.data]

def embed_query(text):
    return embed_texts([text])[0]
