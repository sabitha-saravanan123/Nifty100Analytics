import streamlit as st
import sys
import os
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)
from src.dashboard.utils.db import get_companies,get_ratios
st.title("Sector Analysis")
companies = get_companies()
ratios = get_ratios()
sector = st.selectbox("Select Sector",sorted(companies["sector"].dropna().unique()))
sector_companies = companies[companies["sector"] == sector]
st.subheader("Companies")
st.dataframe(sector_companies)
ids = sector_companies["company_id"]
sector_ratios = ratios[ratios["company_id"].isin(ids)]
st.subheader("Average ROE")
if len(sector_ratios)>0:st.metric("ROE",round(sector_ratios["return_on_equity_pct"].mean(),2))