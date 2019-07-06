import cv2
import numpy as np
import tensorflow as tf

stream = cv2.VideoCapture(0)

while True:
    _, frame = stream.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_red = np.array([150, 150, 50])
    higher_red = np.array([180, 255, 150])

    mask = cv2.inRange(hsv, lower_red, higher_red)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    kernel = np.ones((15, 15), np.float32)
    smoothed = cv2.filter2D(res, -1, kernel)

    blur = cv2.GaussianBlur(res, (15, 15), 0)

    cv2.imshow('smoothed', smoothed)
    cv2.imshow('blur', blur)
    cv2.imshow('res', res)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
stream.release()
