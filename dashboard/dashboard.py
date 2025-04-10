import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Judul aplikasi
st.title("Dashboard Analisis Data")

# Muat dataset day_df dan hour_df
day_df = pd.read_csv("dashboard/day_clean.csv")
hour_df = pd.read_csv("dashboard/hour_clean.csv")

# Menampilkan header
st.title("Dashboard Analisis Data Bike Sharing")
st.write("Analisis data Bike Sharing untuk memahami pola penggunaan sepeda.")

# Menampilkan data yang dibaca
# --- Tren Penjualan Produk X (6 Bulan Terakhir) ---
# Mengubah tipe data kolom 'dateday' menjadi datetime
# day_df['dteday'] = pd.to_datetime(day_df['dteday']) # Line causing the error
day_df['dateday'] = pd.to_datetime(day_df['dateday']) # Corrected line using 'dateday'

# Filter data 6 bulan terakhir
six_months_ago = day_df['dateday'].max() - pd.DateOffset(months=6) # Corrected line using 'dateday'
filtered_data = day_df[day_df['dateday'] >= six_months_ago] # Corrected line using 'dateday'

# Plot tren penjualan
plt.figure(figsize=(12, 6))
plt.plot(filtered_data['dateday'], filtered_data['count']) # Corrected line using 'count'
plt.title('Tren Penjualan Produk X (6 Bulan Terakhir)')
plt.xlabel('Tanggal')
plt.ylabel('Jumlah Penjualan')
plt.grid(True)
plt.show()

# --- Faktor-faktor yang Memengaruhi Jumlah Rental ---
correlation = hour_df[['year', 'hour', 'count']].corr() # Changed to only include numerical columns
print(correlation['count'])

# Visualisasi korelasi menggunakan heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title('Korelasi Antara Jumlah Rental dan Variabel Lainnya')
plt.show()

# --- Distribusi Jumlah Rental Sepeda Berdasarkan Musim ---

# 1. Menghitung jumlah rental per musim
seasonal_distribution = day_df.groupby('season')['count'].sum()
print(seasonal_distribution)

# 2. Visualisasi distribusi menggunakan bar chart
plt.figure(figsize=(8, 6))
seasonal_distribution.plot(kind='bar', color=['skyblue', 'lightgreen', 'orange', 'lightcoral'])
plt.title('Distribusi Jumlah Rental Sepeda Berdasarkan Musim')
plt.xlabel('Musim')
plt.ylabel('Jumlah Rental')
plt.xticks(rotation=0)
plt.show()

# Footer
st.caption("Dibuat oleh [Nama Kamu] - Proyek Analisis Data Dicoding")
