# فهرست قابل فهم آزمایش‌های MLflow

این فایل برای توضیح ساختار پوشه `mlruns/` ایجاد شده است.

## چرا پوشه‌های داخل mlruns نام‌های طولانی دارند؟

MLflow برای هر run یک شناسه یکتا تولید می‌کند. این شناسه‌ها به صورت پوشه‌هایی با نام‌های طولانی در `mlruns/` ذخیره می‌شوند. این نام‌ها نباید تغییر داده شوند، چون ارتباط بین `mlflow.db`، metrics، parameters، models و artifacts از طریق همین شناسه‌ها برقرار می‌شود.

## مسیرهای اصلی MLflow

- پایگاه داده MLflow: `mlflow.db`
- artifacts: `mlruns/`
- راهنمای استفاده: `MLFLOW_USAGE.md`
- تصاویر خروجی: `evidence/mlflow_screenshots/`

## Runs مهم پروژه

| Run Name | Project Step | Status | Metrics | Params |
|---|---|---:|---:|---:|
| `baseline_v3_LogisticRegression` | `nan` | FINISHED | 5 | 10 |
| `baseline_v3_RandomForest` | `nan` | FINISHED | 5 | 13 |
| `baseline_v3_XGBoost` | `nan` | FINISHED | 5 | 14 |
| `baseline_v3_CatBoost` | `nan` | FINISHED | 5 | 12 |
| `best_baseline_v3_CatBoost_test_evaluation` | `nan` | FINISHED | 5 | 4 |
| `tuning_v3_LogisticRegression` | `step_06_cross_validation_hyperparameter_tuning_v3` | FINISHED | 7 | 13 |
| `tuning_v3_RandomForest` | `step_06_cross_validation_hyperparameter_tuning_v3` | FINISHED | 7 | 15 |
| `tuning_v3_XGBoost` | `step_06_cross_validation_hyperparameter_tuning_v3` | FAILED | 7 | 17 |
| `tuning_v3_LogisticRegression` | `step_06_cross_validation_hyperparameter_tuning_v3` | FINISHED | 7 | 15 |
| `tuning_v3_RandomForest` | `step_06_cross_validation_hyperparameter_tuning_v3` | FINISHED | 7 | 17 |
| `tuning_v3_XGBoost` | `step_06_cross_validation_hyperparameter_tuning_v3` | FINISHED | 7 | 19 |
| `tuning_v3_CatBoost` | `step_06_cross_validation_hyperparameter_tuning_v3` | FINISHED | 7 | 16 |
| `best_tuned_v3_CatBoost_test_evaluation` | `step_06_cross_validation_hyperparameter_tuning_v3` | FINISHED | 5 | 6 |
| `threshold_optimization_v3_best_tuned_model` | `step_07_threshold_optimization_v3` | FINISHED | 17 | 8 |
| `final_champion_v3_selection_and_packaging` | `step_08_final_champion_selection_packaging_v3` | FINISHED | 5 | 7 |
| `final_inference_module_v3_test` | `step_09_final_inference_module_v3` | FINISHED | 5 | 6 |

منبع جدول: `reports\step_12_mlflow_documentation_reproducibility_v3\script_01_document_mlflow_and_reproducibility_v3\tables\mlflow_runs_summary.csv`

## تصاویر MLflow

تصاویر زیر برای گزارش نهایی ذخیره شده‌اند:

- `evidence/mlflow_screenshots/01_mlflow_experiment_runs_overview.png`
- `evidence/mlflow_screenshots/02_mlflow_metrics_comparison.png`
- `evidence/mlflow_screenshots/03_mlflow_best_tuned_catboost_run.png`
- `evidence/mlflow_screenshots/04_mlflow_final_champion_run.png`
- `evidence/mlflow_screenshots/05_mlflow_artifacts_view.png`
