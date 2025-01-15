import pandas as pd

def load_data(filepath):
    """
    Load the Bitcoin dataset from the given CSV file.
    """
    # Load data and parse the 'Timestamp' column as datetime
    data = pd.read_csv(filepath, parse_dates=['Timestamp'])
    data.set_index('Timestamp', inplace=True)
    return data