
import cv2

img=cv2.imread('kahlo.jpg')
cv2.imshow('kahlo',img)
cv2.waitKey(0)
cv2.imwrite('kahlo_copy.jpg',img)

img=cv2.imread('ny.jpg')
cv2.imshow('ny',img)
cv2.waitKey(0)

img=cv2.imread('manzara.jpg')
cv2.imshow('manzara',img)
cv2.waitKey(0)

img=cv2.imread('sepet.jpg')
cv2.imshow('sepet',img)
cv2.waitKey(0)

cv2.destroyAllWindows()

