from fastapi import FastAPI
import pickle
import pandas as pd

app = FastAPI()


model = pickle.load(open('xgb_model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))
columns = pickle.load(open('columns.pkl', 'rb'))

@app.get("/")
def home():
    return {"message": "Fraud Detection API is working"}

@app.post("/predict")
def predict(data: dict):

    df = pd.DataFrame([data])

    # encoding
    df = pd.get_dummies(df)

    # align columns
    df = df.reindex(columns=columns, fill_value=0)

    # scaling
    df = scaler.transform(df)

    prediction = model.predict(df)

    return {"prediction": int(prediction[0])}