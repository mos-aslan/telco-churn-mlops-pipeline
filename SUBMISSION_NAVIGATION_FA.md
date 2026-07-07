# راهنمای سریع بررسی پروژه برای استاد

این فایل برای کمک به بررسی سریع پروژه تهیه شده است و مسیر فایل‌ها و شواهد اصلی را مشخص می‌کند.

## 1. لینک مخزن GitHub

```text
https://github.com/mos-aslan/telco-churn-mlops-pipeline
```

## 2. ساختار اصلی پروژه مطابق فایل تکلیف

```text
data/
├── v1/    داده خام
├── v2/    داده پاکسازی‌شده و Encoding شده
└── v3/    داده نهایی Feature Engineering

src/
├── data_loader.py
├── preprocessing.py
├── features.py
├── train.py
├── evaluate.py
├── mlflow_utils.py
└── inference.py

run_pipeline.py
README.md
```

## 3. مسیرهای مهم

| بخش | مسیر | توضیح |
|---|---|---|
| داده خام | `data/v1/` | نسخه خام دیتاست Telco Customer Churn |
| داده پاکسازی‌شده | `data/v2/` | خروجی پاکسازی و Encoding |
| داده نهایی | `data/v3/` | نسخه نهایی مناسب مدل‌سازی |
| کدهای پروژه | `src/` | کد ماژولار پروژه |
| مدل نهایی | `models/final_model/` | مدل CatBoost نهایی و فایل‌های inference |
| خروجی‌های مرحله‌ای | `reports/` | گزارش‌ها، جداول، نمودارها و logs هر مرحله |
| تصاویر شواهد | `evidence/` | تصاویر GitHub، MLflow، Docker و Pipeline |
| MLflow Database | `mlflow.db` | پایگاه داده ثبت آزمایش‌ها |
| MLflow Artifacts | `mlruns/` | artifacts مربوط به اجرای MLflow |

## 4. تصاویر Evidence

```text
evidence/github_screenshots/
evidence/mlflow_screenshots/
evidence/docker_screenshots/
evidence/pipeline_screenshots/
```

## 5. اجرای Pipeline

برای بررسی آماده بودن پروژه:

```bash
python run_pipeline.py --mode check
```

برای مشاهده مشخصات مدل نهایی:

```bash
python run_pipeline.py --mode describe
```

برای پیش‌بینی نمونه:

```bash
python run_pipeline.py --mode predict-sample
```

## 6. اجرای MLflow

```bash
python -m mlflow ui --backend-store-uri sqlite:///mlflow.db --default-artifact-root ./mlruns --host 127.0.0.1 --port 5000
```

سپس در مرورگر:

```text
http://127.0.0.1:5000
```

## 7. اجرای Docker

ساخت image:

```bash
docker build -t telco-churn-mlops:v3-light .
```

اجرای بررسی داخل Docker:

```bash
docker run --rm telco-churn-mlops:v3-light python run_pipeline.py --mode check
```

اجرای پیش‌بینی نمونه داخل Docker:

```bash
docker run --rm telco-churn-mlops:v3-light python run_pipeline.py --mode predict-sample
```

## 8. مدل نهایی

- مدل نهایی: CatBoost
- نسخه دیتاست: v3_encoded_unscaled
- Decision Threshold: 0.5
- Accuracy: 0.757984
- Precision: 0.528998
- Recall: 0.804813
- F1-score: 0.638388
- ROC-AUC: 0.857661

## 9. نکته درباره پوشه mlruns

پوشه `mlruns/` شامل Run IDهای خودکار MLflow است. نام‌های طولانی داخل این پوشه نباید تغییر داده شوند، زیرا MLflow از این شناسه‌ها برای اتصال runs، metrics و artifacts استفاده می‌کند. برای مشاهده ساختار قابل فهم MLflow از فایل `MLFLOW_RUNS_INDEX_FA.md` و تصاویر موجود در `evidence/mlflow_screenshots/` استفاده شود.
