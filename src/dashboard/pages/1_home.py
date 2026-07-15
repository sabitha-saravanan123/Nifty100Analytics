import streamlit as st
from utils.db import get_ratios
st.title("Home Dashboard")
df = get_ratios()
col1,col2,col3 = st.columns(3)
col1.metric("Average ROE", round(df["return_on_equity_pct"].mean(),2))
col2.metric("Average ROCE", round(df["return_on_capital_employed_pct"].mean(),2))
col3.metric("Total Companies", df["company_id"].nunique())
st.subheader("Top 10 Companies")
top=df.sort_values("return_on_equity_pct",ascending=False)
st.dataframe(top.head(10))