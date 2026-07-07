# Experiment Reproducibility Summary

## Project

Telco Customer Churn MLOps Project

## Objective

The objective is to build, evaluate, package, and validate a machine learning model for customer churn prediction using a reproducible MLOps workflow.

## Data Versions

- v1: raw Telco customer churn dataset.
- v2: cleaned readable and encoded dataset after removing leakage and non-informative columns.
- v3: final feature-engineered model-ready dataset.

## Final Model

- Model: CatBoost
- Model status: final_champion_model
- Dataset version: v3_encoded_unscaled
- Final candidate type: Threshold-Optimized Tuned Model
- Decision threshold: 0.5

## Final Test Metrics

- Accuracy: 0.7579843860894251
- Precision: 0.5289982425307557
- Recall: 0.8048128342245989
- F1-score: 0.6383881230116649
- ROC-AUC: 0.8576610090676586

## Reproducibility Components

- MLflow SQLite tracking database.
- MLflow artifacts directory.
- Final model package under models/final_model.
- run_pipeline.py for command-line reproducibility.
- Dockerfile and lightweight Docker image for isolated inference validation.
- Structured reports for each step under the reports directory.

## Docker Validation

The final Docker image validates that the model can run outside Jupyter in an isolated runtime environment.

## Key Commands

```bash
python run_pipeline.py --mode check
python run_pipeline.py --mode describe
python run_pipeline.py --mode predict-sample
docker run --rm telco-churn-mlops:v3-light python run_pipeline.py --mode predict-sample
```

## Generated Step 12 Outputs

- C:\Users\NezarHalabia\finallprogect\reports\step_12_mlflow_documentation_reproducibility_v3\script_01_document_mlflow_and_reproducibility_v3\tables\mlflow_experiment_summary.csv
- C:\Users\NezarHalabia\finallprogect\reports\step_12_mlflow_documentation_reproducibility_v3\script_01_document_mlflow_and_reproducibility_v3\tables\mlflow_runs_summary.csv
- C:\Users\NezarHalabia\finallprogect\reports\step_12_mlflow_documentation_reproducibility_v3\script_01_document_mlflow_and_reproducibility_v3\tables\mlflow_metrics_wide.csv
- C:\Users\NezarHalabia\finallprogect\reports\step_12_mlflow_documentation_reproducibility_v3\script_01_document_mlflow_and_reproducibility_v3\tables\mlflow_artifact_inventory.csv
- C:\Users\NezarHalabia\finallprogect\reports\step_12_mlflow_documentation_reproducibility_v3\script_01_document_mlflow_and_reproducibility_v3\tables\project_reproducibility_manifest.csv
