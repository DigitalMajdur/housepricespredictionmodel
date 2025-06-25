# House Price Prediction (Streamlit)

## Description
This is a minimal and clean Streamlit web app to predict house prices using a trained regression model.

## Features
- Streamlit-based simple UI
- Inputs for bedrooms, bathrooms, floors, and year built
- Uses Linear Regression model (`model.pkl`)
- Displays predicted house price in INR

## How to Run
1. Make sure `model.pkl` is in the same folder.
2. Install dependencies: `pip install streamlit scikit-learn pandas numpy`
3. Run the app: `streamlit run app.py`