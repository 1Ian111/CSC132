#Make Distance Hip Related!!!
#Make Distance Hip Related!!!
#Make Distance Hip Related!!!
import cv2
import sys
import mediapipe as mp
import time
from pynput.keyboard import Key, Controller
import Out_of_Bounds
import subprocess
keyboard = Controller()
OOB = Out_of_Bounds.OutOfBoundsWindow()
buttonA = False
buttonB = False
buttonX = False
buttonY = False
rAnalogUp = False
rAnalogDown = False
rAnalogLeft = False
rAnalogRight = False
lAnalogUp = False
lAnalogDown = False
lAnalogLeft = False
lAnalogRight = False
dpadUp = False
dpadDown = False
dpadLeft = False
dpadRight = False
correctPosition = True
oldPosition = False
startPressed = False
delayPosition = True
resetKeys = False
jumpTime = 0
startTime = 0
prevKneeL = 0
prevKneeR = 0
currentMessage = ""
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_FPS, 30)

mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils
pose = mp_pose.Pose(static_image_mode=False, model_complexity=0)

def checkPosition():
    global currentMessage, correctPosition, oldPosition
    oldPosition = correctPosition
    correctPosition = True
    if(abs(lshoulderx - rshoulderx) > .15):
        if(currentMessage == "Too Close"):
            pass
        else:
            print("Too Close")
        currentMessage = "Too Close"
        correctPosition = False
    if(lshoulderx >= .8):
        if(currentMessage == "Too Far Left"):
            pass
        else:
            print("Too Far Left")
        currentMessage = "Too Far Left"
        correctPosition = False
    if(rshoulderx <= .2):
        if(currentMessage == "Too Far Right"):
            pass
        else:
            print("Too Far Right")
        currentMessage = "Too Far Right"
        correctPosition = False
    if correctPosition == True:
        if(currentMessage == "Just Right!"):
            pass
        else:
            print("Just Right!")
        currentMessage = "Just Right!"
    return correctPosition
def toggleMenu():
    if(abs(lelbowx - relbowx) <= .05 and abs(lelbowy - relbowy) <= .04 and abs(lwristy - rwristy) <= .1 and abs(lwristx - rwristx) >= .05 and abs(lelbowx - nosex) <=.2 and abs(relbowx - nosex) <=.2):
        if(-.1 < (lwristy - lelbowy) < -.05 and -.1 < (lwristy - relbowy) < -.05):
            if(-.1 < (rwristy - lelbowy) < -.05 and -.1 < (rwristy - relbowy) < -.05):
                subprocess.Popen(["python", r"C:\Users\smith\Downloads\New folder\GUI_EXPO2.py"])
                sys.exit()
