import matplotlib.pyplot as plt
import streamlit as st

def plot_historical_prices(data):
    """
    Plot historical Bitcoin prices.
    """
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(data.index, data['Close'], label='Close Price', color='blue')
    ax.set_title("Bitcoin Close Prices Over Time")
    ax.set_xlabel("Time")
    ax.set_ylabel("Close Price (USD)")
    ax.legend()
    st.pyplot(fig)

def plot_predictions(historical_data, predictions):
    """
    Plot historical and predicted Bitcoin prices.
    """
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(historical_data.index, historical_data['Close'], label="Historical Prices", color="blue")
    ax.plot(predictions['Date'], predictions['Predicted Close'], label="Predicted Prices", color="orange", linestyle="--")

    ax.set_title("Bitcoin Price Prediction")
    ax.set_xlabel("Date")
    ax.set_ylabel("Price (USD)")
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)
