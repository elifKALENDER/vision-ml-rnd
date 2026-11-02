# MIUUL Python Coding Camp Plan

## Amaç

Bu programın amacı yeni bir Python kursu bitirmek değil; daha önce gördüğün konuları **boş dosyadan çalışan koda dönüştürme refleksini** güçlendirmek.

Ana hedefler:

- Python temel yapılarını tekrar otomatik hâle getirmek
- Fonksiyon, döngü, koleksiyon ve comprehension kullanımını bağımsız yazabilmek
- CSV / JSON / dosya işlemlerinde rahatlamak
- NumPy ve Pandas ile veri analiz akışını sıfırdan başlatabilmek
- Veri temizleme, filtreleme, `groupby`, `agg`, `merge`, EDA gibi işlemleri uygulayabilmek
- `pytest` ile kendi fonksiyonların için test senaryoları yazmak
- AI'yi kod üreticisi yerine **reviewer / tutor / implementasyon yardımcısı** olarak kullanmak
- Sonraki ML ve Industrial AI çalışmalarına sağlam bir pratik tabanı oluşturmak

---

# 1. Kullanılacak MIUUL Kaynakları

## Şu anda elimizde olan kaynaklar

### `data_structures.py`
Referans konuları:

- `int`, `float`, `str`, `bool`
- list
- dictionary
- tuple
- set
- indexing / slicing
- string methods
- `append`, `pop`, `insert`
- `keys`, `values`, `items`
- type conversion

### `functions_conditions_loops_comprehensions.py`
Referans konuları:

- function tanımlama
- parameters / default parameters
- docstring
- `return`
- fonksiyon içinde fonksiyon çağırma
- local / global variables
- `if / elif / else`
- `for`
- `while`
- `break / continue`
- `enumerate`
- `zip`
- `lambda`
- `map`
- `filter`
- `reduce`
- list comprehension
- dict comprehension

### `data_analysis_with_python.py`
Referans konuları:

- NumPy
- array oluşturma
- `shape`, `size`, `dtype`, `ndim`
- indexing / slicing
- conditional selection
- matematiksel işlemler
- Pandas Series
- `read_csv`
- `head`, `tail`, `shape`, `info`, `columns`, `describe`
- missing values
- selection
- `loc / iloc`
- conditional filtering
- `groupby`
- `agg`
- pivot table
- `apply / lambda`
- `concat / merge`
- Matplotlib
- EDA
- categorical / numerical variable analysis

### `setting_up_working_environment.py`
Cheat sheet olarak kullanılacak:

- Conda environment
- activate / deactivate
- package install/remove/update
- pip

Bu dosya için özel çalışma günü ayrılmayacak.

---

# 2. Ana Çalışma Kuralı

Her problemde aynı protokol uygulanacak:

1. **Problemi kendi cümlelerinle 2–6 adıma böl.**
2. İlk **10–15 dakika AI yok.**
3. Önce boş dosyadan kendin yaz.
4. Syntax tamamen unutulduysa MIUUL referans dosyasında yalnızca ilgili bölüme kısa süre bak.
5. Hâlâ takılırsan ChatGPT'den sırasıyla:
   - küçük ipucu,
   - syntax hatırlatma,
   - minimum düzeltme,
   - en son tam çözüm iste.
6. Çalışan kodu anlamadan geçme.
7. Fonksiyon yazdıysan mümkün olduğunda test yaz.
8. Gün sonunda en az **2 görevi boş dosyada yeniden yaz.**

## Yasaklanan çalışma biçimi

Bu hafta mümkün olduğunca:

- videoyu açıp kodu birebir takip etmek
- kaynak `.py` dosyasındaki çözümü kopyalamak
- ilk zorlukta AI'den tam kod istemek
- aynı anda yeni framework öğrenmeye geçmek
- sadece kod okuyup "anladım" diyerek ilerlemek

yapılmayacak.

---

# 3. Günlük Rutin

Yoğun gün için hedef: yaklaşık **5–7 saat gerçek çalışma**.

## Blok A — Core Coding
**90 dakika**

- saf Python
- fonksiyonlar
- collections
- küçük algoritmalar
- comprehension

## Blok B — Data Coding
**90–120 dakika**

- CSV / JSON
- NumPy / Pandas
- data cleaning
- analysis

## Blok C — Test ve Debug
**45–60 dakika**

- pytest
- edge cases
- traceback
- refactor

## Blok D — Exercism
**30–45 dakika**

- 2–5 problem
- ilk deneme tamamen AI'siz
- mümkünse bir problemi siteyi kapattıktan sonra yeniden yaz

## Blok E — Blank File Repeat
**30–45 dakika**

