# House Price Prediction

## Project Overview
This project predicts house prices using an **XGBoost Regressor**.  
It uses features like area, bedrooms, bathrooms, year built, garage info, and more to predict `SalePrice`.

## Dataset
- File: `data_set.csv`  
- Contains house features such as `LotArea`, `OverallQual`, `GrLivArea`, `GarageArea`, etc.  
- Source: Kaggle House Prices Dataset

## Files in this Repository
`data_set.csv` → House data  
`train.ipynb` → Notebook for training the model  
`xgb_model.jb` → Trained XGBoost model  
`app_xgb.py` → Application to predict house prices  
`README.md` → Project description

## Model Performance
- **Mean Absolute Error (MAE):** 18272.86  
- **R² Score:** 0.8995  

## Workflow
Loading Data → Data Pre-processing → Model Training → Model Testing & Evaluation → Deploying Model & Prediction
