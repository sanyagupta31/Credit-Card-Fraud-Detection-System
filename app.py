import streamlit as st
import joblib
import numpy as np

# 1. Page Configuration
st.set_page_config(page_title="Fraud Guard AI", page_icon="🛡️")

# 2. Model Loading
@st.cache_resource # Isse model baar-baar load nahi hoga
def load_model():
    model = joblib.load("model.pkl")
    scaler = joblib.load("scaler.pkl")
    return model, scaler

model, scaler = load_model()

# 3. UI Design
st.title("🛡️ Credit Card Fraud Detector")
st.markdown("Enter transaction details to check if it's safe or fraudulent.")

# Layout: 2 Columns
col1, col2 = st.columns(2)

with col1:
    amount = st.number_input("Transaction Amount ($)", min_value=0.0, value=10.0)
    v1 = st.number_input("Feature V1", value=0.0)
with col2:
    v2 = st.number_input("Feature V2", value=0.0)

# 4. Prediction Logic
if st.button("Check Transaction"):
    # Preprocessing (Wahi logic jo FastAPI mein tha)
    scaled_amount = scaler.transform([[amount]])[0][0]
    input_data = [v1, v2] + [0.0] * 26 + [scaled_amount]
    
    prediction = model.predict([input_data])[0]
    
    if prediction == 1:
        st.error("⚠️ ALERT: This transaction looks FRAUDULENT!")
    else:
        st.success("✅ SAFE: This transaction appears legitimate.")
# Sidebar for Monitoring
st.sidebar.header("📊 Model Monitoring")
st.sidebar.write(f"Model Version: v1.0")
st.sidebar.write(f"Framework: Scikit-Learn")

# Mock Metrics (Inhe hum baad mein MLflow se connect kar sakte hain)
st.sidebar.metric(label="Model Accuracy", value="99.94%")
st.sidebar.metric(label="Latency", value="12ms")