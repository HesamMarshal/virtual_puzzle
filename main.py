# cvzone 1.5.0
# mediapipe 0.8.7
# TODO: 1. add a flag=false to each part if the part is in it's place change it to true,
#           it is not possible to drag and drop the image
# TODO: 2. add a module to divide any given photo to 9 pisces.
#
############################################################################################

import cv2
from cvzone.HandTrackingModule import HandDetector
import cvzone
import os

WIDTH = 1280
HEIGHT = 720
CLICK = 35
PRECISION = 0.6

cap = cv2.VideoCapture(2, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)

r, frame = cap.read()
print('Resolution: ' + str(frame.shape[0]) + ' x ' + str(frame.shape[1]))

detector = HandDetector(detectionCon=PRECISION)


class DragImg():
    def __init__(self, path, posOrigin, imgType):

        self.path = path
        self.posOrigin = posOrigin
        self.imgType = imgType

        if self.imgType == 'png':
            self.img = cv2.imread(self.path, cv2.IMREAD_UNCHANGED)
        else:
            self.img = cv2.imread(self.path)

        self.size = self.img.shape[:2]

    def update(self, cursor):
        ox, oy = self.posOrigin
        h, w = self.size
        # check if in region
        # print (len(solvedList))
        if ox < cursor[0] < ox + w and oy < cursor[1] < oy + h:
            self.posOrigin = cursor[0] - w // 2, cursor[1] - h // 2
            # 1
            if 185 < self.posOrigin[0] < 215 and 235 < self.posOrigin[1] < 265 \
                    and self.path == "Images_puzzle/puzzle_01.jpg":
                print(self.path)
                solvedList.append(DragImg(self.path, [200, 250], "jpg"))
                listImg.remove(self)
            # 2
            if 385 < self.posOrigin[0] < 415 and 235 < self.posOrigin[1] < 265\
                    and self.path == "Images_puzzle/puzzle_02.jpg":
                print(self.path)
                solvedList.append(DragImg(self.path, [400, 250], "jpg"))
                listImg.remove(self)

            # 3
            if 585 < self.posOrigin[0] < 615 and 235 < self.posOrigin[1] < 265 \
                    and self.path == "Images_puzzle/puzzle_03.jpg":
                print(self.path)
                solvedList.append(DragImg(self.path, [600, 250], "jpg"))
                listImg.remove(self)

            # 4
            if 185 < self.posOrigin[0] < 215 and 350 < self.posOrigin[1] < 400 \
                    and self.path == "Images_puzzle/puzzle_04.jpg":
                print(self.path)
                solvedList.append(DragImg(self.path, [200, 383], "jpg"))
                listImg.remove(self)

            # 5
            if 385 < self.posOrigin[0] < 415 and 350 < self.posOrigin[1] < 400 \
                    and self.path == "Images_puzzle/puzzle_05.jpg":
                print(self.path)
                solvedList.append(DragImg(self.path, [400, 382], "jpg"))
                listImg.remove(self)

            # 6
            if 585 < self.posOrigin[0] < 615 and 350 < self.posOrigin[1] < 400 \
                    and self.path == "Images_puzzle/puzzle_06.jpg":
                print(self.path)
                solvedList.append(DragImg(self.path, [600, 382], "jpg"))
                listImg.remove(self)

            # 7
            if 185 < self.posOrigin[0] < 215 and 500 < self.posOrigin[1] < 530 \
                    and self.path == "Images_puzzle/puzzle_07.jpg":
                print(self.path)
                solvedList.append(DragImg(self.path, [200, 516], "jpg"))
                listImg.remove(self)

            # 8
            if 385 < self.posOrigin[0] < 415 and 500 < self.posOrigin[1] < 530 \
                    and self.path == "Images_puzzle/puzzle_08.jpg":
                print(self.path)
                solvedList.append(DragImg(self.path, [400, 516], "jpg"))
                listImg.remove(self)
            # 9
            if 585 < self.posOrigin[0] < 615 and 500 < self.posOrigin[1] < 530 \
                    and self.path == "Images_puzzle/puzzle_09.jpg":
                print(self.path)
                solvedList.append(DragImg(self.path, [600, 516], "jpg"))
                listImg.remove(self)
# img1 = cv2.imread("ImagesJPG/1.jpg")
# img1 = cv2.imread("Images_puzzle/puzzle_map.png", cv2.IMREAD_UNCHANGED)
# ox, oy = 500, 200


path = "Images_puzzle"
myList = os.listdir(path)
# print(myList)

listImg = []
solvedList = []

# for i, pathImg in enumerate(myList):
#     if "png" in pathImg:
#         imgType = "png"
#     else:
#         imgType = "jpg"
# TODO: Make it modular
imgMap = cv2.imread("Images_puzzle/map.png", cv2.IMREAD_UNCHANGED)
listImg.append(DragImg("Images_puzzle/puzzle_01.jpg", [170, 20], "jpg"))
listImg.append(DragImg("Images_puzzle/puzzle_09.jpg", [390, 20], "jpg"))
listImg.append(DragImg("Images_puzzle/puzzle_04.jpg", [610, 20], "jpg"))
listImg.append(DragImg("Images_puzzle/puzzle_07.jpg", [830, 20], "jpg"))
listImg.append(DragImg("Images_puzzle/puzzle_05.jpg", [1050, 20], "jpg"))
listImg.append(DragImg("Images_puzzle/puzzle_03.jpg", [1050, 160], "jpg"))
listImg.append(DragImg("Images_puzzle/puzzle_08.jpg", [1050, 300], "jpg"))
listImg.append(DragImg("Images_puzzle/puzzle_06.jpg", [1050, 440], "jpg"))
listImg.append(DragImg("Images_puzzle/puzzle_02.jpg", [1050, 570], "jpg"))

print(len(listImg))

while True:
    success, img = cap.read()

    # to flip
    img = cv2.flip(img, 1)
    # img = cvzone.overlayPNG(img, imgMap, [200, 250])
    # Hand Detector
    # not show on image
    # hand = detector.findHands(img, draw=False)

    # no flip
    # hand, img = detector.findHands(img)

    # Use this to flip image
    hands, img = detector.findHands(img, flipType=False)

    if hands:
        lmList = hands[0]['lmList']

        # cursor = lmList[8]
        # check if clicked
        length, info, img = detector.findDistance(lmList[8], lmList[12], img)
        # print(length)
        if length < CLICK:

            cursor = lmList[8]
            # print(cursor)

            for imgObject in listImg:
                imgObject.update(cursor)
    # to avoid out of image
    try:
        for imgObject in listImg:
            h, w,  = imgObject.size
            ox, oy = imgObject.posOrigin
            if imgObject.imgType == "png":
                img = cvzone.overlayPNG(img, imgObject.img, [ox, oy])
            else:
                img[oy:oy + h, ox:ox + w] = imgObject.img

        for imgObject in solvedList:
            h, w,  = imgObject.size
            ox, oy = imgObject.posOrigin
            if imgObject.imgType == "png":
                img = cvzone.overlayPNG(img, imgObject.img, [ox, oy])
            else:
                img[oy:oy + h, ox:ox + w] = imgObject.img

        # Draw for JPG image
        # h, w, _ = img1.shape
        # img[oy:oy + h, ox:ox + w] = img1
        # Draw for PNG Images
    # TODO : add exceptions type
    except:
        pass
    cv2.imshow("Webcam", img)
    cv2.waitKey(1)
