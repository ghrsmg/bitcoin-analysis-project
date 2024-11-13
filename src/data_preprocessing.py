import pandas as pd


def preprocess_data(df):
    # Set timestamp as index for better analysis
    df.set_index('timestamp', inplace=True)

    # Adding additional features for prediction
    df['price_diff'] = df['price'].diff()  # Price change
    df.dropna(inplace=True)  # Remove any NA values
    return df
