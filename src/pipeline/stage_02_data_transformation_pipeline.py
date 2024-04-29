
from src.config.configuration import Configuration
from src.components.data_transformation import DataTransformation
from src import logger
from src.excption.exception import customexception
import sys


class DataTransformationPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = Configuration()
        data_txm_config = config.get_data_transformation_config()
        data_txm = DataTransformation(data_txm_config=data_txm_config)
        data_txm.data_transformation_for_training()


stage_name = "Data Transformation"
if __name__ == "__main__":
    try:
        logger.info("stage - {stage_name} has started ")
        obj = DataTransformationPipeline()
        obj.main()
        logger.info(f"stage {stage_name} completed successfully!")
    except Exception as e:
        raise customexception(e, sys)
