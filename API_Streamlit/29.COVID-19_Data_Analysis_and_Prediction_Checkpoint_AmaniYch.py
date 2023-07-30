# Import libraries
import streamlit as st
import pandas as pd
import joblib

# Load the trained model from the .h5 file
model = joblib.load(r'D:\DataScience\CheckPoints\DS-GMC-Checkpoints\API_Streamlit\best_model.h5')

# Define a function to make predictions using the loaded model
def predict_death(input_data):
    return model.predict([input_data])[0]

# Create the Streamlit app and user interface
st.title('COVID-19 Death Predictor')
st.write('Enter the input data to predict the number of deaths:')

# Add input fields
def user_input_values():
    # Create input fields for each feature
    input_data = {}
    for feature in ['positive', 'negative', 'hospitalizedCurrently']:
        input_data[feature] = st.number_input(f"Enter {feature}:", step=0.01)
        features = pd.DataFrame(input_data, index = [0])
    return features

df = user_input_values()

# Define prediction button
prediction_button = st.button("Predict")
    
# Add a button to trigger predictions  
if prediction_button:
    # Make predictions
    prediction = predict_death(df)

    st.write(f"Predicted Number of Deaths: {prediction:.2f}")