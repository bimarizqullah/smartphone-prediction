import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib
import streamlit as st

# --- Bagian 1: Persiapan Data ---
# Buat dataset
data = {
    "fitur1": [2.5, 1.3, 3.2, 0.8, 3.0, 1.0, 2.7, 1.2, 3.5, 0.5],
    "fitur2": [3.1, 2.8, 4.1, 1.5, 3.5, 2.0, 3.3, 1.9, 4.0, 1.0],
    "label": [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
}
df = pd.DataFrame(data)

# Pisahkan fitur dan label
X = df[["fitur1", "fitur2"]]
y = df["label"]

# Split data menjadi training dan testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# --- Bagian 2: Training Model ---
# Inisialisasi model
model = LogisticRegression()

# Latih model
model.fit(X_train, y_train)

# Evaluasi model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Akurasi model: {accuracy:.2f}")

# Simpan model ke file .sav
joblib.dump(model, "model.sav")
print("Model telah disimpan dalam format .sav")

# --- Bagian 3: Aplikasi Streamlit ---
# Mulai aplikasi Streamlit
st.title("Aplikasi Prediksi Machine Learning")

# Input dari pengguna
st.subheader("Masukkan Nilai Fitur")
fitur1 = st.number_input("Masukkan nilai fitur 1:", min_value=0.0, value=1.0, step=0.1)
fitur2 = st.number_input("Masukkan nilai fitur 2:", min_value=0.0, value=1.0, step=0.1)

# Tombol prediksi
if st.button("Prediksi"):
    # Load model dari file .sav
    loaded_model = joblib.load("model.sav")
    
    # Lakukan prediksi
    prediksi = loaded_model.predict([[fitur1, fitur2]])[0]
    
    # Tampilkan hasil prediksi
    st.write(f"Hasil Prediksi: {'Label 1' if prediksi == 1 else 'Label 0'}")
    st.write(f"Akurasi Model: {accuracy:.2f}")
