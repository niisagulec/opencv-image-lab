import cv2
import numpy as np
import sys
import os

IMAGE_PATH = "../assets/image.jpg" 
OUTPUT_PATH = "../outputs/output.jpg"

img = None
gray = None
blur = None
MIN_CONTOUR_AREA = 1000 

last_result = None
last_count = 0

def nothing(x):
    pass

def process_image(val=None):

    global img, blur, last_result, last_count
    
    if img is None or blur is None:
        return

    low_threshold = cv2.getTrackbarPos("Alt Esik", "Kontrol Penceresi")
    high_threshold = cv2.getTrackbarPos("Ust Esik", "Kontrol Penceresi")

    edges = cv2.Canny(blur, low_threshold, high_threshold)

    kernel = np.ones((5, 5), np.uint8) 
    closed = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel, iterations=2)

    contours, _ = cv2.findContours(closed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    img_copy = img.copy()
    count = 0

    for c in contours:
        area = cv2.contourArea(c)
        
        if area < MIN_CONTOUR_AREA: 
            continue

        count += 1

        cv2.drawContours(img_copy, [c], -1, (0, 255, 0), 2) # Yeşil

        x, y, w, h = cv2.boundingRect(c)
        cv2.rectangle(img_copy, (x, y), (x + w, y + h), (0, 255, 255), 2) # Sarı
        
        M = cv2.moments(c)
        if M["m00"] != 0:
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])

            cv2.putText(img_copy, str(count), (cx - 10, cy - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2) 

    cv2.putText(img_copy, f"NESNE SAYISI: {count}", (10, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2) 

    cv2.imshow("Canny Kenarlari", cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR))
    cv2.imshow("Kontrol Penceresi", img_copy) 


    last_result = img_copy.copy()
    last_count = count

def main():
    global img, gray, blur, last_result, last_count

    img = cv2.imread(IMAGE_PATH)
    if img is None:
        print(f"HATA: Görsel bulunamadı! Lütfen {IMAGE_PATH} dosyasının bulunduğundan emin olun.")
        sys.exit(1)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    cv2.namedWindow("Kontrol Penceresi", cv2.WINDOW_NORMAL)
    cv2.namedWindow("Canny Kenarlari", cv2.WINDOW_NORMAL)

    cv2.createTrackbar("Alt Esik", "Kontrol Penceresi", 30, 255, process_image)
    cv2.createTrackbar("Ust Esik", "Kontrol Penceresi", 100, 255, process_image)

    process_image()

    while True:
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    low = cv2.getTrackbarPos("Alt Esik", "Kontrol Penceresi")
    high = cv2.getTrackbarPos("Ust Esik", "Kontrol Penceresi")


    to_save = last_result if last_result is not None else img
    cv2.imwrite(OUTPUT_PATH, to_save)
    print(f"Kaydedildi: {OUTPUT_PATH}")

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()