import requests
import pandas as pd
import plotly.express as px
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import streamlit as st

# Step 1: Choose the COVID-19 API
api_url = "https://api.covidtracking.com/v1/us/daily.json"

# Step 2: Gather and Store Data
response = requests.get(api_url)
data = response.json()
dt = pd.DataFrame(data)

# Step 3: Data Cleaning
# Remove irrelevant columns
dt = dt[['date', 'positive', 'negative', 'hospitalizedCurrently', 'recovered', 'death']]
# Handle missing values and duplicates (if any)
dt = dt.dropna()
dt = dt.drop_duplicates()

# Step 4: Data Pre-processing (Not required in this example)

# Step 5: Exploratory Data Analysis (EDA)
st.title("COVID-19 Data Analysis")
st.subheader("Raw Data")
st.dataframe(dt)

# Visualize COVID-19 cases over time
fig = px.line(dt, x='date', y=['positive', 'recovered', 'death'], title="COVID-19 Cases Over Time")
st.plotly_chart(fig)

# Step 6: Model Selection and Optimization
# For demonstration purposes, let's predict the future number of positive cases using Linear Regression

# Prepare the data
X = dt[['date']].values
y = dt['positive'].values

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 7: Model Deployment using Streamlit
st.subheader("Predict Future COVID-19 Positive Cases")
st.write("Enter a date in the format 'YYYYMMDD':")
input_date = st.text_input("Input Date", "")

if input_date:
    try:
        input_date = int(input_date)
        prediction = model.predict([[input_date]])
        st.write(f"Predicted number of positive cases on {input_date}: {prediction[0]:.0f}")
    except ValueError:
        st.write("Invalid input date. Please enter a valid date in the format 'YYYYMMDD'.")

# Step 8: Deploy the Streamlit App (Deployed using Streamlit Share or other hosting platforms)
