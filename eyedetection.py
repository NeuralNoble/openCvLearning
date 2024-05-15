import cv2,time

width = 640
height = 360

cam = cv2.VideoCapture(0)

cam.set(3, width)
cam.set(4,height)

face_cascade = cv2.CascadeClassifier('haar/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haar/haarcascade_eye.xml')
cTIme = 0
pTime = 0



while True:
    ret, img = cam.read()
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, f"FPS: {int(fps)}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2)
    faces = face_cascade.detectMultiScale(img,1.3,5)
    for face in faces:
        x,y,w,h = face
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)
        roi = img[y:y+h, x:x+w]
        gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        eyes = eye_cascade.detectMultiScale(gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(img[y:y+h, x:x+w],(ex,ey),(ex+ew,ey+eh),(255,0,0),2)
    cv2.imshow('img', img)
    cv2.waitKey(1)
