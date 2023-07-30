# Checkpoint Objective: Build a Streamlit app that predicts the type of iris flower based on user input using a Random Forest Classifier.

# 1. Import the necessary libraries: Streamlit, sklearn.datasets, and sklearn.ensemble.
import streamlit as st
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

# 2. Load the iris dataset using the "datasets.load_iris()" function and assign the data and target variables to "X" and "Y", respectively.
X = load_iris().data
Y = load_iris().target

# 3. Set up a Random Forest Classifier and fit the model using the "RandomForestClassifier()" and "fit()" functions.
# Fit the model
rfc = RandomForestClassifier()
rfc.fit(X, Y)

# 4. Create a Streamlit app using the "streamlit.title()" and "streamlit.header()" functions to add a title and header to the app.
st.title('Iris Flower Predictor')
st.header('Enter input values')

# 5. Add input fields for sepal length, sepal width, petal length, and petal width using the "streamlit.slider()" function. Use the minimum, maximum, and mean values of each feature as the arguments for the function.
def user_input_values():
    sepal_length = st.slider('Sepal length', float(X[:, 0].min()), float(X[:,0].max()), float(X[:,0].mean()))
    sepal_width = st.slider('Sepal width', float(X[:, 0].min()), float(X[:,0].max()), float(X[:,0].mean()))
    petal_length = st.slider('Petal length', float(X[:, 0].min()), float(X[:,0].max()), float(X[:,0].mean()))
    petal_width = st.slider('Petal width', float(X[:, 0].min()), float(X[:,0].max()), float(X[:,0].mean()))
    data = {'Sepal length' : sepal_length,
            'Sepal width' : sepal_width,
            'Petal length' : petal_length,
            'Petal width' : petal_width}
    features = pd.DataFrame(data, index = [0])
    return features

df = user_input_values()

# 6. Define a prediction button using the "streamlit.button()" function that takes in the input values and uses the classifier to predict the type of iris flower.
# Define prediction button
prediction_button = st.button("Predict")

# Get predictions
if prediction_button:
    pred = rfc.predict(df)
    target_names = load_iris().target_names
    predicted_iris_type = target_names[pred[0]]

# 7. Use the "streamlit.write()" function to display the predicted type of iris flower on the app.
if 'predicted_iris_type' in locals():
    st.write(f'Predicted Iris Flower Type: {predicted_iris_type}')

# 8. Deploy your streamlit app with streamlit share
# https://ds-gmc-checkpoints-5xcagklgh9agfvswkz4lz8.streamlit.app/

# Note: Make sure to run the app using the "streamlit run" command in your terminal.