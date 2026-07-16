import streamlit as st
import sys
import os

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from src.dashboard.utils.db import get_ratios
st.title("Financial Screener")
df = get_ratios()

st.subheader("Presets")
col1,col2,col3 = st.columns(3)
if col1.button("Quality"):
    roe = 15
    de = 1.0
if col2.button("Value"):
    roe = 10
    de = 2.0
if col3.button("Growth"):
    roe = 20
    de = 2.0

roe = st.sidebar.slider("Minimum ROE", 0, 50, 10)
de = st.sidebar.slider("Maximum D/E", 0.0, 5.0, 2.0)
result = df[(df["return_on_equity_pct"] >= roe) &(df["debt_to_equity"] <= de)]
st.write("Companies Found:", len(result))
st.dataframe(result)
csv = result.to_csv(index=False).encode("utf-8")
st.download_button("Download CSV",csv,"screener_output.csv","text/csv")