import sys
from smart_tv_gesture_recognition.cloud_storage.s3_operations import S3Operation
from smart_tv_gesture_recognition.utils.constants import *
from smart_tv_gesture_recognition.entity.artifact_entity import DataIngestionArtifact
from smart_tv_gesture_recognition.entity.config_entity import DataIngestionConfig
from smart_tv_gesture_recognition.exception import HandException
from smart_tv_gesture_recognition.logger import logging

class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig):
        self.data_ingestion_config = data_ingestion_config
        self.s3 = S3Operation()

    def get_data_from_s3(self) -> None:
        try:
            logging.info("Enetered the get_data_from_s3 method of DataIngestion class")
            self.s3.sync_folder_from_s3(
                folder=self.data_ingestion_config.data_path,
                bucket_name=self.data_ingestion_config.bucket_name,
                bucket_folder_name=self.data_ingestion_config.s3_data_folder
            )
            logging.info("Exited the get_data_from_s3 method of DataIngestion class")
        except Exception as e:
            raise HandException(e, sys)
        
    
    def initiate_data_ingestion(self) -> DataIngestionArtifact:
        logging.info("Entered the initiate_data_ingestion method of DataIngestion class")
        try:
            self.get_data_from_s3()
            data_ingestion_artifact: DataIngestionArtifact = DataIngestionArtifact(
                train_file_path=self.data_ingestion_config.train_data_path,
                test_file_path=self.data_ingestion_config.test_data_path
            )
            logging.info("Exited the initiate_data_ingestion method of DataIngestion class")
            return data_ingestion_artifact
        except Exception as e:
            raise HandException(e, sys)