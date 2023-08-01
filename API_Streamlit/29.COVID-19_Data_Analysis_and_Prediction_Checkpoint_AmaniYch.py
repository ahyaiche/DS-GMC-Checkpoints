# Import libraries
import requests
import joblib
import streamlit as st
import pandas as pd

# Load the trained model from the .h5 file
# URL of the model file on GitHub
model_url = 'https://github.com/ahyaiche/DS-GMC-Checkpoints/raw/main/API_Streamlit/COVID_19_model.h5'

# Function to download the model file
def download_model(url, save_path):
    response = requests.get(url)
    with open(save_path, 'wb') as f:
        f.write(response.content)

# Local file path to save the downloaded model
local_model_path = 'COVID_19_model.h5'

# Download the model file from the GitHub URL
download_model(model_url, local_model_path)

# Load the trained model from the downloaded file
model = joblib.load(local_model_path)

# Streamlit app header and description
st.title("COVID-19 Death Prediction")
st.write("This app predicts the number of deaths based on COVID-19 data.")

# Function to get user input data
def user_input_data():
    st.subheader("Enter COVID-19 Data:")
    positive = st.number_input("Positive Cases:", value=0, step=1)
    negative = st.number_input("Negative Cases:", value=0, step=1)
    hospitalized = st.number_input("Hospitalized Cases:", value=0, step=1)
    year = st.number_input("Year:", value=2023, step=1)
    month = st.number_input("Month:", value=7, min_value=1, max_value=12, step=1)
    day = st.number_input("Day:", value=30, min_value=1, max_value=31, step=1)

    # Create a DataFrame to hold the user input data
    input_data = pd.DataFrame({
        'positive': [positive],
        'negative': [negative],
        'hospitalized': [hospitalized],
        'year': [year],
        'month': [month],
        'day': [day]
    })

    return input_data

# Get user input data
input_data = user_input_data()

# Create a button for prediction
if st.button('Predict'):
    # Use the trained model to make predictions on the user input data
    predicted_death = model.predict(input_data)[0]
    # Convert the predicted death to an integer
    rounded_death = int(predicted_death)

    # Display the predicted death
    st.subheader("Predicted Number of Deaths:")
    st.write("The predicted number of deaths is:", rounded_death)