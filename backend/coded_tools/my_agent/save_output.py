from __future__ import annotations

from pathlib import Path


def save_output(content: str, filename: str = "output.tex") -> str:
    out = Path(filename).name
    path = Path.cwd() / out
    path.write_text(content, encoding="utf-8")
    return str(path.resolve())
