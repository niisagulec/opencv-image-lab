# 🖼️ OpenCV – TrackBar ile Dinamik Canny Kenar Tespiti ve Kontur Analizi

Bu proje, OpenCV kullanarak bir görüntüdeki nesneleri dinamik Canny kenar tespiti ile inceleyen ve kontur analizi yapan interaktif bir uygulamadır. Kullanıcı, TrackBar aracılığıyla alt ve üst Canny eşik değerlerini gerçek zamanlı olarak değiştirebilir.

## Özellikler
- 🎛 Dinamik TrackBar Kontrolü: "Alt Eşik" ve "Üst Eşik" TrackBar'ları ile gerçek zamanlı güncelleme.
- 🔍 Kontur Analizi:
  - Küçük konturlar MIN_CONTOUR_AREA ile filtrelenir.
  - Yeşil kontur çizimi.
  - Sarı bounding box.
  - Nesne merkezine numaralandırma.
  - Toplam nesne sayısının ekranda gösterimi.
- 🖼️ Pencereler:
  - Kontrol Penceresi → İşlenmiş görüntü
  - Canny Kenarlari → Canny kenar tespiti çıktısı
- 💾 Otomatik Çıktı Kaydı: Program kapatıldığında son işlenen görüntü kaydedilir.

## Gereksinimler
- Python 3.x
- OpenCV (cv2)
- NumPy

Örnek olarak kurulum:
```bash
pip install opencv-python numpy
```

## Kurulum & Çalıştırma
1. Depoyu klonlayın veya dosyaları indirin.
2. Gerekli paketleri yükleyin.
3. Script'i çalıştırın:
```bash
python main.py
```

(Not: script ismi proje yapısına göre farklı olabilir. Kendi dosyanızın adını kullanın.)

## Kullanım
- TrackBar'lardan "Alt Eşik" ve "Üst Eşik" değerlerini ayarlayarak Canny kenar tespitinin sonucunu gerçek zamanda gözlemleyin.
- Pencerede işlenen görüntüde konturlar, bounding box'lar ve numaralar gösterilir.
- Programdan çıkmak için `q` tuşuna basın.

## Çıktı Kaydetme
- Kullanıcı `q` tuşuna bastığında, ekranda görünen son işlenen görüntü varsayılan olarak `../outputs/output.jpg` konumuna kaydedilir.
- İstediğiniz kaydetme yolunu veya dosya adını script içinde değiştirebilirsiniz.


