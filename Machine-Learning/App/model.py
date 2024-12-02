import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Contoh data
data = pd.read_csv('data.csv')  # Masukkan dataset
X = data[['fitur1', 'fitur2']]  # Pilih kolom fitur
y = data['label']  # Kolom label/target

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model Logistic Regression
model = LogisticRegression()
model.fit(X_train, y_train)

# Prediksi
y_pred = model.predict(X_test)
print(f"Akurasi: {accuracy_score(y_test, y_pred)}")
