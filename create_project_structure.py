import os

# Define directories and files in a simplified structure
structure_with_files = {
    "smart_tv_gesture_recognition/data/raw/": None,
    "smart_tv_gesture_recognition/data/processed/": None,
    "smart_tv_gesture_recognition/data/augmented/": None,
    "smart_tv_gesture_recognition/models/saved_models/": None,
    
    "smart_tv_gesture_recognition/cloud_storage/": [
        "s3_operations.py",
        "__init__.py"
    ],

    "smart_tv_gesture_recognition/entity/":[
        "__init__.py",
        "artifact_entity.py",
        "config_entity.py"
    ],

    "smart_tv_gesture_recognition/pipeline/":[
        "__init__.py",
        "training_pipeline.py"
    ],

    "smart_tv_gesture_recognition/utils/": [
        "__init__.py",
        "preprocess.py",
        "augmentation.py",
        "webcam_capture.py",
        "helper_functions.py"
    ],

    "smart_tv_gesture_recognition/realtime/": [
        "predict.py",
        "webcam_gesture.py",
        "mapping.py"
    ],

    "smart_tv_gesture_recognition/notebooks/": [
        "data_exploration.ipynb",
        "model_training.ipynb"
    ],

    "smart_tv_gesture_recognition/components/": [
        "__init__.py",
        "data_ingestion.py",
        "data_transformation.py",
        "model_evaluation.py",
        "model_training.py",
        "model_pusher.py"
    ],

    "smart_tv_gesture_recognition/": [
        "__init__.py",
        "requirements.txt",
        "README.md",
        "config.yaml",
        "logger.py",
        "exception.py",
        "main.py",
        "setup.py",
        ".gitignore"
    ]
}

# Create directories and files
for folder, files in structure_with_files.items():
    os.makedirs(folder, exist_ok=True)
    if files:
        for file_name in files:
            file_path = os.path.join(folder, file_name)
            with open(file_path, "w") as file:
                file.write(f"# Placeholder content for {file_name}")

print("Directory structure and files created.")
