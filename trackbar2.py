import cv2

width = 640
height = 360


def callback1(value):
    global x
    print(value)
    x = value


def callback2(value):
    global y
    print(value)
    y = value


x = 0
y = 0

cap = cv2.VideoCapture(0)
cap.set(3, width)
cap.set(4, height)

cv2.namedWindow("window")
cv2.resizeWindow("window", width, height)
cv2.moveWindow("window", 0, 0)

cv2.namedWindow("trackbar")
cv2.moveWindow("trackbar", width, 0)

cv2.createTrackbar('x', 'trackbar', 0, 2000, callback1)
cv2.createTrackbar('y', 'trackbar', 0, 2000, callback2)

while True:
    ret, frame = cap.read()
    cv2.moveWindow("window", x, y)

    cv2.imshow("window", frame)
    cv2.waitKey(1)
