import cv2
import mediapipe as mp
import numpy as np
import random
import math

# MediaPipe setup
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=2)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

# Particle cube
NUM_PARTICLES = 300
particles = []

for _ in range(NUM_PARTICLES):
    particles.append([
        random.randint(200, 440),
        random.randint(140, 340),
        random.uniform(-1, 1),
        random.uniform(-1, 1)
    ])

def distance(p1, p2):
    return math.hypot(p1[0]-p2[0], p1[1]-p2[1])

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    explode = False
    spread_force = 0

    if result.multi_hand_landmarks and len(result.multi_hand_landmarks) == 2:
        hand1 = result.multi_hand_landmarks[0]
        hand2 = result.multi_hand_landmarks[1]

        x1 = int(hand1.landmark[mp_hands.HandLandmark.WRIST].x * w)
        y1 = int(hand1.landmark[mp_hands.HandLandmark.WRIST].y * h)
        x2 = int(hand2.landmark[mp_hands.HandLandmark.WRIST].x * w)
        y2 = int(hand2.landmark[mp_hands.HandLandmark.WRIST].y * h)

        d = distance((x1, y1), (x2, y2))
        spread_force = min(d / 100, 5)

        # middle finger check (simple)
        tip = hand1.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y
        pip = hand1.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_PIP].y

        if tip < pip:
            explode = True

        mp_draw.draw_landmarks(frame, hand1, mp_hands.HAND_CONNECTIONS)
        mp_draw.draw_landmarks(frame, hand2, mp_hands.HAND_CONNECTIONS)

    # Particle logic
    for p in particles:
        if explode:
            angle = random.uniform(0, 2*math.pi)
            p[2] = math.cos(angle) * 10
            p[3] = math.sin(angle) * 10
        else:
            p[2] += random.uniform(-spread_force, spread_force)
            p[3] += random.uniform(-spread_force, spread_force)

        p[0] += p[2]
        p[1] += p[3]

        cv2.circle(frame, (int(p[0]), int(p[1])), 2, (0, 255, 255), -1)

    cv2.imshow("Particle Cube", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()