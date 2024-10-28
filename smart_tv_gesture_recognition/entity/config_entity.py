import os
from dataclasses import dataclass
from torch import device

from smart_tv_gesture_recognition.utils.constants import *

@dataclass
class DataIngestionConfig:
    def __init__(self):
        self.s3_data_folder: str = S3_DATA_FOLDER
        self.bucket_name: str = BUCKET_NAME
        self.artifact_dir: str = os.path.join(ARTIFACT_DIR, TIMESTAMP)
        self.data_path: str = os.path.join(self.artifact_dir, 'data_ingestion', self.s3_data_folder)
        self.train_data_path: str = os.path.join(self.data_path,'train')
        self.test_data_path: str = os.path.join(self.data_path,'val')

@dataclass
class DataTransformationConfig:
    def __init__(self):
        self.color_jitter_transforms: dict = {
            "brightness": BRIGHTNESS,
            "contrast": CONTRASt,
            "saturation": SATURATION,
            "hue": HUE
        }

        self.RESIZE: int = RESIZE
        self.CENTERCROP: int = CENTERCROP
        self.RANDOMROTATION: int = RANDOMROTATION

        self.normalize_transforms: dict = {
            "mean": NORMALIZE_LIST_1,
            "std":NORMALIZE_LIST_2
        }

        self.data_loader_params: dict = {
            "batch_size": BATCH_SIZE,
            "shuffle": SHUFFLE,
            "pin_memory": PIN_MEMORY
        }

        self.artifact_dir: str = os.path.join(ARTIFACT_DIR, TIMESTAMP, "data_transformation")
        self.train_transforms_file: str = os.path.join(self.artifact_dir, TRAIN_TRANSFORMS_FILE)
        self.test_transforms_file: str = os.path.join(self.artifact_dir, TEST_TRANSFORMS_FILE)


@dataclass
class ModelTrainerConfig:
    def __init__(self):
        self.artifact_dir: str = os.path.join(ARTIFACT_DIR, TIMESTAMP, "model_training")
        self.trained_model_path: str = os.path.join(self.artifact_dir,TRAINED_MODEL_NAME)
        self.train_transforms_key: str = TRAIN_TRANSFORMS_KEY
        self.epochs: int = EPOCH

        # These values control how the model updates weights during training
        self.optimizer_params: dict = {"lr":0.001, "momentum":0.8}

        # step_size: the freq of adjustment & gamma:the factor by which th lr is multiplied each step
        self.scheduler_params: dict = {"step_size": STEP_SIZE, "gamma": GAMMA} 

        self.device: device = DEVICE