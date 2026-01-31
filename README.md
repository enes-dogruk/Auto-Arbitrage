# ⚡ AUTO // ARBITRAGE

![Project Banner](https://img.shields.io/badge/Status-Active-brightgreen) ![Python](https://img.shields.io/badge/Python-3.10%2B-blue) ![Streamlit](https://img.shields.io/badge/Streamlit-1.31-red) ![License](https://img.shields.io/badge/License-MIT-yellow)

**Yapay Zeka Destekli İkinci El Araç Fiyatlandırma ve Analiz Motoru (v3.5)**

> *"Volatil piyasalarda doğru fiyatı bulmak sanat değil, bilimdir."*

**Auto // Arbitrage**, Türkiye ikinci el araç piyasasındaki verileri analiz ederek, araçların marka, model, yıl, kilometre ve donanım özelliklerine göre **adil piyasa değerini (Fair Market Value)** tahmin eden uçtan uca (End-to-End) bir makine öğrenmesi projesidir.

---

## 📸 Proje Önizlemesi

<img width="1913" height="770" alt="Auto Arbitrage Arayüzü" src="https://github.com/user-attachments/assets/09bc159d-6d32-43dd-8b9b-3c13d07bc2f3" />

---

## 🚀 Özellikler

* **🧠 Yüksek Doğruluklu AI Modeli:** Random Forest algoritması ile eğitilmiş, **%96+ R² skoru** ve **±%4 sapma payı** ile çalışan fiyatlandırma motoru.
* **🎨 Cyberpunk UI/UX:** Streamlit ile geliştirilmiş, modern, karanlık mod (dark mode) ve neon detaylara sahip reaktif arayüz.
* **🎛️ Dinamik Filtreleme:** Seçilen markaya göre modeli, modele göre üretim yıllarını ve yakıt türlerini otomatik filtreleyen akıllı algoritma.
* **📊 İnteraktif Görselleştirme:** Tahmin edilen fiyatın piyasadaki konumunu gösteren Plotly göstergeleri (Gauge Charts) ve Güven Aralığı analizi.
* **🛠️ Özel Marka Çözümleri:** Mercedes, Tesla ve Porsche gibi veri setinde tutarsızlık olabilen markalar için özel veri temizleme (Data Cleaning) katmanları.
* **⚡ Slider Entegrasyonu:** Kullanıcı deneyimini artıran kaydırılabilir yıl ve motor hacmi seçicileri (v3.5 güncellemesi).

---

## 🛠️ Kullanılan Teknolojiler

Bu proje tamamen **Python** ekosistemi kullanılarak geliştirilmiştir:

* **Frontend:** [Streamlit](https://streamlit.io/) (Arayüz tasarımı)
* **Data Processing:** Pandas, NumPy (Veri manipülasyonu ve temizliği)
* **Machine Learning:** Scikit-learn (Random Forest Regressor, One-Hot & Frequency Encoding)
* **Visualization:** Plotly (Grafikler)
* **Version Control:** Git & GitHub

---

## ⚙️ Kurulum ve Çalıştırma

Projeyi yerel makinenizde çalıştırmak için aşağıdaki adımları izleyin:

**1. Repoyu Klonlayın**
```bash
git clone [https://github.com/enes-dogruk/Auto-Arbitrage.git](https://github.com/enes-dogruk/Auto-Arbitrage.git)
cd Auto-Arbitrage

2. Gerekli Kütüphaneleri Yükleyin
pip install -r requirements.txt

3. Uygulamayı Başlatın
streamlit run app.py

📂 Proje Yapısı
Auto-Arbitrage/
├── app.py                   # Ana uygulama dosyası (Streamlit)
├── araba_fiyat_modeli.pkl   # Eğitilmiş ML modeli
├── processed_data.pkl       # İşlenmiş veri (Encoding için gerekli)
├── turkey_used_cars.csv     # Ham veri seti (Veri kaynağı)
├── clean_data.csv           # Temizlenmiş veri seti
├── requirements.txt         # Kütüphane bağımlılıkları
├── .gitignore               # Git tarafından yoksayılacak dosyalar
└── Notebooks/               # Jupyter Notebooks (Eğitim süreci)
    ├── 01_Data_Cleaning.ipynb
    ├── 02_Feature_Engineering.ipynb
    └── 03_Model_Training.ipynb

📊 Model Performansı
Model eğitimi sırasında 5 farklı algoritma test edilmiş ve en iyi sonucu Random Forest Regressor vermiştir.
Metrik |	Değer
--------------
R² Score | 0.96
MAE (Ortalama Mutlak Hata)	| Düşük
Güven Aralığı	| %95

📞 İletişim
Enes Doğruk - www.linkedin.com/in/enesdogruk

Proje Linki: https://github.com/enes-dogruk/Auto-Arbitrage
