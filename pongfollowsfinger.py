import cv2

width = 1280
height = 720
cam = cv2.VideoCapture(0)



class mpHands:
    import mediapipe as mp

    def __init__(self, maxHands=2, minDetectionConfidence=0.5, minTrackingConfidence=0.5):
        self.hands = self.mp.solutions.hands.Hands(
            static_image_mode=False,
            max_num_hands=maxHands,
            min_detection_confidence=minDetectionConfidence,
            min_tracking_confidence=minTrackingConfidence
        )

    def marks(self,frame):
        myHands = []
        frameRGB = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        results = self.hands.process(frameRGB)
        if results.multi_hand_landmarks != None:
            for handLms in results.multi_hand_landmarks:
                myHand = []
                for landmark in handLms.landmark:
                    myHand.append((int(landmark.x*width),int(landmark.y*height)))

                myHands.append(myHand)

        return myHands

boxColor = (0,0,255)
paddleWidth = 125
paddleHeight = 25

findHands = mpHands()
while True:
    ret,frame= cam.read()
    myHands = findHands.marks(frame)
    for hand in myHands:
       cv2.rectangle(frame,(hand[8][0]-paddleWidth//2,0),(hand[8][0]+paddleWidth//2,paddleHeight),(boxColor),-1)


    cv2.imshow('frame',frame)
    cv2.waitKey(1)

