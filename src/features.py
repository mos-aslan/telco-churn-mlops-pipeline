import pandas as pd
import numpy as np


def create_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create engineered features for the Telco Customer Churn dataset.
    This function is used to build dataset version v3.
    """
    df = df.copy()

    if "Total Charges" in df.columns:
        df["Total Charges"] = pd.to_numeric(df["Total Charges"], errors="coerce")
        df["Total Charges"] = df["Total Charges"].fillna(df["Total Charges"].median())

    if "Tenure Months" in df.columns:
        df["Tenure_Group"] = pd.cut(
            df["Tenure Months"],
            bins=[-1, 12, 24, 48, 72],
            labels=["0_12_months", "13_24_months", "25_48_months", "49_72_months"]
        )
        df["Is_New_Customer"] = (df["Tenure Months"] <= 12).astype(int)
        df["Is_Long_Term_Customer"] = (df["Tenure Months"] >= 48).astype(int)

    if "Monthly Charges" in df.columns and "Tenure Months" in df.columns:
        df["Charges_Per_Tenure"] = df["Monthly Charges"] / (df["Tenure Months"] + 1)
        df["Estimated_Total_Charges"] = df["Monthly Charges"] * df["Tenure Months"]
        monthly_median = df["Monthly Charges"].median()
        df["High_Monthly_Charges"] = (df["Monthly Charges"] > monthly_median).astype(int)

    if "Total Charges" in df.columns and "Monthly Charges" in df.columns:
        df["TotalCharges_to_MonthlyRatio"] = df["Total Charges"] / (df["Monthly Charges"] + 1e-6)
        df["TotalCharges_to_MonthlyRatio"] = df["TotalCharges_to_MonthlyRatio"].replace(
            [np.inf, -np.inf],
            np.nan
        )
        df["TotalCharges_to_MonthlyRatio"] = df["TotalCharges_to_MonthlyRatio"].fillna(
            df["TotalCharges_to_MonthlyRatio"].median()
        )

    if "Contract" in df.columns:
        contract_risk_map = {
            "Two year": 0,
            "One year": 1,
            "Month-to-month": 2
        }
        df["Contract_Risk_Level"] = df["Contract"].map(contract_risk_map).fillna(1).astype(int)
        df["Is_Month_To_Month"] = (df["Contract"] == "Month-to-month").astype(int)

    if "Payment Method" in df.columns:
        df["Is_Electronic_Check"] = (df["Payment Method"] == "Electronic check").astype(int)

    if "Internet Service" in df.columns:
        df["Has_Internet_Service"] = (df["Internet Service"] != "No").astype(int)
        df["Is_Fiber_Optic"] = (df["Internet Service"] == "Fiber optic").astype(int)

    service_columns = [
        "Phone Service",
        "Multiple Lines",
        "Online Security",
        "Online Backup",
        "Device Protection",
        "Tech Support",
        "Streaming TV",
        "Streaming Movies"
    ]

    existing_service_columns = [col for col in service_columns if col in df.columns]

    if existing_service_columns:
        df["Total_Services_Count"] = 0
        for col in existing_service_columns:
            df["Total_Services_Count"] += (
                df[col].astype(str).str.lower().eq("yes").astype(int)
            )

    protection_support_columns = [
        "Online Security",
        "Online Backup",
        "Device Protection",
        "Tech Support"
    ]

    existing_protection_support_columns = [
        col for col in protection_support_columns if col in df.columns
    ]

    if existing_protection_support_columns:
        df["Protection_Support_Count"] = 0
        for col in existing_protection_support_columns:
            df["Protection_Support_Count"] += (
                df[col].astype(str).str.lower().eq("yes").astype(int)
            )

    streaming_columns = [
        "Streaming TV",
        "Streaming Movies"
    ]

    existing_streaming_columns = [col for col in streaming_columns if col in df.columns]

    if existing_streaming_columns:
        df["Streaming_Services_Count"] = 0
        for col in existing_streaming_columns:
            df["Streaming_Services_Count"] += (
                df[col].astype(str).str.lower().eq("yes").astype(int)
            )

    if "Online Security" in df.columns:
        df["No_Online_Security"] = (df["Online Security"] == "No").astype(int)

    if "Tech Support" in df.columns:
        df["No_Tech_Support"] = (df["Tech Support"] == "No").astype(int)

    return df
