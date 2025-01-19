Gesture Controlled Media Player

This project demonstrates a **gesture-controlled media player** that uses computer vision and hand gesture recognition to control media playback. By leveraging the **MediaPipe Hands module** and **PyAutoGUI**, the application captures real-time hand gestures through a webcam and maps them to specific media control actions such as play, pause, volume adjustment, and navigation.

---

#### Features:
1. **Real-Time Hand Detection:**
   - Utilizes MediaPipe's Hands module for detecting and tracking hand landmarks in real-time.

2. **Gesture-Based Controls:**
   - Recognizes the number of fingers raised and performs corresponding actions:
     - **0 Fingers**: Stop
     - **1 Finger**: Play/Pause
     - **2 Fingers**: Volume Up
     - **3 Fingers**: Volume Down
     - **4 Fingers**: Forward
     - **5 Fingers**: Backward

3. **Webcam Integration:**
   - Streams live video from the user's webcam, processes frames, and overlays detection results.

4. **On-Screen Feedback:**
   - Displays the detected gesture and corresponding action on the screen for user confirmation.

5. **Keyboard Automation:**
   - Sends keystrokes using PyAutoGUI to control media playback.

---

#### Prerequisites:
Ensure you have the following libraries installed:
- **OpenCV**: For accessing the webcam and processing frames.
- **MediaPipe**: For hand tracking and gesture detection.
- **PyAutoGUI**: For simulating keyboard inputs.

Install them using pip:
```bash
pip install opencv-python mediapipe pyautogui
```

---

#### How to Run:
1. Clone this repository:
   ```bash
   git clone <repository_url>
   ```
2. Navigate to the project directory:
   ```bash
   cd <project_directory>
   ```
3. Run the script:
   ```bash
   python gesture_control.py
   ```
4. Use your webcam to interact with the media player through gestures.

---

#### Usage:
- **Start the application** and ensure your hand is visible to the webcam.
- Perform gestures by raising 0 to 5 fingers.
- To **exit** the application, press the **'q'** key.

---

#### Important Notes:
- The application assumes the gestures are performed with a right hand.
- Ensure proper lighting conditions for accurate hand detection.
- Make sure no other application is interfering with the keyboard inputs.

---

#### Future Enhancements:
- Add support for left-hand gesture detection.
- Extend gestures for additional media controls.
- Implement dynamic gesture recognition for custom actions.

Enjoy controlling your media player hands-free! 🎵🎥
