# پروژه پیاده‌سازی Pipeline استاندارد MLOps برای پیش‌بینی ریزش مشتری

## 1. معرفی پروژه

این پروژه برای درس یادگیری ماشین و با هدف طراحی و پیاده‌سازی یک Pipeline استاندارد MLOps برای پیش‌بینی ریزش مشتریان انجام شده است. دیتاست مورد استفاده، دیتاست Telco Customer Churn مربوط به IBM است که شامل اطلاعات حدود 7000 مشتری یک شرکت مخابراتی می‌باشد.

هدف مدل، پیش‌بینی مقدار `Churn Value` است:

- `Churn Value = 1`: مشتری ریزش کرده است.
- `Churn Value = 0`: مشتری باقی مانده است.

در این پروژه علاوه بر آموزش مدل، نسخه‌بندی داده، ثبت آزمایش‌ها در MLflow، ایجاد Pipeline قابل تکرار، بسته‌بندی مدل نهایی و اجرای آن با Docker نیز انجام شده است.

## 2. ساختار پروژه

ساختار اصلی پروژه مطابق انتظار پروژه به صورت زیر است:

```text
project/
├── data/
│   ├── v1/
│   ├── v2/
│   └── v3/
├── src/
│   ├── data_loader.py
│   ├── preprocessing.py
│   ├── features.py
│   ├── train.py
│   ├── evaluate.py
│   └── mlflow_utils.py
├── run_pipeline.py
└── README.md
```

در کنار این ساختار اصلی، فایل‌ها و پوشه‌های تکمیلی MLOps مانند `models/`, `reports/`, `mlflow.db`, `mlruns/`, `Dockerfile` و `evidence/` نیز برای بازتولیدپذیری، گزارش‌دهی و استقرار اضافه شده‌اند.

## 3. نسخه‌بندی داده‌ها

داده‌ها در سه نسخه مدیریت شده‌اند:

### v1: داده خام

در این نسخه، فایل خام دیتاست بدون تغییر در مسیر زیر قرار دارد:

```text
data/v1/
```

### v2: پاکسازی داده و Encoding

در این نسخه، ستون‌های غیرضروری یا دارای ریسک leakage حذف شده‌اند. همچنین داده‌های categorical به مقادیر عددی تبدیل شده‌اند.

ستون‌های حذف‌شده شامل مواردی مانند `CustomerID`, `Count`, `Country`, `State`, `Lat Long`, `Churn Label`, `Churn Score` و `Churn Reason` هستند.

### v3: Feature Engineering

در این نسخه، داده نهایی مناسب مدل‌سازی ایجاد شده است. مدل نهایی پروژه روی نسخه `v3_encoded_unscaled` آموزش و ارزیابی شده است.

## 4. مدل‌های استفاده‌شده

مدل‌های زیر آموزش، ارزیابی و مقایسه شده‌اند:

- Logistic Regression
- Random Forest
- XGBoost
- CatBoost

برای جلوگیری از overfitting و دستیابی به نتایج پایدار، از Train/Validation/Test split، K-Fold Cross Validation و seed ثابت استفاده شده است.

## 5. معیارهای ارزیابی

معیارهای زیر برای مقایسه مدل‌ها ثبت شده‌اند:

- Accuracy
- Precision
- Recall
- F1-score
- ROC-AUC
- Confusion Matrix

## 6. مدل نهایی

- مدل نهایی: `CatBoost`
- وضعیت مدل: `final_champion_model`
- نسخه دیتاست: `v3_encoded_unscaled`
- نوع انتخاب مدل: `Threshold-Optimized Tuned Model`
- آستانه تصمیم‌گیری: `0.5`

نتایج نهایی مدل روی داده Test:

- Accuracy: `0.757984`
- Precision: `0.528998`
- Recall: `0.804813`
- F1-score: `0.638388`
- ROC-AUC: `0.857661`

## 7. نحوه نصب

ابتدا محیط Python یا Anaconda را فعال کرده و وابستگی‌ها را نصب کنید:

```bash
pip install -r requirements.txt
```

برای اجرای نسخه Docker، وابستگی‌های سبک‌تر در فایل زیر مشخص شده‌اند:

```text
requirements_docker.txt
```

## 8. اجرای Pipeline

برای بررسی آماده بودن پروژه:

```bash
python run_pipeline.py --mode check
```

برای مشاهده مشخصات مدل نهایی:

```bash
python run_pipeline.py --mode describe
```

برای اجرای پیش‌بینی نمونه:

```bash
python run_pipeline.py --mode predict-sample
```

برای پیش‌بینی از روی فایل CSV آماده‌شده:

```bash
python run_pipeline.py --mode predict-csv --input models/final_model/sample_input_features.csv --input-type features
```

## 9. اجرای MLflow

در این پروژه تمامی آزمایش‌ها، پارامترها، نتایج و مدل‌ها در MLflow ثبت شده‌اند. برای باز کردن MLflow UI:

```bash
python -m mlflow ui --backend-store-uri sqlite:///mlflow.db --default-artifact-root ./mlruns --host 127.0.0.1 --port 5000
```

سپس در مرورگر باز کنید:

```text
http://127.0.0.1:5000
```

## 10. استقرار با Docker

برای ساخت Docker Image سبک مدل نهایی:

```bash
docker build -t telco-churn-mlops:v3-light .
```

برای اجرای پیش‌بینی نمونه داخل Docker:

```bash
docker run --rm telco-churn-mlops:v3-light python run_pipeline.py --mode predict-sample
```

برای بررسی پروژه داخل Docker:

```bash
docker run --rm telco-churn-mlops:v3-light python run_pipeline.py --mode check
```

## 11. شواهد و خروجی‌ها

خروجی‌های هر مرحله در پوشه `reports/` ذخیره شده‌اند. تصاویر مورد نیاز برای تحویل نهایی در پوشه `evidence/` قرار داده می‌شوند:

- تصاویر MLflow
- تصاویر Docker
- تصاویر GitHub و Commitها
- تصاویر اجرای Pipeline

## 12. جمع‌بندی

این پروژه یک Pipeline کامل و قابل تکرار MLOps برای پیش‌بینی ریزش مشتری ارائه می‌کند. مدل نهایی CatBoost با ثبت کامل آزمایش‌ها در MLflow و اعتبارسنجی اجرای Docker آماده تحویل و بازتولید است.
