Step 03 - Data Cleaning and Dataset Version v2

This folder contains the outputs of the first data-cleaning script.

Purpose:
Build dataset version v2 from the raw Telco Customer Churn dataset.

Main operations:
- Removed non-informative columns.
- Removed leakage-prone columns.
- Converted Total Charges from object to numeric.
- Imputed missing Total Charges values using the median.
- Encoded categorical variables using one-hot encoding.
- Saved a readable cleaned dataset and an ML-ready encoded dataset.

Output datasets:
- C:\Users\NezarHalabia\finallprogect\data\v2\telco_churn_v2_readable.csv
- C:\Users\NezarHalabia\finallprogect\data\v2\telco_churn_v2.csv

Subfolders:
- tables: CSV summaries documenting the cleaning process.
- figures: reserved for cleaning-related figures if needed.
- logs: JSON and TXT logs describing the full transformation.