Step 09 - Final Inference Module and Reproducibility Test

This folder contains the outputs for the final inference module.

Purpose:
Create a reusable inference module that loads the final model package and produces churn predictions.

Main files:
- C:\Users\NezarHalabia\finallprogect\src\inference.py
- C:\Users\NezarHalabia\finallprogect\run_final_inference_example.py

Supported inference modes:
- Prediction from final feature matrix.
- Prediction from readable/raw Telco customer data.

Outputs:
- single_feature_input_prediction_test.csv
- raw_readable_sample_batch_predictions.csv
- final_inference_reproducibility_test_metrics.csv
- final_inference_test_split_predictions.csv
- final_inference_confusion_matrix_test_split.csv
- final_inference_classification_report_test_split.json

The final inference test uses the same saved test split from Step 6.