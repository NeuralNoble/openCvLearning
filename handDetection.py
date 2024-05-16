import cv2,mediapipe as mp

width = 640
height = 480

cap = cv2.VideoCapture(0)
cap.set(3,width)
cap.set(4,height)

mpHands = mp.solutions.hands
hands = mp.solutions.hands.Hands()

mpDraw = mp.solutions.drawing_utils

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    if results.multi_hand_landmarks:
        for handLandmarks in results.multi_hand_landmarks:
            myHand = []
            mpDraw.draw_landmarks(img,handLandmarks,mpHands.HAND_CONNECTIONS)
            for Landmark in handLandmarks.landmark:
                myHand.append((int(Landmark.x*width), int(Landmark.y*height)))
            cv2.circle(img,myHand[4],15,(255,0,0),-1)

    cv2.imshow('img',img)
    cv2.waitKey(1)





