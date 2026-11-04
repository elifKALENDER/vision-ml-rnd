# R&D Planı

## Hedef
25 Ağustos 2027'ye kadar R&D / Computer Vision pozisyonlarında güçlü, kanıtlı ve işe alınabilir bir aday olmak.

- **Farklılaştırıcı katman:** Mimarlık + 3D/mekânsal akıl yürütme + Generative AI
- **Mühendislik omurgası:** Python + NumPy/OpenCV + PyTorch + dataset engineering + evaluation + Git/Linux

## Kaynak belge
Müfredatın tamamı (148 oturum, modül 0-18, tüm egzersizler): `docs/curriculum.md`
("AI CV R&D Müfredatı — Kurs Sırası ve R&D Külliyatı" belgesinin kendisi). **[ekle: orijinal belgeyi buraya koy]**

Bu dosya bir özettir; ayrıntı ve egzersiz tanımları için asıl kaynak o belgedir.

## Modüller

| # | Modül | Faz | Konu | Oturum |
|---|---|---|---|---|
| 0 | Python + NumPy | A | array, indexing, masking, broadcasting, vektörizasyon | [kontrol et] |
| 1 | Klasik CV | A | renk uzayları, threshold, blur, morfoloji, kenar, kontür, mask/bitwise, affine, histogram | [kontrol et] |
| 2 | Veri + ML baseline | A | pandas, EDA, manifest, kopya/bozuk tespiti, group split, leakage, Pipeline, CV, metrikler | 7 |
| 3 | Klasik ML | A | PCA, k-means, DBSCAN, lineer modeller, bias-variance, kNN, SVM, karar ağaçları, ensemble, hiperparametre arama | 7 |
| 4-18 | Faz B, C, D | B-D | ML matematiği, deney tasarımı, sinir ağları, PyTorch, CNN, Transformer, dataset engineering, object detection, segmentation, video + tracking, Kaggle, projektif geometri, multi-view + 3D, Generative AI, deployment | [curriculum.md'den doldur] |

Her modül bir öncekini ön koşul alır.

## Egzersiz durumu — Modül 1

Modül 1'de 45 egzersiz var. Ders notları ve hatalar her egzersizin kendi `README.md`'sinde (geçiş aşamasında: `lessons.md`).

| Ex | Başlık | Durum |
|---|---|---|
| 1-10 | [kontrol et: başlıkları curriculum.md'den ekle] | [kontrol et] |
| 11 | Color Histograms | Tamamlandı |
| 12 | Histogram as a Diagnostic | Tamamlandı |
| 13 | Equalize a Grayscale Image | Tamamlandı |
| 14 | Compare Blur Methods | Tamamlandı |
| 15 | Blur Parameter Experiment | Tamamlandı |
| 16 | Simple Threshold | Tamamlandı |
| 17 | Adaptive Threshold | Tamamlandı |
| 18 | Otsu | Tamamlandı |
| 19 | Sobel X / Y | Tamamlandı |
| 20 | Laplacian / Scharr | Tamamlandı — [kontrol et: Laplacian yapıldı mı?] |
| 21 | Canny Parameter Search | Tamamlandı |
| 22 | Blur Before Canny | Tamamlandı |
| 23 | Find Contours | Tamamlandı |
| 24 | Filter by Area | Tamamlandı — morfoloji sonrası tekrar ele alınacak (bkz. lessons.md) |
| 25 | Bounding Boxes | Tamamlandı |
| 26 | Translation | Devam ediyor |
| 27-45 | [curriculum.md'den] | Başlanmadı |

## Kaynaklar
- Kaggle OpenCV Tutorial: https://www.kaggle.com/code/talhabu/opencv-tutorial-from-basic-to-advanced
- OpenCV-Python resmi dokümantasyonu
- Hafta 2 Çalışma Kitabı (source-integrated practice)
- `docs/curriculum.md` — AI CV R&D Müfredatı

## Plan değişiklikleri
- **İngilizce gözlemler:** Kodlama sürecinde gözlemler İngilizce yazılıyor; "Teknik İngilizce" hedefine aynı anda hizmet etmesi için.
- **Yöntem sırası esnek:** Bir yöntem görsele uymadığında (ör. düşük kontrastta threshold) plan sırası beklenmeden uygun alternatife (Canny, HSV) geçilebilir.

## Şu an neredeyim
- **Egzersiz:** Modül 1 — Ex 26 (Translation)
- **Durum:** `cv2.warpAffine()` ve 2x3 öteleme matrisi `M = np.float32([[1, 0, tx], [0, 1, ty]])` anlaşıldı; kod henüz yazılıp test edilmedi.
- **Modül 1'de kalan oturum:** 6
- **Son güncelleme:** 2026-11-04
