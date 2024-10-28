# main.py
from smart_tv_gesture_recognition.utils.gesture_recognition import GestureRecognition
from smart_tv_gesture_recognition.utils.youtube_control import YouTubeController
import time

# File paths for model and WebDriver
MODEL_PATH = r"C:\Users\HP\Documents\projects\Hand Gesture Recognition System\artifacts\10_28_2024_18_51_56\model_training\model.pt"  # Replace with your model path
DRIVER_PATH = r"C:\Windows\System32\drivers\chromedriver.exe"  # Replace with path to your ChromeDriver

def main():
    gesture_recognizer = GestureRecognition(model_path=MODEL_PATH)
    youtube_controller = YouTubeController(driver_path=DRIVER_PATH)

    # Continuously detect gestures and control YouTube
    for gesture in gesture_recognizer.capture_gesture():
        if gesture != "unknown":  # Only perform action for known gestures
            print(f"Detected gesture: {gesture}, executing action...")
            youtube_controller.execute_action(gesture)
            time.sleep(0.5)  # Small delay to prevent repeated actions

if __name__ == "__main__":
    main()
