import cv2
import mediapipe as mp
import sys
from time import sleep
from pynput.keyboard import Key, Controller
import time
import subprocess
keyboard = Controller()
leftPressed = False
rightPressed = False
upPressed = False
downPressed = False
jumpPressed = False
runPressed = False
startPressed = False
runToggled = True
startTime = 0
jumpTime = 0

cap = cv2.VideoCapture(0)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1,
                       min_detection_confidence=0.5, min_tracking_confidence=0.5)

mp_drawing = mp.solutions.drawing_utils
def toggleMenu():
    if(middleTipy < middle1y < middle0y and ringTipy < ring1y < ring0y):
        if(pointerTipy > pointer1y and pinkyTipy > pinky1y):
            if(abs(thumbTipy - thumb0y) <= 0.1):
                keyboard.release(Key.shift)
                subprocess.Popen(["python", r"C:\Users\smith\Downloads\New folder\GUI_EXPO2.py"])
                sys.exit()

def up():
    global upPressed
    if(pointerTipy <= pointer0y - 0.2):
        if not upPressed:
            keyboard.press('w')
            upPressed = True
    else:
        if upPressed:
            keyboard.release('w')
            upPressed = False

def down():
    global downPressed
    if(pointerTipy >= pointer0y + 0.2):
        if not downPressed:
            keyboard.press('s')
            downPressed = True
    else:
        if downPressed:
            keyboard.release('s')
            downPressed = False

def right():
    global rightPressed
    if(pointerTipx < pointer0x - 0.1):
        if not rightPressed:
            keyboard.press('d')
            rightPressed = True
    else:
        if rightPressed:
            keyboard.release('d')
            rightPressed = False

def left():
    global leftPressed
    if(pointerTipx > pointer0x + 0.08):
        if not leftPressed:
            keyboard.press('a')
            leftPressed = True
    else:
        if leftPressed:
            keyboard.release('a')
            leftPressed = False

def jump():
    global jumpPressed, jumpTime
    if(abs(thumbTipx - pointer1x) >= 0.13 or abs(thumbTipy - pointer1y) >= 0.13):
        if(abs(thumbTipx - thumb0x) >= 0.03 and abs(thumbTipy - thumb0y) >= 0.04):
            if not jumpPressed:
                keyboard.press(' ')
                jumpPressed = True
                jumpTime = time.time()
    if jumpPressed and time.time() - jumpTime >= 0.6:
        keyboard.release(' ')
        jumpPressed = False

def run():
    global runPressed, runToggled

    pinkyRaised = pinkyTipy < pinky0y - 0.1

    # Only toggle if pinky just went up and cooldown has passed
    if pinkyRaised and runToggled:
        runPressed = not runPressed

        if runPressed: 
            keyboard.press(Key.shift)
        else:
            keyboard.release(Key.shift)

    # Update previous state
    runToggled = not pinkyRaised


def start():
    global startPressed, startTime
    pinky = pinkyTipy < pinky2y < pinky1y < pinky0y
    ring = ringTipy < ring2y < ring1y < ring0y
    middle = middleTipy < middle2y < middle1y < middle0y
    pointer = pointerTipy < pointer2y < pointer1y < pointer0y
    thumb = thumbTipy < thumb2y < thumb1y < thumb0y
    handy = middleTipy <= ringTipy < pinkyTipy < thumbTipy
    handx = (pinkyTipx - ringTipx) <= 0.05 and ringTipx - middleTipx <= 0.05
    if(pinky and ring and middle and handy and handx):
        if startPressed == False and (time.time() - startTime) >= 0.5:
            keyboard.press(Key.enter)
            startPressed = True
            startTime = time.time()
    else:
        if startPressed:
            keyboard.release(Key.enter)
            startPressed = False

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

            toggleMenu()
            left()
            right()
            up()
            down()
            jump()
            start()
            run()
                 
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            


cap.release()
cv2.destroyAllWindows() 