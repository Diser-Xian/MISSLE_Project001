import cv2
import mediapipe as mp
import numpy as np
import math

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    max_num_hands=1,
    model_complexity=0,
    min_detection_confidence=0.8,
    min_tracking_confidence=0.8
)

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

canvas = None
smooth_point = None

PINCH_ON = 45
PINCH_OFF = 70
drawing = False

CUBE_SIZE = 10
SPAWN_DIST = 12  # distance before placing next cube
last_spawn = None

def distance(p1, p2):
    return math.hypot(p1[0]-p2[0], p1[1]-p2[1])

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape

    if canvas is None:
        canvas = np.zeros_like(frame)

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    if result.multi_hand_landmarks:
        lm = result.multi_hand_landmarks[0].landmark

        ix = int(lm[8].x * w)
        iy = int(lm[8].y * h)
        tx = int(lm[4].x * w)
        ty = int(lm[4].y * h)

        dist = distance((ix,iy), (tx,ty))

        # pinch hysteresis
        if not drawing and dist < PINCH_ON:
            drawing = True
            last_spawn = None
        elif drawing and dist > PINCH_OFF:
            drawing = False
            last_spawn = None
            smooth_point = None

        raw = (ix, iy)
        if smooth_point is None:
            smooth_point = raw
        else:
            smooth_point = (
                int(smooth_point[0]*0.85 + raw[0]*0.15),
                int(smooth_point[1]*0.85 + raw[1]*0.15)
            )

        if drawing:
            if last_spawn is None or distance(smooth_point, last_spawn) > SPAWN_DIST:
                x = smooth_point[0] - CUBE_SIZE//2
                y = smooth_point[1] - CUBE_SIZE//2
                cv2.rectangle(canvas, (x,y), (x+CUBE_SIZE, y+CUBE_SIZE), (0,0,255), -1)
                last_spawn = smooth_point

    output = cv2.add(frame, canvas)
    cv2.imshow("Air Cube Draw", output)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()