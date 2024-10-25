import os

# Define the directory structure
directory_structure = {
    "smart_tv_gesture_recognition": {
        "data": {
            "raw": {},
            "processed": {},
            "augmented": {}
        },
        "models": {
            "saved_models": {}
        },
        "utils": {},
        "realtime": {},
        "notebooks": {},
        "components":{}
    }
}

# Function to create directories
def create_directory_structure(base_path, structure):
    for folder, subfolders in structure.items():
        path = os.path.join(base_path, folder)
        os.makedirs(path, exist_ok=True)
        create_directory_structure(path, subfolders)

# Base path for the project
base_path = "."  # Current directory

# Create the directory structure
create_directory_structure(base_path, directory_structure)

# Files to create with placeholder text
files_to_create = {
    # Root files
    "smart_tv_gesture_recognition/requirements.txt": "",
    "smart_tv_gesture_recognition/README.md": "# Smart TV Gesture Recognition Project\n\nThis project uses deep learning to recognize gestures for controlling a smart TV.",
    "smart_tv_gesture_recognition/config.yaml": "",

    # Model files
    "smart_tv_gesture_recognition/models/cnn_lstm_model.py": "# CNN + LSTM model architecture placeholder",
    "smart_tv_gesture_recognition/models/train_model.py": "# Training script placeholder",
    "smart_tv_gesture_recognition/models/evaluate_model.py": "# Evaluation script placeholder",

    # Utility files
    "smart_tv_gesture_recognition/utils/preprocess.py": "# Preprocessing script placeholder",
    "smart_tv_gesture_recognition/utils/augmentation.py": "# Data augmentation script placeholder",
    "smart_tv_gesture_recognition/utils/webcam_capture.py": "# Webcam capture script placeholder",
    "smart_tv_gesture_recognition/utils/helper_functions.py": "# Helper functions placeholder",

    # Realtime recognition files
    "smart_tv_gesture_recognition/realtime/predict.py": "# Prediction script placeholder",
    "smart_tv_gesture_recognition/realtime/webcam_gesture.py": "# Real-time gesture recognition script placeholder",
    "smart_tv_gesture_recognition/realtime/mapping.py": "# Gesture-to-command mapping placeholder",

    # Notebooks
    "smart_tv_gesture_recognition/notebooks/data_exploration.ipynb": "",
    "smart_tv_gesture_recognition/notebooks/model_training.ipynb": "",

    # Logs
    "smart_tv_gesture_recognition/logger.py": "",

    # Exception
    "smart_tv_gesture_recognition/exception.py": "",

    # Components
    "smart_tv_gesture_recognition/components/data_ingestion.py": "",
    "smart_tv_gesture_recognition/components/data_transformation.py": "",
    "smart_tv_gesture_recognition/components/model_evaluation.py": "",
    "smart_tv_gesture_recognition/components/model_training.py": "",
    "smart_tv_gesture_recognition/components/model_pusher.py": ""

}

# Create files and write placeholder text
for file_path, content in files_to_create.items():
    with open(file_path, "w") as file:
        file.write(content)

print("Directory structure and necessary files have been created.")
