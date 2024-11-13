from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np


def train_model(df):
    # Using price_diff as feature to predict future price
    X = df[['price_diff']].shift(1).fillna(0).values
    y = df['price'].values

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

    model = LinearRegression()
    model.fit(X_train, y_train)
    return model


def predict(model, df):
    X = df[['price_diff']].shift(1).fillna(0).values
    predictions = model.predict(X)
    df['predicted_price'] = predictions
    return df
