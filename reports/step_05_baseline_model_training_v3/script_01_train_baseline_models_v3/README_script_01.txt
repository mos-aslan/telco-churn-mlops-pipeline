Step 05 - Baseline Model Training on v3 Dataset

This folder contains the outputs of baseline model training.

Purpose:
Train and compare baseline classification models using the final feature-engineered v3 dataset.

Dataset:
- C:\Users\NezarHalabia\finallprogect\data\v3\telco_churn_v3.csv

Models trained:
- Logistic Regression
- Random Forest
- XGBoost
- CatBoost

Evaluation design:
- Train / Validation / Test split
- Validation set used for model selection
- Test set used only for final evaluation of the selected best model

Selection rule:
Highest validation F1-score, then highest validation ROC-AUC.

MLflow:
- Tracking URI: sqlite:///C:/Users/NezarHalabia/finallprogect/mlflow.db
- Artifact location: file:///C:/Users/NezarHalabia/finallprogect/mlruns

Subfolders:
- tables: metrics, confusion matrices, classification reports, feature importances, and split summaries.
- figures: confusion matrix, ROC curve, and feature-importance plots.
- logs: reproducibility logs and selected-model details.

Best baseline model: CatBoost
Best model path: C:\Users\NezarHalabia\finallprogect\models\baseline_v3\best_baseline_model_v3.joblib