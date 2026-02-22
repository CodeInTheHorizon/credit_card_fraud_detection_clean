import streamlit as st
import pandas as pd
import joblib
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.model import load_model
from src.scoring import compute_anomaly_score, assign_risk, prepare_features

# -------------------------------------------------
# Page config
# -------------------------------------------------
st.set_page_config(
    page_title="Fraud Detection Dashboard",
    page_icon="💳",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------------------------------------
# Constants (VERY IMPORTANT)
# -------------------------------------------------
MAX_UI_ROWS = 50000   # UI safety limit

# -------------------------------------------------
# Load model & default threshold (cached)
# -------------------------------------------------
@st.cache_resource
def get_model():
    return load_model("models/isolation_forest.pkl")

@st.cache_data
def get_default_threshold():
    return float(joblib.load("models/fraud_threshold.pkl"))

model = get_model()
default_threshold = get_default_threshold()

# -------------------------------------------------
# Sidebar - Control Panel
# -------------------------------------------------
st.sidebar.header("⚙️ Control Panel")

threshold = st.sidebar.slider(
    "Fraud Risk Threshold",
    min_value=0.0,
    max_value=1.5,
    value=default_threshold,
    step=0.01,
    help="Higher threshold = fewer alerts (high precision), "
         "Lower threshold = more fraud capture (high recall)"
)

st.sidebar.markdown("---")

st.sidebar.info(
    "🚨 **High Risk transactions** should be manually reviewed.\n\n"
    "Adjust threshold to control the precision–recall trade-off."
)

# -------------------------------------------------
# Main Title
# -------------------------------------------------
st.markdown(
    """
    <h1 style='text-align:center;'>💳 Credit Card Fraud Detection Dashboard</h1>
    <p style='text-align:center; color: gray;'>
    Unsupervised anomaly detection using Isolation Forest
    </p>
    """,
    unsafe_allow_html=True
)

st.divider()

# -------------------------------------------------
# Upload CSV
# -------------------------------------------------
uploaded_file = st.file_uploader(
    "📤 Upload transaction CSV file",
    type=["csv"]
)

# -------------------------------------------------
# Session state (prevents reruns)
# -------------------------------------------------
if "scored" not in st.session_state:
    st.session_state.scored = False
if "results_df" not in st.session_state:
    st.session_state.results_df = None

# -------------------------------------------------
# Cached model scoring (CRITICAL FIX)
# -------------------------------------------------
@st.cache_data(show_spinner=False)
def run_scoring(df):
    X = prepare_features(df)
    return compute_anomaly_score(model, X)

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # ---- LIMIT DATA FOR UI ----
    if len(df) > MAX_UI_ROWS:
        st.warning(
            f"Dataset has {len(df)} rows. "
            f"Using first {MAX_UI_ROWS} rows for UI performance."
        )
        df = df.head(MAX_UI_ROWS)

    st.subheader("📄 Uploaded Data Preview")
    st.dataframe(df.head(), use_container_width=True)

    if st.button("🚀 Run Fraud Detection"):
        st.session_state.scored = True

        with st.spinner("🔍 Running fraud detection model..."):
            scores = run_scoring(df)

        df["Fraud_Score"] = scores
        df["Risk_Level"] = df["Fraud_Score"].apply(
            lambda x: assign_risk(x, threshold)
        )

        st.session_state.results_df = df

# -------------------------------------------------
# Display Results (ONLY if model already ran)
# -------------------------------------------------
if st.session_state.scored and st.session_state.results_df is not None:
    df = st.session_state.results_df

    # -------------------------------
    # KPI Section
    # -------------------------------
    total_txn = len(df)
    high_risk = (df["Risk_Level"] == "High Risk").sum()
    medium_risk = (df["Risk_Level"] == "Medium Risk").sum()
    low_risk = (df["Risk_Level"] == "Low Risk").sum()

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Total Transactions", total_txn)
    c2.metric("High Risk 🚨", high_risk)
    c3.metric("Medium Risk ⚠️", medium_risk)
    c4.metric("Low Risk ✅", low_risk)

    st.divider()

    # -------------------------------
    # Results Table
    # -------------------------------
    st.subheader("🔍 Detection Results")

    risk_filter = st.selectbox(
        "Filter by Risk Level",
        ["All", "High Risk", "Medium Risk", "Low Risk"]
    )

    if risk_filter != "All":
        view_df = df[df["Risk_Level"] == risk_filter]
    else:
        view_df = df

    view_df = view_df.nlargest(1000, "Fraud_Score")

    st.dataframe(
        view_df.head(50),
        use_container_width=True
    )

    # -------------------------------
    # Visualizations
    # -------------------------------
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📊 Risk Distribution")
        st.bar_chart(df["Risk_Level"].value_counts())

    with col2:
        st.subheader("📈 Fraud Score Distribution")
        st.line_chart(
            df["Fraud_Score"]
            .sort_values()
            .reset_index(drop=True)
        )

    # -------------------------------
    # Explainability Section
    # -------------------------------
    with st.expander("ℹ️ How to Interpret These Results"):
        st.markdown(
            """
            - **Fraud Score**: Higher score = more anomalous transaction.
            - **Low Risk**: Normal transaction behavior.
            - **Medium Risk**: Mild deviation, monitor if needed.
            - **High Risk**: Strong anomaly, manual review recommended.

            ⚠️ Model is **unsupervised** — it learns normal behavior and
            flags deviations without using labels during detection.
            """
        )

    st.success("✅ Fraud detection completed successfully.")
