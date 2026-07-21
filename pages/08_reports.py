import streamlit as st
import sys
import os
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)
from src.dashboard.utils.db import get_ratios
st.title("Reports")
df = get_ratios()
st.dataframe(df)
csv = df.to_csv(index=False).encode("utf-8")
st.download_button(
    "Download Financial Ratios",
    csv,
    "financial_ratios.csv",
    "text/csv")