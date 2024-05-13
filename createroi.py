import cv2

evt = 0

def createroi(event, x,y,flags, param):
    global evt
    global pnt1
    global pnt2

    if event == cv2.EVENT_LBUTTONDOWN:
        print(event,x,y)
        pnt1 = (x,y)
        evt = event

    if event == cv2.EVENT_LBUTTONUP:
        print(event,x,y)
        pnt2=(x,y)
        evt = event

    if event == cv2.EVENT_RBUTTONUP:
        evt= event




height = 360
width = 640
cv2.namedWindow('cam')


cam = cv2.VideoCapture(0)
cam.set(3,width)
cam.set(4,height)


cv2.setMouseCallback('cam', createroi)

while True:
    sucess, img = cam.read()

    if evt==4:
        cv2.rectangle(img,pnt1,pnt2,(0,0,255),2)
        ROI = img[pnt1[1]:pnt2[1],pnt1[0]:pnt2[0]]
        cv2.imshow('ROI',ROI)
        cv2.moveWindow('ROI',int(width*1.1),0)

    if evt==5:
        cv2.destroyWindow('ROI')
    # if evt == 4:
    #     cv2.rectangle(img, pnt1, pnt2, (0, 0, 255), 2)
    #     ROI = img[pnt1[1], pnt2[1]:pnt1[0], pnt2[0]]
    #     if ROI.shape[0] > 0 and ROI.shape[1] > 0:
    #         cv2.imshow('ROI', ROI)
    #         cv2.moveWindow('ROI', int(width * 1.1), 0)

    cv2.imshow('cam',img)

    cv2.waitKey(1)
