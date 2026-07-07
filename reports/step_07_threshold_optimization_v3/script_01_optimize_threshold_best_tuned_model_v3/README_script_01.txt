Step 07 - Threshold Optimization

This folder contains the threshold optimization outputs for the best tuned model.

Purpose:
Optimize the classification threshold for the final tuned model without using the test set for threshold selection.

Method:
- Load the best tuned model from Step 6.
- Reconstruct the same Train_Validation and Test split.
- Generate out-of-fold probabilities on the Train_Validation split using 5-fold CV.
- Search thresholds from 0.10 to 0.90.
- Select the threshold using OOF F1-score, with recall preference when F1 values are close.
- Evaluate default threshold and optimized threshold on the Test set.

Important:
The test set is used only after threshold selection.

Output folders:
- tables: threshold search results, selected threshold, test comparison, confusion matrix, classification report.
- figures: threshold curves, confusion matrix, ROC curve, precision-recall curve.
- logs: reproducibility logs.

Best model: CatBoost
Selected threshold: 0.5
Final candidate model: C:\Users\NezarHalabia\finallprogect\models\final_candidate_v3\final_candidate_model_v3.joblib