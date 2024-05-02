import pandas as pd
from src.components.data_transformation import DataTransformation
from src.utils.common import load_model
from src.entity.config_entity import PredictionConfig
from src.excption.exception import customexception
import sys


class Prediction:
    def __init__(self, config: PredictionConfig) -> None:
        self.config = config

    def initiate_prediction(self, data: pd.DataFrame):
        try:
            transformed_data = DataTransformation.get_basic_transfomed_data(df=data)
            print(transformed_data.columns)

            model = load_model(self.config.model_path)

            prediction = model.predict(transformed_data)
            return prediction
        except Exception as e:
            raise customexception(e, sys)
