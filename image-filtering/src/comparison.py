import cv2
import numpy as np
import os

input_folder = "../../assets/images"
output_folder = "../outputs"
os.makedirs(output_folder, exist_ok=True)

images = {
    "Kahlo": cv2.imread(os.path.join(input_folder, "kahlo.jpg")),
    "Manzara": cv2.imread(os.path.join(input_folder, "manzara.jpg")),
    "Sepet": cv2.imread(os.path.join(input_folder, "sepet.jpg"))
}

def put_label(img, text):
    labeled = img.copy()
    cv2.rectangle(labeled, (0, 0), (labeled.shape[1], 30), (0, 0, 0), -1)
    cv2.putText(labeled, text, (10, 22), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    return labeled

def resize_same_height(img_list, height=200):
    resized = [cv2.resize(img, (int(img.shape[1]*height/img.shape[0]), height)) for img in img_list]
    return cv2.hconcat(resized)

# --- Gaussian, Median, Bilateral, Denoising ---
for name, func in {
    "Gaussian": lambda i: cv2.GaussianBlur(i, (5, 5), 0),
    "Median": lambda i: cv2.medianBlur(i, 5),
    "Bilateral": lambda i: cv2.bilateralFilter(i, 9, 75, 75),
    "Denoised": lambda i: cv2.fastNlMeansDenoisingColored(i, None, 7, 7, 7, 21)
}.items():

    processed = [put_label(func(img), label) for label, img in images.items()]
    stacked = resize_same_height(processed)
    cv2.imwrite(os.path.join(output_folder, f"comparison_{name.lower()}.jpg"), stacked)
    print(f"✅ {name} karşılaştırması kaydedildi.")
