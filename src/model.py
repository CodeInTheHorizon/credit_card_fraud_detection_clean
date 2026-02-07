import joblib

def load_model(model_path="models/isolation_forest.pkl"):
    """
    Load trained Isolation Forest model
    """
    return joblib.load(model_path)