def buttons():
    global buttonA, buttonB, buttonX, buttonY, prevKneeL, prevKneeR, jumpTime
    #Presses A button on controller
    def buttona():
        global buttonA, jumpTime
        if(abs(lwristx - rshoulderx) <= 0.15 and abs(lwristy - rshouldery) <= 0.15):
            if not buttonA:
                keyboard.press('z')
                buttonA = True
                jumpTime = time.time()
        #elif(abs(rthumbx - rshoulderx) <= 0.2 and abs(rthumby - rshouldery) <= 0.2):
        #    if not buttonA:
        #        keyboard.press('z')
        #        buttonA = True
        else:
            # Release after .6 seconds
            if buttonA and (time.time() - jumpTime >= .6):
                keyboard.release('z')
                buttonA = False
    #Presses B button on controller
    def buttonb():
        global buttonB
        #if(abs(lthumbx - lshoulderx) <= 0.2 and abs(lthumby - lshouldery) <= 0.2):
        #    if not buttonB:
        #        keyboard.press('x')
        #        buttonB = True
        if(abs(rwristx - lshoulderx) <= 0.15 and abs(rwristy - lshouldery) <= 0.15):
            if not buttonB:
                keyboard.press('x')
                buttonB = True
        else:
            if buttonB:
                keyboard.release('x')
                buttonB = False
    #Presses X button on controller
    def buttonx():
        global buttonX
        if(abs(lthumbx - rhipx) <= 0.1 and abs(lthumby - rhipy) <= 0.1):
            if not buttonX:
                keyboard.press('c')
                buttonX = True
        elif(abs(rthumbx - rhipx) <= 0.1 and abs(rthumby - rhipy) <= 0.1):
            if not buttonX:
                keyboard.press('c')
                buttonX = True
        else:
            if buttonX:
                keyboard.release('c')
                buttonX = False
    #Presses Y button on controller
    def buttony():
        global buttonY
        if(abs(lthumbx - lshoulderx) <= 0.1 and abs(lthumby - lshouldery) <= 0.1):
            if not buttonY:
                keyboard.press('v')
                buttonY = True
        elif(abs(rthumbx - lshoulderx) <= 0.1 and abs(rthumby - lshouldery) <= 0.1):
            if not buttonY:
                keyboard.press('v')
                buttonY = True
        else:
            if buttonY:
                keyboard.release('v')
                buttonY = False
    #Alternate way to press the A button on controller
    def jump():
        global prevKneeL, prevKneeR, buttonA, jumpTime
        if not buttonA and (lfootindy - prevKneeL) >= 0.02 and (rfootindy - prevKneeR) >= 0.02:
            keyboard.press('z')
            buttonA = True
            jumpTime = time.time()

        # Release after .6 seconds
        if buttonA and (time.time() - jumpTime >= .6):
            keyboard.release('z')
            buttonA = False
        prevKneeL = lfootindy
        prevKneeR = rfootindy
    buttona()
    buttonb()
    buttonx()
    buttony()
    jump()
        
#Controls analog stick directions
def lanalog():
    global lAnalogDown, lAnalogLeft, lAnalogRight, lAnalogUp
    #Presses analog stick up on controller
    def lanalogup():
        global lAnalogUp
        if(.12 < abs(lshoulderx - rshoulderx) < .15):
            if not lAnalogUp:
                keyboard.press('w')
                lAnalogUp = True
        else:
            if lAnalogUp:
                keyboard.release('w')
                lAnalogUp = False
    #Presses analog stick down on controller
    def lanalogdown():
        global lAnalogDown
        if(abs(lshoulderx - rshoulderx) <= 0.09):
            if not lAnalogDown:
                keyboard.press('s')
                lAnalogDown = True
        else:
            if lAnalogDown:
                keyboard.release('s')
                lAnalogDown = False
    #Presses analog stick right on controller
    def lanalogright():
        global lAnalogRight
        if rhipx <= 0.4:
            if not lAnalogRight:
                keyboard.press('d')
                lAnalogRight = True
        else:
            if lAnalogRight:
                keyboard.release('d')
                lAnalogRight = False
    #Presses analog stick left on controller
    def lanalogleft():
        global lAnalogLeft
        if lhipx >= 0.6:
            if not lAnalogLeft:
                keyboard.press('a')
                lAnalogLeft = True
        else:
            if lAnalogLeft:
                keyboard.release('a')
                lAnalogLeft = False
    lanalogup()
    lanalogdown()
    lanalogright()
    lanalogleft()

