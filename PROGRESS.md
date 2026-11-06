# PROGRESS

## Nerede kaldım
- **Modül 1, 1a** (`m01a_opencv_core_v2`). 25/25 egzersizin kodu yazılmış; v2'de egzersizler 8 problemin altına toplandı. `cvtools.py`'de P1–P7 araçları yazıldı ve ayrı scriptle sınandı. Notebook test hücreleri (`✓`) henüz çalıştırılmadı.
- **Sıradaki adım:** Notebook test hücrelerini P1–P7 için çalıştır (`importlib.reload(cvtools)`), sonra P8 — `find_boxes`, `draw_boxes`.
- Önceki plandan yarım kalan: Ex 26 (Translation, 1b'de 9.1). `cv2.warpAffine` ve `M = np.float32([[1, 0, tx], [0, 1, ty]])` anlaşıldı, kod henüz yazılıp test edilmedi.
- Son güncelleme: 2026-11-06

Oturum günlüğü ve hatalar: `JOURNAL.md`.

## Modüller

Dosya adı = modül numarası (`m03_…` → Modül 3, `k1_…` → Kaggle 1). 1 oturum = 5 egzersiz (Modül 1a/1b hariç: 1 oturum = 1 problem). Toplam (Modül 1'in eski 6 oturumluk planıyla): 159 oturum, ~795 egzersiz.

- [ ] **0 Python + NumPy** · `m00_numpy_core` · egzersizler bitti, düzeltmeler bekliyor
- [ ] **1 Klasik CV** · `m01a_opencv_core_v2` / `m01b_opencv_transforms_morph_v2` / `m01c_opencv_pipelines_rnd` · 0/17 · RND-001 (alt liste aşağıda)
- [ ] **2 Veri + ML baseline** · `m02_data_ml_baseline` · 0/7 · RND-002
- [ ] **3 Klasik ML derinleşme** · `m03_classical_ml` · 0/7 · RND-003
- [ ] **4 ML matematiği** · `m04_math_for_ml` · 0/8 · TN-001
- [ ] **5 Deney tasarımı ve istatistik** · `m05_experiment_stats` · 0/5 · TN-002
- [ ] **6 Sinir ağları sıfırdan + optimizasyon** · `m06_nn_from_scratch` · 0/7 · RND-004
- [ ] **7 PyTorch + eğitim zanaatı** · `m07_pytorch_training` · 0/8 · RND-005
- [ ] **8 CNN mimarileri + transfer learning** · `m08_cnn_transfer` · 0/6 · RND-006
- [ ] **9 Transformer, self-supervised, multimodal** · `m09_transformers_ssl_multimodal` · 0/8 · RND-007
- [ ] **10 Dataset engineering (+ Blender sentetik veri)** · `m10_dataset_engineering` · 0/6 · RND-008
- [ ] **11 Object detection** · `m11_detection` · 0/6 · RND-009
- [ ] **12 Segmentation** · `m12_segmentation` · 0/6 · RND-010
- [ ] **13 Video + tracking** · `m13_video_tracking` · 0/5 · RND-011
- [ ] **K1 Kaggle 1 (Faz C kapısı)** · `k1_kaggle` · 0/5 · RND-012
- [ ] **14 Projektif geometri + kamera** · `m14_projective_geometry` · 0/8 · RND-013
- [ ] **15 Multi-view geometri + 3D rekonstrüksiyon** · `m15_multiview_3d` · 0/8 · RND-014
- [ ] **15b Radyometri, PBR, differentiable rendering** · `m15b_rendering_pbr` · 0/6 · RND-019
- [ ] **16 Generative I — diffusion temeli** · `m16_diffusion_foundations` · 0/8 · RND-015
- [ ] **17 Generative II — kontrollü üretim + değerlendirme** · `m17_controlled_generation` · 0/8 · RND-016
- [ ] **18 Mühendislik, deployment ve verimlilik** · `m18_deployment_efficiency` · 0/6 · RND-017
- [ ] **K2 Kaggle 2 (ölçülebilir hedef: Top %20)** · `k2_kaggle` · 0/4 · RND-018
- [ ] **EK Ek oturumlar (A–D)** · `extras` · 0/5

**`extras` yerleşimi:** EK-A frekans alanı → Modül 4'ten sonra · EK-B belirsizlik → Modül 9'dan sonra · EK-C GPU/sistem → Modül 18 içinde · EK-D1–D2 ileri matematik → Faz D sonrası.

## Modül 0 ve 1'i kapatan oturumlar

**Modül 0 düzeltmeleri** (eski planda Oturum 1'in parçasıydı)
- [ ] `m00`: TODO 7, 8, 10, 15, 17 + Ex 2, 5, 6

**1a — `m01a_opencv_core_v2`** (her problem: eksik gözlem ve inceleme notlarını kapat → aracı `cvtools.py`'ye yaz → test `✓`)
- [ ] P1 Ex 1–4 → `load_bgr`, `show` (Ex 1 inceleme değerleri) · araç yazıldı, notebook testi bekliyor
- [ ] P2 Ex 5–6 → `color_mask`, `apply_mask` (Ex 6 HSV aralığını belgele) · araç yazıldı, notebook testi bekliyor
- [ ] P3 Ex 7–9 → `excess_green` (Ex 9 taşma ve BGR gösterim hataları) · araç yazıldı, notebook testi bekliyor
- [ ] P4 Ex 10–13 → `diagnose_exposure` · araç yazıldı, notebook testi bekliyor
- [ ] P5 Ex 14–15 → `smooth` · araç yazıldı, notebook testi bekliyor
- [ ] P6 Ex 16–18 → `binarize` (Ex 17 düzelt ve yorumla) · araç yazıldı, notebook testi bekliyor
- [ ] P7 Ex 19–22 → `edge_map` (Ex 22'yi tek değişkenle yeniden yap) · araç yazıldı, notebook testi bekliyor
- [ ] P8 Ex 23–25 → `find_boxes`, `draw_boxes`
- [ ] Final v1 → `outputs/facade_v1.png` + karar kaydı (`images/facade.jpg` gerekli, henüz yok)

**1b — `m01b_opencv_transforms_morph_v2`** (Ex 26–35)
- [ ] P9 Ex 26–29 → `rotate`, `resize_scale`
- [ ] P10 Ex 30 → `crop_boxes`
- [ ] P11 Ex 31–32 → `clean_mask` (sonra Ex 24'e dön, bkz. JOURNAL)
- [ ] P12 Ex 33–35 → `combine`
- [ ] Final v2 → `outputs/facade_v2.png`, `outputs/windows/` + karar kaydı

**1c — `m01c_opencv_pipelines_rnd`** (Ex 36–45)
- [ ] Ex 36–40: mini pipeline'lar ve kontrollü deney
- [ ] Kapanış: AI'sız final challenge, klasör pipeline'ı (`pipeline.py`), RND-001 taslağı
- [ ] Ex 41–45: sıfırdan convolution, Modül 1 kapanış

## Paralel hatlar (`learning/tracks/`)
- [ ] **P1 Python mühendisliği** · `p1_python_engineering.ipynb` · 0/6
- [ ] **P2 CS temeli — algoritmalar ve veri yapıları** · `p2_cs_algorithms.ipynb` · 0/10
- [ ] **P3 Teknik İngilizce** · `p3_technical_english.md` · günlük 15–20 dk
- [ ] **P4 Araştırma okuryazarlığı** · `p4_research_literacy.md` · ayda 1 makale
- [ ] **P5 Deneyim ve görünürlük** · `p5_experience_visibility.md` · modül sonu kontrolü

## Plan notları
- Gözlemler İngilizce yazılıyor; P3 (Teknik İngilizce) hedefine aynı anda hizmet etsin diye.
- Yöntem sırası esnek: bir yöntem görsele uymadığında (ör. düşük kontrastta threshold) plan sırası beklenmeden uygun alternatife (Canny, HSV) geçilebilir.
