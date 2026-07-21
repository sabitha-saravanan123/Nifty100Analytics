import streamlit as st
import sys
import os
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)
from src.dashboard.utils.db import get_ratios
st.title("Capital Allocation")
df = get_ratios()
if "free_cash_flow_cr" not in df.columns:
    df["free_cash_flow_cr"] = 0
def pattern(x):
    if x > 0:
        return "Positive"
    if x < 0:
        return "Negative"
    return "Neutral"
df["Capital Pattern"] = df["free_cash_flow_cr"].apply(pattern)
st.dataframe(df[["company_id","free_cash_flow_cr","Capital Pattern"]])