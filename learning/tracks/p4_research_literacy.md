# P4 — Araştırma okuryazarlığı (Faz B'den itibaren)

Hedef: Bir makaleyi okuyup ne iddia ettiğini, nasıl ölçtüğünü ve neyi göstermediğini 1 sayfada yazabilmek; bir sonucu yeniden üretebilmek.

## Yöntem: üç geçiş ([Keshav, How to Read a Paper](https://web.stanford.edu/class/ee384m/Handouts/HowtoReadPaper.pdf))

1. **5–10 dk:** başlık, abstract, giriş, bölüm başlıkları, sonuç. Çıktı: makale hangi problemi, hangi iddiayla çözüyor?
2. **1 saat:** figürler, tablolar, deney kurulumu. Çıktı: baseline ne, metrik ne, ablation'lar ne gösteriyor?
3. **Gerektiğinde:** yöntemi kafanda yeniden kur; varsayımları ve zayıf noktaları listele.

## Makale notu şablonu (`papers/<yıl>-<kısa-ad>.md`)

```markdown
# <Title> (<year>)
Link: · Read: <date> · Passes: 1/2/3
## Problem
## Claim (one sentence)
## Method (5 lines)
## Evidence: baselines, metrics, datasets, key table
## What it does NOT show
## Relevance to my work (MassToRender / ImageToRender / …)
## Questions
```

## Okuma sırası (modüllerle birlikte)

**Modül 5 — Deney tasarımı ve istatistik**
- [Henderson et al. — Deep RL that Matters (seed variance)](https://arxiv.org/abs/1709.06560)

**Modül 6 — Sinir ağları sıfırdan + optimizasyon**
- [Adam (Kingma & Ba)](https://arxiv.org/abs/1412.6980)
- [Batch Normalization](https://arxiv.org/abs/1502.03167)

**Modül 7 — PyTorch + eğitim zanaatı**
- [Cyclical LR / LR range test (Smith)](https://arxiv.org/abs/1506.01186)

**Modül 8 — CNN mimarileri + transfer learning**
- [VGG](https://arxiv.org/abs/1409.1556)
- [ResNet](https://arxiv.org/abs/1512.03385)
- [MobileNets](https://arxiv.org/abs/1704.04861)
- [Grad-CAM](https://arxiv.org/abs/1610.02391)

**Modül 9 — Transformer, self-supervised, multimodal**
- [Attention Is All You Need](https://arxiv.org/abs/1706.03762)
- [ViT](https://arxiv.org/abs/2010.11929)
- [SimCLR](https://arxiv.org/abs/2002.05709)
- [MAE](https://arxiv.org/abs/2111.06377)
- [DINOv2](https://arxiv.org/abs/2304.07193)
- [CLIP](https://arxiv.org/abs/2103.00020)

**Modül 10 — Dataset engineering (+ Blender sentetik veri)**
- [Datasheets for Datasets](https://arxiv.org/abs/1803.09010)

**Modül 11 — Object detection**
- [Faster R-CNN](https://arxiv.org/abs/1506.01497)
- [YOLO](https://arxiv.org/abs/1506.02640)
- [FPN](https://arxiv.org/abs/1612.03144)
- [DETR](https://arxiv.org/abs/2005.12872)

**Modül 12 — Segmentation**
- [U-Net](https://arxiv.org/abs/1505.04597)
- [DeepLabV3](https://arxiv.org/abs/1706.05587)
- [Mask R-CNN](https://arxiv.org/abs/1703.06870)
- [Segment Anything](https://arxiv.org/abs/2304.02643)

**Modül 13 — Video + tracking**
- [SORT](https://arxiv.org/abs/1602.00763)
- [RAFT](https://arxiv.org/abs/2003.12039)
- [ByteTrack](https://arxiv.org/abs/2110.06864)

**Modül 14 — Projektif geometri + kamera**
- [SIFT (Lowe 2004)](https://www.cs.ubc.ca/~lowe/papers/ijcv04.pdf)
- [SuperGlue](https://arxiv.org/abs/1911.11763)
- [LightGlue](https://arxiv.org/abs/2306.13643)
- [LoFTR](https://arxiv.org/abs/2104.00680)

**Modül 15 — Multi-view geometri + 3D rekonstrüksiyon**
- [DUSt3R](https://arxiv.org/abs/2312.14132)
- [MASt3R](https://arxiv.org/abs/2406.09756)
- [NeRF](https://arxiv.org/abs/2003.08934)
- [3D Gaussian Splatting](https://arxiv.org/abs/2308.04079)
- [PointNet](https://arxiv.org/abs/1612.00593)
- [Depth Anything](https://arxiv.org/abs/2401.10891)

**Modül 16 — Generative I — diffusion temeli**
- [VAE](https://arxiv.org/abs/1312.6114)
- [GAN](https://arxiv.org/abs/1406.2661)
- [DDPM](https://arxiv.org/abs/2006.11239)
- [DDIM](https://arxiv.org/abs/2010.02502)
- [Classifier-free guidance](https://arxiv.org/abs/2207.12598)
- [Latent Diffusion](https://arxiv.org/abs/2112.10752)

**Modül 17 — Generative II — kontrollü üretim + değerlendirme**
- [ControlNet](https://arxiv.org/abs/2302.05543)
- [IP-Adapter](https://arxiv.org/abs/2308.06721)
- [LoRA](https://arxiv.org/abs/2106.09685)
- [MVDream](https://arxiv.org/abs/2308.16512)

**Modül K2 — Kaggle 2 (ölçülebilir hedef: Top %20)**
- [Model soups](https://arxiv.org/abs/2203.05482)

## Reprodüksiyon merdiveni

| Faz | Hedef | Örnek |
|---|---|---|
| B | Bir figürü yeniden üret | Grad-CAM figürü (Modül 8); DINOv2 patch PCA görselleştirmesi (Modül 9) |
| C | Küçük bir tabloyu yeniden üret | U-Net makalesindeki deneyin küçük ölçekli versiyonu; bir detection ablation'ı |
| D | Bir sonucu kendi verinde test et | MASt3R derinlik metriğini Blender GT ile; DDPM/DDIM adım-kalite eğrisi |

## Takip

- Haftada 10 dk: [Hugging Face Papers](https://huggingface.co/papers) ve arXiv cs.CV başlıkları. Sadece başlık + abstract; ilgini çekeni listeye ekle.
- Ayda 1 makale üç geçişle, notu `papers/` altına.
- Her RND'nin *Related work* paragrafı en az 2 makaleye atıf yapar.
