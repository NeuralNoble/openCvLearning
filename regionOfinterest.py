import cv2 , time , numpy as np

cap = cv2.VideoCapture(0)
wCam, hCam = 640, 480
cap.set(3, wCam)
cap.set(4, hCam)

pTime = 0
cTime = 0

while True:
    sucess , frame = cap.read()
    frameROI = frame[150:210,250:450]
    frameROIGray = cv2.cvtColor(frameROI, cv2.COLOR_BGR2GRAY)
    cv2.imshow('ROI',frameROIGray)
    cv2.moveWindow('ROI',650,0)
    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime
    cv2.putText(frame,'FPS'+ str(int(fps)) , (20,70),cv2.FONT_HERSHEY_SIMPLEX,2,(255,255,255))
    frameROI_resized = cv2.resize(frameROI, (140, 60))
    frame[200:260,300:440] = frameROI_resized
    cv2.imshow('webcam', frame)
    cv2.waitKey(1)


