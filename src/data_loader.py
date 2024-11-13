import pandas as pd
import requests


def load_data(from_api=True):
    if from_api:
        url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=365"
        response = requests.get(url)
        data = response.json()['prices']
        df = pd.DataFrame(data, columns=['timestamp', 'price'])
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    else:
        df = pd.read_csv('data/bitcoin_data.csv')

    return df
