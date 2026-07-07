from pathlib import Path
import json

import numpy as np
import pandas as pd
import joblib

from src.features import create_features


def get_project_root() -> Path:
    return Path(__file__).resolve().parents[1]


def load_final_assets(project_root=None):
    """
    Load the final model, feature names, threshold, and metadata.
    """
    if project_root is None:
        project_root = get_project_root()
    else:
        project_root = Path(project_root)

    final_model_dir = project_root / "models" / "final_model"

    model_path = final_model_dir / "final_model.joblib"
    feature_names_path = final_model_dir / "feature_names.json"
    threshold_path = final_model_dir / "decision_threshold.json"
    metadata_path = final_model_dir / "final_model_metadata.json"

    if not model_path.exists():
        raise FileNotFoundError(f"Final model not found: {model_path}")

    if not feature_names_path.exists():
        raise FileNotFoundError(f"Feature names file not found: {feature_names_path}")

    if not threshold_path.exists():
        raise FileNotFoundError(f"Decision threshold file not found: {threshold_path}")

    if not metadata_path.exists():
        raise FileNotFoundError(f"Final metadata file not found: {metadata_path}")

    model = joblib.load(model_path)

    with open(feature_names_path, "r", encoding="utf-8") as file:
        feature_names = json.load(file)

    with open(threshold_path, "r", encoding="utf-8") as file:
        threshold_data = json.load(file)

    with open(metadata_path, "r", encoding="utf-8") as file:
        metadata = json.load(file)

    threshold = float(threshold_data["decision_threshold"])

    return model, feature_names, threshold, metadata


def align_feature_dataframe(df_features: pd.DataFrame, feature_names: list) -> pd.DataFrame:
    """
    Align an already feature-engineered dataframe to the exact model feature order.
    Missing columns are filled with 0. Extra columns are ignored.
    """
    df_aligned = df_features.copy()

    for column in feature_names:
        if column not in df_aligned.columns:
            df_aligned[column] = 0

    df_aligned = df_aligned[feature_names]

    return df_aligned


def prepare_raw_dataframe(df_raw: pd.DataFrame, feature_names: list) -> pd.DataFrame:
    """
    Convert readable/raw Telco customer data into the final model feature matrix.
    This applies the same feature-engineering logic used to create v3.
    """
    df = df_raw.copy()

    leakage_or_target_columns = [
        "CustomerID",
        "Count",
        "Country",
        "State",
        "Lat Long",
        "Churn Label",
        "Churn Value",
        "Churn Score",
        "Churn Reason"
    ]

    columns_to_drop = [col for col in leakage_or_target_columns if col in df.columns]
    df = df.drop(columns=columns_to_drop)

    if "Total Charges" in df.columns:
        df["Total Charges"] = pd.to_numeric(df["Total Charges"], errors="coerce")
        df["Total Charges"] = df["Total Charges"].fillna(df["Total Charges"].median())

    df = create_features(df)

    high_cardinality_or_identifier_columns = [
        "City",
        "Zip Code"
    ]

    columns_to_drop_v3 = [
        col for col in high_cardinality_or_identifier_columns if col in df.columns
    ]

    df = df.drop(columns=columns_to_drop_v3)

    categorical_columns = df.select_dtypes(include=["object", "category"]).columns.tolist()

    df_encoded = pd.get_dummies(
        df,
        columns=categorical_columns,
        drop_first=True,
        dtype=int
    )

    df_encoded = align_feature_dataframe(df_encoded, feature_names)

    return df_encoded


def probability_to_risk_level(probability: float, threshold: float) -> str:
    """
    Convert churn probability into an interpretable risk level.
    """
    if probability >= max(0.75, threshold + 0.20):
        return "High"
    elif probability >= threshold:
        return "Medium"
    else:
        return "Low"


def predict_from_feature_dataframe(df_features: pd.DataFrame, project_root=None) -> pd.DataFrame:
    """
    Predict churn from a dataframe that already contains final model features.
    """
    model, feature_names, threshold, metadata = load_final_assets(project_root)

    df_aligned = align_feature_dataframe(df_features, feature_names)

    probabilities = model.predict_proba(df_aligned.to_numpy())[:, 1]
    predictions = (probabilities >= threshold).astype(int)

    results = pd.DataFrame({
        "churn_probability": probabilities,
        "decision_threshold": threshold,
        "prediction": predictions
    })

    results["risk_level"] = results["churn_probability"].apply(
        lambda value: probability_to_risk_level(value, threshold)
    )

    return results


def predict_from_raw_dataframe(df_raw: pd.DataFrame, project_root=None) -> pd.DataFrame:
    """
    Predict churn from readable/raw Telco customer records.
    """
    model, feature_names, threshold, metadata = load_final_assets(project_root)

    df_prepared = prepare_raw_dataframe(df_raw, feature_names)

    probabilities = model.predict_proba(df_prepared.to_numpy())[:, 1]
    predictions = (probabilities >= threshold).astype(int)

    results = pd.DataFrame({
        "churn_probability": probabilities,
        "decision_threshold": threshold,
        "prediction": predictions
    })

    results["risk_level"] = results["churn_probability"].apply(
        lambda value: probability_to_risk_level(value, threshold)
    )

    return results


def predict_single_raw_record(record: dict, project_root=None) -> dict:
    """
    Predict churn for one raw customer record provided as a dictionary.
    """
    df_raw = pd.DataFrame([record])
    result = predict_from_raw_dataframe(df_raw, project_root=project_root)

    return result.iloc[0].to_dict()
