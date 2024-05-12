import cv2, time , numpy as np

cam = cv2.VideoCapture(0)
width = 640
height = 360
snipWidth = 120
snipHeight = 60
boxCR = width//2
boxCC = height//2

deltaRow , deltaCol =2,2


cam.set(3, width)
cam.set(4, height)



while True:
    sucsess , frame = cam.read()
    frameROI = frame[boxCR-snipHeight//2:boxCR+snipHeight//2,boxCC-snipWidth//2:boxCC+snipWidth//2]
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)
    frame[boxCR - snipHeight // 2:boxCR + snipHeight // 2, boxCC - snipWidth // 2:boxCC + snipWidth // 2]=frameROI
    if boxCR - snipHeight//2 <=0 or boxCR+snipHeight//2 >=height:
        deltaRow = deltaRow *(-1)

    if boxCC - snipWidth//2 <=0 or boxCC+snipWidth >=width:
        deltaCol = deltaCol *(-1)


    boxCR = boxCR + deltaRow
    boxCC = boxCC + deltaCol


    cv2.imshow('webcam',frame)
    cv2.waitKey(1)


