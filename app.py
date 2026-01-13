import os
import streamlit as st
import numpy as np

# ===============================
# Detect Streamlit Cloud
# ===============================
IS_CLOUD = os.getenv("STREAMLIT_CLOUD") == "1"


if not IS_CLOUD:
    import cv2
    import mediapipe as mp
    import pyautogui as p

# ===============================
# PAGE CONFIG
# ===============================
st.set_page_config(page_title="Gesture Media Control", layout="wide")

# ===============================
# LOAD CSS
# ===============================
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ===============================
# TITLE
# ===============================
st.markdown('<div class="title">🖐 Gesture Controlled Media Player</div>', unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

# ===============================
# UI
# ===============================
col1, col2 = st.columns([1, 2])

with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🎮 Controls")
    start = st.button("▶ Start Camera")
    stop = st.button("⏹ Stop Camera")
    about = st.button("ℹ️ About This App")

    st.markdown("### ✋ Gestures")
    st.write("✊ 0 Fingers → Reset")
    st.write("☝️ 1 Finger → Play / Pause")
    st.write("✌️ 2 Fingers → Volume Up")
    st.write("🤟 3 Fingers → Volume Down")
    st.write("🖐 4 Fingers → Forward")
    st.write("✋ 5 Fingers → Backward")
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("📸 Live Camera")
    FRAME_WINDOW = st.image([])
    gesture_box = st.empty()
    st.markdown("</div>", unsafe_allow_html=True)

# ===============================
# GESTURE ICON UI
# ===============================
def show_gesture(icon, text):
    gesture_box.markdown(
        f"""
        <div style="text-align:center;font-size:60px;font-weight:bold;
                    color:#00f5ff;text-shadow:0 0 20px #00f5ff;">
            {icon}<br>
            <span style="font-size:28px;">{text}</span>
        </div>
        """,
        unsafe_allow_html=True
    )

# ===============================
# CLOUD MODE
# ===============================
if IS_CLOUD:
    show_gesture("☁️", "Cloud Demo Mode")
    st.info("🚀 This is a UI demo on Streamlit Cloud. Run locally to use webcam & gestures.")

# ===============================
# LOCAL MODE (Full AI)
# ===============================
if not IS_CLOUD:

    mp_hands = mp.solutions.hands
    mp_draw = mp.solutions.drawing_utils

    def count_fingers(hand_landmarks):
        tip_ids = [4, 8, 12, 16, 20]
        fingers = []

        if hand_landmarks.landmark[tip_ids[0]].x < hand_landmarks.landmark[tip_ids[0] - 1].x:
            fingers.append(1)
        else:
            fingers.append(0)

        for i in range(1, 5):
            if hand_landmarks.landmark[tip_ids[i]].y < hand_landmarks.landmark[tip_ids[i] - 2].y:
                fingers.append(1)
            else:
                fingers.append(0)

        return fingers.count(1)

    if "play_allowed" not in st.session_state:
        st.session_state.play_allowed = True

    if start:
        cap = cv2.VideoCapture(0)

        with mp_hands.Hands(min_detection_confidence=0.7,
                            min_tracking_confidence=0.7) as hands:

            while cap.isOpened():
                success, frame = cap.read()
                if not success:
                    st.error("Camera not working")
                    break

                frame = cv2.flip(frame, 1)
                rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                results = hands.process(rgb)

                num_fingers = -1

                if results.multi_hand_landmarks:
                    for hand_landmarks in results.multi_hand_landmarks:
                        mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                        num_fingers = count_fingers(hand_landmarks)

                # State
                if num_fingers == 0:
                    st.session_state.play_allowed = True
                    show_gesture("✊", "READY")
                elif num_fingers > 1:
                    st.session_state.play_allowed = False

                # Actions
                if num_fingers == 1:
                    show_gesture("☝️", "PLAY / PAUSE")
                    if st.session_state.play_allowed:
                        p.press("space")
                        st.session_state.play_allowed = False

                elif num_fingers == 2:
                    show_gesture("✌️", "VOLUME UP")
                    p.press("volumeup")

                elif num_fingers == 3:
                    show_gesture("🤟", "VOLUME DOWN")
                    p.press("volumedown")

                elif num_fingers == 4:
                    show_gesture("🖐", "FORWARD")
                    p.press("right")

                elif num_fingers == 5:
                    show_gesture("✋", "BACKWARD")
                    p.press("left")

                FRAME_WINDOW.image(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

                if stop:
                    cap.release()
                    break

# ===============================

# ===============================
# ABOUT POPUP
# ===============================
if about:
    st.markdown(
        """
        <div style="background:rgba(0,0,0,0.85);padding:30px;border-radius:20px;
                    box-shadow:0 0 30px #00f5ff;color:white;text-align:center;">
            <h2 style="color:#00f5ff;">🖐 Gesture Controlled Media Player</h2>
            <p>This AI-powered web app lets you control media using hand gestures.</p>
            <p>Built with <b>MediaPipe</b>, <b>OpenCV</b>, <b>PyAutoGUI</b> and <b>Streamlit</b>.</p>
            <p style="margin-top:20px;font-weight:bold;
                      background:linear-gradient(90deg,#00f5ff,#00c3ff,#7f7cff);
                      -webkit-background-clip:text;color:transparent;
                      text-shadow:0 0 15px rgba(0,195,255,0.8);">
                Created by Chethan Karnati🚀
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
