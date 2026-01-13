# 🖐 Gesture Controlled Media Player (AI Web App)

An AI-powered web application that allows users to control their media player using simple hand gestures captured through a webcam.
This project combines Computer Vision and Human–Computer Interaction to provide a futuristic, touch-free way to control media playback.

---

## 🚀 Features

* Real-time hand tracking using webcam
* Finger counting with MediaPipe
* Gesture-based control of:

  * ▶ Play / Pause
  * 🔊 Volume Up
  * 🔉 Volume Down
  * ⏩ Forward
  * ⏪ Backward
* Live camera feed inside a web browser
* Beautiful modern UI built with Streamlit
* Gesture icons and visual feedback
* Smooth, non-glitchy gesture detection
* Contactless media control

---

## 🧠 How It Works

The application uses **MediaPipe Hands** to detect hand landmarks from the webcam feed.
The number of raised fingers is calculated from the landmarks, and a corresponding media action is triggered using **PyAutoGUI** to control the system’s media keys.

To avoid accidental toggling, the Play/Pause gesture works only when the hand is closed first and then opened.

### ✋ Gesture Mapping

| Gesture      | Action       |
| ------------ | ------------ |
| ✊ 0 Fingers  | Reset        |
| ☝️ 1 Finger  | Play / Pause |
| ✌️ 2 Fingers | Volume Up    |
| 🤟 3 Fingers | Volume Down  |
| 🖐 4 Fingers | Forward      |
| ✋ 5 Fingers  | Backward     |

---

## 🛠 Tech Stack

* **Python**
* **OpenCV** – Camera and image processing
* **MediaPipe** – Hand landmark detection
* **PyAutoGUI** – System media key control
* **Streamlit** – Web UI and app framework

---

## 📂 Project Structure

Only the necessary project files are included in the repository.

```
gesture-media-control/
│
├── app.py             # Main Streamlit application
├── style.css          # Custom UI styling
├── requirements.txt  # Python dependencies
├── .gitignore         # Files and folders ignored by Git
└── README.md
```

> ⚠️ The virtual environment (`venv/`) is intentionally not included.
> It is recreated locally using `requirements.txt`.

---

## ▶ How to Run Locally

1. Clone the repository:

```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
```

2. Create a virtual environment (recommended):

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the app:

```bash
streamlit run app.py
```

5. Open the browser and allow camera access.

---

## 🌐 Deployment (Free)

This app can be deployed on **Streamlit Cloud**.

Steps:

1. Push this repository to GitHub
2. Go to [https://share.streamlit.io](https://share.streamlit.io)
3. Sign in with GitHub
4. Select this repository
5. Choose `app.py` as the main file
6. Click **Deploy**

You will get a public link to share your live AI app.

---

## 🎯 Use Cases

* Touch-free media control
* Smart TV and PC interaction
* Accessibility support
* AI-based human–computer interaction
* Computer vision demos

---

## 👨‍💻 Author

**Chethan**
Computer Science Engineer | AI & Computer Vision Enthusiast

This project was built to demonstrate real-time AI-powered gesture control using modern computer vision techniques.

