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
                       min_detection_confidence=0.5, min_tracking_confidence=0.5)

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
            
            wristy = hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].y
            thumb0y = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_CMC].y
            thumb1y = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_MCP].y
            thumb2y = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP].y
            thumbTipy = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y
            pointer0y = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP].y
            pointer1y = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP].y
            pointer2y = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_DIP].y
            pointerTipy = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y
            middle0y = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP].y
            middle1y = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_PIP].y
            middle2y = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_DIP].y
            middleTipy = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y
            ring0y = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_MCP].y
            ring1y = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_PIP].y
            ring2y = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_DIP].y
            ringTipy = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].y
            pinky0y = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_MCP].y
            pinky1y = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_PIP].y
            pinky2y = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_DIP].y
            pinkyTipy = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].y

            wristx = hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].x
            thumb0x = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_CMC].x
            thumb1x = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_MCP].x
            thumb2x = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP].x
            thumbTipx = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x
            pointer0x = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP].x
            pointer1x = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP].x
            pointer2x = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_DIP].x
            pointerTipx = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x
            middle0x = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP].x
            middle1x = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_PIP].x
            middle2x = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_DIP].x
            middleTipx = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].x
            ring0x = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_MCP].x
            ring1x = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_PIP].x
            ring2x = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_DIP].x
            ringTipx = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].x
            pinky0x = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_MCP].x
            pinky1x = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_PIP].x
            pinky2x = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_DIP].x
            pinkyTipx = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].x


            if (abs(pointerTipy - thumb0y) <= .2):
                pointer1_gesture = 'none'
            elif(pointerTipy < thumb0y):
                pointer1_gesture = 'pointing up'
            elif pointerTipy > thumb0y:
                pointer1_gesture = 'pointing down'
            else:
                pointer1_gesture = 'other'
            
            if (abs(pointerTipx - wristx) <= .2):
                pointer2_gesture = 'none'
            elif(pointerTipx > wristx):
                pointer2_gesture = 'pointing left'
            elif pointerTipx < wristx:
                pointer2_gesture = 'pointing right'
            else:
                pointer2_gesture = 'other'
            
            if (abs(pinkyTipy - pinky0y) <= .15 and abs(pinkyTipx - pinky0x) <= .15):
                pinky_gesture = 'nojump'
            else:
                pinky_gesture = 'jump'
            
            if pointer1_gesture == 'pointing up':
                keyboard.release('s')
                keyboard.press('w')
            elif pointer1_gesture == 'pointing down':
                keyboard.release('w')
                keyboard.press('s')
            elif(pointer1_gesture == 'none'):
                keyboard.release('w')
                keyboard.release('s')
            
            if pointer2_gesture == 'pointing left':
                keyboard.release('d')
                keyboard.press('a')
            elif pointer2_gesture == 'pointing right':
                keyboard.release('a')
                keyboard.press('d')
            elif(pointer2_gesture == 'none'):
                keyboard.release('a')
                keyboard.release('d')
                    
            if pinky_gesture == 'jump':
                pydirectinput.keyDown(' ')
            else:
                 pydirectinput.keyUp(' ')
                 
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break


cap.release()
cv2.destroyAllWindows() 