import cv2

import numpy as np

img = np.zeros((512,512,3))

#Rectangle
cv2.rectangle(img,pt1=(120,120),pt2=(320,320),color=(255,180,0),thickness=3)

#circle
cv2.circle(img,center=(150,150),radius=50,color=(255,120,100),thickness=3)

#text
cv2.putText(img,org=(200,200),fontScale=3,color=(255,255,156),thickness=2,lineType=cv2.LINE_AA,text="hello",fontFace=cv2.FONT_ITALIC)

cv2.imshow("testing",img)
cv2.waitKey(0)