O gün çözdüğün 2 problemi:

- notlara bakmadan
- eski dosyayı açmadan
- sıfırdan

tekrar yaz.

---

# 4. 7 Günlük Yoğun Kamp

---

## GÜN 1 — Core Python Reactivation

### Kaynak
- `data_structures.py`
- `functions_conditions_loops_comprehensions.py`
- mevcut `exercises.py`

### Konular

- [ ] `if / elif / else`
- [ ] function
- [ ] parameter
- [ ] `return` vs `print`
- [ ] list
- [ ] dictionary
- [ ] tuple
- [ ] set
- [ ] loop
- [ ] accumulator
- [ ] `append`
- [ ] basic file read/write

### Mevcut çalışma dosyası

Önce eski `exercises.py` içindeki kalan görevleri tamamla:

- [ ] Exercise 9 — CSV/Pandas filtering
- [ ] Exercise 10 — Mini Industrial Anomaly Report
- [ ] Exercise 11 — JSON
- [ ] Exercise 12 — try/except

### Sonra

`miuul_python_homework_01_core.py`

içinden ilk bölümlere başla.

Hedef:

- [ ] Exercises 1–15
- [ ] Fonksiyonların en az yarısı için pytest
- [ ] 2 problemi boş dosyada yeniden yaz

### Gün sonu kriteri

Şunları bakmadan açıklayabilmelisin:

- `return` ve `print` farkı
- list / tuple / dict / set farkı
- `for` + accumulator
- dictionary key/value erişimi
- bir fonksiyonun input/output mantığı

---

## GÜN 2 — Loops, Enumerate, Zip, Comprehensions

### Kaynak
`functions_conditions_loops_comprehensions.py`

### Konular

- [ ] nested loops
- [ ] `break`
- [ ] `continue`
- [ ] `while`
- [ ] `enumerate`
- [ ] `zip`
- [ ] lambda
- [ ] `map`
- [ ] `filter`
- [ ] `reduce`
- [ ] list comprehension
- [ ] dict comprehension
- [ ] ternary / conditional expression

### Homework

`miuul_python_homework_01_core.py`

- [ ] Exercises 16–27
- [ ] Final Challenge
- [ ] pytest

### Ek çalışma

Aynı problemi mümkünse iki şekilde çöz:

1. normal `for`
2. comprehension / functional yaklaşım

Örnek düşünce:

```text
filter with loop
→ filter with list comprehension
→ compare readability
```

### Gün sonu AI'siz tekrar

- [ ] `enumerate` kullanılan bir problem
- [ ] `zip` kullanılan bir problem
- [ ] list comprehension
- [ ] dict comprehension
- [ ] list-of-dicts üzerinde filtreleme

---

## GÜN 3 — NumPy + Pandas Foundations

### Kaynak
`data_analysis_with_python.py`

### NumPy

- [ ] `np.array`
- [ ] `shape`
- [ ] `size`
- [ ] `dtype`
- [ ] `ndim`
- [ ] indexing
- [ ] slicing
- [ ] conditional selection
- [ ] `mean`
- [ ] `sum`
- [ ] `min`
- [ ] `max`
- [ ] `var`

### Pandas başlangıç

- [ ] `Series`
- [ ] `DataFrame`
- [ ] `pd.read_csv`
- [ ] `head`
- [ ] `tail`
- [ ] `shape`
- [ ] `info`
- [ ] `columns`
- [ ] `dtypes`
- [ ] `describe`
- [ ] missing-value inspection

### Ana veri

`machine_sensor_dirty.csv`

üzerinden çalış.

### Görevler

- [ ] CSV oku
- [ ] shape bul
- [ ] dtypes incele
- [ ] missing değerleri say
- [ ] duplicate kontrol et
- [ ] şüpheli dtype tespit et
- [ ] numeric conversion yap
- [ ] status stringlerini normalize et

### Dosya

`day02_python_data_intensive.py`

Block A + Block B tamamlanacak.

---

## GÜN 4 — Pandas Analysis

### Kaynak
`data_analysis_with_python.py`

### Konular

- [ ] column selection
- [ ] `loc`
- [ ] `iloc`
- [ ] boolean filtering
- [ ] birden fazla koşul
- [ ] `&`
- [ ] `|`
- [ ] `groupby`
- [ ] `agg`
- [ ] sorting
- [ ] yeni column oluşturma
- [ ] `apply`
- [ ] lambda
- [ ] `concat`
- [ ] `merge`

### Ana görevler

`machine_sensor_dirty.csv` üzerinden:

