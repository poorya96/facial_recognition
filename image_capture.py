import cv2
import os
from datetime import datetime

# Change this to the name of the person you're photographing
PERSON_NAME = "Name"

# IP Camera URL 
IP_CAMERA_URL = "http://IP_Address:Port/video"  # Example for IP Webcam app => 192.168.100.47:8080

def create_folder(name):
    dataset_folder = "dataset"
    if not os.path.exists(dataset_folder):
        os.makedirs(dataset_folder)
    
    person_folder = os.path.join(dataset_folder, name)
    if not os.path.exists(person_folder):
        os.makedirs(person_folder)
    return person_folder

def capture_photos(name):
    folder = create_folder(name)

    # Open the video stream
    cap = cv2.VideoCapture(IP_CAMERA_URL, cv2.CAP_FFMPEG)

    if not cap.isOpened():
        print("Error: Cannot open video stream. Check the URL or network.")
        return

    photo_count = 0
    print(f"Taking photos for {name}. Press SPACE to capture, 'q' to quit.")
    
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to retrieve frame. Exiting...")
            break

        cv2.imshow('Capture', frame)
        
        key = cv2.waitKey(1) & 0xFF
        if key == ord(' '):  # Space key
            photo_count += 1
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{name}_{timestamp}.jpg"
            filepath = os.path.join(folder, filename)
            cv2.imwrite(filepath, frame)
            print(f"Photo {photo_count} saved: {filepath}")
        elif key == ord('q'):  # Q key
            break

    cap.release()
    cv2.destroyAllWindows()
    print(f"Photo capture completed. {photo_count} photos saved for {name}.")

if __name__ == "__main__":
    capture_photos(PERSON_NAME)
