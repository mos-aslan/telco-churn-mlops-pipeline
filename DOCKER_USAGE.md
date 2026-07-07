# Docker Usage - Telco Customer Churn MLOps Project

## Purpose

This document explains how to build and run the final lightweight Docker container.

The container is designed for inference and reproducibility validation only.
It does not retrain the model and does not run MLflow tracking.

## Docker Image

```text
telco-churn-mlops:v3-light
```

## Build Image

Run from the project root:

```bash
docker build -t telco-churn-mlops:v3-light .
```

## Run Project Readiness Check

```bash
docker run --rm telco-churn-mlops:v3-light python run_pipeline.py --mode check
```

## Describe Final Model

```bash
docker run --rm telco-churn-mlops:v3-light python run_pipeline.py --mode describe
```

## Run Sample Prediction

```bash
docker run --rm telco-churn-mlops:v3-light python run_pipeline.py --mode predict-sample
```

## Run Feature CSV Prediction

```bash
docker run --rm telco-churn-mlops:v3-light python run_pipeline.py --mode predict-csv --input models/final_model/sample_input_features.csv --input-type features
```

## Notes

- The image uses requirements_docker.txt.
- The final model is loaded from models/final_model/final_model.joblib.
- This Docker setup validates deployment readiness without unnecessary training dependencies.
