# Bitcoin Price Prediction Application

A comprehensive Streamlit-based application to analyze historical Bitcoin price data and predict future trends using machine learning models.
## Features
1. Data Handling

Loads large-scale historical Bitcoin data from a CSV file (e.g., btcusd_1-min_data.csv).
Efficient preprocessing to handle extensive datasets.

2. Visualization

Interactive visualizations of historical Bitcoin prices.
Future predictions plotted alongside historical data for comparison.

3. Machine Learning Model

Uses a linear regression model to predict Bitcoin prices for the next two years.
Predictions start from the last known price, ensuring a realistic continuation of trends.

4. Streamlit Interface

User-friendly web interface for:
Exploring historical data.
Viewing prediction trends for the next two years.
Interacting with visualizations dynamically.

## Setup
Steps to Set Up the Application
Clone the Repository

git clone https://github.com/your-username/bitcoin-price-prediction.git
cd bitcoin-price-prediction

Create a Virtual Environment
venv\Scripts\activate

Install Dependencies
pip install -r requirements.txt

Run the Application (streamlit run main.py)
