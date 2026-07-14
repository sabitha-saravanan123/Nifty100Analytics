import sqlite3
import pandas as pd
import streamlit as st
DATABASE = "db/nifty100.db"
@st.cache_data
def load_table(table):
    conn = sqlite3.connect(DATABASE)
    df = pd.read_sql(f"SELECT * FROM {table}", conn)
    conn.close()
    return df
def get_companies():
    return load_table("companies")
def get_ratios():
    return load_table("financial_ratios")
def get_peer():
    return load_table("peer_percentiles")