import json
from pathlib import Path
import pandas as pd
import streamlit as st
import yfinance as yf

def load_presets():
    path = Path("data/presets.json")
    if not path.exists():
        return []
    
    with open(path, "r") as f:
        return json.load(f)

@st.cache_data
def load_stock_historical_data(ticker_symbol, start_date):
    try:
        df = yf.download(ticker_symbol, start=start_date,auto_adjust=True, progress=False)
        if df.empty:
            raise ValueError(f"No data found for ticker symbol: {ticker_symbol}")
        return df[['Close']].rename(columns={'Close': 'Price'})
    except Exception as e:
        cache = pd.read_csv("data/cache.csv", index_col="Dates", parse_dates=True)
        if ticker_symbol in cache.columns:
            ticker_data = cache[[ticker_symbol]].dropna().rename(columns={ticker_symbol: 'Price'})
            return ticker_data[ticker_data.index >= start_date]
        raise RuntimeError(f"Failed to fetch data for {ticker_symbol} and no cached data available. Error: {e}")