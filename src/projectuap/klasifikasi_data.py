import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import SMOTE  # Library untuk oversampling
from pytorch_tabnet.tab_model import TabNetClassifier
import numpy as np
import torch
import joblib
import os

def handle_missing_values(data):
    """
    Menangani missing value dengan mengisi mean untuk kolom numerik
    dan modus untuk kolom kategorikal.
    """
    for column in data.columns:
        if data[column].dtype == 'object':
            data[column].fillna(data[column].mode()[0], inplace=True)
        else:
            data[column].fillna(data[column].mean(), inplace=True)
    return data

def klasifikasi_data():
    st.title("🤖 Klasifikasi Data")

    if 'data' not in st.session_state:
        st.warning("Unggah data terlebih dahulu.")
        return

    data = st.session_state['data']

    # Penanganan missing value otomatis
    data = handle_missing_values(data)

    # Pilih fitur dan target
    st.subheader("⚙️ Pilihan Fitur dan Target")
    all_columns = data.columns
    fitur = st.multiselect("Pilih Kolom Fitur:", all_columns)
    target = st.selectbox("Pilih Kolom Target:", all_columns)

    if fitur and target:
        # Memisahkan data menjadi fitur dan target
        X = data[fitur]
        y_categorical = pd.Categorical(data[target])  # Konversi target menjadi kategori
        y = y_categorical.codes  # Numerik
        categories = y_categorical.categories  # Simpan kategori

        # Mengonversi fitur kategorikal menjadi numerik
        X = pd.get_dummies(X)

        # Penanganan ketidakseimbangan data dengan SMOTE
        try:
            smote = SMOTE(sampling_strategy='auto', random_state=42, k_neighbors=min(5, len(X) - 1))
            X, y = smote.fit_resample(X, y)
            st.info("Data telah diseimbangkan menggunakan SMOTE.")
        except ValueError as e:
            st.error(f"Lanjutkan Mengisi Dengan Memilih Fitur Semua Kolom Kecuali Kolom 'y' dan Target Kolom 'y'")
            return

        # Standarisasi data untuk model tertentu (misalnya Neural Network)
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)

        # Membagi data menjadi training dan testing
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Pilih model untuk klasifikasi
        st.subheader("🧠 Pilihan Model Klasifikasi")
        model_name = st.radio("Pilih Model:", ["Decision Tree", "Random Forest", "MLPCLassifier", "TabNet"])

        if st.button("Jalankan Model"):
            model = None
            model_path = None

            if model_name == "Decision Tree":
                model = DecisionTreeClassifier(random_state=42)
                model_path = "D:/TUGAS KULIAH SEMESTER 7/PRAKTIKUM PEMBELAJARAN MESIN/UAP/projectuap/src/projectuap/model/decision_tree_model.h5"
            elif model_name == "Random Forest":
                model = RandomForestClassifier(random_state=42)
                model_path = "D:/TUGAS KULIAH SEMESTER 7/PRAKTIKUM PEMBELAJARAN MESIN/UAP/projectuap/src/projectuap/model/random_forest_model.h5"
            elif model_name == "MLPCLassifier":
                model = MLPClassifier(
                    hidden_layer_sizes=(100, 50),
                    max_iter=500,
                    activation='relu',
                    solver='adam',
                    random_state=42
                )
                model_path = "D:/TUGAS KULIAH SEMESTER 7/PRAKTIKUM PEMBELAJARAN MESIN/UAP/projectuap/src/projectuap/model/neural_network_model.h5"
            elif model_name == "TabNet":
                model_path = "D:/TUGAS KULIAH SEMESTER 7/PRAKTIKUM PEMBELAJARAN MESIN/UAP/projectuap/src/projectuap/model/tabnet_model.h5"
                X_train_np = np.array(X_train, dtype=np.float32)
                X_test_np = np.array(X_test, dtype=np.float32)
                y_train_np = np.array(y_train, dtype=np.int64)
                y_test_np = np.array(y_test, dtype=np.int64)

                model = TabNetClassifier(
                    n_d=8, n_a=8, n_steps=3,
                    gamma=1.3, lambda_sparse=1e-4,
                    optimizer_fn=torch.optim.Adam,
                    optimizer_params=dict(lr=2e-2),
                    verbose=0
                )

                # Latih model TabNet
                model.fit(
                    X_train_np, y_train_np,
                    eval_set=[(X_test_np, y_test_np)],
                    eval_metric=['accuracy'],
                    max_epochs=100,
                    patience=10,
                    batch_size=32,
                    virtual_batch_size=16
                )
                y_pred = model.predict(X_test_np)
                accuracy = accuracy_score(y_test_np, y_pred)

                # Konversi prediksi menjadi kategori
                y_pred_categories = [categories[pred] for pred in y_pred]

                # Simpan model TabNet
                if os.path.exists(model_path):
                    os.remove(model_path)
                model.save_model(model_path)

                # Simpan hasil ke session_state
                st.session_state["results"] = {
                    "model": model_name,
                    "accuracy": accuracy,
                    "predictions": y_pred_categories,
                    "actual": [categories[act] for act in y_test_np],
                    "model_path": model_path
                }

                # st.success(f"Model {model_name} selesai dilatih dan disimpan sebagai '{model_path}'!")
                st.write(f"Akurasi: {accuracy:.2f}")
                return

            # Penanganan data untuk Neural Network (scaling)
            if model_name == "Neural Network":
                X_train_input, X_test_input = X_scaled[:len(y_train)], scaler.transform(X_test[:len(y_test)])
                joblib.dump(scaler, "D:/TUGAS KULIAH SEMESTER 7/PRAKTIKUM PEMBELAJARAN MESIN/UAP/projectuap/src/projectuap/model/scaler.h5")  # Simpan scaler
            else:
                X_train_input, X_test_input = X_train, X_test

            # Latih model
            model.fit(X_train_input, y_train)
            y_pred = model.predict(X_test_input)
            accuracy = accuracy_score(y_test, y_pred)

            # Konversi prediksi menjadi kategori
            y_pred_categories = [categories[pred] for pred in y_pred]

            # Simpan model
            if os.path.exists(model_path):
                os.remove(model_path)
            joblib.dump(model, model_path)

            # Simpan hasil ke session_state
            st.session_state["results"] = {
                "model": model_name,
                "accuracy": accuracy,
                "predictions": y_pred_categories,
                "actual": [categories[act] for act in y_test],
                "model_path": model_path
            }

            # st.success(f"Model {model_name} selesai dilatih dan disimpan sebagai '{model_path}'!")
            st.write(f"Akurasi: {accuracy:.2f}")