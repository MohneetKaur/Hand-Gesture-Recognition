from datetime import datetime
from typing import List

import torchvision

TIMESTAMP: datetime = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")


# Data Ingestion Constants
ARTIFACT_DIR: str = "artifacts"

BUCKET_NAME: str = "handgesturerecognition"

S3_DATA_FOLDER: str = "raw"