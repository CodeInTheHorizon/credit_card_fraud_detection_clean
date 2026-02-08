# Real-Time Anomaly Detection in Credit Card Transactions

## 📌 Problem Statement

Credit card fraud detection is a critical challenge due to **extreme class imbalance**.
Fraudulent transactions represent less than **0.2%** of total transactions, making
traditional supervised classification approaches unreliable and misleading when
evaluated using accuracy.

This project focuses on detecting anomalous credit card transactions using
**unsupervised machine learning techniques**, where the model learns normal behavior
and flags deviations as potential fraud.

---

## 📊 Dataset Overview

- Public credit card transaction dataset
- Features `V1`–`V28` are **PCA-transformed** to preserve customer privacy
- `Amount` feature represents transaction value and contains extreme outliers
- Target column `Class`:
  - `0` → Normal transaction
  - `1` → Fraudulent transaction
- Fraud cases account for **< 0.2%** of the dataset

---

## 🧠 Why Unsupervised Learning?

In real-world fraud detection systems:

- Fraud labels are **rare, delayed, or incomplete**
- Fraud patterns evolve continuously
- Models must operate in **near real-time**

Unsupervised models are well-suited because they:

- Learn patterns of **normal transactions**
- Flag statistically rare and unusual behavior
- Do not rely on labeled fraud data during detection

---

## 🗂️ Project Structure

# Real-Time Anomaly Detection in Credit Card Transactions

## 📌 Problem Statement

Credit card fraud detection is a critical challenge due to **extreme class imbalance**.
Fraudulent transactions represent less than **0.2%** of total transactions, making
traditional supervised classification approaches unreliable and misleading when
evaluated using accuracy.

This project focuses on detecting anomalous credit card transactions using
**unsupervised machine learning techniques**, where the model learns normal behavior
and flags deviations as potential fraud.

---

## 📊 Dataset Overview

- Public credit card transaction dataset
- Features `V1`–`V28` are **PCA-transformed** to preserve customer privacy
- `Amount` feature represents transaction value and contains extreme outliers
- Target column `Class`:
  - `0` → Normal transaction
  - `1` → Fraudulent transaction
- Fraud cases account for **< 0.2%** of the dataset

---

## 🧠 Why Unsupervised Learning?

In real-world fraud detection systems:

- Fraud labels are **rare, delayed, or incomplete**
- Fraud patterns evolve continuously
- Models must operate in **near real-time**

Unsupervised models are well-suited because they:

- Learn patterns of **normal transactions**
- Flag statistically rare and unusual behavior
- Do not rely on labeled fraud data during detection

---

## 🗂️ Project Structure

credit_card_fraud_detection/
│
├── notebooks/ # EDA, experiments, model evaluation
├── src/ # Production-ready ML logic
│ ├── model.py # Model loading utilities
│ └── scoring.py # Feature prep, scoring, risk assignment
├── models/ # Saved models & preprocessing artifacts
├── ui/ # Streamlit dashboard
├── data/ # Sample / raw datasets
├── requirements.txt
└── README.md

---

## 🚀 Phase-wise Implementation

### 🔹 Phase 1: Exploratory Data Analysis & Scaling

- Class imbalance analysis
- Distribution analysis of transaction `Amount`
- Identified heavy-tailed outliers
- Applied **RobustScaler** to stabilize feature scaling
- PCA feature inspection for variance behavior

---

### 🔹 Phase 2: Unsupervised Model Building

#### Week 2: Isolation Forest

- Trained primarily on **normal transactions**
- Hyperparameters explored:
  - `n_estimators`
  - `contamination`
- Evaluation focused on:
  - Precision
  - Recall
  - Confusion matrices (not accuracy)

**Key Result:**  
Isolation Forest achieved the best balance between fraud recall and false positives
while scaling efficiently to large datasets.

---

#### Week 3: Local Outlier Factor (LOF)

- Density-based anomaly detection algorithm
- Applied to a **subset of data** due to computational complexity

**Key Observations:**

