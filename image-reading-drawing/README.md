# Görüntü Okuma ve Çizim Projesi

Bu proje, **OpenCV** kütüphanesi kullanılarak temel görüntü okuma, görüntüleme ve kullanıcı etkileşimli çizim işlemlerini gerçekleştirmek için hazırlanmıştır.  
Amaç, farklı görüntüleri ekranda göstermek ve klavye girdileriyle çizimler yaparak OpenCV’nin temel fonksiyonlarını öğrenmektir.

---

## 🎯 Amaç ve Uygulanan İşlemler

### Görüntü Okuma ve Gösterme (`read-show.py`)
- `cv2.imread()` ile görselleri okur  
- `cv2.imshow()` ile görüntüleri ekranda gösterir  
- `cv2.waitKey()` ile kullanıcıdan giriş bekler  
- `cv2.imwrite()` ile bir görselin kopyasını kaydeder (`kahlo_copy.jpg`)  
- `cv2.destroyAllWindows()` ile pencereleri kapatır  

Uygulanan görseller:
- `kahlo.jpg`
- `ny.jpg`
- `manzara.jpg`
- `sepet.jpg`

---

### Çizim Uygulaması (`draw_shapes.py`)
Bu dosya, kullanıcı klavye tuşlarına bastıkça farklı şekiller çizer.

| Tuş | İşlem |
|-----|--------|
| **1** | Mavi çizgi çizer (`cv2.line`) |
| **2** | Yeşil dikdörtgen çizer (`cv2.rectangle`) |
| **3** | Kırmızı daire çizer (`cv2.circle`) |
| **q** | Uygulamayı kapatır |

Kullanıcı, çizim işlemlerini etkileşimli olarak gerçekleştirir ve değişiklikleri anında görüntü üzerinde görür.

