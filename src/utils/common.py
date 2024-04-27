from box import ConfigBox
from pathlib import Path
from src.excption.exception import customexception
import sys
import yaml
from src import logger
from ensure import ensure_annotations
import os
import json
import pickle
import xgboost as xgb


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    try:
        with open(path_to_yaml) as f:
            content = yaml.safe_load(f)
            logger.info(f"file loaded succesfully from the path {path_to_yaml}")
            return ConfigBox(content)
    except Exception as e:
        raise customexception(e, sys)


@ensure_annotations
def create_directories(paths: list):
    try:
        for path in paths:
            os.makedirs(path, exist_ok=True)
    except Exception as e:
        raise customexception(e, sys)


@ensure_annotations
def save_json(path: Path, data: dict):
    try:
        with open(path, "w") as f:
            json.dump(data, f, indent=4)
        logger.info(f"json file save successfully at {path}")
    except Exception as e:
        raise customexception(e, sys)


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    with open(path, "r") as f:
        content = json.load(f)
        logger.info(f"json file loaded successfully from {path}")
        return ConfigBox(content)


@ensure_annotations
def save_model(model, path: Path):
    try:
        with open(path, "wb") as f:
            pickle.dump(model, f)
            logger.info("model saves successfully!")

    except Exception as e:
        raise customexception(e, sys)


@ensure_annotations
def load_model(path: Path):
    try:
        with open(path, "rb") as f:
            model = pickle.load(f)
        return model
        logger.info("model loaded succesfully!")
    except Exception as e:
        raise (e, sys)


if __name__ == "__main__":
    model = xgb.XGBRFRegressor()
    save_model(model, Path('artifacts/model.pkl'))
