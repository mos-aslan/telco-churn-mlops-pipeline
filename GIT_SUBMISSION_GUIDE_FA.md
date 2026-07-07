# راهنمای Git و GitHub برای تحویل پروژه

این پروژه باید در یک Git Repository قرار گیرد و تغییرات با Commitهای منظم ثبت شوند.

## 1. مقداردهی اولیه Git

از مسیر اصلی پروژه اجرا شود:

```bash
git init
git status
```

## 2. تنظیم اطلاعات کاربر

در صورت نیاز:

```bash
git config user.name "Your Name"
git config user.email "your_email@example.com"
```

## 3. Commitهای پیشنهادی

برای حرفه‌ای‌تر شدن تاریخچه پروژه، Commitها می‌توانند به صورت زیر باشند:

```bash
git add data src run_pipeline.py requirements.txt README.md
git commit -m "Initial MLOps project structure and data versioning"

git add reports models mlflow.db mlruns
git commit -m "Add MLflow experiments, model outputs, and reports"

git add Dockerfile .dockerignore requirements_docker.txt DOCKER_USAGE.md
git commit -m "Add Docker deployment package for final model inference"

git add evidence PROJECT_STRUCTURE.md SUBMISSION_CHECKLIST.md MLFLOW_USAGE.md EXPERIMENT_REPRODUCIBILITY_SUMMARY.md GIT_SUBMISSION_GUIDE_FA.md
git commit -m "Add final documentation and submission evidence structure"
```

## 4. اتصال به GitHub

بعد از ساخت Repository در GitHub:

```bash
git remote add origin https://github.com/USERNAME/REPOSITORY_NAME.git
git branch -M main
git push -u origin main
```

## 5. تصاویر مورد نیاز

پس از Push، تصاویر زیر گرفته و در مسیر `evidence/github_screenshots/` ذخیره شوند:

- صفحه اصلی Repository
- ساختار پوشه‌ها در GitHub
- Commit History
- آخرین Push موفق
