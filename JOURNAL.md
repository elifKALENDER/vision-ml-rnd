# JOURNAL

Kendi okuma dosyam. İki bölüm var: **Hatalar ve dersler** (konuya göre, tekrar düşmemek için) ve **Oturum günlüğü** (tarihli, en yeni en üstte). İlerleme durumu burada değil, `PROGRESS.md`'de.

## Hatalar ve dersler

### P1 — Görüntü okuma (`load_bgr`)
- `cv2.imread` dosyayı okuyamazsa hata vermez, sessizce `None` döndürür. Hata çok sonra, ilk `.shape` ya da `cvtColor` çağrısında çıkar. Bu yüzden `load_bgr` `None` görünce hemen `FileNotFoundError` fırlatıyor.
- Windows'ta `cv2.imread` ASCII olmayan karakter içeren yollarda (ör. Türkçe harfli klasör adı) okuyamayabilir ve yine `None` döner. Dosya yerindeyse ilk şüpheli yol adıdır.
- Hata mesajında `image::` yazım hatası vardı (çift iki nokta). Düzeltildi: `"Could not read image: {path}"`.
- PEP 8: `if img is None: raise ...` tek satırda yazılmaz; `raise` alt satıra, girintili.

### Blur (Ex 14–15, P5)
- Kernel boyutu (ör. `(7,7)`) filtrenin baktığı komşuluk penceresidir. Yöntemleri adil karşılaştırmak için hepsinde aynı tutulmalı.

### Sobel / Scharr (Ex 19–20, P7)
- Gradyan operatörlerine BGR görüntü verilirse 3 kanallı, anlamsız çıktı gelir. Önce griye çevir (`cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)`).
- Sabit adı `cv2.CV_64F` (alt çizgili), `cv2.CV64F` değil.

### Find Contours (Ex 23, P8)
- `counters` / `contours` gibi benzer isimler `NameError` üretir; değişken adlarını tutarlı tut.
- `cv2.drawContours` görüntüyü yerinde değiştirir. Orijinali korumak için `.copy()` üzerinde çiz.
- Beyaz arka planlı, düşük kontrastlı görselde global threshold nesneyi arka plandan ayıramaz.

### Filter by Area (Ex 24, P8)
- `filtered.append(contours)` tüm listeyi tek eleman olarak ekler; doğrusu `filtered.append(cnt)`.
- **Düzeltilmiş ders:** Canny ince ve çoğu zaman açık kenar çizgileri üretir. Bu çizgiler üzerinde bulunan konturların `contourArea` değeri nesnenin alanını değil, 1–2 piksellik kenar şeridinin alanını ölçer. Kuyruğun 95 piksel çıkması bu yüzdendi; `min_area`'yı 100'den 90'a düşürmek bir sonraki görselde yine bozulan geçici bir çözüm.
- **Doğru yaklaşım:** Canny çıktısını `cv2.dilate` veya `cv2.morphologyEx(..., cv2.MORPH_CLOSE, ...)` ile kapatıp sonra kontur bulmak ya da kenar yerine dolu bir maske (ör. HSV eşikleme) kullanmak.
- **Yapılacak:** Morfolojiden sonra (1b, P11 `clean_mask`) Ex 24'e dönüp iki yaklaşımı aynı görselde karşılaştır.

### Bounding Boxes (Ex 25, P8)
- `cv2.rectangle(img, (x, y), (x + w, y + h), ...)`: `pt1` sol üst köşe, `pt2` sağ alt köşe.

### Dosya yolları ve klasörler
- Kural: üretilen dosyalar `outputs/` altına yazılır (git-ignored). `m01a_opencv_core_v2` ise `OUTPUT_DIR = Path("cv_outputs")` kullanıyor; `cv_outputs/` git-ignored değil. Düzeltmesi bende.
- Proje klasörü taşınınca göreli yollar bozulabilir (taşımadan sonra `m01a`'daki maske kaydı `outputs/duck_yellow_mask.png` olarak düzeltildi). Notebook'lar her zaman `learning/` klasöründen çalıştırılır.

### Ortam
- PyCharm'da `.ipynb` çıktıları görünmediği için terminalden `.py` çalıştırmaya geçildi. Bu kalıcı akış olarak kalabilir; görsel çıktı için `cv2.imwrite` ile dosyaya yaz veya `matplotlib` kullan.
- `environment.yml`'de `numpy=2.5` gibi kısmi sürümler PyCharm'da yanlış "requirements not satisfied" uyarısı verir (`=2.5`i `==2.5.0` okuyor). Tam sürüm yaz: `2.5.1`.

## Oturum günlüğü

### 2026-11-05 — cvtools.py İngilizceleştirme, kod kuralları, doküman düzeni
- `learning/cvtools.py` içindeki docstring ve açıklamalar İngilizceye çevrildi (açık isteğimle istisna; kod gövdelerine dokunulmadı).
- Claude kurallarına eklendi: `learning/` kuralı `.py` dosyalarını da kapsar; koddaki her şey İngilizce olur (davranışı belirleyen string değerler hariç).
- `diagnose_exposure`'ın döndürdüğü `"karanlık"` / `"aşırı parlak"` / `"normal"` değerleri bilerek Türkçe bırakıldı (test hücresi karşılaştırıyor olabilir).
- `load_bgr` hata mesajındaki `image::` yazım hatası düzeltildi.
- Dokümanlar yeniden düzenlendi: `plan.md` ve `lessons.md` kaldırıldı; içerikleri `README.md`, `PROGRESS.md` ve bu dosyaya taşındı. Oturum günlüğü artık burada.
- **Açık iş:** `m01a_v2`'deki `cv_outputs/` → `outputs/`; `images/facade.jpg` henüz yok (final v1 için gerekli); `m01a_v2` ve `m01b_v2` henüz commit edilmedi.
- **Sıradaki:** `m01a_v2` Problem 1: `show()`'u yaz, test hücresi `✓`.

### 2026-11-02 — Proje yeniden adlandırma ve ortam düzeni
- Remote ve yerel repo `industrial-ai-ml-prep` → `vision-ml-rnd` olarak yeniden adlandırıldı, proje klasörü taşındı.
- Notebook'lar modül numarasına göre yeniden adlandırıldı (commit `3532c16`).
- Taşımadan sonra bozulan yol düzeltildi: `m01a` 24. hücre maskeyi `outputs/duck_yellow_mask.png` olarak kaydediyor.
- Conda env `vision-ml-rnd` adıyla klonlandı, Jupyter kernel kaydedildi, `environment.yml` ve README kurulum bölümü eklendi.
- Tüm notebook'lar yeni ortamda baştan sona çalıştırıldı: m07+ dışında hata yok (onlarda `torch` yok, beklenen durum).
- PyCharm yorumlayıcısı `vision-ml-rnd`'e geçirildi. Eski env `industrial-ai-ml-prep` ve Jupyter kernel'i silindi.
- `environment.yml` sürümleri tam sürüme sabitlendi (`numpy=2.5` → `2.5.1` vb.).
- Repo düzeni gözden geçirildi: `.gitattributes` eklendi (LF), `rnd/README.md` tablosu tamamen İngilizce yapıldı. Bilinçli olarak bırakılanlar: `archive/` adları (dondurulmuş), `learning/data/m2_images` → `m02_images` (m02 notebook kodunda geçiyor, Modül 2'de kendim değiştireceğim).
- **Sıradaki:** `m01b` (dönüşümler + morfoloji).
