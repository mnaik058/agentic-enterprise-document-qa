from .config import settings
from .embeddings import embed_query
from .vector_store import VectorStore
import numpy as np
import faiss

class LocalRetriever:
    def __init__(self, top_k=None, threshold=0.20):
        self.top_k = top_k or settings.top_k
        self.threshold = threshold
        self.store = VectorStore(settings.storage_dir)

    def exists(self):
        return self.store.exists()

    def search(self, query):
        index, metadata = self.store.load()
        q = np.asarray([embed_query(query)], dtype="float32")
        faiss.normalize_L2(q)
        scores, ids = index.search(q, self.top_k)
        results = []
        for score, idx in zip(scores[0], ids[0]):
            if idx < 0 or float(score) < self.threshold:
                continue
            item = dict(metadata[idx])
            item["score"] = float(score)
            results.append(item)
        return results
