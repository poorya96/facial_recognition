Face Recognition with Raspberry Pi Using a Smartphone Camera

Overview

This project implements real-time face recognition on a Raspberry Pi using an IP camera (smartphone camera) as the video source. The system detects faces, matches them with known individuals, and controls a GPIO pin based on authentication status.

Features

Real-time face detection and recognition

Uses a smartphone camera as an IP camera

Controls a GPIO pin (e.g., LED) for authorized faces

Displays FPS (frames per second) for performance monitoring

Requirements

Hardware:

Raspberry Pi (Pi 4, Pi 5, etc.)

LED (optional, for GPIO control)

Software & Libraries:

Python 3

OpenCV (cv2)

face_recognition library

numpy

picamera2 (if using Raspberry Pi Camera)

gpiozero (for GPIO control)

pickle (for storing known face encodings)

An IP camera app on your smartphone (e.g., DroidCam, IP Webcam)

Installation

Install dependencies:

sudo apt update && sudo apt upgrade -y
sudo apt install python3-opencv
pip install face_recognition numpy gpiozero picamera2

Enable camera module on Raspberry Pi:

sudo raspi-config

Go to Interface Options -> Enable Camera

Reboot the Raspberry Pi

Set up the IP Camera:

Install DroidCam (Android) or IP Webcam

Start streaming and note the camera URL (e.g., http://192.168.X.X:4747/video)

Usage

Run the script:

python face_recognition_pi.py

If an authorized face is detected, the LED connected to GPIO 14 will turn ON, otherwise, it will stay OFF.

Press q to exit.

Connecting the LED to GPIO 14

Connect the positive leg (anode) of the LED to GPIO 14.

Connect the negative leg (cathode) to a 330Ω resistor, then to GND.

Customization

Change the IP Camera URL:
Update IP_CAMERA_URL in the script:

IP_CAMERA_URL = "http://192.168.X.X:4747/video"

Add known faces:

Collect images of known people.

Use face_recognition to encode them and save them in encodings.pickle.

Modify authorized users:
Update authorized_names in the script:

authorized_names = ["john", "mary"]  # Case-sensitive

Troubleshooting

If the video does not appear, ensure the IP camera URL is correct and reachable.

If face recognition is slow, reduce the cv_scaler value for performance optimization.

If GPIO does not respond, check your wiring and run the script with sudo.

License

This project is open-source and free to use for educational and personal projects.

