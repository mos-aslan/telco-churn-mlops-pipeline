from pathlib import Path
import pandas as pd

from src.inference import predict_from_feature_dataframe, predict_from_raw_dataframe


PROJECT_ROOT = Path(__file__).resolve().parent

sample_features_path = PROJECT_ROOT / "models" / "final_model" / "sample_input_features.csv"

sample_features = pd.read_csv(sample_features_path)

prediction = predict_from_feature_dataframe(
    sample_features,
    project_root=PROJECT_ROOT
)

print(prediction)
