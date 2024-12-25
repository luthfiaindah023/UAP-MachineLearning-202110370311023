# analisis_data.py
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

def analisis_data():
    st.title("🔍 Analisis Data")

    # Pastikan data ada di session_state
    if 'data' in st.session_state:
        data = st.session_state['data']
        
        # Menampilkan statistik dasar
        st.subheader("Statistik Deskriptif Data")
        st.write(data.describe())

        # Menampilkan pilihan untuk memilih kolom untuk grafik
        st.subheader("Pilih Kolom untuk Melihat Grafik")

        # Pilih kolom untuk ditampilkan grafiknya
        column_selected = st.selectbox("Pilih kolom untuk grafik:", data.columns)

        # Menampilkan grafik untuk kolom yang dipilih
        if column_selected:
            st.write(f"**Grafik untuk kolom {column_selected}:**")

            # Cek apakah kolom numerik atau kategorikal
            if data[column_selected].dtype == 'object':  # Kolom Kategorikal
                st.write("Diagram Batang untuk kolom kategorikal:")
                fig, ax = plt.subplots()
                sns.countplot(x=data[column_selected], ax=ax)
                st.pyplot(fig)

                # Menampilkan jumlah entri untuk setiap kategori
                st.write("Jumlah setiap kategori:")
                category_counts = data[column_selected].value_counts()
                st.write(category_counts)

            else:  # Kolom Numerik
                st.write("Histogram untuk kolom numerik:")
                fig, ax = plt.subplots()
                sns.histplot(data[column_selected], kde=True, ax=ax)
                st.pyplot(fig)

                # Menampilkan jumlah total entri untuk kolom numerik
                st.write("Jumlah data dalam kolom numerik:")
                st.write(f"Jumlah total entri : {data[column_selected].count()}")
                st.write(f"Jumlah nilai unik    : {data[column_selected].nunique()}")
                st.write(f"Nilai minimum           : {data[column_selected].min()}")
                st.write(f"Nilai maksimum     : {data[column_selected].max()}")

    else:
        st.warning("Data belum diunggah. Silakan unggah data terlebih dahulu pada menu upload data.")
