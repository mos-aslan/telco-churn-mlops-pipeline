import mlflow
import mlflow.sklearn


def setup_mlflow(experiment_name='Telco_Churn_MLOps'):
    mlflow.set_experiment(experiment_name)


def log_experiment(model, model_name, dataset_version, params, metrics):
    with mlflow.start_run(run_name=f'{dataset_version}_{model_name}'):
        mlflow.log_param('model_name', model_name)
        mlflow.log_param('dataset_version', dataset_version)
        for key, value in params.items():
            mlflow.log_param(key, value)
        for key, value in metrics.items():
            if key != 'confusion_matrix' and value is not None:
                mlflow.log_metric(key, value)
        mlflow.sklearn.log_model(model, artifact_path='model')