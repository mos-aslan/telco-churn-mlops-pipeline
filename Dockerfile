FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*

COPY requirements_docker.txt /app/requirements_docker.txt

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r /app/requirements_docker.txt

COPY src /app/src
COPY data /app/data
COPY models/final_model /app/models/final_model
COPY run_pipeline.py /app/run_pipeline.py
COPY PIPELINE_USAGE.md /app/PIPELINE_USAGE.md

RUN mkdir -p /app/reports/final_pipeline_runs

CMD ["python", "run_pipeline.py", "--mode", "predict-sample"]
