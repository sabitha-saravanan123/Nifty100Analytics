import streamlit as st
import sys
import os
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)
from src.dashboard.utils.db import get_ratios
st.title("Trend Analysis")
df = get_ratios()
company = st.selectbox("Select Company",sorted(df["company_id"].unique()))
metric = st.selectbox("Select Metric",
    [ "return_on_equity_pct",
        "return_on_capital_employed_pct",
        "net_profit_margin_pct",
        "debt_to_equity",
        "asset_turnover"])
company_df = df[df["company_id"] == company]
st.subheader(metric)
if "year" in company_df.columns:
    company_df = company_df.sort_values("year")
    st.line_chart(company_df.set_index("year")[metric])
else:
    st.warning("Year column not found.")