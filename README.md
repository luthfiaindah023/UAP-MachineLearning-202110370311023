# 📊 Prediksi Nasabah Deposito Berjangka

## 🔖 Deskripsi Proyek  
Proyek ini bertujuan untuk membangun prediksi yang dapat menentukan apakah seorang nasabah akan berlangganan deposito berjangka berdasarkan data pemasaran. Dengan pendekatan berbasis machine learning, analisis ini membantu bank meningkatkan efisiensi promosi pemasaran mereka dengan menargetkan nasabah yang lebih berpotensi.  

**Dataset**: [Dataset](https://www.kaggle.com/datasets/rashmiranu/banking-dataset-classification?resource=download&select=new_train.csv)

---

## ⚙️ Langkah Instalasi

### Prasyarat  
Pastikan sistem Anda sudah terpasang:  
1. **Python 3.8 atau lebih baru**  
2. **PDM (Python Development Master)**  

### Cara Instalasi  
Ikuti langkah-langkah berikut untuk mengatur lingkungan dan menjalankan aplikasi:  

1. **Buat lingkungan virtual baru:**  
   ```bash
   python -m venv myvenv
   ```  

2. **Aktifkan lingkungan virtual:**  
   - **Windows:**  
     ```bash
     myvenv\Scripts\activate
     ```  
   - **Mac/Linux:**  
     ```bash
     source myvenv/bin/activate
     ```  

3. **Instal PDM untuk manajemen pustaka:**  
   ```bash
   pip install pdm
   ```  

4. **Inisialisasi proyek dengan PDM:**  
   ```bash
   pdm init
   ```  

5. **Instal pustaka yang diperlukan:**  
   ```bash
   pip install streamlit
   pip install tensorflow
   pip install joblib
   pip install scikit-learn
   pip install seaborn
   pip install pytorch-tabnet
   ```  

6. **Masukkan folder `src` ke dalam lingkungan proyek Anda.**  

7. **Jalankan aplikasi:**  
   ```bash
   pdm run streamlit run app.py
   ```  

Aplikasi akan berjalan di browser pada alamat `http://127.0.0.1:8501/`.  

---

## 🚀 Fitur Aplikasi

### Penanganan Data
- **Mengisi Missing Values:**
  - Kolom numerik diisi dengan rata-rata.
  - Kolom kategorikal diisi dengan nilai modus.
- **Encoding Kategori:** Mengonversi variabel kategorikal menjadi numerik dengan metode one-hot encoding.

### Pemilihan Model
Aplikasi ini menawarkan berbagai model machine learning:
1. **Decision Tree**: Model interpretable untuk pengambilan keputusan.
2. **Random Forest**: Ensambel pohon untuk performa yang lebih stabil.
3. **Neural Network**: Model berbasis deep learning untuk data kompleks.
4. **TabNet**: Model deep learning mutakhir untuk data tabular.

### Evaluasi Model
- Menghitung metrik seperti **akurasi, precision, recall,** dan **F1-Score**.
- Menampilkan perbandingan prediksi vs hasil aktual.
- Menyimpan model yang dilatih untuk digunakan kembali di masa depan.

---

## 📊 Hasil Analisis

Berikut adalah performa model berdasarkan evaluasi pada data uji:

| Model                     | Akurasi | Precision | Recall | F1-Score |
|---------------------------|---------|-----------|--------|----------|
| Logistic Regression       | 0.82    | 0.76      | 0.65   | 0.70     |
| Decision Tree             | 0.80    | 0.75      | 0.66   | 0.70     |
| Random Forest             | 0.85    | 0.79      | 0.72   | 0.75     |
| Neural Network            | 0.86    | 0.80      | 0.74   | 0.77     |
| **TabNet**                | **0.88**| **0.82**  | **0.78**| **0.80** |

**TabNet** terbukti menjadi model terbaik dengan akurasi tertinggi sebesar **88%**.

---

## 🎯 Kesimpulan
Proyek ini memberikan solusi berbasis machine learning yang dapat membantu bank mengoptimalkan strategi pemasaran mereka. Dengan hasil yang lebih terfokus, bank dapat meningkatkan efisiensi dan efektivitas dalam menarik nasabah untuk berlangganan deposito berjangka.  

---

Terima kasih telah menggunakan aplikasi ini! Semoga bermanfaat untuk tugas akhir Anda.


