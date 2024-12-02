# Import libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error

# 1. Membaca dataset
df_mobil = pd.read_csv("CarPrice_Assignment.csv")
print("Dataset:")
print(df_mobil.head())  # Menampilkan 5 baris pertama dataset

# 2. Menampilkan semua tipe data pada dataset
print("\nTipe data pada dataset:")
print(df_mobil.dtypes)

# 3. Menampilkan deskripsi statistik dataset
print("\nDeskripsi statistik dataset:")
print(df_mobil.describe())

# 4. Menampilkan Grafik distribusi harga mobil
plt.figure(figsize=(10,4))

plt.subplot(1,2,1)
plt.title('Car Price Distribution Plot')
sns.histplot(df_mobil['price'])

plt.show()

# 5. Menampilkan distribusi jumlah mobil berdasarkan nama mobil (CarName)
car_counts = df_mobil['CarName'].value_counts()
plt.figure(figsize=(10,6))
car_counts.plot(kind="bar")
plt.title("CarName Distribution")
plt.xlabel("CarName")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.show()

# 6. Menampilkan 10 nama mobil terbanyak pada Dataset
print("\n10 Nama Mobil Terbanyak:")
nama_terbanyak = df_mobil['CarName'].value_counts().head(10)
print(nama_terbanyak)

# 7. Membuat WordCloud dari kolom 'CarName'
text = ' '.join(df_mobil['CarName'].dropna())
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')  # Menyembunyikan axis
plt.show()

# 8. Menampilkan grafik scatter antara highwaympg dan price
plt.scatter(df_mobil['highwaympg'], df_mobil['price'])
plt.xlabel('highwaympg')
plt.ylabel('price')
plt.show()

# 9. Persiapan Data untuk Regresi Linear
x = df_mobil[['highwaympg', 'curbweight', 'horsepower']]
y = df_mobil['price']

# 10. Split data ke dalam training dan testing set
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# 11. Melatih model regresi linear
model_regresi = LinearRegression()
model_regresi.fit(x_train, y_train)

# 12. Membuat prediksi dengan data uji
model_regresi_pred = model_regresi.predict(x_test)

# 13. Visualisasi perbandingan harga aktual dan prediksi
plt.scatter(x_test.iloc[:, 0], y_test, label='Actual Prices', color='blue')
plt.scatter(x_test.iloc[:, 0], model_regresi_pred, label="Predicted Prices", color='red')
plt.xlabel('highwaympg')
plt.ylabel('price')
plt.legend()
plt.show()

# 14. Prediksi harga untuk data baru
x_new = np.array([[32, 2338, 75]])  # Contoh data baru (highwaympg, curbweight, horsepower)
harga_x = model_regresi.predict(x_new)
print(f"Prediksi harga untuk data baru: {int(harga_x)}")

# 15. Evaluasi model menggunakan Mean Absolute Error, Mean Squared Error, dan Root Mean Squared Error
mae = mean_absolute_error(y_test, model_regresi_pred)
print(f'Mean Absolute Error (MAE): {mae:.2f}')

mse = mean_squared_error(y_test, model_regresi_pred)
print(f'Mean Squared Error (MSE): {mse:.2f}')

rmse = np.sqrt(mse)
print(f'Root Mean Squared Error (RMSE): {rmse:.2f}')

#pickle
import pickle

filename = 'model_prediksi_harga_mobil.sav'
pickle.dump(model_regresi, open(filename, 'wb'))