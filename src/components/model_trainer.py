import xgboost as xgb
from src import logger
import pandas as pd
from src.utils.common import save_model, create_directories
from src.excption.exception import customexception
import sys
from src.entity.config_entity import ModelTrainerConfig


class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig) -> None:
        self.config = config

    def initiate_model_training(self):
        try:
            create_directories([self.config.model_trainer_root])
            params = self.config.params.xgboost
            model = xgb.XGBRegressor(**params)
            logger.info(model.get_params())
            train_data = pd.read_csv(self.config.transformed_train_data)
            X = train_data.drop(self.config.target, axis=1)
            y = train_data[self.config.target]
            logger.info(self.config.model_path)
            model.fit(X, y)
            save_model(model=model, path=self.config.model_path)
        except Exception as e:
            raise customexception(e, sys)