- High accuracy on normal transactions
- Fraud recall consistently **below 5%**
- Poor scalability for large, high-dimensional datasets

**Conclusion:**  
LOF is unsuitable for real-time fraud detection at scale.

---

## 📈 Phase 3: Threshold Tuning & Evaluation

- Accuracy intentionally avoided
- Evaluation based on:
  - Precision
  - Recall
  - F1-score
- Precision–Recall curves used to select operating point

### ✅ Threshold Recommendation

The final fraud score threshold was selected by **maximizing the F1-score**,
achieving a balanced trade-off between:

- Capturing fraudulent transactions
- Maintaining a manageable false positive rate

This threshold is recommended for deployment.

---

## 🏆 Final Model Selection

| Model            | Scalability | Fraud Recall | Deployment Suitability |
| ---------------- | ----------- | ------------ | ---------------------- |
| Isolation Forest | High        | Strong       | ✅ Recommended         |
| LOF              | Low         | Very Weak    | ❌ Not Suitable        |

Isolation Forest was selected as the final model.

---

## 🖥️ Streamlit Dashboard

An interactive Streamlit application was built to demonstrate real-time inference.

### Features:

- Upload raw transaction CSV files
- Dynamic fraud threshold tuning
- Real-time anomaly scoring
- Risk categorization:
  - Low Risk
  - Medium Risk
  - High Risk
- Interactive tables and visualizations

The UI mirrors the **exact training pipeline** during inference, ensuring
feature consistency and reliable fraud scoring.

---

## 🧠 Key Insights

- Accuracy is misleading for fraud detection
- Recall–precision trade-off is a **business decision**
- Unsupervised models are more realistic for fraud systems
- Isolation Forest outperforms density-based methods
- Threshold tuning is as important as model selection

---

## 🛠️ Tech Stack

- Python
- Pandas, NumPy
- Scikit-learn
- Matplotlib
- Streamlit
- Git & GitHub

---

## ▶️ How to Run

````bash
pip install -r requirements.txt
streamlit run ui/app.py


---

## 🚀 Phase-wise Implementation

### 🔹 Phase 1: Exploratory Data Analysis & Scaling
- Class imbalance analysis
- Distribution analysis of transaction `Amount`
- Identified heavy-tailed outliers
- Applied **RobustScaler** to stabilize feature scaling
- PCA feature inspection for variance behavior

---

### 🔹 Phase 2: Unsupervised Model Building

#### Week 2: Isolation Forest
- Trained primarily on **normal transactions**
- Hyperparameters explored:
  - `n_estimators`
  - `contamination`
- Evaluation focused on:
  - Precision
  - Recall
  - Confusion matrices (not accuracy)

**Key Result:**
Isolation Forest achieved the best balance between fraud recall and false positives
while scaling efficiently to large datasets.

---

#### Week 3: Local Outlier Factor (LOF)

- Density-based anomaly detection algorithm
- Applied to a **subset of data** due to computational complexity

**Key Observations:**
- High accuracy on normal transactions
- Fraud recall consistently **below 5%**
- Poor scalability for large, high-dimensional datasets

**Conclusion:**
LOF is unsuitable for real-time fraud detection at scale.

---

## 📈 Phase 3: Threshold Tuning & Evaluation

- Accuracy intentionally avoided
- Evaluation based on:
  - Precision
  - Recall
  - F1-score
- Precision–Recall curves used to select operating point

### ✅ Threshold Recommendation

The final fraud score threshold was selected by **maximizing the F1-score**,
achieving a balanced trade-off between:
- Capturing fraudulent transactions
- Maintaining a manageable false positive rate

This threshold is recommended for deployment.

---

## 🏆 Final Model Selection

| Model              | Scalability | Fraud Recall | Deployment Suitability |
|-------------------|------------|--------------|------------------------|
| Isolation Forest  | High       | Strong       | ✅ Recommended          |
| LOF               | Low        | Very Weak    | ❌ Not Suitable         |

