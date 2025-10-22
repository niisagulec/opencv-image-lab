import cv2
import numpy as np

img1=cv2.imread('../assets/images/sepet.jpg')
img2=cv2.imread('../assets/images/kahlo.jpg')
img3=cv2.imread('../assets/images/ny.jpg')
img4=cv2.imread('../assets/images/manzara.jpg')


img1_gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img2_hsv = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)
img3_rgb = cv2.cvtColor(img3, cv2.COLOR_BGR2RGB)

img4_bright = cv2.convertScaleAbs(img4, alpha=1.2, beta=30)  

img1_resized = cv2.resize(img1, (300, 300))
img2_resized = cv2.resize(img2, (300, 300))
img3_resized = cv2.resize(img3, (300, 300))
img4_resized = cv2.resize(img4, (300, 300))
img1_rotated = cv2.rotate(img1_resized, cv2.ROTATE_180)

img1_cropped = img1_resized[50:250, 50:250]
img2_cropped = img2_resized[50:250, 50:250]

img1_cropped = cv2.resize(img1_cropped, (200, 200))
img2_cropped = cv2.resize(img2_cropped, (200, 200))


img2_hsv_bgr = cv2.cvtColor(img2_hsv, cv2.COLOR_HSV2BGR)
img3_rgb_bgr = cv2.cvtColor(img3_rgb, cv2.COLOR_RGB2BGR)


cv2.imwrite('outputs/img1_cropped.jpg', img1_cropped)
cv2.imwrite('outputs/img2_cropped.jpg', img2_cropped)
cv2.imwrite('outputs/img1_gray.jpg', img1_gray)
cv2.imwrite('outputs/img2_hsv.jpg', img2_hsv_bgr)
cv2.imwrite('outputs/img3_rgb.jpg', img3_rgb_bgr)
cv2.imwrite('outputs/img4_bright.jpg', img4_bright)
cv2.imwrite('outputs/img1_blur.jpg', img1_blur)
cv2.imwrite('outputs/img1_rotated.jpg', img1_rotated)
cv2.imwrite('outputs/img1_resized.jpg', img1_resized)
cv2.imwrite('outputs/img2_resized.jpg', img2_resized)
cv2.imwrite('outputs/img3_resized.jpg', img3_resized)
cv2.imwrite('outputs/img4_resized.jpg', img4_resized)



