import joblib

# Load scaler (used during training)
AMOUNT_SCALER = joblib.load("models/amount_scaler.pkl")

def prepare_features(df):
    """
    Prepare features EXACTLY as model was trained on:
    Time + V1–V28 + Amount + Amount_scaled
    """
    df = df.copy()

    # Drop target if present
    if "Class" in df.columns:
        df = df.drop(columns=["Class"])

    # Ensure Amount_scaled exists
    if "Amount_scaled" not in df.columns:
        if "Amount" not in df.columns:
            raise ValueError("Input must contain 'Amount' column")
        df["Amount_scaled"] = AMOUNT_SCALER.transform(df[["Amount"]])

    # DO NOT drop Time
    # DO NOT drop Amount
    # DO NOT reorder columns manually

    return df


def compute_anomaly_score(model, X):
    return -model.decision_function(X)


def assign_risk(score, threshold):
    if score >= threshold * 1.5:
        return "High Risk"
    elif score >= threshold:
        return "Medium Risk"
    else:
        return "Low Risk"
