Step 11 - Lightweight Docker Packaging and Validation

This folder contains Docker packaging and validation outputs for the lightweight inference container.

Purpose:
Validate that the final model can run inside Docker without unnecessary training dependencies.

Generated root-level files:
- C:\Users\NezarHalabia\finallprogect\Dockerfile
- C:\Users\NezarHalabia\finallprogect\.dockerignore
- C:\Users\NezarHalabia\finallprogect\requirements_docker.txt
- C:\Users\NezarHalabia\finallprogect\DOCKER_USAGE.md

Docker image tag:
- telco-churn-mlops:v3-light

Validation outputs:
- docker_light_readiness_check.csv
- docker_light_command_results.csv
- docker_light_validation_summary.json

Notes:
- This Docker image is for inference and reproducibility validation.
- It does not retrain the model.
- It does not require MLflow inside the container.