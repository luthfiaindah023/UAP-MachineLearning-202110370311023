# 📊 Prediksi Nasabah Deposito Berjangka

## 🔖 Deskripsi Project  
Proyek ini bertujuan untuk membangun prediksi yang dapat menentukan apakah seorang nasabah akan berlangganan deposito berjangka berdasarkan data pemasaran. Dengan pendekatan berbasis machine learning, analisis ini membantu bank meningkatkan efisiensi promosi pemasaran mereka dengan menargetkan nasabah yang lebih berpotensi.  

**Dataset**: [Dataset](https://www.kaggle.com/datasets/rashmiranu/banking-dataset-classification?resource=download&select=new_train.csv)

---

## ⚙️ Langkah Instalasi
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


---

## 🚀 Fitur Aplikasi

### Penanganan Data
- **Mengisi Missing Values:**
  - Kolom numerik diisi dengan rata-rata.
  - Kolom kategorikal diisi dengan nilai modus.
- **Normalisasi:** Menstandarisasi fitur dan target dengan menggunakan metode standar scaler.
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

**- Model TabNet**

|                           | Precision|   Recall  | F1-Score | support  |
|---------------------------|----------|-----------|----------|----------|
| No                        | 0.93     | 0.96      | 0.94     | 5,79     |
| Yes                       | 0.63     | 0.48      | 0.55     | 792      |
| accuracy                  | 0.90     | 0.90      | 0.90     |          |
| macro avg                 | 0.78     | 0.72      | 0.75     | 6,59     |
| weighted avg              | 0.89     | 0.90      | 0.90     | 6,59     |


---

## 🎯 Kesimpulan
Proyek ini memberikan solusi berbasis machine learning yang dapat membantu bank mengoptimalkan strategi pemasaran mereka. Dengan hasil yang lebih terfokus, bank dapat meningkatkan efisiensi dan efektivitas dalam menarik nasabah untuk berlangganan deposito berjangka.  

---

Terima kasih telah menggunakan aplikasi ini!


