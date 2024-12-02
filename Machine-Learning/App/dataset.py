import pandas as pd

# Buat dataset
data = {
    "fitur1": [2.5, 1.3, 3.2, 0.8, 3.0, 1.0, 2.7, 1.2, 3.5, 0.5],
    "fitur2": [3.1, 2.8, 4.1, 1.5, 3.5, 2.0, 3.3, 1.9, 4.0, 1.0],
    "label": [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
}

# Simpan dataset ke file CSV
df = pd.DataFrame(data)
df.to_csv("data.csv", index=False)

print("Dataset telah disimpan ke 'data.csv'")
