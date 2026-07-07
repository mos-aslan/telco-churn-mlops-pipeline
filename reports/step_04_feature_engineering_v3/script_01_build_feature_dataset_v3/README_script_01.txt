Step 04 - Feature Engineering and Dataset Version v3

This folder contains the outputs of the feature-engineering script.

Purpose:
Build dataset version v3 from the cleaned readable v2 dataset.

Main operations:
- Created tenure-based features.
- Created charge-based features.
- Created contract and payment risk features.
- Created internet and service-count features.
- Removed high-cardinality or pseudo-identifier columns.
- Encoded categorical variables.
- Scaled selected numeric columns using StandardScaler.

Output datasets:
- C:\Users\NezarHalabia\finallprogect\data\v3\telco_churn_v3_readable.csv
- C:\Users\NezarHalabia\finallprogect\data\v3\telco_churn_v3_encoded_unscaled.csv
- C:\Users\NezarHalabia\finallprogect\data\v3\telco_churn_v3.csv

Subfolders:
- tables: CSV summaries documenting feature engineering.
- figures: diagnostic plots for engineered features.
- logs: JSON and TXT logs describing the transformation.