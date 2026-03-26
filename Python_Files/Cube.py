import cv2
import mediapipe as mp
import numpy as np
import math

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    max_num_hands=1,
    model_complexity=0,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

# ----- Cube definition (3D) -----
CUBE_SIZE = 120
original_size = CUBE_SIZE

cube_points = np.array([
    [-1, -1, -1],
    [ 1, -1, -1],
    [ 1,  1, -1],
    [-1,  1, -1],
    [-1, -1,  1],
    [ 1, -1,  1],
    [ 1,  1,  1],
    [-1,  1,  1]
], dtype=float)

edges = [
    (0,1),(1,2),(2,3),(3,0),
    (4,5),(5,6),(6,7),(7,4),
    (0,4),(1,5),(2,6),(3,7)
]

angle_x = 0
angle_y = 0
scale = 1.0

center_x = 320
center_y = 240

PINCH_MIN = 30
PINCH_MAX = 160

def project(points):
    projected = []
    for x,y,z in points:
        factor = 400 / (400 + z)
        px = int(x * factor + center_x)
        py = int(y * factor + center_y)
        projected.append((px, py))
    return projected

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame,1)
    h,w,_ = frame.shape

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    hand_present = False

    if result.multi_hand_landmarks:
        hand_present = True
        lm = result.multi_hand_landmarks[0].landmark

        # Hand center
        hx = lm[9].x * w
        hy = lm[9].y * h

        # Normalize rotation by screen
        angle_y = (hx - w/2) / w * math.pi
        angle_x = (hy - h/2) / h * math.pi

        # Pinch for scaling
        ix, iy = lm[8].x*w, lm[8].y*h
        tx, ty = lm[4].x*w, lm[4].y*h
        pinch = math.hypot(ix-tx, iy-ty)

        scale = np.interp(pinch, [PINCH_MIN, PINCH_MAX], [0.5, 2.0])
        scale = max(0.5, min(scale, 2.0))

    # Reset if no hand
    if not hand_present:
        angle_x *= 0.9
        angle_y *= 0.9
        scale += (1.0 - scale) * 0.1

    # ----- Transform cube -----
    transformed = []
    for p in cube_points:
        x,y,z = p * CUBE_SIZE * scale

        # rotate X
        y2 = y * math.cos(angle_x) - z * math.sin(angle_x)
        z2 = y * math.sin(angle_x) + z * math.cos(angle_x)

        # rotate Y
        x3 = x * math.cos(angle_y) + z2 * math.sin(angle_y)
        z3 = -x * math.sin(angle_y) + z2 * math.cos(angle_y)

        transformed.append([x3,y2,z3])

    projected = project(transformed)

    # Draw cube
    for e in edges:
        p1 = projected[e[0]]
        p2 = projected[e[1]]
        cv2.line(frame, p1, p2, (255,0,0), 3)

    cv2.imshow("3D Cube Control", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()