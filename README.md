<div align="center">
  <h1>🌌 EXOSKELETON OS // HAND TRACKER</h1>
  <p><b>Advanced Neural-Network Powered Hand Articulation Tracking</b></p>
</div>

<br>

> **SYS_STATUS:** ONLINE   
> **VERSION:** 2.0.0 (Tasks API Integrated)  
> **INTERFACE:** Python 3.x / OpenCV / MediaPipe  

---

## ⚡ CORE DIRECTIVES

This repository contains the source code for the **Exoskeleton OS Tracker**, a high-performance computer vision application. It utilizes modern AI models to track hand joint landmarks in real-time, overlaying a custom **cyberpunk-styled cybernetic exoskeleton** onto the user's hands via webcam feed.

### 🧬 Key Features
- **Neural Tracking Matrix**: Powered by the modern `MediaPipe Tasks API` natively optimized for ARM architecture.
- **Biometric Overlay**: Projects dynamic neon Cyan connections with solid White energy cores onto bone structures. 
- **Articulated Nodes**: Highlights 21 key articulation points per hand using Purple node markers.
- **Tactile Sensors**: Visually amplifies the 5 fingertips for precision feedback.
- **Tactical HUD**: Integrated Heads-Up Display showing system status, crosshair telemetry, and real-time FPS monitoring.

---

## 🔧 SYSTEM REQUIREMENTS & DEPLOYMENT

### Dependencies
Ensure your environment meets the following specifications to initialize the tracking sequence:
* **Python 3.12** (optimized for macOS ARM64 compatibility)
* `opencv-python`
* `mediapipe`

### Initialization Protocol

1. **Clone the mainframe data:**
   ```bash
   git clone https://github.com/RealTim21/Handtracker.git
   cd Handtracker
   ```

2. **Establish isolated neural environment (Virtual Env):**
   ```bash
   python3.12 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install required augmentations:**
   ```bash
   pip install opencv-python mediapipe
   ```

4. **Acquire the Neural Model:**
   Download the Hand Landmarker `.task` file required for inference:
   ```bash
   curl -O https://storage.googleapis.com/mediapipe-models/hand_landmarker/hand_landmarker/float16/1/hand_landmarker.task
   ```

5. **Execute OS Boot Sequence:**
   ```bash
   python main.py
   ```

---

## 🛑 EMERGENCY OVERRIDE
To safely terminate the visualizer and sever the camera feed, ensure the application window has focus and press the **`q`** key.

---
<div align="center">
  <i>"Upgrading human potential through visual augmentation."</i>
</div>
