import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Prediksi Nasabah Deposito Berjangka",
    page_icon="📊",
    layout="wide",
)

# Header Section
st.title("📊 Prediksi Nasabah Deposito Berjangka")
st.markdown(
    """
    Selamat datang di aplikasi **Prediksi Nasabah Deposito Berjangka**! 
    Gunakan aplikasi ini untuk melakukan prediksi pada dataset tabular Anda dengan mudah.
    """
)

# Sidebar for navigation
st.sidebar.title("Navigasi")
st.sidebar.markdown("Gunakan menu berikut untuk berpindah antar halaman.")

# Navigation options
menu = st.sidebar.radio(
    "Pilih Halaman:",
    ("Home", "Upload Data", "Analisis Data", "Klasifikasi", "Hasil")
)

if menu == "Home":
    st.subheader("🏠 Halaman Utama")
    st.markdown(
        """
        Di halaman ini, Anda dapat memahami fungsi aplikasi dan bagaimana cara menggunakannya.
        - **Upload Data:** Unggah dataset Anda dalam format CSV/Excel.
        - **Analisis Data:** Analisis statistik awal pada data Anda.
        - **Klasifikasi:** Lakukan klasifikasi pada data tabular Anda.
        - **Hasil:** Lihat hasil klasifikasi yang telah dilakukan.
        
        Silakan pilih halaman lain dari menu navigasi di sebelah kiri untuk memulai.
        """
    )

elif menu == "Upload Data":
    from upload_data import upload_data
    upload_data()

elif menu == "Analisis Data":
    from analisis_data import analisis_data
    analisis_data()

elif menu == "Klasifikasi":
    from klasifikasi_data import klasifikasi_data
    klasifikasi_data()

elif menu == "Hasil":
    from hasil_data import hasil_data
    hasil_data()
