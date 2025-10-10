import cv2
import numpy as np
import sys


p1 = '../outputs/img1_rotated.jpg'    
p2 = '../outputs/img2_resized.jpg'    
p3 = '../outputs/img3_rgb.jpg'        
p4 = '../outputs/img4_bright.jpg'     

img1 = cv2.imread(p1)
img2 = cv2.imread(p2)
img3 = cv2.imread(p3)
img4 = cv2.imread(p4)

if img1 is None:
    print(f"Not found: {p1}"); sys.exit(1)
if img2 is None:
    print(f"Not found: {p2}"); sys.exit(1)
if img3 is None:
    print(f"Not found: {p3}"); sys.exit(1)
if img4 is None:
    print(f"Not found: {p4}"); sys.exit(1)

imgs = [img1, img2, img3, img4]
for i, im in enumerate(imgs):
    if im.ndim == 2:
        imgs[i] = cv2.cvtColor(im, cv2.COLOR_GRAY2BGR)
img1, img2, img3, img4 = imgs

size = (200, 200)
img1 = cv2.resize(img1, size)
img2 = cv2.resize(img2, size)
img3 = cv2.resize(img3, size)
img4 = cv2.resize(img4, size)

top = np.hstack((img1, img2))
bottom = np.hstack((img3, img4))
collage = np.vstack((top, bottom))

out = '../outputs/collage.jpg'
cv2.imwrite(out, collage)
cv2.imshow('Collage', collage)
cv2.waitKey(0)
cv2.destroyAllWindows()
