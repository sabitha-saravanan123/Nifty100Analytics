import streamlit as st
import sys
import os

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from src.dashboard.utils.db import get_ratios
st.title("Peer Comparison")
df = get_ratios()
company = st.selectbox("Select Company",sorted(df["company_id"].unique()))
peer = df[df["company_id"] == company]
st.subheader("Company KPIs")
st.dataframe(peer)
st.subheader("ROE Chart")
st.bar_chart(peer["return_on_equity_pct"])