from pathlib import Path
from .config import settings
from .loaders import load_document
from .chunking import make_chunks
from .embeddings import embed_texts
from .vector_store import VectorStore

def ingest_files(paths):
    chunks = []
    for path in paths:
        p = Path(path)
        text = load_document(p)
        chunks.extend(make_chunks(text, p.name, settings.chunk_size, settings.chunk_overlap))
    if not chunks:
        raise ValueError("No usable content found.")
    vectors = embed_texts([c.text for c in chunks])
    metadata = [{"file": c.file_name, "chunk": c.chunk_id, "text": c.text} for c in chunks]
    VectorStore(settings.storage_dir).save(vectors, metadata)
    return {"documents": len({c.file_name for c in chunks}), "chunks": len(chunks)}

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("directory")
    args = parser.parse_args()
    paths = [p for p in Path(args.directory).iterdir() if p.is_file()]
    print(ingest_files(paths))
