
def preprocess_data(data):
    """
    Resample to daily data and clean the Bitcoin dataset for analysis.
    """
    data = data.set_index('Timestamp')
    daily_data = data.resample('D').mean()
    daily_data = daily_data.dropna()
    return daily_data
