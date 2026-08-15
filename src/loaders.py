from pathlib import Path
import pandas as pd
from pypdf import PdfReader

SUPPORTED = {".pdf", ".txt", ".csv", ".xlsx", ".xls"}

def load_document(path: str | Path) -> str:
    p = Path(path)
    suffix = p.suffix.lower()
    if suffix not in SUPPORTED:
        raise ValueError(f"Unsupported file type: {p.suffix}")
    if suffix == ".pdf":
        reader = PdfReader(str(p))
        text = "\n".join(page.extract_text() or "" for page in reader.pages)
    elif suffix == ".txt":
        text = p.read_text(encoding="utf-8", errors="ignore")
    elif suffix == ".csv":
        text = pd.read_csv(p).to_csv(index=False)
    else:
        sheets = pd.read_excel(p, sheet_name=None)
        text = "\n\n".join(f"Sheet: {name}\n{df.to_csv(index=False)}" for name, df in sheets.items())
    if not text.strip():
        raise ValueError(f"No extractable text found in {p.name}")
    return text