#Presses D-pad up on the controller
def dpad():
    global dpadUp, dpadDown, dpadLeft, dpadRight
    leftBox = (lshoulderx + lhipx)/2
    rightBox = (rshoulderx + rhipx)/2
    topBox = (lshouldery + rshouldery)/2
    bottomBox = (lhipy + rhipy)/2
    midPointy = (topBox + bottomBox)/2
    midPointx = (leftBox + rightBox)/2
    wristx = (lwristx + rwristx)/2
    wristy = (lwristy + rwristy)/2
    if(abs(lwristx - rwristx) <= 0.05 and abs(lwristy - rwristy) <= 0.05):
        if(rightBox < wristx < leftBox and topBox < wristy < bottomBox):
            #Presses the D-pad up on the controller
            def dpadup():
                global dpadUp
                if(topBox < wristy < (midPointy - .05)):
                    if not dpadUp:
                        keyboard.press(Key.up)
                        dpadUp = True
            #Presses the D-pad down on the controller
            def dpaddown():
                global dpadDown
                if(midPointy + .05 < wristy < bottomBox):
                    if not dpadDown:
                        keyboard.press(Key.down)
                        dpadDown = True
            #Presses the D-pad left on the controller
            def dpadleft():
                global dpadLeft
                if(leftBox < wristx < midPointx - 0.05):
                    if not dpadLeft:
                        keyboard.press(Key.left)
                        dpadLeft = True
            #Presses the D-pad right on the controller
            def dpadright():
                global dpadRight
                if(midPointx + 0.05 < wristx < rightBox):
                    if not dpadRight:
                        keyboard.press(Key.right)
                        dpadRight = True
            dpadup()
            dpaddown()
            dpadleft()
            dpadright()
    else:
        if(dpadUp == True or dpadDown == True or dpadLeft == True or dpadRight == True):
            dpadUp = False
            dpadDown = False
            dpadLeft = False
            dpadRight = False
            keyboard.release(Key.up)
            keyboard.release(Key.down)
            keyboard.release(Key.left)
            keyboard.release(Key.right)


#Controls the right analog stick on controller
def ranalog():
    global rAnalogDown, rAnalogUp, rAnalogLeft, rAnalogRight
    #Presses right analog stick down on controller
    def ranalogdown():
        global rAnalogDown
        if(abs(nosey - ((lshouldery + rshouldery)/2)) <= 0.02):
            if not rAnalogDown:
                keyboard.press('k')
                rAnalogDown = True
        else:
            if rAnalogDown:
                keyboard.release('k')
                rAnalogDown = False
    #Presses right analog stick up on controller
    def ranalogup():
        global rAnalogUp
        if(abs(nosey - ((lshouldery + rshouldery)/2)) >= 0.15):
            if not rAnalogUp:
                keyboard.press('i')
                rAnalogUp = True
        else:
            if rAnalogUp:
                keyboard.release('i')
                rAnalogUp = False
    #Presses right analog stick left on controller
    def ranalogleft():
        global rAnalogLeft
        if(abs(nosex - lshoulderx) <= 0.05):
            if not rAnalogLeft:
                keyboard.press('j')
                rAnalogLeft = True
        else:
            if rAnalogLeft:
                keyboard.release('j')
                rAnalogLeft = False
    #Presses right analog stick right on controller
    def ranalogright():
        global rAnalogRight
        if(abs(nosex - rshoulderx) <= 0.05):
            if not rAnalogRight:
                keyboard.press('l')
                rAnalogRight = True
        else:
            if rAnalogRight:
                keyboard.release('l')
                rAnalogRight = False
    ranalogup()
    ranalogdown()
    ranalogleft()
    ranalogright()

#Presses start button on controller
def start():
    global startPressed, startTime
    if(abs(lindexy - rindexy) <= .1 and abs(lwristy - rwristy) <= .1 and abs(rwristx - lwristx) > .4):
        if startPressed == False and (time.time() - startTime) >= 0.5:
            keyboard.press(Key.enter)
            startPressed = True
            startTime = time.time()
    else:
        if startPressed:
            keyboard.release(Key.enter)
            startPressed = False

def resetkeys():
    global resetKeys
    if(resetKeys == True):
        keyboard.release('z')
        keyboard.release('x')
        keyboard.release('c')
        keyboard.release('v')
        keyboard.release(Key.up)
        keyboard.release(Key.down)
        keyboard.release(Key.left)
        keyboard.release(Key.right)
        keyboard.release('i')
        keyboard.release('j')
        keyboard.release('k')
        keyboard.release('l')
        keyboard.release('w')
        keyboard.release('a')
        keyboard.release('s')
        keyboard.release('d')
    resetKeys = False

