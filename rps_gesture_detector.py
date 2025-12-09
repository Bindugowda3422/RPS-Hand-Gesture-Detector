import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

while True:
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape

    result = hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    gesture = "Show Hand"

    if result.multi_hand_landmarks:
        hand = result.multi_hand_landmarks[0]

        # Get landmark list (x, y)
        lm = [(int(p.x * w), int(p.y * h)) for p in hand.landmark]

        fingers = []

        # Thumb
        fingers.append(1 if lm[4][0] > lm[3][0] else 0)

        # Other fingers
        tips = [8, 12, 16, 20]
        for tip in tips:
            fingers.append(1 if lm[tip][1] < lm[tip - 2][1] else 0)

        total = sum(fingers)

        # Gesture logic
        if total == 0:
            gesture = "Rock"
        elif total == 5:
            gesture = "Paper"
        elif fingers[1] == 1 and fingers[2] == 1 and total == 2:
            gesture = "Scissors"
        elif fingers[1] == 1 and total == 1:
            gesture = "Pencil"

        draw.draw_landmarks(frame, hand, mp_hands.HAND_CONNECTIONS)

    cv2.putText(frame, gesture, (10, 70),
                cv2.FONT_HERSHEY_SIMPLEX, 1.8, (0, 255, 0), 3)

    cv2.imshow("RPS Detector", frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()