- [ ] temperature > 80
- [ ] vibration > 2.5
- [ ] pressure > 50
- [ ] temperature > 85 OR vibration > 2.5
- [ ] anomaly column
- [ ] anomaly rate
- [ ] status bazlı groupby
- [ ] mean / median / max / min
- [ ] top risky machines
- [ ] basit risk score

### Çıktı

Küçük bir:

`machine_sensor_cleaned.csv`

oluştur.

---

## GÜN 5 — EDA + Visualization + Reusable Analysis

### Kaynak
`data_analysis_with_python.py`

### Konular

- [ ] genel veri resmi
- [ ] categorical variable analysis
- [ ] numerical variable analysis
- [ ] `value_counts`
- [ ] ratios
- [ ] quantiles
- [ ] histogram
- [ ] boxplot
- [ ] temel Matplotlib
- [ ] correlation kavramına giriş

### Fonksiyon pratiği

Kendi versiyonlarını yaz:

- [ ] `check_df(df)`
- [ ] `categorical_summary(df, column)`
- [ ] `numerical_summary(df, column)`

MIUUL çözümünü kopyalama.

Önce davranışı tarif et, sonra kendin implement et.

### Çıktı

Bir veri seti için:

- [ ] genel özet
- [ ] missing summary
- [ ] categorical summary
- [ ] numerical summary
- [ ] 3 grafik
- [ ] her grafik için 1–2 cümle yorum

---

## GÜN 6 — Mini Data Engineering / Analysis Pipeline

### Ana çalışma

`day02_python_data_intensive.py`

Block C + Block D tamamlanacak.

### Fonksiyonlar

- [ ] `load_sensor_data(path)`
- [ ] `clean_sensor_data(df)`
- [ ] `add_anomaly_feature(df)`
- [ ] `summarize_sensor_data(df)`
- [ ] `run_pipeline(input_path, output_path)`

### Akış

```text
raw CSV
↓
load
↓
validation
↓
cleaning
↓
feature creation
↓
analysis
↓
summary
↓
clean CSV
↓
JSON summary
```

### Test

Minimum testler:

- [ ] loader
- [ ] duplicate removal
- [ ] numeric conversion
- [ ] status normalization
- [ ] anomaly rule
- [ ] summary calculations

### Mühendislik soruları

Kod bittikten sonra cevapla:

- Fonksiyon neden `return` ediyor?
- Neden DataFrame'i `.copy()` etmek isteyebilirsin?
- Bozuk bir numeric değer nasıl ele alındı?
- Missing value stratejin ne?
- Hangi assumptions var?
- Production ortamında ne eksik?

---

## GÜN 7 — AI'siz Sınav + Refactor

### Bölüm 1 — 60 dakika AI yok

Daha önce görmediğin bir CSV kullan.

Yap:

- [ ] CSV oku
- [ ] shape / dtype
- [ ] missing values
- [ ] duplicates
- [ ] cleaning
- [ ] filtering
- [ ] groupby
- [ ] anomaly feature
- [ ] summary
- [ ] temiz CSV kaydet
- [ ] en az 2 reusable function
- [ ] en az 3 pytest test

### Bölüm 2 — Review

Testten sonra ChatGPT ile kod review:

- yanlış algoritma kararları
- gereksiz global variables
- `print` yerine `return`
- naming
- duplicated logic
- edge cases
- readability
- test coverage

### Bölüm 3 — Blank File

Hiçbir dosyaya bakmadan yaz:

- [ ] küçük bir function
- [ ] list/dict problem
- [ ] CSV read
- [ ] Pandas filter
- [ ] groupby
- [ ] pytest test

---

# 5. Haftalık Başarı Ölçütü

Hafta sonunda aşağıdakilere `Evet / Kısmen / Hayır` ver.

| Beceri | Durum |
|---|---|
| Boş dosyadan function yazabiliyorum | |
| `return` / `print` farkı refleks oldu | |
| list/dict/tuple/set farklarını biliyorum | |
| accumulator yazabiliyorum | |
| nested list/dict okuyabiliyorum | |
| comprehension yazabiliyorum | |
| `enumerate` ve `zip` kullanabiliyorum | |
| CSV okuyabiliyorum | |
| DataFrame incelemeyi kendim başlatabiliyorum | |
| missing values bulabiliyorum | |
| duplicate temizleyebiliyorum | |
| dtype problemi fark edebiliyorum | |
| conditional filtering yapabiliyorum | |
| `groupby/agg` yapabiliyorum | |
| basit EDA yapabiliyorum | |
| fonksiyonlarımı pytest ile test edebiliyorum | |
| traceback okuyup hata hipotezi kurabiliyorum | |
| AI olmadan 45–60 dk kod yazabiliyorum | |

