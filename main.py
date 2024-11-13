import streamlit as st
from src.data_loader import load_data
from src.data_preprocessing import preprocess_data
from src.model import train_model, predict
from src.visualization import plot_data, plot_predictions

st.title("Bitcoin Price Prediction App")

# Load and display the data
data = load_data(from_api=True)
st.subheader("Bitcoin Price Data")
st.write(data.head())

# Preprocess and visualize the data
processed_data = preprocess_data(data)
st.subheader("Historical Price Chart")
plot_data(processed_data)

# Train model and make predictions
model = train_model(processed_data)
predicted_data = predict(model, processed_data)

# Display predictions
st.subheader("Predicted vs. Historical Prices")
plot_predictions(predicted_data)
