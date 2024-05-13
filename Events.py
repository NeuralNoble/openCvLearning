import cv2, time


evt = 0
def mouseClick(event, x, y, flags, param):
    global evt
    global pnt

    if event == cv2.EVENT_LBUTTONDOWN:
        print("mouse clicked at" + str(x) + ", " + str(y),event)
        evt = event
        pnt = (x,y)
    if event == cv2.EVENT_LBUTTONUP:
        print("mouse clicked at" + str(x) + ", " + str(y), event)
        evt = event
        pnt = (x, y)




cam = cv2.VideoCapture(0)
cam.set(3, 640)
cam.set(4,360)
cv2.namedWindow("events")
cv2.setMouseCallback("events",mouseClick)


while True:
    sucess , frame = cam.read()
    if evt ==1:
        cv2.circle(frame,pnt,25,(255,0,0),2)

    cv2.imshow('events',frame)
    cv2.waitKey(1)