import streamlit as st
import numpy as np
import pickle

model = pickle.load(open('model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

st.set_page_config(page_title="House Price Predictor", layout="centered")

st.title("House Price Prediction")
st.write("Enter house details below to predict the price:")

bedrooms = st.number_input("Number of Bedrooms", min_value=0, max_value=10, step=1)
bathrooms = st.number_input("Number of Bathrooms", min_value=0, max_value=10, step=1)
sqft_living = st.number_input("Living Area (sqft)", 300, 10000, step = 50)
floors = st.number_input("Number of Floors", min_value=0, max_value=5, step=1)
yr_built = st.number_input("Year Built", min_value=1800, max_value=2025, step=1)
grade = st.selectbox("House Grade (1-13)", list(range(1, 14)))
condition = st.selectbox("House Condition (1-5)", list(range(1, 6)))

if st.button("Predict Price"):
    input_data = np.array([[bedrooms, bathrooms, sqft_living, floors, yr_built, grade,
                            condition]])
    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)[0]
    
    st.success(f"Estimated House Price: ${int(prediction):,}")