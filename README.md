# 🚚 Food Delivery Time Prediction

Aplikasi Machine Learning untuk **memprediksi waktu pengantaran makanan** berdasarkan berbagai faktor seperti jarak, cuaca, traffic, jenis kendaraan, pengalaman kurir, dan waktu pengantaran.

## 📌 Business Understanding
Dalam industri *food delivery*, **kecepatan pengantaran** adalah salah satu faktor kunci dalam menjaga kepuasan pelanggan.  
Tujuan utama project ini adalah:
1. Memprediksi waktu pengantaran makanan secara akurat.
2. Mengidentifikasi faktor-faktor yang paling memengaruhi waktu pengantaran.
3. Memberikan insight dan rekomendasi untuk meningkatkan efisiensi operasional.

---

## 🗂️ Dataset
Dataset yang digunakan berisi data historis pengantaran makanan dengan fitur-fitur:
- `Distance_km`: Jarak pengiriman (km)  
- `Preparation_Time_min`: Waktu persiapan restoran (menit)  
- `Weather`: Kondisi cuaca (Clear, Rainy, Foggy, Storm)  
- `Traffic_Level`: Tingkat kemacetan (Low, Medium, High)  
- `Vehicle_Type`: Jenis kendaraan (Scooter, Bike, Car)  
- `Courier_Experience_yrs`: Pengalaman kurir (tahun)  
- `Time_of_Day`: Waktu pengiriman (Morning, Afternoon, Evening, Night)  
- `Delivery_Time_min`: Target waktu pengantaran (menit)

---

## 🤖 Model yang Digunakan
Beberapa algoritma telah diuji:
- **Linear Regression** → R² ≈ **0.77** (Model terbaik ✅)  
- Decision Tree → R² ≈ 0.43  
- Random Forest → R² ≈ 0.75  
- XGBoost → R² ≈ 0.70  

---

## 🖥️ Aplikasi Streamlit
Aplikasi ini memiliki 4 menu utama:
1. **🏠 Home** → Deskripsi project & business understanding  
2. **📊 EDA** → Visualisasi data & analisis hubungan variabel  
3. **🤖 Prediksi** → Form input untuk memprediksi waktu pengantaran  
4. **📈 Evaluasi Model** → Perbandingan performa model ML  

---

## 🚀 Cara Menjalankan Aplikasi

### 1. Clone Repository
```bash
git clone https://github.com/username/food-delivery-time-prediction.git
cd food-delivery-time-prediction
```
### 2. Install Dependencies
```bash
pip install -r requirement.txt
```
### 3. Jalankan Streamlit APp
```bash
streamlit run app.py
```
---
## 🌐 Deploy ke Streamlit Cloud
1. Push repository ini ke GitHub.
2. Masuk ke Streamlit Cloud.
3. Hubungkan akun GitHub → pilih repository ini.
4. Pilih app.py sebagai entry point.
5. Streamlit akan otomatis menjalankan aplikasi 🚀
---
## Tampilan Aplikasi
- Home
- EDA - Distribusi Waktu
- Prediksi
- Evaluasi Model
---
## ✨ Author
Saya **Gulbuddin Ikhmatiar Possumah** membuat project ini sebagai bagian dari pembelajaran mandiri saya dalam _Machine Learning & Data Science._
