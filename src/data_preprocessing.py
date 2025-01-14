import pandas as pd

def preprocess_data(data):
    """
    Resample and clean the Bitcoin dataset for analysis.
    """
    # Resample to daily data for aggregation
    data = data.set_index('Timestamp')
    daily_data = data.resample('D').mean()
    daily_data = daily_data.dropna()
    return daily_data
