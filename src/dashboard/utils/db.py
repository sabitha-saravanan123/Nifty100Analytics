import sqlite3
import pandas as pd
import streamlit as st
from src.dashboard.utils.db import get_ratios
DB = "db/nifty100.db"
@st.cache_data
def get_table(table):
    conn = sqlite3.connect(DB)
    df = pd.read_sql(f"SELECT * FROM {table}", conn)
    conn.close()
    return df
def get_companies():
    return get_table("companies")
def get_ratios():
    return get_table("financial_ratios")