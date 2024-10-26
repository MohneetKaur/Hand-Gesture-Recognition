import sys
from smart_tv_gesture_recognition.components.data_ingestion import DataIngestion

from smart_tv_gesture_recognition.entity.artifact_entity import (
    DataIngestionArtifact
)

from smart_tv_gesture_recognition.entity.config_entity import (
    DataIngestionConfig
)

from smart_tv_gesture_recognition.exception import HandException
from smart_tv_gesture_recognition.logger import logging

class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()

    
    def start_data_ingestion(self) -> DataIngestionArtifact:
        logging.info("Entered the start_data_ingestion method of TrainPipeline class")
        try:
            logging.info("Getting data from the S3 bucket")
            data_ingestion = DataIngestion(data_ingestion_config=self.data_ingestion_config)
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            logging.info("Got train_set and test_set from S3 bucket")
            logging.info("Exited the start_data_ingestion method of TrainPipeline class")

            return data_ingestion_artifact
        except Exception as e:
            raise HandException(e, sys)
        

    

    def run_pipeline(self) -> None:
        logging.info("Entered the run_pipeline method of TrainPipeline class")
        try:
            data_ingestion_artifact: DataIngestionArtifact = self.start_data_ingestion()



            logging.info("Exited the run_pipeline method of TrainPipeline class")
        except Exception as e:
            raise HandException(e, sys)