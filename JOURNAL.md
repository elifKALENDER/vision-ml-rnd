# JOURNAL

Tekrar okuyup çalışmak için. **Hatalar ve dersler** (konuya göre) ve **Oturum günlüğü** (en yeni üstte). İlerleme durumu `PROGRESS.md`'de.

## Hatalar ve dersler

### P1 — `load_bgr`
- `cv2.imread` okuyamazsa hata vermez, `None` döndürür; hata sonradan çıkar. Hemen `FileNotFoundError` fırlat.
- Windows'ta Türkçe harfli yollar `imread`'de `None` verebilir.

### P1 — `show`
- `plt.subplots(1, 1)` dizi değil tek `Axes` döndürür. `squeeze=False` ile `axs` hep 2 boyutlu: `axs[r][c]`, kapatmak için `axs.ravel()`. Emin değilsen `print(axs.shape)`.
- `for i, img in enumerate(images)` tek döngü yeter; içine bir döngü daha koyma.
- Girinti = kapsam: `set_title` döngü dışına düşünce sadece son görüntü başlık aldı.
- Önceden kontrol edilebilen şey için `try/except` değil `if` + `raise ValueError`. `try/except` bilemediğin şeyler için (dosya açma, `imread`). Gövdesiz `except:` `SyntaxError` verir.
- Önce doğrula, sonra çiz. Bilgiyi `print` yerine hata mesajına yaz.
- Yarım `def` tüm `cvtools` import'unu bozar; kontrol: `python -c "import cvtools"`.
- Test: `m01a_opencv_core_v2` hücre 18 (`importlib.reload(cvtools)` ile kernel'i yeniden başlatmadan).

### P2 — `color_mask`, `apply_mask`
- Bir fonksiyon, bir iş: `color_mask` maskeyi **bulur** (`inRange`, `(H, W)` uint8, 0/255), `apply_mask` **uygular** (`bitwise_and`).
- Kod kopyalarken fonksiyonun parametrelerine bak (`NameError: lower_hsv`). Parametre olarak gelen maskeyi yeniden hesaplama.
- `cv2.resize` boyut uyumsuzluğunu sessizce gizler; hata olarak görünmeli.

### Blur (Ex 14–15)
- Yöntemleri karşılaştırırken kernel boyutunu hepsinde aynı tut.

### Sobel / Scharr (Ex 19–20)
- Gradyan operatörüne BGR değil gri görüntü ver.
- Sabit adı `cv2.CV_64F`.

### Find Contours (Ex 23)
- Benzer değişken adları (`counters`/`contours`) `NameError` üretir.
- `cv2.drawContours` görüntüyü yerinde değiştirir; `.copy()` üzerinde çiz.
- Düşük kontrastlı görselde global threshold nesneyi ayıramaz.

### Filter by Area (Ex 24)
- `filtered.append(cnt)`, `append(contours)` değil.
- Canny açık, ince kenar verir; `contourArea` nesnenin değil kenar şeridinin alanını ölçer. `min_area`'yı ayarlamak geçici çözüm.
- Doğrusu: Canny çıktısını `dilate`/`MORPH_CLOSE` ile kapatmak ya da dolu maske (HSV eşikleme) kullanmak.
- **Yapılacak:** 1b P11 (`clean_mask`) sonrası Ex 24'e dönüp iki yaklaşımı karşılaştır.

### Bounding Boxes (Ex 25)
- `cv2.rectangle(img, (x, y), (x + w, y + h), ...)`: sol üst ve sağ alt köşe.

### Yollar ve ortam
- Üretilen dosyalar `outputs/` altına (git-ignored). `m01a_v2` `cv_outputs/` kullanıyor, düzeltilecek.
- Notebook'lar `learning/` klasöründen çalıştırılır; klasör taşınınca göreli yollar bozulabilir.
- PyCharm'da `.ipynb` çıktısı görünmüyorsa terminalden `.py` çalıştır; görsel için `cv2.imwrite` veya `matplotlib`.
- `environment.yml`'de tam sürüm yaz (`2.5.1`); `2.5` PyCharm'da yanlış uyarı verir.

## Oturum günlüğü

### 2026-11-05 — cvtools düzeltmeleri, kurallar, doküman düzeni
- `cvtools.py` docstring'leri İngilizceye çevrildi. Kural: koddaki her şey İngilizce (`"karanlık"` gibi test edilen string'ler hariç).
- Dokümanlar yeniden düzenlendi: `plan.md` ve `lessons.md` kalktı, günlük bu dosyaya geldi.
- `load_bgr`, `show` (+`ncols`), `color_mask`, `apply_mask` yazıldı; ayrı scriptle sınandı, geçti.
- **Açık:** notebook hücre 18 ve 31 henüz çalıştırılmadı; `show` docstring'ine `ncols`; `cv_outputs/` → `outputs/`; `images/facade.jpg` yok; v2 notebook'lar ve `cvtools.py` commit edilmedi.
- **Sıradaki:** hücre 18 ve 31 `✓`, sonra P3 (`excess_green`).

### 2026-11-02 — Proje yeniden adlandırma ve ortam
- Repo `industrial-ai-ml-prep` → `vision-ml-rnd`; notebook'lar modül numarasıyla yeniden adlandırıldı.
- Conda env `vision-ml-rnd` kuruldu (`environment.yml`), Jupyter kernel kaydedildi, eski env silindi.
- Tüm notebook'lar çalıştırıldı: m07+ dışında hata yok (`torch` yok, beklenen).
- Bilerek bırakıldı: `archive/` adları, `learning/data/m2_images` (Modül 2'de kendim değiştireceğim).
- **Sıradaki:** `m01b`.
