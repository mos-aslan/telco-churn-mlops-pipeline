import pandas as pd


def clean_data(df):
    df = df.copy()
    columns_to_drop = [
        'CustomerID',
        'Count',
        'Country',
        'State',
        'Lat Long',
        'Churn Label',
        'Churn Score',
        'CLTV',
        'Churn Reason'
    ]
    existing_cols = [col for col in columns_to_drop if col in df.columns]
    df = df.drop(columns=existing_cols)
    if 'Total Charges' in df.columns:
        df['Total Charges'] = pd.to_numeric(df['Total Charges'], errors='coerce')
        df['Total Charges'] = df['Total Charges'].fillna(df['Total Charges'].median())
    return df


def encode_categorical_features(df, target_col='Churn Value'):
    df = df.copy()
    categorical_cols = df.select_dtypes(include=['object']).columns.tolist()
    if target_col in categorical_cols:
        categorical_cols.remove(target_col)
    df = pd.get_dummies(df, columns=categorical_cols, drop_first=True)
    return df