import os
import sys

import bentoml
import joblib
import torch
import torch.nn.functional as F
from torch.nn import Module
from torch.optim import Optimizer
from torch.optim.lr_scheduler import StepLR, _LRScheduler
from torchvision.models import EfficientNet_B0_Weights
from torchvision import models
from tqdm import tqdm

from smart_tv_gesture_recognition.utils.constants import * 
from smart_tv_gesture_recognition.entity.artifact_entity import (
    DataTransformationArtifact,
    ModelTrainerArtifact,
)
from smart_tv_gesture_recognition.entity.config_entity import ModelTrainerConfig
from smart_tv_gesture_recognition.exception import HandException
from smart_tv_gesture_recognition.logger import logging

class ModelTrainer:
    def __init__(
        self,
        data_transformation_artifact: DataTransformationArtifact,
        model_trainer_config: ModelTrainerConfig,
    ):
        """
        Initializes the ModelTrainer class with configuration and data artifacts.
        
        :param data_transformation_artifact: Holds transformed training and testing datasets.
        :param model_trainer_config: Configuration that includes model parameters, device settings, and paths.
        """
        self.model_trainer_config: ModelTrainerConfig = model_trainer_config
        self.data_transformation_artifact: DataTransformationArtifact = data_transformation_artifact

        # Load a pretrained EfficientNet model and modify the final layer for 5 gesture classes
        self.model: Module = models.efficientnet_b0(weights=EfficientNet_B0_Weights.IMAGENET1K_V1)
        num_features = self.model.classifier[1].in_features
        self.model.classifier[1] = torch.nn.Sequential(torch.nn.Dropout(0.05),torch.nn.Linear(num_features, 5))  # 5 classes for gestures
        self.model = self.model.to(self.model_trainer_config.device)

    def train(self, optimizer: Optimizer) -> None:
        logging.info("Entered the train method of Model trainer class")

        try:
            self.model.train()  # Set model to training mode
            pbar = tqdm(self.data_transformation_artifact.transformed_train_object)

            correct = 0
            processed = 0

            for batch_idx, (data, target) in enumerate(pbar):
                data, target = data.to(DEVICE), target.to(DEVICE)
                optimizer.zero_grad()
                y_pred = self.model(data)
                loss = F.cross_entropy(y_pred, target)
                loss.backward()
                optimizer.step()

                pred = y_pred.argmax(dim=1, keepdim=True)
                correct += pred.eq(target.view_as(pred)).sum().item()
                processed += len(data)
                pbar.set_description(
                    desc=f"Loss={loss.item()} Batch_id={batch_idx} Accuracy={100*correct/processed:0.2f}"
                )

            logging.info("Exited the train method of Model trainer class")

        except Exception as e:
            raise HandException(e, sys)

    def test(self) -> None:
        logging.info("Entered the test method of Model trainer class")

        try:
            self.model.eval()
            test_loss = 0.0
            correct = 0

            with torch.no_grad():
                for data, target in self.data_transformation_artifact.transformed_test_object:
                    data, target = data.to(DEVICE), target.to(DEVICE)
                    output = self.model(data)
                    test_loss += F.cross_entropy(output, target, reduction="sum").item()
                    pred = output.argmax(dim=1, keepdim=True)
                    correct += pred.eq(target.view_as(pred)).sum().item()

                test_loss /= len(self.data_transformation_artifact.transformed_test_object.dataset)
                print(
                    "Test set: Average loss: {:.4f}, Accuracy: {}/{} ({:.2f}%)\n".format(
                        test_loss,
                        correct,
                        len(self.data_transformation_artifact.transformed_test_object.dataset),
                        100.0 * correct / len(self.data_transformation_artifact.transformed_test_object.dataset),
                    )
                )

            logging.info("Exited the test method of Model trainer class")

        except Exception as e:
            raise HandException(e, sys)

    def initiate_model_trainer(self) -> ModelTrainerArtifact:
        try:
            logging.info("Entered the initiate_model_trainer method of Model trainer class")

            optimizer = torch.optim.SGD(
                self.model.parameters(), **self.model_trainer_config.optimizer_params
            )

            scheduler = StepLR(
                optimizer=optimizer, **self.model_trainer_config.scheduler_params
            )

            for epoch in range(1, self.model_trainer_config.epochs + 1):
                print("Epoch : ", epoch)
                self.train(optimizer=optimizer)
                scheduler.step()
                self.test()

            os.makedirs(self.model_trainer_config.artifact_dir, exist_ok=True)
            torch.save(self.model, self.model_trainer_config.trained_model_path)

            train_transforms_obj = joblib.load(
                self.data_transformation_artifact.train_transform_file_path
            )

            model_trainer_artifact = ModelTrainerArtifact(
                trained_model_path=self.model_trainer_config.trained_model_path
            )

            logging.info("Exited the initiate_model_trainer method of Model trainer class")
            return model_trainer_artifact

        except Exception as e:
            raise HandException(e, sys)
