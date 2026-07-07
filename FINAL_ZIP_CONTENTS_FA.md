# محتوای فایل ZIP نهایی

این فایل توضیح می‌دهد که چه مواردی باید داخل فایل ZIP نهایی LMS قرار بگیرد و چه مواردی نباید ارسال شود.

## موارد داخل ZIP

- `data/` شامل نسخه‌های v1، v2 و v3
- `src/` شامل کدهای ماژولار پروژه
- `models/final_model/` شامل مدل نهایی
- `reports/` شامل خروجی‌ها، جداول، نمودارها و logs
- `evidence/` شامل تصاویر GitHub، MLflow، Docker و Pipeline
- `mlflow.db` و `mlruns/` برای باز کردن MLflow UI
- `run_pipeline.py` برای اجرای Pipeline
- `Dockerfile` و فایل‌های Docker
- `README.md` و مستندات کمکی
- گزارش نهایی Word پس از آماده‌سازی

## موارد حذف‌شده از ZIP

- `.git/` چون GitHub Repository و screenshots آن ارائه شده‌اند
- `.ipynb_checkpoints/` و `__pycache__/` چون فایل‌های موقت هستند
- `catboost_info/` چون خروجی موقت CatBoost است
- `models/baseline_v3/`, `models/tuned_v3/`, `models/final_candidate_v3/` چون مدل نهایی در `models/final_model/` موجود است
- فایل Excel خام تکراری در ریشه پروژه؛ نسخه صحیح در `data/v1/` قرار دارد
- `final_project.ipynb` برای کاهش حجم؛ کد اصلی در فایل‌های `.py` و گزارش‌ها موجود است
