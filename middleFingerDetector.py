import cv2
import mediapipe as mp

# Parameters
width = 640
height = 480

# Initialize video capture
cam = cv2.VideoCapture(0)
cam.set(3, width)
cam.set(4, height)

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5,
                       min_tracking_confidence=0.5)
mp_draw = mp.solutions.drawing_utils


def is_middle_finger_raised(landmarks):
    # Indices for finger landmarks
    tip_ids = [4, 8, 12, 16, 20]

    # Check if middle finger is raised
    middle_finger_raised = landmarks[12].y > landmarks[10].y  # Middle finger tip is above PIP joint
    other_fingers_down = (
        landmarks[8].y > landmarks[6].y and  # Index finger
        landmarks[16].y > landmarks[14].y and  # Ring finger
        landmarks[20].y > landmarks[18].y and  # Pinky finger
        landmarks[4].x < landmarks[3].x if landmarks[4].y > landmarks[2].y else landmarks[4].x > landmarks[3].x  # Thumb
    )
    return middle_finger_raised and other_fingers_down


while True:
    ret, frame = cam.read()
    if not ret:
        break

    # Convert frame to RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process frame with MediaPipe
    results = hands.process(frame_rgb)

    # Draw landmarks and check for middle finger
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            if is_middle_finger_raised(hand_landmarks.landmark):
                cv2.putText(frame, "Middle Finger Detected", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Show frame
    cv2.imshow('frame', frame)

    # Break on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cam.release()
cv2.destroyAllWindows()
