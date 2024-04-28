from src.pipeline.stage_01_data_ingestion_pipeline import DataIngestionPipeline
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
