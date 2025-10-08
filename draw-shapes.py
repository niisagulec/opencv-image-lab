import cv2
import numpy as np

img=cv2.imread('assets/images/sepet.jpg')

while True:
    cv2.imshow('assets/images/sepet',img)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('1'):
        cv2.line(img, (50, 50), (200, 50), (255, 0, 0), 2)
    if key == ord('2'):
        cv2.rectangle(img, (150, 100), (250, 180), (0, 255, 0), 2)
    if key == ord('3'):
        cv2.circle(img, (300, 250), 50, (0, 0, 255), 2)
    if key == ord('q'):
        break

cv2.destroyAllWindows()
