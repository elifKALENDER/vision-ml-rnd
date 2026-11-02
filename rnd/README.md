# R&D reports

Each report lives in its own folder: `RND-NNN-<topic>/` with `report.md`, `figures/`, `configs/`. Technical notes (TN) are shorter method notes. Negative results are reports too.

| No | Module | Question | Finding | Status |
|---|---|---|---|---|
| RND-001 | 1 | SketchToRender: how does sketch preprocessing (raw / Canny / adaptive threshold) change line fidelity of the render? | — | planned |
| RND-002 | 2 | Dataset audit + leakage-free baseline: how much does a group split change the score? | — | planned |
| RND-003 | 3 | Faz B'deki derin modellerin karşısına konacak en güçlü klasik baseline hangisi? | — | planned |
| TN-001 | 4 | ML matematiği | — | planned |
| TN-002 | 5 | Deney tasarımı ve istatistik | — | planned |
| RND-004 | 6 | Sıfırdan yazılmış bir MLP, küçük veride klasik baseline'ı geçebiliyor mu; init ve optimizer seçimi ne kadar fark yaratıyor? | — | planned |
| RND-005 | 7 | Küçük bir mimari görsel setinde sıfırdan eğitilmiş küçük bir CNN, klasik baseline'ı geçiyor mu? | — | planned |
| RND-006 | 8 | Küçük mimari veri setlerinde transfer learning: linear probe mu, kısmi mi, tam fine-tune mu? | — | planned |
| RND-007 | 9 | Tarihi yapı elemanları için az örnekli sınıflandırmada hangi donmuş özellikler en iyi: ResNet, DINOv2, CLIP? | — | planned |
| RND-008 | 10 | Kendi etiketlerim ne kadar tutarlı ve bu, ulaşılabilecek en yüksek mAP için ne anlama geliyor? | — | planned |
| RND-009 | 11 | Gerçek + sentetik görsellerle eğitilen bir detector, cephedeki pencereleri güvenilir şekilde sayabiliyor mu? | — | planned |
| RND-010 | 12 | Cephe elemanı segmentasyonunda SAM 2 sıfır-atış mı, eğitilmiş U-Net mi? | — | planned |
| RND-011 | 13 | Sabit bir kameradan elde edilen yaya yörüngeleri arzu yollarını ortaya çıkarabilir mi? | — | planned |
| RND-012 | K1 | Bu yarışmada skoru en çok ne değiştirdi: veri, çözünürlük, backbone, ensemble? | — | planned |
| RND-013 | 14 | Tekrarlı cephelerde klasik (SIFT + RANSAC) mi öğrenilmiş (LightGlue) eşleştirme mi daha güvenilir? | — | planned |
| RND-014 | 15 | MASt3R derinliği, orijinal ve clay ön işlemeli girdilerde Blender ground truth'a göre ne kadar farklı? | — | planned |
| RND-015 | 16 | RTX 2060'ta SD 1.5 için adım sayısı × scheduler: kalite (CLIP/FID) ve süre dengesi nerede? | — | planned |
| RND-016 | 17 | MassToRender benchmark v1: yapıyı hangi ControlNet bileşeni, malzemeyi hangisi taşıyor? | — | planned |
| RND-017 | 18 | Modellerimin RTX 2060'ta dağıtım maliyeti: PyTorch FP32, FP16, ONNX ve TensorRT karşılaştırması | — | planned |
| RND-018 | K2 | Kaggle 1'e göre ne değişti: hangi yeni yöntem kaç sıra kazandırdı? | — | planned |
