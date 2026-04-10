# Car Insurance Fraud Detection System

## Project Overview
This project is a machine learning system designed to detect fraudulent car insurance claims using an XGBoost model.  
It includes a trained model, a FastAPI backend for serving predictions, and a Streamlit frontend for user interaction.

---

## Features
- Predict whether an insurance claim is Fraud or Not Fraud
- REST API using FastAPI
- Interactive web interface using Streamlit
- Handles multiple input features (policy, insured, incident, and date information)
- Uses a trained XGBoost classification model

---

## Machine Learning Model
- Algorithm: XGBoost Classifier
- Preprocessing: Scaling and Encoding
- Saved files:
  - xgb_model.pkl (trained model)
  - scaler.pkl (feature scaling)
  - columns.pkl (feature columns used during training)

---

## Tech Stack
- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- FastAPI
- Streamlit
- Requests

---

## How to Run

### 1. Install dependencies
pip install -r requirements.txt

---

### 2. Run FastAPI backend
uvicorn main:app --reload

---

### 3. Run Streamlit frontend
streamlit run app.py

---

## Output
The system returns:
- 0: Not Fraud
- 1: Fraud

---

## Project Objective
The goal of this project is to detect fraudulent insurance claims using machine learning in order to help reduce financial losses for insurance companies.

---

## Author
Hager Zakaria  
Computer Science Student  
Interested in Artificial Intelligence and Software Engineering
