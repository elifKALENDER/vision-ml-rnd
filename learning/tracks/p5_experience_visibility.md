# P5 — Deneyim ve görünürlük (Faz B'den itibaren, paralel)

Kendi kanıt hiyerarşin şöyleydi: kurs < kişisel proje < GitHub + tekrar üretilebilir deney < Kaggle < gerçek ekip/araştırma deneyimi. Bu hat, sıralamanın en üst iki basamağını KPSS sürecinde de mümkün olan ölçüde kurar.

## 1. Açık kaynak merdiveni (Faz B → D)

Her basamak bir öncekinden sonra:

1. **Issue reproduction:** diffusers, ultralytics, kornia, nerfstudio veya fiftyone'da açık bir bug'ı minimal örnekle tekrar üret, issue'ya yaz.
2. **Docs PR:** Bir dokümantasyon hatası veya eksik örnek.
3. **Test PR:** Kapsanmayan bir fonksiyona test.
4. **Küçük bug fix PR.**
5. **Örnek/tutorial katkısı:** Kendi alanından, örneğin mimari görsellerle bir ControlNet örneği.

Hedef: Faz D sonunda en az bir merge edilmiş PR.

## 2. Yayın

- Her RND → GitHub (`rnd/`) + Medium'da Türkçe kısa versiyon + LinkedIn gönderisi.
- LinkedIn formatı: Problem → Approach → Experiment → Result → Limitation → Next. Bir figür. Başarısız deneyler de paylaşılır.
- Her faz sonunda bir tutorial: o fazın en zor kavramı, kendi örneklerinle.

## 3. Network

- Ayda 1 R&D insanına bağlam + ilgi + ne yaptığın + öğrenme niyetiyle yaz. İlk mesajda iş isteme.
- Şablon (eski planından): *"Hi, I am an architect working on computer vision and visual AI projects (MassToRender, SketchToRender). I am building a corpus of reproducible experiments and found your work on [topic] relevant. I would be happy to learn how you approached [specific question]."*
- Eski TeknoKent bağlantıların ve Kocaeli'deki üniversiteler (ör. Gebze Teknik Üniversitesi, Kocaeli Üniversitesi) CV/AI laboratuvarları.

## 4. Ortak deney

- Faz C'den itibaren: bir araştırmacı, doktora öğrencisi ya da açık kaynak ekibiyle **tek bir ortak deney**. Senin verin ya da benchmark'ın, onların yöntemi gibi.
- Çıktı: ortak bir RND veya bir workshop/poster başvurusu.

## 5. İş dönüşümü (zamanı gelince, KPSS planına göre)

Eski planın 11–12. aylarındaki adımlar, sen başlatana kadar beklemede:

- CV konumlandırması: *"Architect working on computer vision and visual AI R&D; builds reproducible benchmarks for architectural image generation."* Kanıt seviyesini aşan başlıklardan kaçın.
- Portfolyo sırası: MassToRender benchmark (RND-016) → MassToRender derinlik (RND-014) → SketchToRender (RND-001) → ImageToRender (RND-007) → Detection/Segmentation (RND-009/010) → Kaggle write-up'ları.
- Hedefli başvurular (sayı değil uyum), mülakat provası (P3).

## Modül sonu kontrolü (her modülde)

- [ ] Bu modülün RND'si yayında mı (GitHub + Medium + LinkedIn)?
- [ ] Bu ay bir R&D insanına ulaştım mı?
- [ ] Açık kaynak merdiveninde bir basamak çıktım mı?
