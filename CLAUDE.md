# CLAUDE.md

Bu dosya her oturumun başında okunur. Repo/ortam değişikliği yapılan oturumların sonunda **Altyapı günlüğü** bölümüne kısa bir kayıt eklenir.

## Proje
- Repo: `F:\vision-ml-rnd`, remote `https://github.com/elifKALENDER/vision-ml-rnd.git` (branch `main`).
- Klasik CV'den derin öğrenme, 3D ve generative modellere uzanan egzersiz temelli müfredat. Uzun vadeli hedef: **MassToRender** (bkz. README).
- Python ortamı: conda env `vision-ml-rnd` (`C:\Users\ekale\.conda\envs\vision-ml-rnd\python.exe`, Python 3.13), tanımı `environment.yml`'de. Jupyter kernel: `vision-ml-rnd`. Sistem `python` komutu yok, bu yolu kullan. Conda: `C:\ProgramData\anaconda3\Scripts\conda.exe`.
- `torch` henüz kurulu değil, Modül 7'de eklenecek. m07+ notebook'lar o zamana kadar `import torch`'ta durur.
- Doğrulama: tüm notebook'lar `learning/` çalışma diziniyle baştan sona çalıştırılarak test edilir.
- Müfredat ilerlemesi ve modül/oturum planı **`PROGRESS.md`**'de tutulur. Burada tekrarlanmaz.

## Klasör kuralları
- Notebook'lar `learning/` altında, modül numarasıyla adlandırılır (`m01a_…`, `k1_…`, `tracks/p1_…`).
- Girdiler `learning/images/`, `learning/data/` içinde.
- Üretilen dosyalar `learning/outputs/` içine yazılır (git-ignored). Notebook'lar göreli yol kullanır, `learning/` klasöründen çalıştırılır.

## Çalışma tarzı
- Türkçe konuş.
- Kullanıcı yazarak öğrenmek istiyor: düzeltmenin *nedenini* açıkla, anlamlı kısımları ona bırak, hazır çözüm verme.
- **`learning/` notebook'larındaki koda asla dokunma.** Bunlar öğrenme dosyaları. Kullanıcı hata alınca sorar: sebebini açıkla, ipucu ver, düzeltmeyi kendisi yapsın. Egzersizler ayrı bir Claude sohbetinde (öğrenme arşivi) yürütülüyor.
- Kural `learning/` altındaki **tüm dosyaları** kapsar (`.py` yardımcıları dahil, örn. `cvtools.py`), sadece `.ipynb`'yi değil. Kullanıcı o an açıkça isterse istisna yapılır; istisna sadece istenen kapsamla sınırlıdır.
- **Dil kuralı:** Koddaki her şey İngilizce olur: docstring'ler, yorumlar, hata mesajları, değişken/fonksiyon adları. Konuşma Türkçe kalır. İstisna: kodun davranışını belirleyen string değerler (örn. `diagnose_exposure`'ın döndürdüğü `"karanlık"`) testler karşılaştırdığı için kullanıcı değiştirmedikçe aynen kalır.
- Notebook diff'leri gürültülü (base64 çıktılar). Değişikliklere hücre kaynağı üzerinden bak.
- Oturum sonunda kullanıcı ders notları yapıştırırsa kökteki `lessons.md`'ye ekle (dosya zaten var, üzerine yazma, sonuna ekle); yapıştırmazsa sor.

## Altyapı günlüğü
<!-- Repo, ortam ve araç değişiklikleri. Egzersiz ilerlemesi burada değil, PROGRESS.md'deki "Oturum günlüğü"nde. En yeni en üstte. Her oturum: "### YYYY-MM-DD — konu", altında ne yapıldı, açık işler, sıradaki adım. -->

### 2026-11-05 — cvtools.py İngilizceleştirme ve kod kuralları
- `learning/cvtools.py` içindeki docstring ve açıklamalar İngilizceye çevirildi (kullanıcının açık isteğiyle istisna; kod gövdelerine dokunulmadı).
- "Çalışma tarzı"na iki kural eklendi: `learning/` kuralı `.py` dosyalarını da kapsar; koddaki her şey İngilizce olur (davranışı belirleyen string değerler hariç).
- `diagnose_exposure`'ın döndürdüğü `"karanlık"` / `"aşırı parlak"` / `"normal"` değerleri bilerek Türkçe bırakıldı (test hücresi karşılaştırıyor olabilir).
- **Açık iş:** `load_bgr` hata mesajındaki `image::` yazım hatası (kullanıcı düzeltecek).
- **Sıradaki:** `m01b` (dönüşümler + morfoloji).

### 2026-11-02 — Proje yeniden adlandırma ve ortam düzeni
- Remote ve yerel repo `industrial-ai-ml-prep` → `vision-ml-rnd` olarak yeniden adlandırıldı, proje klasörü taşındı.
- Notebook'lar modül numarasına göre yeniden adlandırıldı (commit `3532c16`).
- Taşımadan sonra bozulan yol düzeltildi: `m01a` 24. hücre maskeyi `outputs/duck_yellow_mask.png` olarak kaydediyor.
- Conda env `vision-ml-rnd` adıyla klonlandı, Jupyter kernel kaydedildi, `environment.yml` ve README kurulum bölümü eklendi.
- Tüm notebook'lar yeni ortamda baştan sona çalıştırıldı: m07+ dışında hata yok (onlarda `torch` yok, beklenen durum).
- PyCharm yorumlayıcısı `vision-ml-rnd`'e geçirildi. Eski env `industrial-ai-ml-prep` ve Jupyter kernel'i silindi.
- `environment.yml` sürümleri tam sürüme sabitlendi (`numpy=2.5` → `2.5.1` vb.): PyCharm `=2.5`i `==2.5.0` okuyup yanlış "requirements not satisfied" uyarısı veriyordu.
- Repo düzeni gözden geçirildi: `.gitattributes` eklendi (LF), `rnd/README.md` tablosu tamamen İngilizce yapıldı, bu bölüm "Altyapı günlüğü" olarak ayrıldı. Bilinçli olarak bırakılanlar: `archive/` adları (dondurulmuş), `learning/data/m2_images` → `m02_images` (m02 notebook kodunda geçiyor, kullanıcı Modül 2'de kendisi değiştirecek).
- **Sıradaki:** `m01b` (dönüşümler + morfoloji).
