# Ders notları ve hatalar

Geçici dosya. Her bölüm ilgili egzersiz klasörünün `README.md`'sine taşınacak.

## Ex 14-15 — Blur
- Kernel boyutu (ör. `(7,7)`) filtrenin baktığı komşuluk penceresidir. Yöntemleri adil karşılaştırmak için hepsinde aynı tutulmalı.

## Ex 19-20 — Sobel / Scharr
- Gradyan operatörlerine BGR görüntü verilirse 3 kanallı, anlamsız çıktı gelir. Önce griye çevir (`cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)`).
- Sabit adı `cv2.CV_64F` (alt çizgili), `cv2.CV64F` değil.

## Ex 23 — Find Contours
- `counters` / `contours` gibi benzer isimler `NameError` üretir; değişken adlarını tutarlı tut.
- `cv2.drawContours` görüntüyü yerinde değiştirir. Orijinali korumak için `.copy()` üzerinde çiz.
- Beyaz arka planlı, düşük kontrastlı görselde global threshold nesneyi arka plandan ayıramaz.

## Ex 24 — Filter by Area
- `filtered.append(contours)` tüm listeyi tek eleman olarak ekler; doğrusu `filtered.append(cnt)`.
- **Düzeltilmiş ders:** Canny ince ve çoğu zaman açık kenar çizgileri üretir. Bu çizgiler üzerinde bulunan konturların `contourArea` değeri nesnenin alanını değil, 1-2 piksellik kenar şeridinin alanını ölçer. Kuyruğun 95 piksel çıkması bu yüzdendi; `min_area`'yı 100'den 90'a düşürmek bir sonraki görselde yine bozulan geçici bir çözüm.
- **Doğru yaklaşım:** Canny çıktısını `cv2.dilate` veya `cv2.morphologyEx(..., cv2.MORPH_CLOSE, ...)` ile kapatıp sonra kontur bulmak ya da kenar yerine dolu bir maske (ör. HSV eşikleme) kullanmak.
- **Yapılacak:** Morfoloji egzersizinden sonra Ex 24'e dönüp iki yaklaşımı aynı görselde karşılaştır.

## Ex 25 — Bounding Boxes
- `cv2.rectangle(img, (x, y), (x + w, y + h), ...)`: `pt1` sol üst köşe, `pt2` sağ alt köşe.

## Ortam
- PyCharm'da `.ipynb` çıktıları görünmediği için terminalden `.py` çalıştırmaya geçildi. Bu kalıcı akış olarak kalabilir; görsel çıktı için `cv2.imwrite` ile dosyaya yaz veya `matplotlib` kullan.
