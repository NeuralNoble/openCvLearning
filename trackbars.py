import cv2

width = 640
height = 360
def callback1(val):
    global xpos
    print(val)
    xpos = val

def callback2(val):
    global ypos
    print(val)
    ypos = val
def callback3(val):
    global rad
    print(val)
    rad = val

xpos = 50
ypos = 50
rad = 25
cap = cv2.VideoCapture(0)
cap.set(3, width)
cap.set(4, height)

cv2.namedWindow("window")
cv2.resizeWindow("window", width, height)
cv2.moveWindow("window", 0, 0)

cv2.namedWindow("trackbar")

cv2.moveWindow("trackbar", width, 0)

cv2.createTrackbar('x',"trackbar",xpos,1920,callback1)
cv2.createTrackbar('y',"trackbar",ypos,1920,callback2)
cv2.createTrackbar('rad',"trackbar",rad,1920,callback3)

while True:
    sucess , img = cap.read()
    cv2.circle(img, (xpos,ypos),rad,(0,0,255),2)
    cv2.imshow('window',img)
    cv2.waitKey(1)
