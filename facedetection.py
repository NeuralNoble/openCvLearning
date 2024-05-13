import cv2,numpy as np

width = 640
height = 360

cap = cv2.VideoCapture(0)
cap.set(3,width)
cap.set(4,height)

face_cascade = cv2.CascadeClassifier('haar/haarcascade_frontalface_default.xml')


while True:
    ret, frame = cap.read()
    frameGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(frameGray, 1.3,5)
    # for face in faces:
    #     x, y, w, h = face
    #     cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0),2)

    for (x, y, w, h) in faces:

        for i in range(y, y + h, 10):
            cv2.line(frame, (x, i), (x + w, i), (255, 0, 0), 1)

        for i in range(x, x + w, 10):
            cv2.line(frame, (i, y), (i, y + h), (255, 0, 0), 1)

    cv2.imshow('frame',frame)

    cv2.moveWindow('frame',0,0)
    cv2.waitKey(1)
