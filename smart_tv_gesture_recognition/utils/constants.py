from datetime import datetime
from typing import List
import torch

import torchvision

TIMESTAMP: datetime = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")


# Data Ingestion Constants
ARTIFACT_DIR: str = "artifacts"

BUCKET_NAME: str = "handgesturerecognition"

S3_DATA_FOLDER: str = "raw"

# Data Transformation Constants
CLASS_LABEL_1:str = 'RIGHT SWIPE'
CLASS_LABEL_2:str = 'LEFT SWIPE'
CLASS_LABEL_3:str = 'THUMBS DOWN'
CLASS_LABEL_4:str = 'THUMBS UP'
CLASS_LABEL_5:str = 'STOP GESTURE'

BRIGHTNESS: int = 0.10
CONTRASt: int = 0.1
SATURATION: int = 0.10
HUE: int = 0.1
RESIZE: int = 0.1
RESIZE: int = 224
CENTERCROP: int = 224
RANDOMROTATION: int = 10

NORMALIZE_LIST_1: List[int] = [0.485, 0.456, 0.406]

NORMALIZE_LIST_2: List[int] = [0.229, 0.224, 0.225]

TRAIN_TRANSFORMS_KEY: str = "HandGesture_train_transforms"

TRAIN_TRANSFORMS_FILE: str = "train_transforms.pkl"

TEST_TRANSFORMS_FILE: str = "test_transforms.pkl"

BATCH_SIZE: int = 2

SHUFFLE: bool = False

PIN_MEMORY: bool = True

# Model Trainer Constants

TRAINED_MODEL_DIR: str = "trained_model"

TRAINED_MODEL_NAME: str = "model.pt"

DEVICE: torch.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

STEP_SIZE: int = 6

GAMMA: int = 0.5

EPOCH: int = 1

PREDICTION_LABEL: dict = {
    0: "right swipe",      # Maps to 'Next Video'
    1: "left swipe",       # Maps to 'Previous Video'
    2: "thumbs up",        # Maps to 'Volume Up'
    3: "thumbs down",      # Maps to 'Volume Down'
    4: "stop gesture"      # Maps to 'Play/Pause Toggle'
}

# Define the actions based on the gestures
ACTIONS = {
    "right swipe": "next_video",
    "left swipe": "previous_video",
    "thumbs up": "volume_up",
    "thumbs down": "volume_down",
    "stop gesture": "play_pause"
}

