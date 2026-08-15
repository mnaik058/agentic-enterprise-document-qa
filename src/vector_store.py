import json
from pathlib import Path
import numpy as np
import faiss

class VectorStore:
    def __init__(self, directory="storage"):
        self.directory = Path(directory)
        self.directory.mkdir(parents=True, exist_ok=True)
        self.index_path = self.directory / "index.faiss"
        self.meta_path = self.directory / "metadata.json"

    def save(self, vectors, metadata):
        matrix = np.asarray(vectors, dtype="float32")
        if matrix.ndim != 2 or len(matrix) == 0:
            raise ValueError("No vectors to store.")
        faiss.normalize_L2(matrix)
        index = faiss.IndexFlatIP(matrix.shape[1])
        index.add(matrix)
        faiss.write_index(index, str(self.index_path))
        self.meta_path.write_text(json.dumps(metadata, indent=2), encoding="utf-8")

    def load(self):
        if not self.exists():
            raise FileNotFoundError("Vector store does not exist.")
        return faiss.read_index(str(self.index_path)), json.loads(self.meta_path.read_text(encoding="utf-8"))

    def exists(self):
        return self.index_path.exists() and self.meta_path.exists()
