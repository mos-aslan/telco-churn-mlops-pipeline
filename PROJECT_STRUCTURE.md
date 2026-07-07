# ساختار پروژه

این فایل ساختار نهایی پروژه را برای بررسی سریع نشان می‌دهد.

```text
finallprogect/
├── data/
│   ├── v1/                         نسخه خام دیتاست
│   ├── v2/                         نسخه پاکسازی‌شده و Encoding شده
│   └── v3/                         نسخه نهایی Feature Engineering
│
├── src/
│   ├── __init__.py
│   ├── config.py                   تنظیمات مرکزی پروژه
│   ├── data_loader.py              بارگذاری داده
│   ├── preprocessing.py            پیش‌پردازش داده
│   ├── features.py                 Feature Engineering
│   ├── train.py                    آموزش مدل
│   ├── evaluate.py                 ارزیابی مدل
│   ├── inference.py                ماژول پیش‌بینی نهایی
│   └── mlflow_utils.py             ابزارهای MLflow
│
├── models/
│   └── final_model/                مدل نهایی و فایل‌های وابسته
│
├── reports/                        خروجی مرحله‌به‌مرحله پروژه
│   ├── step_02_initial_eda/
│   ├── step_03_data_cleaning_v2/
│   ├── step_04_feature_engineering_v3/
│   ├── step_05_baseline_model_training_v3/
│   ├── step_06_cross_validation_hyperparameter_tuning_v3/
│   ├── step_07_threshold_optimization_v3/
│   ├── step_08_final_champion_selection_packaging_v3/
│   ├── step_09_final_inference_module_v3/
│   ├── step_10_pipeline_validation_v3/
│   ├── step_11_docker_packaging_validation_v3_light/
│   ├── step_12_mlflow_documentation_reproducibility_v3/
│   └── final_documentation/
│
├── evidence/
│   ├── mlflow_screenshots/
│   ├── docker_screenshots/
│   ├── github_screenshots/
│   ├── pipeline_screenshots/
│   └── lms_submission_screenshots/
│
├── mlruns/                         Artifacts مربوط به MLflow
├── mlflow.db                       پایگاه داده MLflow
├── run_pipeline.py                 فایل اصلی اجرای Pipeline
├── Dockerfile                      Docker Image سبک برای inference
├── .dockerignore
├── requirements.txt
├── requirements_docker.txt
├── README.md
├── PIPELINE_USAGE.md
├── DOCKER_USAGE.md
├── MLFLOW_USAGE.md
└── EXPERIMENT_REPRODUCIBILITY_SUMMARY.md
```
