from src.chunking import split_text, make_chunks

def test_split_text_nonempty():
    chunks = split_text("a " * 100, chunk_size=50, overlap=10)
    assert chunks
    assert all(chunks)

def test_metadata():
    chunks = make_chunks("hello world", "demo.txt", 50, 5)
    assert chunks[0].file_name == "demo.txt"
    assert chunks[0].chunk_id == 0
