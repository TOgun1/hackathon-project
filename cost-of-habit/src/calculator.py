import yfinance as yf
import pandas as pd
import streamlit as st

def calculate_dca(df, frequency, cost):
    df2 = df.resample(frequency).last()

    df2['cash_spent'] = cost
    df2['cumulative_cash'] = df2['cash_spent'].cumsum()

    df2['shares_bought'] = df2['cash_spent'] / df2['Price']
    df2['cm_shares'] = df2['shares_bought'].cumsum()

    df2['portfolio_value'] = df2['cm_shares'] * df2['Price']
    recent = df2['cash_spent'].iloc[-1] # Gets the last item
    total_spent = float(recent['cumulative_cash'])
    final = float(recent['portfolio_value'])

    profit_margin = final - total_spent

    profit_pct = (profit_margin / total_spent) * 100 if total_spent != 0 else 0
    return {
        "df": df2[['cumulative_cash', 'portfolio_value']],
        "total_cash": round(total_spent, 2),
        "portfolio_value": round(final, 2),
        "profit": round(profit_margin, 2),
        "profit_pct": round(profit_pct, 1)
    }



