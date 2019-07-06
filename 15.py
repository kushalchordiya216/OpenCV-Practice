import cv2
import numpy as np

stream = cv2.VideoCapture(0)
fgbg = cv2.createBackgroundSubtractorMOG2()

while True:
    ret, frame = stream.read()
    fgmask = fgbg.apply(frame)

    res = cv2.bitwise_and(frame, frame, mask=fgmask)
    cv2.imshow('fgmask', frame)
    cv2.imshow('frame', fgmask)
    cv2.imshow('res', res)

    k = cv2.waitKey(5) & 0xff
    if k == 27:
        break

stream.release()
cv2.destroyAllWindows()
