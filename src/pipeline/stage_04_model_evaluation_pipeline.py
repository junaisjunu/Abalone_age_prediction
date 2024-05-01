from src.config.configuration import Configuration
from src.components.model_evaluation import ModelEvaluation
from src.excption.exception import customexception
import sys
from src import logger


class ModelEvaluationPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = Configuration()
        eval_config = config.get_model_evaluation_config()
        eval = ModelEvaluation(eval_config)
        eval.initiate_evaluation()


stage_name = "Model Evaluation"
if __name__ == "__main__":
    try:
        logger.info("stage - {stage_name} has started ")
        obj = ModelEvaluationPipeline()
        obj.main()
        logger.info(f"stage {stage_name} completed successfully!")
    except Exception as e:
        raise customexception(e, sys)
