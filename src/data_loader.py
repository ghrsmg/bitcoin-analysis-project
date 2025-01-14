import pandas as pd

def load_data(filepath):
    """
    Load the Bitcoin dataset from the given CSV file.
    """
    data = pd.read_csv(filepath)
    data['Timestamp'] = pd.to_datetime(data['Timestamp'], unit='s')
    return data
