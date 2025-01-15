import streamlit as st
from src.data_loader import load_data
from src.model import predict_prices
from src.vizualization import plot_historical_prices, plot_predictions

# Streamlit App
st.title("Bitcoin Data Analysis and Predictions")

# Load Data
data_path = "C:/Users/ASUS/Desktop/projects/bitcoin-analysis-project/data/data_by_day.csv"
data = load_data(data_path)

# Preprocess Data
daily_data = data

# Display Data
st.subheader("Bitcoin Data Till Today")
st.write(daily_data)

# Plot Historical Data
st.subheader("Historical Bitcoin Prices")
plot_historical_prices(daily_data)

# Predictions
st.subheader("Price Predictions for the next years")
predictions = predict_prices(daily_data, future_days=1095 + 3650)
st.write(predictions)

# Plot Predictions
plot_predictions(daily_data, predictions)
