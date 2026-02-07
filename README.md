# Real-Time Anomaly Detection in Credit Card Transactions

## Problem Statement

Financial fraud detection is a critical challenge due to the extreme imbalance between legitimate and fraudulent transactions. Fraudulent transactions represent a very small fraction of overall data, making traditional classification approaches unreliable.

This project focuses on detecting anomalous credit card transactions using unsupervised machine learning techniques.

## Dataset

- The dataset consists of anonymized credit card transactions.
- Features `V1` to `V28` are PCA-transformed components to preserve user privacy.
- The `Amount` feature represents transaction value and contains extreme outliers.
- The target variable `Class` indicates fraud (1) or normal transaction (0).
- The dataset is highly imbalanced, with fraud cases accounting for less than 0.2% of total transactions.

## Project Status

- [x] Exploratory Data Analysis (EDA)
- [x] Class imbalance analysis
- [x] Distribution analysis of transaction Amount
- [x] Robust scaling strategy identified
- [ ] Model training
- [ ] Model evaluation
- [ ] Deployment

> Note: Exploratory analysis was initially performed in a Jupyter environment and finalized within the project repository for reproducibility.

### Week 2: Isolation Forest Implementation

The objective of this phase is to detect anomalous transactions using a tree-based unsupervised learning approach.

Isolation Forest was trained primarily on normal transactions to establish a baseline of legitimate behavior.
Multiple configurations of the model were evaluated by varying the number of estimators and the contamination parameter.

Model performance was assessed using confusion matrices and class-wise precision and recall, with special emphasis on recall for the fraud class.
These experiments form the basis for selecting an optimal contamination threshold that balances fraud detection capability with an acceptable false positive rate.

“Multiple contamination thresholds were evaluated to balance recall and false positives.”

“Phase 1 (EDA & Scaling) and Phase 2 – Week 2 (Isolation Forest) have been implemented within the same technical notebook for continuity and reproducibility.”

## Week 3: Local Outlier Factor (LOF)

In this phase, a density-based anomaly detection approach using Local Outlier Factor (LOF)
was implemented and evaluated.

Due to the quadratic computational complexity of LOF, the algorithm was applied on a
representative subset of transactions rather than the full dataset. This reflects
real-world deployment constraints, where LOF is unsuitable for large-scale, real-time
fraud detection systems.

### Key Observations

- LOF demonstrated high accuracy on normal transactions but very low recall on fraudulent cases.
- Even after hyperparameter tuning (`n_neighbors`, `contamination`), the maximum fraud recall
  remained below 5%.
- Execution time analysis showed that LOF does not scale efficiently compared to Isolation Forest.

### Conclusion

Despite tuning, Local Outlier Factor failed to achieve an acceptable balance between precision
and recall for fraud detection. These findings highlight the limitations of density-based
methods for highly imbalanced, high-dimensional financial transaction data.

### Threshold Recommendation

Based on Precision–Recall curve analysis, the final fraud score threshold was
selected by maximizing the F1-score. This operating point provides a balanced
trade-off between fraud detection recall and false positive rates.

We recommend using this threshold for deployment, as it captures a significant
portion of fraudulent transactions while maintaining a manageable level of
false alarms in real-world scenarios.

## Final Recommendation

After evaluating multiple unsupervised anomaly detection techniques, Isolation
Forest was selected as the final model for fraud detection. It demonstrated
strong scalability, faster execution time, and superior fraud recall compared
to Local Outlier Factor.

Local Outlier Factor was found to be computationally expensive and ineffective
at identifying fraudulent transactions in highly imbalanced, high-dimensional
data. Therefore, Isolation Forest is recommended for real-time fraud detection
applications.

PCA-based visualizations were used to qualitatively assess the separation between
normal and anomalous transactions, providing visual validation of the model behavior.


### Streamlit Application
The project includes an interactive Streamlit web application that allows users to:
- Upload raw transaction data (creditcard.csv)
- Adjust fraud risk sensitivity using a threshold slider
- Run real-time fraud detection
- Visualize risk distribution and flagged transactions

The application mirrors the model’s training pipeline during inference, ensuring strict feature consistency and reliable anomaly scoring.
