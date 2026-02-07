import streamlit as st
import pandas as pd
import joblib

from src.model import load_model
from src.scoring import compute_anomaly_score, assign_risk, prepare_features

# -------------------------------
# Load model & default threshold
# -------------------------------
@st.cache_resource
def get_model():
    return load_model("models/isolation_forest.pkl")

@st.cache_data
def get_threshold():
    return joblib.load("models/fraud_threshold.pkl")

model = get_model()
default_threshold = get_threshold()


# -------------------------------
# Sidebar controls
# -------------------------------
st.sidebar.header("Risk Threshold Settings")

threshold = st.sidebar.slider(
    "Fraud Risk Threshold",
    min_value=0.0,
    max_value=1.0,
    value=float(default_threshold),
    step=0.01
)

st.sidebar.info(
    "High Risk transactions should be manually reviewed by a human analyst."
)


st.title("💳 Credit Card Fraud Detection System")
st.write(
    "An unsupervised fraud detection system using **Isolation Forest**, "
    "designed for highly imbalanced financial transaction data."
)

# -------------------------------
# Load model & threshold
# -------------------------------
@st.cache_resource
def get_model():
    return load_model("models/isolation_forest.pkl")

@st.cache_data
def get_threshold():
    return joblib.load("models/fraud_threshold.pkl")

model = get_model()
threshold = get_threshold()

# -------------------------------
# Upload CSV
# -------------------------------
uploaded_file = st.file_uploader(
    "Upload transaction CSV file",
    type=["csv"]
)

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("Uploaded Data Preview")
    st.dataframe(df.head())

    if st.button("Run Fraud Detection"):
        X = prepare_features(df)
        scores = compute_anomaly_score(model, X)

        df["Fraud_Score"] = scores
        df["Risk_Level"] = df["Fraud_Score"].apply(
            lambda x: assign_risk(x, threshold)
        )

        st.subheader("Detection Results")
        st.dataframe(df.head(20))

        st.subheader("Risk Distribution")
        st.bar_chart(df["Risk_Level"].value_counts())

        st.success("Fraud detection completed successfully.")
