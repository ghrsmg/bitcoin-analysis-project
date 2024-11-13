import matplotlib.pyplot as plt
import streamlit as st

def plot_data(df):
    fig, ax = plt.subplots()
    ax.plot(df.index, df['price'], label="Historical Price")
    ax.set_title("Bitcoin Historical Prices")
    ax.set_xlabel("Date")
    ax.set_ylabel("Price (USD)")
    ax.legend()
    st.pyplot(fig)

def plot_predictions(df):
    fig, ax = plt.subplots()
    ax.plot(df.index, df['price'], label="Historical Price")
    ax.plot(df.index, df['predicted_price'], label="Predicted Price", linestyle="--")
    ax.set_title("Bitcoin Price Prediction")
    ax.set_xlabel("Date")
    ax.set_ylabel("Price (USD)")
    ax.legend()
    st.pyplot(fig)
