import cv2 as cv
import numpy as np

capture = cv.VideoCapture(0)
# frame = cv.imread("capture", 0)

while True:
    isTrue, frame = capture.read()
    resized_image = cv.resize(frame, (400, 600))
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.putText(frame, 'yes', (0, 225),cv.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 1)
    cv.imshow("Resize", gray)
    cv.imshow("ttt", resized_image)
    cv.imshow('O', frame)


    if cv.waitKey(20) & 0xFF == ord('q'):
        break


