import streamlit as st
st.set_page_config(page_title="Nifty 100 Analytics",layout="wide",initial_sidebar_state="expanded")
st.title("📈 Nifty 100 Analytics Dashboard")
st.sidebar.title("Navigation")
page = st.sidebar.radio("Choose Screen",["Home","Company Profile","Screener","Peer Comparison","Trend Analysis","Sector Analysis","Capital Allocation","Reports"])
st.write(f"### {page}")
st.write("Page is under development.")