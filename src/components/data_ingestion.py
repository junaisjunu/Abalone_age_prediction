import requests
from src.excption.exception import customexception
import sys
from src.utils.common import create_directories


class DataIngestion:
    def __init__(self, config) -> None:
        self.config = config

    def download_data(self):
        create_directories([self.config.data_ingestion_root])
        try:
            response = requests.get(self.config.data_url)
            if response.status_code == 200:
                with open(self.config.data_path, 'wb') as f:
                    f.write(response.content)
                print(f"File downloaded successfully to {self.config.data_path}")
            else:
                print(f"Failed to download file, status code: {response.status_code}")
        except Exception as e:
            raise customexception(e, sys)
