# ⚡ Power Analyzer Simulation

Elektrik-elektronik mühendisliğinde kullanılan temel kavramları (RMS, aktif güç, güç faktörü, faz farkı, THD) yazılım ortamında simüle eden Python projesi.

Bu repo, hem öğrenme amaçlıdır hem de gerçek donanım tabanlı güç analizörlerine geçiş için bir ön çalışmadır.

---

## 🚀 Özellikler

- Sentetik gerilim ve akım sinyali üretimi (faz farkı, harmonik, gürültü ekleme)
- RMS, aktif güç, güç faktörü hesaplamaları
- Faz farkı tespiti (cross-correlation yöntemi)
- FFT analizi ve **Total Harmonic Distortion (THD)** ölçümü
- Grafiksel çıktıların kaydedilmesi (zaman domeni + frekans domeni)

---

## 📂 Proje Yapısı

```
power-analyzer-sim/
│── data/ # Örnek sinyaller (CSV)
│── figures/ # Grafik çıktıları
│── src/ # Modüller
│ ├── generate_signals.py
│ ├── calculations.py
│ ├── fft_analysis.py
│ ├── visualize.py
│── tests/ # Basit testler
│── main.py # Giriş noktası
│── requirements.txt
│── README.md
```


---

## 🖥️ Kurulum

```bash
git clone https://github.com/kullanici/power-analyzer-sim.git
cd power-analyzer-sim
python -m venv .venv
.venv\Scripts\activate  # (Windows)
pip install -r requirements.txt
python main.py
```

## 📊 Örnek Çıktı

```
=== Güç Analizörü Sonuçları ===
Vrms: 229.81 V
Irms: 7.07 A
Aktif Güç (P): 1407.29 W
Güç Faktörü (PF): 0.866
Faz Farkı: 30.00°
Gerilim THD: 10.20%
Akım THD: 10.35%
```

## 📈 Görseller

- Gerilim ve Akım: 
![Gerilim ve Akım](figures/signals.png)

- Anlık Güç:
![Anlık Güç](figures/power.png)

- Gerilim FFT:
![Gerilim FFT](figures/fft_voltage.png)

- Akım FFT:
![Akım FFT](figures/fft_current.png)

## 🎯 Geliştirme Planı

 - Zero-crossing ile faz farkı ölçümü ekle
 - Daha karmaşık harmonik kombinasyonları
 - Gerçek sensör verisi (donanım entegrasyonu)
 - Basit bir GUI (ör. Tkinter/Dash)

## 🔢 Matematiksel Formüller

RMS:  
![RMS](figures/rms_formula_v2.png?raw=true)

Aktif Güç:  
![P](figures/active_power_formula_v2.png?raw=true)

Reaktif Güç:  
![Q](figures/reactive_power_formula_v2.png?raw=true)

THD:  
![THD](figures/thd_formula_v2.png?raw=true)



## 📚 Kaynaklar

- *Electrical Power Systems Basics* (Thomas Wildi)  
- [NumPy Documentation](https://numpy.org/doc/stable/)  
- [SciPy Signal Processing](https://docs.scipy.org/doc/scipy/reference/signal.html)


