# Görüntü Manipülasyonu Projesi

Bu proje, **OpenCV** kütüphanesi kullanılarak temel görüntü işleme ve manipülasyon tekniklerini uygulamak için hazırlanmıştır.  
Amaç; farklı görseller üzerinde renk uzayı dönüşümleri, boyutlandırma, döndürme, parlaklık ayarı ve kolaj oluşturma işlemlerini gerçekleştirmektir.

---

## 🎯 Amaç ve Uygulanan İşlemler

Bu projede aşağıdaki görüntü işleme adımları uygulanmıştır:

### Temel Görüntü İşlemleri (`process-images.py`)
- Görüntü okuma (`cv2.imread`)
- Renk uzayı dönüşümleri:
  - BGR → **Gray**, **HSV**, **RGB**
- Parlaklık ve kontrast artırma (`convertScaleAbs`)
- Boyutlandırma (resize)
- Döndürme (`cv2.rotate`)
- Kırpma (crop)
- Kırpılan ve dönüştürülen görüntülerin dosyaya kaydedilmesi

### Kolaj Oluşturma (`create_collage.py`)
- Dönüştürülmüş görsellerin okunması
- Boyutlandırma ve hizalama
- Görsellerin 2x2 matris şeklinde birleştirilmesi (`np.hstack`, `np.vstack`)
- Kolajın kaydedilmesi (`collage.jpg`)
- Sonucun ekranda görüntülenmesi (`cv2.imshow`)

