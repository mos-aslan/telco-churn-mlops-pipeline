# Final Pipeline Usage - Telco Customer Churn MLOps Project

## Purpose

This file explains how to run the final reproducible pipeline after the final model has been trained, tuned, selected, and packaged.

The final pipeline does not retrain the model. It validates the project structure and performs inference using the packaged final model.

## Final Model

The final model is stored in:

```text
models/final_model/final_model.joblib
```

The decision threshold is stored in:

```text
models/final_model/decision_threshold.json
```

The required feature order is stored in:

```text
models/final_model/feature_names.json
```

## Commands

Run the following commands from the project root:

```bash
python run_pipeline.py --mode check
```

```bash
python run_pipeline.py --mode describe
```

```bash
python run_pipeline.py --mode predict-sample
```

For prediction from a feature-engineered CSV file:

```bash
python run_pipeline.py --mode predict-csv --input models/final_model/sample_input_features.csv --input-type features
```

For prediction from readable or raw Telco customer data:

```bash
python run_pipeline.py --mode predict-csv --input path/to/raw_customers.csv --input-type raw
```

## Outputs

Pipeline outputs are saved in:

```text
reports/final_pipeline_runs/
```

Step 10 validation outputs are saved in:

```text
reports/step_10_final_pipeline_validation_v3/script_01_build_and_validate_run_pipeline_v3/
```
