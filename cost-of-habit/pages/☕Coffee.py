import streamlit as st

st.set_page_config(page_title="Starbucks", page_icon="☕", layout="wide")
st.title("☕ Morning Coffee")

st.sidebar.success("☕")

col_1, col_2, col_3, col_4 = st.columns(4)
with col_1:
    ticker = st.write("SBUX")
with col_2:
    amount = st.number_input("Amount (£)", value=3.80, step=0.50)
with col3:
    freq = st.selectbox("Frequency", ["daily", "weekly", "monthly"], index=0)
with col4:
    start_date = st.text_input("Start Date", value="2019-01-01")

try:
    with st.spinner("Inputing variable..."):
        res = simulate_habit(ticker=ticker, amount=amount, freq=freq, start_date=start_date)