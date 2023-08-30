#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import pandas as pd
import pickle
from fbprophet import Prophet

# Load or prepare the DataFrame 'df'
df = pd.read_csv('Forex Fundumental News For USD.csv')

# List of columns to analyze
columns_to_analyze = [
    'ISM Manufacturing PMI', 'ISM Services PMI', 'Housing Starts',
    'Non-Farm Employment Change', 'Unemployment  Rate',
    'Consumer Price Index (CPI)', 'Producer Price Index (PPI)',
    'Retail Sales'
]

# Function to load the Prophet models
def load_prophet_models():
    prophet_models = {}
    for column in columns_to_analyze:
        with open(f"{column}_prophet_model.pkl", "rb") as model_file:
            model = pickle.load(model_file)
            prophet_models[column] = model
    return prophet_models

# Streamlit app header
st.title("Forex News Sentiment Prediction")

# Load the Prophet models
prophet_models = load_prophet_models()

# Input form for each column and future date
for column in columns_to_analyze:
    st.header(f"Predict sentiment for {column}")
    future_date = st.date_input(f"Select a future date for {column}")
    
    if st.button("Predict"):
        # Create a DataFrame with the future date
        future_df = pd.DataFrame({'ds': [future_date]})
        
        # Load the corresponding Prophet model for the column
        model = prophet_models[column]
        
        # Use the model to make predictions
        forecast = model.predict(future_df)
        predicted_sentiment = 'Positive' if forecast['yhat'].iloc[0] > 0 else 'Negative'
        
        # Display the prediction
        st.subheader("Prediction:")
        st.write(f"Predicted sentiment for {column} on {future_date}: {predicted_sentiment}")

