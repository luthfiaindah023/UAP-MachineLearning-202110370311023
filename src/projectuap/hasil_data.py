import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, classification_report

def hasil_data():
    st.title("📊 Hasil Klasifikasi")

    # Memastikan ada hasil klasifikasi di session_state
    if "results" in st.session_state:
        results = st.session_state["results"]

        # Tampilkan informasi hasil klasifikasi
        st.subheader("Hasil Akhir")
        st.markdown(f"**Model yang digunakan:** {results['model']}")
        st.markdown(f"**Akurasi Model:** {results['accuracy'] * 100:.2f}%")

        # Tampilkan hasil prediksi dan nilai aktual
        st.subheader("📊 Hasil Prediksi vs Nilai Aktual")
        hasil_df = pd.DataFrame({"Nilai Aktual": results["actual"], "Prediksi": results["predictions"]})
        st.dataframe(hasil_df)

        # Tambahkan grafik Confusion Matrix
        st.subheader("📊 Confusion Matrix")
        cm = confusion_matrix(results["actual"], results["predictions"])
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=["No", "Yes"], yticklabels=["No", "Yes"])
        ax.set_xlabel("Prediksi")
        ax.set_ylabel("Nilai Aktual")
        plt.tight_layout()  # Menambahkan layout yang rapi
        st.pyplot(fig)

        # Tambahkan grafik distribusi prediksi
        st.subheader("📊 Distribusi Prediksi")
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.countplot(x=results["predictions"], palette="viridis", ax=ax)

        # Tambahkan angka count di atas setiap batang
        for p in ax.patches:
            ax.annotate(f'{int(p.get_height())}', 
                        (p.get_x() + p.get_width() / 2., p.get_height()), 
                        ha='center', va='baseline', fontsize=12, color='black', xytext=(0, 5), 
                        textcoords='offset points')

        ax.set_title("Distribusi Prediksi")
        ax.set_xlabel("Prediksi")
        ax.set_ylabel("Jumlah")
        plt.tight_layout()  # Menambahkan layout yang rapi
        st.pyplot(fig)

        # Tambahkan classification report
        st.subheader("📊 Classification Report")
        report = classification_report(results["actual"], results["predictions"], target_names=["No", "Yes"], output_dict=True)
        report_df = pd.DataFrame(report).transpose()
        st.dataframe(report_df)

    else:
        st.warning("Belum ada hasil klasifikasi. Silakan jalankan model di halaman 'Klasifikasi'.")
