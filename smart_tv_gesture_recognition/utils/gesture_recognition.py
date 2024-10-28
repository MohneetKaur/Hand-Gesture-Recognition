# gesture_recognition.py
import cv2
import torch
from torchvision import transforms

# Define your PREDICTION_LABEL dictionary
PREDICTION_LABEL = {
    0: "right swipe",
    1: "left swipe",
    2: "thumbs up",
    3: "thumbs down",
    4: "stop gesture"
}

class GestureRecognition:
    def __init__(self, model_path, device="cpu"):
        self.device = device
        self.model = torch.load(model_path, map_location=device)
        self.model.eval()
        self.transform = transforms.Compose([
            transforms.ToPILImage(),
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
        ])

    def recognize_gesture(self, frame):
        # Preprocess the frame and get the prediction
        input_tensor = self.transform(frame).unsqueeze(0).to(self.device)
        with torch.no_grad():
            output = self.model(input_tensor)
            predicted_label = output.argmax(dim=1).item()
        
        return PREDICTION_LABEL.get(predicted_label, "unknown")

    def capture_gesture(self):
        cap = cv2.VideoCapture(0)  # Open default camera
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            
            # Predict gesture
            gesture = self.recognize_gesture(frame)
            cv2.putText(frame, f"Gesture: {gesture}", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            cv2.imshow("Gesture Detection", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

            yield gesture  # Yield detected gesture to be used in main.py

        cap.release()
        cv2.destroyAllWindows()
