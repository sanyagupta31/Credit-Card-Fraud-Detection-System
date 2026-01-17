import joblib
import pandas as pd
from fastapi import FastAPI
import sqlalchemy

app = FastAPI()

# Model load karna
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")

DATABASE_URL = "mysql+pymysql://root:password@db/ml_db"

@app.post("/predict")
def predict(amount: float, v1: float, v2: float):
    try:
        # 1. Scaler use karke amount ko transform karo
        scaled_amount = scaler.transform([[amount]])[0][0]
        
        # 2. Model ko 30 features chahiye hote hain (V1-V28 + Scaled_Amount + dummy)
        # Hum v1, v2 asli bhej rahe hain aur baaki 27 features ko 0.0 maan rahe hain
        input_data = [v1, v2] + [0.0] * 26 + [scaled_amount]
        
        # 3. Prediction
        prediction = model.predict([input_data])[0]
        result = "Fraud" if prediction == 1 else "Safe"
        
        # 4. SQL mein save karo
        engine = sqlalchemy.create_engine(DATABASE_URL)
        with engine.connect() as conn:
            conn.execute(
                sqlalchemy.text("INSERT INTO predictions (amount, result) VALUES (:amount, :result)"),
                {"amount": amount, "result": result}
            )
            conn.commit()
            
        return {"prediction": result, "db_status": "Saved successfully"}
    
    except Exception as e:
        return {"error": str(e), "suggestion": "Check if model expects 30 features"}