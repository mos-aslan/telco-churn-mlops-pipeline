from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]

DATA_DIR = PROJECT_ROOT / 'data'
RAW_DATA_DIR = DATA_DIR / 'v1'
CLEAN_DATA_DIR = DATA_DIR / 'v2'
FEATURE_DATA_DIR = DATA_DIR / 'v3'

MODELS_DIR = PROJECT_ROOT / 'models'
REPORTS_DIR = PROJECT_ROOT / 'reports'
FIGURES_DIR = REPORTS_DIR / 'figures'

TARGET_COLUMN = 'Churn Value'

RANDOM_STATE = 42
TEST_SIZE = 0.20
VALIDATION_SIZE = 0.20

MLFLOW_EXPERIMENT_NAME = 'Telco_Churn_MLOps'

RAW_DATA_FILE = 'Telco_customer_churn.xlsx'
CLEAN_DATA_FILE = 'telco_churn_v2.csv'
FEATURE_DATA_FILE = 'telco_churn_v3.csv'
RESULTS_FILE = 'model_comparison_results.csv'
BEST_MODEL_FILE = 'best_model.joblib'