---

# 6. Git Çalışma Düzeni

Repo:

`industrial-ai-ml-prep`

Önerilen yapı:

```text
industrial-ai-ml-prep/
│
├── reference/
│   ├── data_structures.py
│   ├── functions_conditions_loops_comprehensions.py
│   ├── data_analysis_with_python.py
│   └── setting_up_working_environment.py
│
├── day-01-python-reactivation/
│   ├── exercises.py
│   └── test_exercises.py
│
├── homework/
│   ├── miuul_python_homework_01_core.py
│   └── test_homework_01.py
│
├── data-practice/
│   ├── day02_python_data_intensive.py
│   ├── machine_sensor_dirty.csv
│   └── test_day02_python_data.py
│
└── README.md
```

### Commit yaklaşımı

Küçük ama anlamlı commit'ler:

```text
day 1: complete core Python reactivation
day 2: practice comprehensions and functional tools
day 3: add NumPy and Pandas exercises
day 4: clean and analyze sensor dataset
day 5: add reusable EDA functions
day 6: build sensor data pipeline
day 7: complete no-AI coding assessment
```

---

# 7. Exercism Kuralı

Her gün:

- 30–45 dakika
- 2–5 problem
- ilk deneme AI'siz
- çözümü hemen açma
- bir problemi sonradan boş dosyada tekrar yaz

Exercism ana kurs değildir.

Görevi:

**coding fluency + problem-solving repetition**

---

# 8. İngilizceyi Programa Dahil Etme

Kod pratiği aynı zamanda teknik İngilizce pratiği olacak.

Her gün:

- değişken isimleri İngilizce
- function isimleri İngilizce
- docstring İngilizce
- commit mesajı İngilizce
- gün sonunda 5 dakika yaptığın işi İngilizce anlat

Örnek günlük sorular:

- What does this function return?
- Why did you use a dictionary here?
- What caused the error?
- How did you handle missing values?
- Why did you choose this filtering condition?
- What would you improve in production?

---

# 9. Sonraki Aşama — Machine Learning

Şu anda yüklenen MIUUL Python/Data Analysis dosyaları temel Python, NumPy, Pandas ve EDA tarafını kapsıyor.

Machine Learning kursu dosyaları ayrıca incelendikten sonra ayrı bir:

**Homework 04 — Machine Learning Fundamentals**

oluşturulacak.

Planlanan başlıklar, yalnızca ilgili MIUUL kaynakları doğrulandıktan sonra detaylandırılacak:

- train/test
- preprocessing
- baseline model
- fit / predict
- metrics
- model comparison
- error analysis

Bu bölüm tamamlandıktan sonra:

1. Predictive Maintenance / Anomaly Detection case study
2. Visual Quality Inspection case study
3. Industrial AI Copilot mini PoC

çalışmalarına geçilecek.

---

# 10. Diğer MIUUL Klasörleri

Ekranda görülen diğer materyaller:

- machine learning kursu
- Time series kursu
- CRM
- Web Scraping
- NLP
- recommender systems
- big data
- container / environment / deployment

Bu klasörlerin içerikleri henüz ayrıntılı olarak incelenmediği için bu ana programa detaylı konu ataması yapılmadı.

Sırası geldiğinde dosyalar yüklenip **aynı sistemle ayrı homework paketlerine** dönüştürülecek:

```text
kaynak not
→ çözümü görünmeyen ödev
→ bağımsız implementasyon
→ pytest
→ mini project
```

---

# 11. ChatGPT ile Çalışma Komutumuz

Bu plana döndüğümüzde şu çalışma biçimini kullan:

> **“MIUUL kamp planına devam ediyoruz. Gün X, şu görevdeyim. Tam çözümü verme.”**

ChatGPT'nin rolü:

1. önce kodunu incelemek
2. hatalı düşünceyi göstermek
3. küçük ipucu vermek
4. gerekirse syntax hatırlatmak
5. minimum düzeltme yapmak
6. ancak son aşamada tam çözümü göstermek

---

# 12. Ana İlke

Bu kampın başarı kriteri:

> **Kaç konu gördüğün değil, kaç problemi kendi ellerinle başlatıp bitirebildiğin.**

Her gün mümkün olduğunca çok kod yaz; ama asıl hedef aynı temel örüntüleri tekrar tekrar **kendin üretmek**:

```text
problem
↓
input/output
↓
data structure
↓
function
↓
loop / condition
↓
return
↓
test
↓
debug
↓
refactor
```

Bu zincir refleks hâline geldiğinde AI destekli geliştirmede de problemi yöneten taraf sen olacaksın.
