import cv2
import mediapipe as mp
from time import sleep
from pynput.keyboard import Key, Controller
import pyautogui
import pydirectinput
keyboard = Controller()


cap = cv2.VideoCapture(0)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1,
                       min_detection_confidence=0.7, min_tracking_confidence=0.7)

mp_drawing = mp.solutions.drawing_utils

while True:
    ret, frame = cap.read()
    cv2.imshow("Hand Gesture", frame)
    if not ret:
        break

    image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = hands.process(image_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:

            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
            pointerTipy = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y
            pointerTipx = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x
            thumbTipy = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y
            thumbTipx = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x
            pointer1y = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP].y
            pointer1x = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP].x

            pointerY = pointerTipy * 1080
            pointerX = (abs(1 - pointerTipx)) * 1920
            
            pyautogui.moveTo(pointerX, pointerY)

            if (abs(thumbTipy - pointer1y) >= .15 or abs(thumbTipx - pointer1x) >= .15):
                pyautogui.click()
                 
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break


cap.release()
cv2.destroyAllWindows() 