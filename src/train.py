from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

try:
    from xgboost import XGBClassifier
except Exception:
    XGBClassifier = None

try:
    from catboost import CatBoostClassifier
except Exception:
    CatBoostClassifier = None


def get_models(random_state=42):
    models = {
        'LogisticRegression': LogisticRegression(max_iter=1000, random_state=random_state),
        'RandomForest': RandomForestClassifier(n_estimators=100, random_state=random_state, class_weight='balanced')
    }
    if XGBClassifier is not None:
        models['XGBoost'] = XGBClassifier(
            n_estimators=100,
            learning_rate=0.1,
            max_depth=3,
            eval_metric='logloss',
            random_state=random_state
        )
    if CatBoostClassifier is not None:
        models['CatBoost'] = CatBoostClassifier(
            iterations=100,
            learning_rate=0.1,
            depth=6,
            random_state=random_state,
            verbose=False
        )
    return models