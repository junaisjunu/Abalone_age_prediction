from src.config.configuration import Configuration
from src.components.data_ingestion import DataIngestion
from src.excption.exception import customexception
import sys
from src import logger


class DataIngestionPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = Configuration()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(data_ingestion_config)
        data_ingestion.download_data()


stage_name = "Data ingestion"
if __name__ == "__main__":
    try:
        logger.info(f"stage - {stage_name} has started")
        obj = DataIngestionPipeline()
        obj.main()
        logger.info(f"{stage_name} completed successfully!")
    except Exception as e:
        raise customexception(e, sys)
