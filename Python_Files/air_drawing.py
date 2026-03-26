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
prev_point = None
smooth_point = None

PINCH_ON = 45   # pixels
PINCH_OFF = 70  # pixels

drawing = False

def lerp(p1, p2, t):
    return (int(p1[0] + (p2[0]-p1[0])*t),
            int(p1[1] + (p2[1]-p1[1])*t))

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

        dist = math.hypot(ix - tx, iy - ty)

        # Hysteresis
        if not drawing and dist < PINCH_ON:
            drawing = True
        elif drawing and dist > PINCH_OFF:
            drawing = False
            prev_point = None
            smooth_point = None

        # Strong smoothing
        raw = (ix, iy)
        if smooth_point is None:
            smooth_point = raw
        else:
            smooth_point = (
                int(smooth_point[0]*0.85 + raw[0]*0.15),
                int(smooth_point[1]*0.85 + raw[1]*0.15)
            )

        if drawing:
            if prev_point is not None:
                # interpolate to avoid gaps
                steps = int(math.hypot(smooth_point[0]-prev_point[0],
                                        smooth_point[1]-prev_point[1]) / 2)
                for i in range(steps):
                    p = lerp(prev_point, smooth_point, i/steps)
                    cv2.circle(canvas, p, 2, (0,0,255), -1)
            prev_point = smooth_point
        else:
            prev_point = None

    output = cv2.add(frame, canvas)
    cv2.imshow("Stable Air Draw", output)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()