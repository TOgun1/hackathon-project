import streamlit as st
import pandas as pd
from src.data_loader import load_presets
from src.engine import calculate_coh
import plotly.express as px
presets = load_presets()
st.title("Cost of Habit")
st.write("What if you bought equity instead of everyday expenses?")

st.sidebar.title("Preset Options")
preset = st.sidebar.selectbox(
    "Choose a preset:",
    ["Coffee","Phone Upgrade","Gym Membership","Netflix Subscription"],
    format_func=lambda k: k.replace("_", " ").title(),
)
selected = presets[preset]
frequency_map = {
    "Daily": "B",
    "Weekly": "W-FRI",
    "Monthly": "ME"
}
date=st.selectbox("Choose a start date:", ["2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023", "2024", "2025", "2026"])
freq=st.selectbox("Choose the frequency of your habit:", ["Daily", "Weekly", "Monthly"])
ticker = selected["ticker"]
default_cost = selected["cost"]
cost=st.number_input("Enter the cost of your habit (Optional):", min_value=0.0,value=float(default_cost), step=0.01, format="%.2f")
frequency = frequency_map[freq]
if st.button("Calculate"):
    # Call the calculation function here
    try:
        results = calculate_coh(ticker, cost if cost > 0 else default_cost, date, frequency)
        col1, col2, col3 = st.columns(3)
        col1.metric("Cash Spent", f"£{results['total_cash']:,.2f}")
        col2.metric("portfolio_value", f"£{results['portfolio_value']}", f"£{results['profit']}")
        col3.metric("ROI", f"{results['profit_pct']}%")

        chart_data = results['df'].rename(columns={
            "cumulative_cash": "Cash Spent",
            "portfolio_value": "Portfolio Value"
        })
        fig = px.line(
            chart_data,
            x=chart_data.index,
            y=["Cash Spent", "Portfolio Value"],
            labels={"value": "Total Value (£)", "index": "Date", "variable": "Metric"},
            color_discrete_map={"Cash Spent": "#ef553b", "Portfolio Value": "#00cc96"}
        )
        st.plotly_chart(fig, use_container_width=True)
    except Exception as e:
        st.error(f"An error occurred during calculation: {e}")
    pass