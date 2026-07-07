# راهنمای سریع بررسی پروژه برای استاد

این فایل نقطه شروع بررسی پروژه است و مسیرهای اصلی را مشخص می‌کند.

## 1. لینک GitHub

```text
https://github.com/mos-aslan/telco-churn-mlops-pipeline
```

## 2. ساختار اصلی مورد انتظار

```text
Final_project_submission/
├── data/
│   ├── v1/
│   ├── v2/
│   └── v3/
├── src/
├── models/final_model/
├── reports/
├── evidence/
├── mlruns/
├── docs/
├── mlflow.db
├── Dockerfile
├── requirements.txt
├── requirements_docker.txt
├── run_pipeline.py
├── README.md
├── SUBMISSION_NAVIGATION_FA.md
└── گزارش_نهایی_پروژه.docx
```

## 3. مسیرهای اصلی

| بخش | مسیر | توضیح |
|---|---|---|
| داده‌ها | `data/v1`, `data/v2`, `data/v3` | نسخه خام، پاکسازی‌شده و نهایی |
| کدها | `src/` | فایل‌های ماژولار پروژه |
| اجرای Pipeline | `run_pipeline.py` | اجرای check، describe و predict |
| مدل نهایی | `models/final_model/` | مدل نهایی CatBoost و فایل‌های inference |
| MLflow | `mlflow.db` و `mlruns/` | ثبت آزمایش‌ها، metrics، params و artifacts |
| Docker | `Dockerfile`, `.dockerignore`, `requirements_docker.txt` | استقرار مدل نهایی |
| تصاویر شواهد | `evidence/` | GitHub، MLflow، Docker و Pipeline |
| مستندات کمکی | `docs/` | فایل‌های راهنما و Audit |
| گزارش نهایی | `گزارش_نهایی_پروژه.docx` | گزارش Word نهایی پس از آماده‌سازی |

## 4. اجرای سریع Pipeline

```bash
python run_pipeline.py --mode check
python run_pipeline.py --mode describe
python run_pipeline.py --mode predict-sample
```

## 5. اجرای MLflow

```bash
python -m mlflow ui --backend-store-uri sqlite:///mlflow.db --default-artifact-root ./mlruns --host 127.0.0.1 --port 5000
```

سپس:

```text
http://127.0.0.1:5000
```

## 6. اجرای Docker

```bash
docker build -t telco-churn-mlops:v3-light .
docker run --rm telco-churn-mlops:v3-light python run_pipeline.py --mode check
docker run --rm telco-churn-mlops:v3-light python run_pipeline.py --mode predict-sample
```

## 7. مدل نهایی

- مدل نهایی: CatBoost
- نسخه دیتاست: v3_encoded_unscaled
- Decision Threshold: 0.5
- Accuracy: 0.757984
- Precision: 0.528998
- Recall: 0.804813
- F1-score: 0.638388
- ROC-AUC: 0.857661

## 8. نکته درباره mlruns

پوشه‌های داخل `mlruns/` دارای نام‌های طولانی هستند، چون MLflow برای هر run یک شناسه یکتا ایجاد می‌کند. این نام‌ها نباید تغییر داده شوند. توضیح کامل در فایل زیر آمده است:

```text
docs/MLFLOW_RUNS_INDEX_FA.md
```
