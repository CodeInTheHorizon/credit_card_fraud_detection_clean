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