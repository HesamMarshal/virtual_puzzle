# cvzone 1.5.0
# mediapipe 0.8.7

import cv2
from cvzone.HandTrackingModule import HandDetector
import cvzone
import os

WIDTH = 1280
HEIGHT = 720
CLICK = 50

cap = cv2.VideoCapture(2, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)

r, frame = cap.read()
print('Resolution: ' + str(frame.shape[0]) + ' x ' + str(frame.shape[1]))


detector = HandDetector(detectionCon=0.7)

class DragImg():
    def __init__(self,path,posOrigin, imgType):

        self.path = path
        self.posOrigin = posOrigin
        self.imgType = imgType

        if self.imgType == 'png':
            self.img =cv2.imread(self.path, cv2.IMREAD_UNCHANGED)
        else:
            self.img = cv2.imread(self.path)

        self.size = self.img.shape[:2]
    def update(self, cursor):
        ox, oy = self.posOrigin
        h,w = self.size
        # check if in region
        if ox < cursor[0] < ox + w and oy < cursor[1] < oy + h:
            self.posOrigin = cursor[0] - w // 2, cursor[1] - h // 2






# img1 = cv2.imread("ImagesJPG/1.jpg")
# img1 = cv2.imread("ImagesPNG/1.png", cv2.IMREAD_UNCHANGED)
# ox, oy = 500, 200
path = "Images_puzzle"
myList = os.listdir(path)
print(myList)

listImg = []

for i, pathImg in enumerate(myList):

    if "png" in pathImg:
        imgType = "png"
    else:
        imgType = "jpg"

    listImg.append(DragImg(F"{path}/{pathImg}",[50+ i*100 ,50],imgType))

print(len(listImg))

while True:
    success, img = cap.read()
    # to flip
    img = cv2.flip(img, 1)

    # Hand Detector
    # not show on image
    # hand = detector.findHands(img, draw=False)

    # no flip
    # hand, img = detector.findHands(img)

    # fliped used
    hands, img = detector.findHands(img, flipType=False)

    if hands:
        lmList = hands[0]['lmList']

        # cursor = lmList[8]
        # check if clicked
        length, info, img = detector.findDistance(lmList[8], lmList[12], img)
        # print(length)
        if length < CLICK:
            cursor = lmList[8]
            for imgObject in listImg:
                imgObject.update(cursor)
            # check if in region sent to object
            # if ox < cursor[0] < ox + w and oy < cursor[1] < oy + h:
            #     ox, oy = cursor[0] - w // 2, cursor[1] - h // 2
    #to avoid out of image
    try:

        for imgObject in listImg:
            h, w,  = imgObject.size
            ox,oy = imgObject.posOrigin
            if imgObject.imgType == "png":
                img = cvzone.overlayPNG(img, imgObject.img, [ox, oy])
            else:
                img[oy:oy + h, ox:ox + w] = imgObject.img

        # Draw for JPG image
       # h, w, _ = img1.shape
        # img[oy:oy + h, ox:ox + w] = img1

        # Draw for PNG Images
        # img = cvzone.overlayPNG(img, img1, [ox, oy])

    except:
        pass
    cv2.imshow("Webcam", img)
    cv2.waitKey(1)
