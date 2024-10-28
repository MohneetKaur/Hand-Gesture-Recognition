from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service  # Import Service for ChromeDriver
import time

class YouTubeController:
    def __init__(self, driver_path):
        # Initialize the Service with the path to ChromeDriver
        service = Service(driver_path)
        self.driver = webdriver.Chrome(service=service)  # Pass service instead of executable_path
        self.driver.get('https://youtu.be/4dsFQFCvVGU?list=RDtgtLnxBNS2s')  # Replace with desired video ID
        time.sleep(5)  # Allow time for YouTube to load

    def execute_action(self, gesture_label):
        # Map gesture labels to YouTube actions
        if gesture_label == "right swipe":
            self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.SHIFT + "n")  # Next video
        elif gesture_label == "left swipe":
            self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.SHIFT + "p")  # Previous video
        elif gesture_label == "thumbs up":
            # Increase video volume by 10%
            self.driver.execute_script(
                "document.querySelector('video').volume = Math.min(1, document.querySelector('video').volume + 0.1);"
            )
        elif gesture_label == "thumbs down":
            # Decrease video volume by 10%
            self.driver.execute_script(
                "document.querySelector('video').volume = Math.max(0, document.querySelector('video').volume - 0.1);"
            )
        elif gesture_label == "stop gesture":
            # Toggle play/pause using "k" key
            self.driver.find_element(By.TAG_NAME, "body").send_keys("k")
