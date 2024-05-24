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

    def marks(self, frame):
        myHands = []
        frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(frameRGB)
        if results.multi_hand_landmarks != None:
            for handLms in results.multi_hand_landmarks:
                myHand = []
                for landmark in handLms.landmark:
                    myHand.append((int(landmark.x * width), int(landmark.y * height)))

                myHands.append(myHand)

        return myHands


boxColor = (0, 0, 255)
paddleWidth = 125
paddleHeight = 25
ballRadius = 15
ballColor = (255, 0, 0)
xPos = (width // 2)
yPos = (height // 2)
deltax = 2
deltay = 2
lives = 5
score = 0
font = cv2.FONT_HERSHEY_SIMPLEX

findHands = mpHands()
while True:
    ret, frame = cam.read()
    cv2.circle(frame, (xPos, yPos), ballRadius, ballColor, -1)
    cv2.putText(frame, str(score), (25, int(6 * paddleHeight)), font, 5, (0, 0, 255), 5)
    cv2.putText(frame, str(lives), (width - 125, int(6 * paddleHeight)), font, 5, (0, 0, 255), 5)
    myHands = findHands.marks(frame)

    for hand in myHands:
        cv2.rectangle(frame, (hand[8][0] - paddleWidth // 2, 0), (hand[8][0] + paddleWidth // 2, paddleHeight),
                      boxColor, -1)

    topEdge = yPos - ballRadius
    bottomEdge = yPos + ballRadius
    leftEdge = xPos - ballRadius
    rightEdge = xPos + ballRadius

    if leftEdge <= 0 or rightEdge >= width:
        deltax = deltax * -1
    if bottomEdge >= height:
        deltay = deltay * -1

    if topEdge <= paddleHeight:
        if xPos >= (hand[8][0] - paddleWidth // 2) and xPos <= (hand[8][0] + paddleWidth // 2):
            deltay = deltay * -1
            score = score+1

            if score == 5 or score == 10 or score == 15 or score == 20:
                deltax = deltax*2
                deltay = deltay*2
        else:
            xPos = width // 2
            yPos = height // 2
            lives = lives - 1

    xPos = xPos + deltax
    yPos = yPos + deltay

    cv2.imshow('frame', frame)
    if lives ==0:
        break
    cv2.waitKey(1)
