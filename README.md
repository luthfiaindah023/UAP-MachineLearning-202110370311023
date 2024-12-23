# 📊 Prediksi Nasabah yang Berpotensi Berlangganan Deposito Berjangka

## 🔖 Deskripsi Project  
Bank Portugis mengalami penurunan pendapatan dan berusaha mencari solusi untuk mengatasinya. Setelah melakukan investigasi, ditemukan bahwa penyebab utamanya adalah kurangnya investasi dari nasabah pada deposito berjangka. Project ini bertujuan untuk membangun prediksi yang dapat menentukan apakah seorang nasabah akan berlangganan deposito berjangka ("ya/tidak") berdasarkan fitur yang tersedia. Dengan pendekatan berbasis machine learning dan deep learning, analisis ini membantu bank meningkatkan efisiensi promosi pemasaran mereka dengan menargetkan nasabah yang lebih berpotensi.

### Fitur Dataset
| **Fitur**     | **Tipe Fitur**         | **Deskripsi**                                                                                                                                         |
|---------------|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| age           | Numerik                | Usia nasabah                                                                                                                                           |
| job           | Kategorikal (nominal) | Jenis pekerjaan ('admin.','blue-collar','entrepreneur', dll.)                                                                                          |
| marital       | Kategorikal (nominal) | Status pernikahan ('divorced','married','single','unknown')                                                                                            |
| education     | Kategorikal (nominal) | Tingkat pendidikan ('basic.4y','basic.6y','high.school', dll.)                                                                                         |
| default       | Kategorikal (nominal) | Kredit macet? ('no','yes','unknown')                                                                                                                   |
| housing       | Kategorikal (nominal) | Memiliki pinjaman rumah? ('no','yes','unknown')                                                                                                        |
| loan          | Kategorikal (nominal) | Memiliki pinjaman pribadi? ('no','yes','unknown')                                                                                                      |
| contact       | Kategorikal (nominal) | Jenis kontak komunikasi ('cellular','telephone')                                                                                                       |
| month         | Kategorikal (ordinal) | Bulan terakhir kontak ('jan', 'feb', ... , 'dec')                                                                                                      |
| day_of_week   | Kategorikal (ordinal) | Hari terakhir kontak ('mon','tue', dll.)                                                                                                              |
| duration      | Numerik                | Durasi kontak terakhir, dalam detik (atribut ini sangat memengaruhi output)                                                                            |
| campaign      | Numerik                | Jumlah kontak selama kampanye ini untuk nasabah                                                                                                        |
| pdays         | Numerik                | Jumlah hari setelah kontak terakhir dari kampanye sebelumnya (999 berarti tidak pernah dihubungi sebelumnya)                                           |
| previous      | Numerik                | Jumlah kontak sebelumnya                                                                                                                               |
| poutcome      | Kategorikal (nominal) | Hasil kampanye sebelumnya ('failure','nonexistent','success')                                                                                          |
| y             | Biner                  | Apakah nasabah berlangganan deposito berjangka? ('yes','no')     

**Dataset**: [Dataset](https://www.kaggle.com/datasets/rashmiranu/banking-dataset-classification?resource=download&select=new_train.csv)

---

## 📑Overview Dataset
Dataset ini berasal dari kaggle yang berisi tentang promosi pemasaran yang dilakukan oleh Bank Portugis melalui komunikasi telepon. Data berjumlah 32.950 yang terdiri dari 21 fitur yang mencakup informasi demografis, status finansial, dan riwayat interaksi pelanggan dengan bank. Target variabel adalah "y", yang menunjukkan apakah pelanggan berlangganan deposito berjangka ("yes") atau tidak ("no"). [Dataset Banking](https://www.kaggle.com/datasets/rashmiranu/banking-dataset-classification?resource=download&select=new_train.csv)

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
- **Random Forest dan TabNet** menunjukkan hasil atau performa yang baik dengan akurasi lebih dari 93%
- **Decision Tree** kurang unggul dibandingkan dengan random forest dan tabnet dikarenakan sulit menangkap pola kompleks dan bisa bias terhadap fitur dominan, sehingga kurang efektif pada data dengan variasi tinggi.

Berikut adalah performa model berdasarkan evaluasi pada data uji:

- **Model Random Forest**
  - **Confusion Matrix**
    
    ![Confusion Matrix](https://drive.google.com/uc?id=1bzunwOooOeG_BQ7LartxiEUn-g-uMelu)
 
  
  - **Classification Report**
  
    |                           | Precision|   Recall  | F1-Score | support  |
    |---------------------------|----------|-----------|----------|----------|
    | No                        | 0.93     | 0.97      | 0.95     | 5,766    |
    | Yes                       | 0.97     | 0.93      | 0.95     | 5,930    |
    | accuracy                  | 0.95     | 0.95      | 0.95     |          |
    | macro avg                 | 0.95     | 0.95      | 0.95     | 11,696   |
    | weighted avg              | 0.95     | 0.95      | 0.95     | 11,696   |

  - **Distribusi Prediksi**
    
     ![Deskripsi Gambar](https://drive.google.com/uc?id=13GxunjnPKMyXMjQo7onjd1Qu7XbRhKcB)

- **Model TabNet**
  - **Confusion Matrix**
    
    ![Deskripsi Gambar](https://drive.google.com/uc?id=1GBmphsMzuvAVUCP1lWAs9MhfcMrvBjT9)


  - **Classification Report**

    |                           | Precision|   Recall  | F1-Score | support  |
    |---------------------------|----------|-----------|----------|----------|
    | No                        | 0.92     | 0.98      | 0.95     | 5,766    |
    | Yes                       | 0.98     | 0.91      | 0.94     | 5,930    |
    | accuracy                  | 0.94     | 0.94      | 0.94     |          |
    | macro avg                 | 0.95     | 0.95      | 0.94     | 11,696   |
    | weighted avg              | 0.95     | 0.94      | 0.94     | 11,696   |

  - **Distribusi Prediksi**
    
     ![Deskripsi Gambar](https://drive.google.com/uc?id=1KUz9WOJKbrKIwJIPDGot8pCgVUyxn4vK)


---

## 🎯 Kesimpulan
Proyek ini memberikan solusi berbasis machine learning yang dapat membantu bank mengoptimalkan strategi pemasaran mereka. Dengan hasil yang lebih terfokus, bank dapat meningkatkan efisiensi dan efektivitas dalam menarik nasabah untuk berlangganan deposito berjangka.  

---

Terima kasih telah menggunakan aplikasi ini!


