# Rock-Paper-Scissors Hand Gesture Detector

This project uses **OpenCV** and **MediaPipe** to detect hand gestures in real time using a webcam.  
It recognizes the following gestures:
- ✊ Rock  
- ✋ Paper  
- ✌️ Scissors  
- ✏️ Pencil (index finger only)

## Tech Stack

- Python  
- OpenCV (Computer Vision)  
- MediaPipe Hands (Hand Landmark Detection)

## How to Run

1. Install the required libraries:
   pip install -r requirements.txt

2. Run the script:
   python rps_gesture_detector.py

3. Press `q` to close the program.

## Project Structure

rps_gesture_detector.py   → Main program  
requirements.txt          → Required libraries  
README.md                 → Project documentation

## Features

- Real-time hand tracking using webcam  
- Detects Rock, Paper, Scissors, and Pencil gestures  
- Uses MediaPipe’s 21 hand landmarks  
- Lightweight and easy to run  
- Beginner-friendly project for AI/ML portfolios