while True:
    ret, frame = cap.read()
    cv2.imshow("Hand Gesture", frame)
    if not ret:
        break

    image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = pose.process(image_rgb)

    if results.pose_landmarks:
        mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        nosex = results.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].x
        leyeinx = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_EYE_INNER].x
        leyex = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_EYE].x
        leyeoutx = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_EYE_OUTER].x
        reyeinx = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_EYE_INNER].x
        reyex = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_EYE].x
        reyeoutx = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_EYE_OUTER].x
        learx = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_EAR].x
        rearx = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_EAR].x
        lmouthx = results.pose_landmarks.landmark[mp_pose.PoseLandmark.MOUTH_LEFT].x
        rmouthx = results.pose_landmarks.landmark[mp_pose.PoseLandmark.MOUTH_RIGHT].x
        lshoulderx = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER].x
        rshoulderx = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER].x
        lelbowx = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_ELBOW].x
        relbowx = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ELBOW].x
        lwristx = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_WRIST].x
        rwristx = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST].x
        lpinkyx = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_PINKY].x
        rpinkyx = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_PINKY].x
        lindexx = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_INDEX].x
        rindexx = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_INDEX].x
        lthumbx = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_THUMB].x
        rthumbx = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_THUMB].x
        lhipx = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_HIP].x
        rhipx = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_HIP].x
        lkneex = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_KNEE].x
        rkneex = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_KNEE].x
        lanklex = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_ANKLE].x
        ranklex = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ANKLE].x
        lheelx = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_HEEL].x
        rheelx = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_HEEL].x
        lfootindx = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_FOOT_INDEX].x
        rfootindx = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_FOOT_INDEX].x

        nosey = results.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].y
        leyeiny = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_EYE_INNER].y
        leyey = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_EYE].y
        leyeouty = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_EYE_OUTER].y
        reyeiny = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_EYE_INNER].y
        reyey = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_EYE].y
        reyeouty = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_EYE_OUTER].y
        leary = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_EAR].y
        reary = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_EAR].y
        lmouthy = results.pose_landmarks.landmark[mp_pose.PoseLandmark.MOUTH_LEFT].y
        rmouthy = results.pose_landmarks.landmark[mp_pose.PoseLandmark.MOUTH_RIGHT].y
        lshouldery = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER].y
        rshouldery = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER].y
        lelbowy = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_ELBOW].y
        relbowy = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ELBOW].y
        lwristy = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_WRIST].y
        rwristy = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST].y
        lpinkyy = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_PINKY].y
        rpinkyy = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_PINKY].y
        lindexy = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_INDEX].y
        rindexy = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_INDEX].y
        lthumby = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_THUMB].y
        rthumby = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_THUMB].y
        lhipy = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_HIP].y
        rhipy = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_HIP].y
        lkneey = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_KNEE].y
        rkneey = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_KNEE].y
        lankley = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_ANKLE].y
        rankley = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ANKLE].y
        lheely = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_HEEL].y
        rheely = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_HEEL].y
        lfootindy = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_FOOT_INDEX].y
        rfootindy = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_FOOT_INDEX].y

        #hugging left wrist -.03, right writst -.01
        #X left wrist -.09, right wrist -.085
        #if checkPosition():
            #print("left wrist elbow " + str(lwristy - lelbowy))
            #print("right wrist elbow " + str(rwristy - lelbowy))
        #Left Low Right High
        toggleMenu()
        if checkPosition() == True:
            if(oldPosition == False):
                OOB.hide()
            buttons()
            lanalog()
            ranalog()
            dpad()
            start()
            resetKeys = True
        else:
            OOB.show()
            resetkeys()
                 
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


cap.release()
cv2.destroyAllWindows() 