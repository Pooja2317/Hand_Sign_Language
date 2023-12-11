import cv2
import numpy as np
from cvzone.HandTrackingModule import HandDetector
import math
import time

cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=2)
offset = 40
imgSize = 300
folder = "Data/A"
counter = 0

while True:

    success, img = cap.read()
    hands, img = detector.findHands(img)
    if hands :
        hand = hands[0]
        x, y ,h , w = hand['bbox']
        #imgWhite = np.ones((imgSize,imgSize,3),np.uint8)*255

        imgCrop = img[y-offset:y+h+offset , x-offset:x+w+offset]

        imgCropShape = imgCrop.shape


        aspectRatio = h/w

        if aspectRatio > 1:
            k = imgSize/h
            wCal = math.ceil(k * w)
            imgResize = cv2.resize(imgCrop,(wCal,imgSize))
            imgResizeShape = imgResize.shape
            wGap = math.ceil((imgSize-wCal)/2)

          #  imgWhite[:,wGap:wCal+wGap] = imgResize

        if aspectRatio<=1:
            k = imgSize/w
            hCal = math.ceil(k*h)
            imgResize = cv2.resize(imgCrop,(hCal,imgSize))
            imgResizeShape = imgResize.shape
            hGap = math.ceil((imgSize - hCal) / 2)

            #imgWhite[hGap:hCal+hGap , :] = imgResize




        cv2.imshow("ImageCrop",imgCrop)
        #cv2.imshow("Image White ",imgWhite)


    cv2.imshow("Image",img)
    key = cv2.waitKey(1)
    if key == ord("s"):
        counter += 1
        cv2.imwrite(f'{folder}/Image_{time.time()}.jpg', imgCrop)
        print(counter)