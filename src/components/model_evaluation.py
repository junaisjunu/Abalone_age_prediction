from src.utils.common import load_model, create_directories, save_json
import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score, mean_squared_log_error
from src import logger
import mlflow
from src.entity.config_entity import ModelEvaluationConfig
from src.excption.exception import customexception
import sys
from mlflow.models.signature import infer_signature
from urllib.parse import urlparse


class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig) -> None:
        self.config = config

    def initiate_evaluation(self):
        try:
            model = load_model(self.config.model_path)
            eval_data = pd.read_csv(self.config.test_data_path)
            X = eval_data.drop(self.config.target, axis=1)
            y_test = eval_data[self.config.target]
            logger.info(self.config.params)
            params = self.config.params
            # model prediction
            y_pred = model.predict(X)
            create_directories([self.config.model_evaluation_root])
            mae = mean_absolute_error(y_test, y_pred)
            rmse = mean_squared_error(y_test, y_pred, squared=False)
            r2 = r2_score(y_test, y_pred)
            rmlse = mean_squared_log_error(y_test, y_pred, squared=False)
            logger.info(f" model - \n MAE = {mae} \n RMSE = {rmse} \n R2 Score = {r2} \n RMLSE = {rmlse} \n ============================")
            metrics = {"MAE": mae,
                       "RMSE": rmse,
                       "r2": r2,
                       "rmlse": rmlse}
            eval_score = {
                "Model Parms": params,
                "evaluation metrics": metrics
            }
            save_json(self.config.evaluation_score, eval_score)
            mlflow.set_registry_uri(uri=self.config.mlflow_uri)
            tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme
            logger.info(f"url = {tracking_url_type_store}")
            # Creat      a new MLflow Experiment
            mlflow.set_experiment("New test")
            # Start     an MLflow run
            with mlflow.start_run():
                mlflow.log_params(params)
                mlflow.log_metrics(metrics)
                mlflow.set_tag("Training Info", "Xg boost model")
                # Infer the model signature
                signature = infer_signature(model_input=X, model_output=y_pred)
                if tracking_url_type_store != "file":
                    mlflow.xgboost.log_model(
                        xgb_model=model,
                        artifact_path="artifacts",
                        signature=signature,
                        input_example=X,
                        registered_model_name="XGBoost model",
                    )
                else:
                    mlflow.xgboost.log_model(
                        xgb_model=model,
                        artifact_path="artifacts",
                        signature=signature,
                        input_example=X
                    )
        except Exception as e:
            raise customexception(e, sys)
