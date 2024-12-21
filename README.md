# 📊 Prediksi Nasabah Deposito Berjangka  
## Overview Project
Proyek ini bertujuan untuk membangun prediksi yang dapat menentukan apakah seorang nasabah akan berlangganan deposito berjangka berdasarkan data pemasaran. Dengan pendekatan berbasis machine learning, analisis ini membantu bank meningkatkan efisiensi promosi pemasaran mereka dengan menargetkan nasabah yang lebih berpotensi.

**Link Dataset** : [Banking Dataset](https://www.kaggle.com/datasets/rashmiranu/banking-dataset-classification?resource=download&select=new_train.csv)

## ⚙️ Langkah Instalasi
Buat lingkungan virtual baru:

bash
python -m venv myvenv
Aktifkan lingkungan virtual:

Windows:
bash
Salin kode
myvenv\Scripts\activate
Mac/Linux:
bash
Salin kode
source myvenv/bin/activate
Instal PDM untuk manajemen pustaka:

bash
Salin kode
pip install pdm
Inisialisasi proyek dengan PDM:

bash
Salin kode
pdm init
Instal pustaka yang diperlukan:

bash
Salin kode
pip install streamlit
pip install tensorflow
pip install joblib
pip install scikit-learn
pip install seaborn
pip install pytorch-tabnet
Masukkan folder src yang telah disiapkan ke dalam lingkungan proyek Anda.

Jalankan aplikasi:

bash
Salin kode
pdm run streamlit run app.py
