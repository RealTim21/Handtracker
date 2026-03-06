import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import time

def draw_exoskeleton(image, hand_landmarks_list):
    """Draws a cyberpunk style exoskeleton on detected hands."""
    h, w, c = image.shape
    
    # Standard 21 points of MediaPipe Hand skeleton
    connections = [
        (0,1), (1,2), (2,3), (3,4),       # Thumb
        (0,5), (5,6), (6,7), (7,8),       # Index
        (5,9), (9,10), (10,11), (11,12),  # Middle
        (9,13), (13,14), (14,15), (15,16),# Ring
        (13,17), (0,17), (17,18), (18,19), (19,20) # Pinky & Base
    ]
    
    for landmarks in hand_landmarks_list:
        # Map normalized landmarks to pixel coordinates
        pts = {}
        for idx, lm in enumerate(landmarks):
            pts[idx] = (int(lm.x * w), int(lm.y * h))
            
        # Draw outer glowing lines (Cyan)
        for start, end in connections:
            if start in pts and end in pts:
                cv2.line(image, pts[start], pts[end], (255, 255, 0), 6) # Cyan outer
                cv2.line(image, pts[start], pts[end], (255, 255, 255), 2) # White inner core
                
        # Draw joints (Purple)
        for idx in range(21):
            if idx in pts:
                cv2.circle(image, pts[idx], 6, (255, 0, 255), cv2.FILLED)
                
        # Emphasize fingertips (Yellow)
        fingertips = [4, 8, 12, 16, 20]
        for tip in fingertips:
            if tip in pts:
                cv2.circle(image, pts[tip], 10, (0, 255, 255), cv2.FILLED)

def main():
    print("Initializing modern Exoskeleton OS framework (Tasks API)...")
    
    # Initialize the HandLandmarker builder
    base_options = python.BaseOptions(model_asset_path='hand_landmarker.task')
    options = vision.HandLandmarkerOptions(
        base_options=base_options,
        running_mode=vision.RunningMode.VIDEO,
        num_hands=2,
        min_hand_detection_confidence=0.5,
        min_hand_presence_confidence=0.5,
        min_tracking_confidence=0.5)

    cap = cv2.VideoCapture(0)
    pTime = time.time()
    
    # Start tracking context
    with vision.HandLandmarker.create_from_options(options) as landmarker:
        start_time_ms = int(time.time() * 1000)

        print("\\n>> SYSTEM ONLINE <<")
        print("Press 'q' in the camera window to safely shut down.")
        
        while cap.isOpened():
            success, image = cap.read()
            if not success:
                print("Ignoring empty camera frame or webcam not available.")
                break

            # Process image directly since Hands API needs Timestamp
            current_time_ms = int(time.time() * 1000) - start_time_ms
            
            # Flip image for a selfie-view display
            image = cv2.flip(image, 1)

            # Convert to RGB as MediaPipe expects
            image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=image_rgb)
            
            # Perform tracking
            result = landmarker.detect_for_video(mp_image, current_time_ms)

            # Draw Exoskeleton if hands are found
            if result.hand_landmarks:
                draw_exoskeleton(image, result.hand_landmarks)

            # HUD Elements (Heads Up Display)
            cTime = time.time()
            fps = 5 / (cTime - pTime) if (cTime - pTime) > 0 else 0
            pTime = cTime
            
            # Top Left UI
            cv2.putText(image, 'SYS: ONLINE  v2.0', (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
            cv2.putText(image, f'FPS: {int(fps)}', (20, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2, cv2.LINE_AA)
            
            # Crosshair center UI
            h, w, c = image.shape
            cx, cy = w // 2, h // 2
            cv2.circle(image, (cx, cy), 30, (0, 255, 0), 1)
            cv2.line(image, (cx, cy - 40), (cx, cy + 40), (0, 255, 0), 1)
            cv2.line(image, (cx - 40, cy), (cx + 40, cy), (0, 255, 0), 1)

            # Display image
            cv2.imshow('Exoskeleton OS Tracker', image)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                print("Shutting down Exoskeleton System...")
                break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
