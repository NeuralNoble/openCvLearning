import cv2 , numpy as np
evt = 0
xVal = 0
yVal = 0
def click(event, x, y, flags, param):
    global evt
    global xVal
    global yVal

    if event == cv2.EVENT_LBUTTONDOWN:
        print(event)
        evt = event
        xVal = x
        yVal = y
    if event== cv2.EVENT_LBUTTONUP:
        print(event)
        evt = event
width = 640
height = 360

cam = cv2.VideoCapture(0)
cam.set(3, width)
cam.set(4, height)

cv2.namedWindow('colorpicker', cv2.WINDOW_NORMAL)

cv2.setMouseCallback('colorpicker',click)


while True:
    ret, img = cam.read()
    if evt ==1:
        x = np.zeros([250, 250, 3], dtype=np.uint8)
        clr = img[yVal][xVal]
        print(clr)
        x[:,:] = clr
        cv2.imshow('color',x)
        cv2.moveWindow('color',width,0)
        evt =0
    cv2.imshow('colorpicker',img)
    cv2.waitKey(1)