import cv2
import os

input_folder = "../../assets/images"
output_folder = "../outputs"
os.makedirs(output_folder, exist_ok=True)


images = ["kahlo.jpg", "manzara.jpg", "sepet.jpg"]

def apply_blurring(img):
    gaussian = cv2.GaussianBlur(img, (5, 5), 0)
    median = cv2.medianBlur(img, 5)
    bilateral = cv2.bilateralFilter(img, 9, 75, 75)
    denoised = cv2.fastNlMeansDenoisingColored(img, None, 7, 7, 7, 21) #kenarları yumusatarak temizliyor
    return {
        "Original": img,
        "Gaussian": gaussian,
        "Median": median,
        "Bilateral": bilateral,
        "Denoised": denoised
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


for name in images:
    path = os.path.join(input_folder, name)
    img = cv2.imread(path)

    if img is None:
        print(f"⚠️ Görüntü okunamadı: {path}")
        continue

  
    results = apply_blurring(img)

    combined = stack_images([put_label(v, k) for k, v in results.items()])

   
    out_path = os.path.join(output_folder, f"{os.path.splitext(name)[0]}_blurs.jpg")
    cv2.imwrite(out_path, combined)
    print(f"✅ {name} için blurlu çıktı kaydedildi: {out_path}")
