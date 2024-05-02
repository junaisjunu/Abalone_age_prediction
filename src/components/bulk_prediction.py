from src.config.configuration import Configuration
from src.utils.common import load_model, create_directories
import pandas as pd
from src.components.data_transformation import DataTransformation
from src import logger


class BulkPredction:
    def __init__(self) -> None:
        pass

    def initiate_bulk_prediction(self, data: pd.DataFrame):
        configuration = Configuration()
        config = configuration.get_bulk_prediction_config()
        logger.info("Bulk prediction has started")
        model = load_model(config.model_path)
        transformed_data = DataTransformation.get_basic_transfomed_data(data)
        create_directories([config.bulk_prediction_root])
        prediction = model.predict(transformed_data)
        rounded_prediction = [round(val, 2) for val in prediction]
        data['Predicted Rings'] = rounded_prediction
        data.to_csv(config.result_data, index=False)
        logger.info(f"bulk prediction has complted , saved the file at {config.result_data}")
        return config.result_data
