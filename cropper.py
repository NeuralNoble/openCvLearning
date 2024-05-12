import cv2
import numpy as np

img  = cv2.imread('dog.jpeg')

flag = False
ix = -1
iy = -1

def crop(event,x,y,flags,param):

    global ix,iy,flag

    if event ==1:
        flag = True;
        ix = x
        iy = y




    elif event == 4:
        flag = False
        fx=x
        fy = y
        cv2.rectangle(img, pt1=(ix, iy), pt2=(x, y), thickness=1, color=(0, 0, 0))
        cropped =  img[iy:fy,ix:fx]
        cv2.imshow('result',cropped)
        cv2.waitKey(0)


cv2.namedWindow(winname="cropper")
cv2.setMouseCallback("cropper",crop)

while True:
    cv2.imshow("cropper",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cv2.destroyWindow()