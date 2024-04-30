from src.pipeline.stage_01_data_ingestion_pipeline import DataIngestionPipeline
from src.pipeline.stage_02_data_transformation_pipeline import DataTransformationPipeline
from src.pipeline.stage_03_model_trainer_pipeline import ModelTrainerPipeline
from src import logger
from src.excption.exception import customexception
import sys


stage_name = "Data ingestion"
if __name__ == "__main__":
    try:
        logger.info(f"stage - {stage_name} has started")
        obj = DataIngestionPipeline()
        obj.main()
        logger.info(f"{stage_name} completed successfully!")
    except Exception as e:
        raise customexception(e, sys)


stage_name = "Data Transformation"
if __name__ == "__main__":
    try:
        logger.info("stage - {stage_name} has started ")
        obj = DataTransformationPipeline()
        obj.main()
        logger.info(f"stage {stage_name} completed successfully!")
    except Exception as e:
        raise customexception(e, sys)


stage_name = "Model Training"
if __name__ == "__main__":
    try:
        logger.info("stage - {stage_name} has started ")
        obj = ModelTrainerPipeline()
        obj.main()
        logger.info(f"stage {stage_name} completed successfully!")
    except Exception as e:
        raise customexception(e, sys)
