from dataclasses import dataclass
from pathlib import Path


@dataclass
class DataIngestionConfig:
    data_ingestion_root: Path
    data_url: str
    data_path: Path


@dataclass
class DataTransformationConfig:
    data_transformation_root: Path
    data_path: Path


@dataclass
class ModelTrainerConfig:
    transformed_train_data: Path
    model_trainer_root: Path
    model_path: Path
    params: str
    target: str


@dataclass
class ModelEvaluationConfig:
    model_evaluation_root: Path
    model_path: Path
    evaluation_score: Path
    test_data_path: Path
    target: str
    params: dict


@dataclass
class PredictionConfig:
    model_path: Path
