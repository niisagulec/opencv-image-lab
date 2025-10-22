import cv2
import numpy as np
import os

input_folder = "../../assets/images"
output_folder = "../outputs"
os.makedirs(output_folder, exist_ok=True)

images = ["kahlo.jpg", "manzara.jpg", "sepet.jpg"]

def apply_morphology(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    kernel = np.ones((3, 3), np.uint8)
    erode = cv2.erode(binary, kernel, iterations=1)
    dilate = cv2.dilate(binary, kernel, iterations=1)
    open_img = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)
    close_img = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)
    return {
        "Binary": cv2.cvtColor(binary, cv2.COLOR_GRAY2BGR),
        "Erode": cv2.cvtColor(erode, cv2.COLOR_GRAY2BGR),
        "Dilate": cv2.cvtColor(dilate, cv2.COLOR_GRAY2BGR),
        "Open": cv2.cvtColor(open_img, cv2.COLOR_GRAY2BGR),
        "Close": cv2.cvtColor(close_img, cv2.COLOR_GRAY2BGR)
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

        results = apply_morphology(img)
        morph_stack = stack_images([put_label(v, k) for k, v in results.items()])
        out_path = os.path.join(output_folder, f"{os.path.splitext(name)[0]}_morph.jpg")
        cv2.imwrite(out_path, morph_stack)
        print(f"✅ {name} için morfolojik işlem çıktısı kaydedildi: {out_path}")
