
import cv2
import cv2

img = cv2.imread('assets/images/kahlo.jpg')
cv2.imshow('kahlo', img)
cv2.waitKey(0)
cv2.imwrite('assets/images/kahlo_copy.jpg', img)

img = cv2.imread('assets/images/ny.jpg')
cv2.imshow('ny', img)
cv2.waitKey(0)

img = cv2.imread('assets/images/manzara.jpg')
cv2.imshow('manzara', img)
cv2.waitKey(0)

img = cv2.imread('assets/images/sepet.jpg')
cv2.imshow('sepet', img)
cv2.waitKey(0)

cv2.destroyAllWindows()