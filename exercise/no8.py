import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Judul aplikasi
st.title("Aplikasi Web dengan Gambar, Dataset, dan Grafik")

# Sidebar untuk navigasi
st.sidebar.header("Menu Navigasi")
menu = st.sidebar.selectbox("Pilih Halaman:", ["Home", "Dataset", "Grafik"])

# Halaman 1: Home
if menu == "Home":
    st.subheader("Selamat Datang di Halaman Home")
    
    # Menampilkan gambar
    st.image("image.png", caption="Gambar Ilustrasi", use_column_width=True)

# Halaman 2: Dataset
elif menu == "Dataset":
    st.subheader("Halaman Dataset")
    
    # Membaca dataset
    try:
        dataset_path = "data.csv"  # Ubah path ini jika diperlukan
        df = pd.read_csv(dataset_path)
        
        # Menampilkan dataset
        st.write("Dataset:")
        st.dataframe(df)
    except FileNotFoundError:
        st.error(f"File dataset '{dataset_path}' tidak ditemukan. Pastikan file tersebut berada di direktori yang benar.")

# Halaman 3: Grafik
elif menu == "Grafik":
    st.subheader("Halaman Grafik")
    
    # Membaca dataset
    try:
        dataset_path = "data.csv"  # Ubah path ini jika diperlukan
        df = pd.read_csv(dataset_path)
    
        # Kolom yang diperlukan
        required_columns = ['ApplicantIncome', 'LoanAmount']
    
        # Periksa apakah kolom yang diperlukan ada di dataset
        if all(col in df.columns for col in required_columns):
            st.write("Grafik: Applicant Income vs Loan Amount")
            fig, ax = plt.subplots()
            ax.bar(df['ApplicantIncome'], df['LoanAmount'])
            ax.set_xlabel("Applicant Income")
            ax.set_ylabel("Loan Amount")
            st.pyplot(fig)
        else:
            missing_cols = set(required_columns) - set(df.columns)
            st.error(f"Dataset tidak memiliki kolom berikut: {missing_cols}")
    except FileNotFoundError:
        st.error(f"File dataset '{dataset_path}' tidak ditemukan. Pastikan file tersebut berada di direktori yang benar.")
