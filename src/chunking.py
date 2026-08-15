from dataclasses import dataclass

@dataclass
class Chunk:
    text: str
    file_name: str
    chunk_id: int

def split_text(text: str, chunk_size: int = 900, overlap: int = 150) -> list[str]:
    text = " ".join(text.split())
    if not text:
        return []
    chunks = []
    start = 0
    while start < len(text):
        end = min(start + chunk_size, len(text))
        chunks.append(text[start:end])
        if end == len(text):
            break
        start = max(end - overlap, start + 1)
    return chunks

def make_chunks(text: str, file_name: str, chunk_size: int = 900, overlap: int = 150) -> list[Chunk]:
    return [Chunk(t, file_name, i) for i, t in enumerate(split_text(text, chunk_size, overlap))]
