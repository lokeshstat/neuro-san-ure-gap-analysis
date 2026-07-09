from __future__ import annotations

import streamlit as st
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
BACKEND = ROOT / "backend"
if str(BACKEND) not in sys.path:
    sys.path.insert(0, str(BACKEND))

from run import invoke_agent  # noqa: E402

st.set_page_config(page_title="Neuro-san Network", layout="wide")
st.title("Neuro-san Generated Network")

prompt = st.text_area("Inquiry", "Hello")
if st.button("Run"):
    st.code(invoke_agent(prompt))
