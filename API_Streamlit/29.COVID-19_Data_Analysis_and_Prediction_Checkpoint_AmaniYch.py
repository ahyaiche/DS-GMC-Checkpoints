# Import libraries
import streamlit as st
import pandas as pd
import joblib

# Load the trained model from the .h5 file
model = joblib.load('COVID_19_model.h5')

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