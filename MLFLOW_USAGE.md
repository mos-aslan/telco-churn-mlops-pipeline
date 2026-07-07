# MLflow Usage - Telco Customer Churn MLOps Project

## Purpose

This document explains how MLflow is used in the project for experiment tracking and reproducibility.

## Tracking Backend

The project uses an SQLite-backed MLflow tracking store:

```text
C:\Users\NezarHalabia\finallprogect\mlflow.db
```

The artifact directory is:

```text
C:\Users\NezarHalabia\finallprogect\mlruns
```

## Experiment Name

```text
Telco_Churn_MLOps
```

## Launch MLflow UI

Run the following command from the project root or from Anaconda Prompt:

```bash
python -m mlflow ui --backend-store-uri sqlite:///C:/Users/NezarHalabia/finallprogect/mlflow.db --default-artifact-root file:///C:/Users/NezarHalabia/finallprogect/mlruns --host 127.0.0.1 --port 5000
```

Then open the local MLflow interface at:

```text
http://127.0.0.1:5000
```

## What was tracked

- Baseline model training.
- Cross-validation and hyperparameter tuning.
- Final champion model selection.
- Final inference reproducibility testing.

## Final Model

- Model: CatBoost
- Dataset version: v3_encoded_unscaled
- Decision threshold: 0.5
- F1-score: 0.6383881230116649
- ROC-AUC: 0.8576610090676586

## Notes

The Docker container is designed for inference and reproducibility validation only.
MLflow tracking remains available locally through the SQLite backend and the mlruns artifact directory.
