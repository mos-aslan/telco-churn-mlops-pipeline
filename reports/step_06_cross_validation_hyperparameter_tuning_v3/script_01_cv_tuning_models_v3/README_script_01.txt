Step 06 - Cross-Validation and Hyperparameter Tuning

This folder contains the clean re-run outputs of hyperparameter tuning using stratified K-fold cross-validation.

Purpose:
Improve model performance and compare tuned models using cross-validation.

Cleaning behavior:
- Previous local Step 6 outputs were deleted before this run.
- Previous active MLflow runs related to Step 6 were deleted before this run.

Dataset:
- C:\Users\NezarHalabia\finallprogect\data\v3\telco_churn_v3_encoded_unscaled.csv

Models tuned:
- Logistic Regression
- Random Forest
- XGBoost
- CatBoost

Evaluation design:
- Stratified K-fold cross-validation on Train_Validation split
- Test set kept untouched until final evaluation
- Best model selected by highest Mean CV F1-score, then highest Mean CV ROC-AUC

Subfolders:
- tables: CV results, tuning summary, test results, confusion matrices, reports, and feature importance tables.
- figures: CV comparison charts, confusion matrix, ROC curve, and feature importance plots.
- logs: JSON and TXT reproducibility logs.

Best tuned model: CatBoost
Best tuned model path: C:\Users\NezarHalabia\finallprogect\models\tuned_v3\best_tuned_model_v3.joblib
MLflow tracking URI: sqlite:///C:/Users/NezarHalabia/finallprogect/mlflow.db