Isolation Forest was selected as the final model.

---

## 🖥️ Streamlit Dashboard

An interactive Streamlit application was built to demonstrate real-time inference.

### Features:
- Upload raw transaction CSV files
- Dynamic fraud threshold tuning
- Real-time anomaly scoring
- Risk categorization:
  - Low Risk
  - Medium Risk
  - High Risk
- Interactive tables and visualizations

The UI mirrors the **exact training pipeline** during inference, ensuring
feature consistency and reliable fraud scoring.

---

## 🧠 Key Insights

- Accuracy is misleading for fraud detection
- Recall–precision trade-off is a **business decision**
- Unsupervised models are more realistic for fraud systems
- Isolation Forest outperforms density-based methods
- Threshold tuning is as important as model selection

---

## 🛠️ Tech Stack

- Python
- Pandas, NumPy
- Scikit-learn
- Matplotlib
- Streamlit
- Git & GitHub

---

## ▶️ How to Run

```bash
pip install -r requirements.txt
streamlit run ui/app.py


---

## 🚀 Phase-wise Implementation

### 🔹 Phase 1: Exploratory Data Analysis & Scaling
- Class imbalance analysis
- Distribution analysis of transaction `Amount`
- Identified heavy-tailed outliers
- Applied **RobustScaler** to stabilize feature scaling
- PCA feature inspection for variance behavior

---

### 🔹 Phase 2: Unsupervised Model Building

#### Week 2: Isolation Forest
- Trained primarily on **normal transactions**
- Hyperparameters explored:
  - `n_estimators`
  - `contamination`
- Evaluation focused on:
  - Precision
  - Recall
  - Confusion matrices (not accuracy)

**Key Result:**
Isolation Forest achieved the best balance between fraud recall and false positives
while scaling efficiently to large datasets.

---

#### Week 3: Local Outlier Factor (LOF)

- Density-based anomaly detection algorithm
- Applied to a **subset of data** due to computational complexity

**Key Observations:**
- High accuracy on normal transactions
- Fraud recall consistently **below 5%**
- Poor scalability for large, high-dimensional datasets

**Conclusion:**
LOF is unsuitable for real-time fraud detection at scale.

---

## 📈 Phase 3: Threshold Tuning & Evaluation

- Accuracy intentionally avoided
- Evaluation based on:
  - Precision
  - Recall
  - F1-score
- Precision–Recall curves used to select operating point

### ✅ Threshold Recommendation

The final fraud score threshold was selected by **maximizing the F1-score**,
achieving a balanced trade-off between:
- Capturing fraudulent transactions
- Maintaining a manageable false positive rate

This threshold is recommended for deployment.

---

## 🏆 Final Model Selection

| Model              | Scalability | Fraud Recall | Deployment Suitability |
|-------------------|------------|--------------|------------------------|
| Isolation Forest  | High       | Strong       | ✅ Recommended          |
| LOF               | Low        | Very Weak    | ❌ Not Suitable         |

Isolation Forest was selected as the final model.

---

## 🖥️ Streamlit Dashboard

An interactive Streamlit application was built to demonstrate real-time inference.

### Features:
- Upload raw transaction CSV files
- Dynamic fraud threshold tuning
- Real-time anomaly scoring
- Risk categorization:
  - Low Risk
  - Medium Risk
  - High Risk
- Interactive tables and visualizations

The UI mirrors the **exact training pipeline** during inference, ensuring
feature consistency and reliable fraud scoring.

---

## 🧠 Key Insights

- Accuracy is misleading for fraud detection
- Recall–precision trade-off is a **business decision**
- Unsupervised models are more realistic for fraud systems
- Isolation Forest outperforms density-based methods
- Threshold tuning is as important as model selection

---

## 🛠️ Tech Stack

- Python
- Pandas, NumPy
- Scikit-learn
- Matplotlib
- Streamlit
- Git & GitHub

---

## ▶️ How to Run

```bash
pip install -r requirements.txt
streamlit run ui/app.py

````
