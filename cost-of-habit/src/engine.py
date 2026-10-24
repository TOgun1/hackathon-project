from data_loader import load_stock_historical_data
from calculator import calculate_dca

def calculate_coh(ticker, cost, start_yr, frequency):
    date = f"{start_yr}-01-01"
    df = load_stock_historical_data(ticker, date)
    result = calculate_dca(df, frequency, cost)

    return result


