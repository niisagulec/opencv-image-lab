import cv2
import numpy as np
import os

input_folder = "../../assets/images"
output_folder = "../outputs"
os.makedirs(output_folder, exist_ok=True)

images = ["kahlo.jpg", "manzara.jpg", "sepet.jpg"]

def apply_edge_detection(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
    sobel = np.uint8(np.clip(cv2.magnitude(sobelx, sobely), 0, 255))
    canny = cv2.Canny(gray, 100, 200)
    return {
        "Original": img,
        "Sobel": cv2.cvtColor(sobel, cv2.COLOR_GRAY2BGR),
        "Canny": cv2.cvtColor(canny, cv2.COLOR_GRAY2BGR)
    }

def put_label(img, text):
    labeled = img.copy()
    cv2.rectangle(labeled, (0, 0), (labeled.shape[1], 30), (0, 0, 0), -1)
    cv2.putText(labeled, text, (10, 22), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    return labeled

def stack_images(img_list):
    min_height = min(img.shape[0] for img in img_list)
    resized = [cv2.resize(img, (int(img.shape[1]*min_height/img.shape[0]), min_height)) for img in img_list]
    return cv2.hconcat(resized)

if __name__ == "__main__":
    for name in images:
        path = os.path.join(input_folder, name)
        img = cv2.imread(path)
        if img is None:
            print(f"⚠️ Görüntü okunamadı: {path}")
            continue

        results = apply_edge_detection(img)
        edge_stack = stack_images([put_label(v, k) for k, v in results.items()])
        out_path = os.path.join(output_folder, f"{os.path.splitext(name)[0]}_edges.jpg")
        cv2.imwrite(out_path, edge_stack)
        print(f"✅ {name} için kenar algılama çıktısı kaydedildi: {out_path}")
