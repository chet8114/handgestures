import cv2
import mediapipe as mp
import pyautogui as p

# Initialize MediaPipe Hands module
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

# Function to count fingers
def count_fingers(hand_landmarks):
    tip_ids = [4, 8, 12, 16, 20]  # Finger tip landmarks
    fingers = []

    # Thumb: Check if the tip is to the left of the previous landmark (for right hand)
    if hand_landmarks.landmark[tip_ids[0]].x < hand_landmarks.landmark[tip_ids[0] - 1].x:
        fingers.append(1)
    else:
        fingers.append(0)

    # Other fingers: Check if the tip is higher than the preceding joint
    for i in range(1, 5):
        if hand_landmarks.landmark[tip_ids[i]].y < hand_landmarks.landmark[tip_ids[i] - 2].y:
            fingers.append(1)
        else:
            fingers.append(0)

    return fingers.count(1)

# Start the webcam feed
cap = cv2.VideoCapture(0)

# Use MediaPipe Hands with high detection and tracking confidence
with mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7) as hands:
    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            print("Error accessing camera!")
            break

        # Flip the frame horizontally for natural interaction
        frame = cv2.flip(frame, 1)

        # Convert the frame to RGB
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(frame_rgb)

        # Initialize variable for detected number of fingers
        num_fingers = -1

        # If hand landmarks are detected, process each hand
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                num_fingers = count_fingers(hand_landmarks)

        # Handle gesture controls based on the number of fingers detected
        if num_fingers == 0:
            cv2.putText(frame, "STOP", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            p.press("space")  # Pause/Play
        elif num_fingers == 1:
            cv2.putText(frame, "PLAY/PAUSE", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            p.press("space")
        elif num_fingers == 2:
            cv2.putText(frame, "VOLUME UP", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            p.press("volumeup")
        elif num_fingers == 3:
            cv2.putText(frame, "VOLUME DOWN", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            p.press("volumedown")
        elif num_fingers == 4:
            cv2.putText(frame, "FORWARD", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            p.press("right")
        elif num_fingers == 5:
            cv2.putText(frame, "BACKWARD", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            p.press("left")

        # Display the output
        cv2.imshow("Gesture Controlled Media Player", frame)

        # Exit on pressing 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
     