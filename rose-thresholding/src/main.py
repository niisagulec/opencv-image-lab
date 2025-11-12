import cv2
import numpy as np
import os

img = cv2.imread("../assets/rose.jpg")
if img is None:
    raise FileNotFoundError("Görsel bulunamadı!")


hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Kırmızı aralıkları
lower1 = np.array([0, 80, 50])
upper1 = np.array([10, 255, 255])
lower2 = np.array([160, 80, 50])
upper2 = np.array([179, 255, 255])

mask1 = cv2.inRange(hsv, lower1, upper1)
mask2 = cv2.inRange(hsv, lower2, upper2)
mask = cv2.bitwise_or(mask1, mask2)

# Maskeyi temizle 
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel, iterations=1)
mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=1)
mask = cv2.medianBlur(mask, 5)

hsv_new = hsv.copy()
mask_bool = mask > 0

target_hue = 140  # mor

hsv_new[..., 0][mask_bool] = target_hue

sat = hsv[..., 1].astype(np.float32)
sat[mask_bool] = np.clip(sat[mask_bool] * 1.35, 0, 255)
hsv_new[..., 1] = sat.astype(np.uint8)

recolored = cv2.cvtColor(hsv_new, cv2.COLOR_HSV2BGR)

blended = cv2.addWeighted(recolored, 0.85, img, 0.15, 0)

alpha = cv2.GaussianBlur(mask.astype(np.float32) / 255.0, (21, 21), 0)
alpha_3 = alpha[..., None]

result_f = blended.astype(np.float32) * alpha_3 
result = np.clip(result_f, 0, 255).astype(np.uint8)


out_dir = "../outputs"
os.makedirs(out_dir, exist_ok=True)
out_path = os.path.join(out_dir, "output.jpg")
cv2.imwrite(out_path, result)