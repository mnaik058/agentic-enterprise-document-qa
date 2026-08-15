from pathlib import Path
import pytest
from src.loaders import load_document

def test_txt_loader(tmp_path: Path):
    p = tmp_path / "demo.txt"
    p.write_text("Enterprise policy text.", encoding="utf-8")
    assert "Enterprise policy" in load_document(p)

def test_unsupported(tmp_path: Path):
    p = tmp_path / "demo.doc"
    p.write_text("x", encoding="utf-8")
    with pytest.raises(ValueError):
        load_document(p)
