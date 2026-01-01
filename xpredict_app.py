import pandas as pd
import streamlit as st
import joblib

# Load model safely
try:
    model = joblib.load('xgb_model.jb')
except:
    st.error("Model file not found!")
    st.stop()

st.set_page_config(page_title="House Price Prediction", layout="centered")

st.title(" House Price Prediction")
st.write("Enter the house details below to predict the price")

inputs = [
    'OverallQual', 'GrLivArea', 'GarageArea', '1stFlrSF',
    'FullBath', 'YearBuilt', 'YearRemodAdd', 'MasVnrArea',
    'Fireplaces', 'BsmtFinSF1', 'LotFrontage', 'WoodDeckSF',
    'OpenPorchSF', 'LotArea', 'CentralAir'
]

input_data = {}

col1, col2 = st.columns(2)

for i, feature in enumerate(inputs):
    col = col1 if i % 2 == 0 else col2

    if feature == 'CentralAir':
        input_data[feature] = col.selectbox(
            "Central Air",
            options=['Yes', 'No']
        )
    else:
        input_data[feature] = col.number_input(
            feature,
            min_value=0.0,
            value=50.0 if feature in ['GrLivArea', 'LotArea'] else 1.0,
            step=1.0
        )

if st.button(" Predict Price"):
    # Convert categorical
    input_data['CentralAir'] = 1 if input_data['CentralAir'] == 'Yes' else 0

    # Validation
    if input_data['GrLivArea'] == 0 or input_data['LotArea'] == 0:
        st.warning("Area values must be greater than 0")
    else:
        input_df = pd.DataFrame([input_data], columns=inputs)
        prediction = model.predict(input_df)


        st.success(f"💰 Estimated House Price: **${prediction[0]:,.2f}**")
