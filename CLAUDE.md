# CLAUDE.md

Bu dosya her oturumun başında okunur. Oturum sonunda **Oturum günlüğü** bölümüne kısa bir kayıt eklenir.

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
- Notebook diff'leri gürültülü (base64 çıktılar). Değişikliklere hücre kaynağı üzerinden bak.

## Oturum günlüğü
<!-- En yeni en üstte. Her oturum: "### YYYY-MM-DD — konu", altında ne yapıldı, açık işler, sıradaki adım. -->

### 2026-11-02 — Proje yeniden adlandırma ve ortam düzeni
- Remote ve yerel repo `industrial-ai-ml-prep` → `vision-ml-rnd` olarak yeniden adlandırıldı, proje klasörü taşındı.
- Notebook'lar modül numarasına göre yeniden adlandırıldı (commit `3532c16`).
- Taşımadan sonra bozulan yol düzeltildi: `m01a` 24. hücre maskeyi `outputs/duck_yellow_mask.png` olarak kaydediyor.
- Conda env `vision-ml-rnd` adıyla klonlandı, Jupyter kernel kaydedildi, `environment.yml` ve README kurulum bölümü eklendi.
- Tüm notebook'lar yeni ortamda baştan sona çalıştırıldı: m07+ dışında hata yok (onlarda `torch` yok, beklenen durum).
- **Açık:** PyCharm yorumlayıcısı `vision-ml-rnd`'e geçirilecek, sonra eski env `industrial-ai-ml-prep` ve kernel'i silinecek.
- **Sıradaki:** `m01b` (dönüşümler + morfoloji).
