import streamlit as st
import sys
import os

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from src.dashboard.utils.db import get_ratios
st.title("Company Profile")
df=get_ratios()
company=st.selectbox("Select Company ID",sorted(df["company_id"].unique()))
data=df[df["company_id"]==company]
if len(data)>0:
    row=data.iloc[0]
    c1,c2,c3=st.columns(3)
    c1.metric("ROE",round(row["return_on_equity_pct"],2))
    c2.metric("ROCE",round(row["return_on_capital_employed_pct"],2))
    c3.metric("NPM",round(row["net_profit_margin_pct"],2))
    st.subheader("Financial Data")
    st.dataframe(data)