from src.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH, SCHEMA_FILE_PATH
from src.utils.common import read_yaml, create_directories
from src.entity.config_entity import DataIngestionConfig, DataTransformationConfig, ModelTrainerConfig, ModelEvaluationConfig, PredictionConfig
from pathlib import Path


class Configuration:
    def __init__(self, config_path=CONFIG_FILE_PATH, params_path=PARAMS_FILE_PATH, schema_path=SCHEMA_FILE_PATH) -> None:
        self.config = read_yaml(config_path)
        self.params = read_yaml(params_path)
        self.schema = read_yaml(schema_path)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        data_ingestion_config = DataIngestionConfig(
            data_ingestion_root=Path(config.data_ingestion_root),
            data_url=config.data_url,
            data_path=config.data_path
        )
        return data_ingestion_config

    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation
        data_txm_config = DataTransformationConfig(
            data_transformation_root=Path(config.data_transformation_root),
            data_path=Path(config.data_path),
            # transformed_data_path=config.transformed_data_path
            # target=config.target
        )

        return data_txm_config

    def get_model_trainer_config(self):
        config = self.config.model_trainer
        model_trainer_config = ModelTrainerConfig(
            transformed_train_data=Path(config.transformed_train_data),
            model_trainer_root=Path(config.model_trainer_root),
            model_path=Path(config.model_path),
            params=self.params,
            target=config.target
        )
        return model_trainer_config

    def get_model_evaluation_config(self):
        config = self.config.model_evaluation
        model_eval_config = ModelEvaluationConfig(
            model_evaluation_root=Path(config.model_evaluation_root),
            model_path=Path(config.model_path),
            evaluation_score=Path(config.evaluation_score),
            test_data_path=Path(config.test_data_path),
            target=config.target,
            params=dict(self.params.xgboost)
        )
        return model_eval_config

    def get_prediction_config(self):
        config = self.config.prediction
        prediction_config = PredictionConfig(
            model_path=Path(config.model_path)
        )
        return prediction_config
