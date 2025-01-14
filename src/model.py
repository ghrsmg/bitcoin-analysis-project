from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd

def predict_prices(data, future_days=730):
    """
    Predict Bitcoin prices using a linear regression model.
    Predictions start from the last known close price.
    """
    X = np.arange(len(data)).reshape(-1, 1)
    y = data['Close'].values

    model = LinearRegression()
    model.fit(X, y)

    future_X = np.arange(len(data), len(data) + future_days).reshape(-1, 1)
    future_predictions = model.predict(future_X)

    last_price = y[-1]
    prediction_diff = future_predictions[0] - last_price
    adjusted_predictions = future_predictions - prediction_diff

    last_date = data.index[-1]
    future_dates = [last_date + pd.Timedelta(days=i) for i in range(1, future_days + 1)]

    future_df = pd.DataFrame({'Date': future_dates, 'Predicted Close': adjusted_predictions})
    return future_df
