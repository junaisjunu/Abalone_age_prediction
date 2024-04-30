from src.config.configuration import Configuration
from src.components.model_trainer import ModelTrainer
from src import logger
from src.excption.exception import customexception
import sys


class ModelTrainerPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = Configuration()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(model_trainer_config)
        model_trainer.initiate_model_training()


stage_name = "Model Training"
if __name__ == "__main__":
    try:
        logger.info("stage - {stage_name} has started ")
        obj = ModelTrainerPipeline()
        obj.main()
        logger.info(f"stage {stage_name} completed successfully!")
    except Exception as e:
        raise customexception(e, sys)
