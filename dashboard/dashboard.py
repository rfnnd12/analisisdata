import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Membaca data
data = pd.read_csv('data/data_1.csv')  # Pastikan file CSV berada dalam folder yang sama

# Judul dashboard
st.title("Dashboard Analisis Data Bike Sharing")

# Tampilkan data
st.subheader("Data Head")
st.write(data.head())

# Statistik deskriptif
st.subheader("Statistik Deskriptif")
st.write(data.describe())

# --- Pertanyaan Bisnis 1: Pola Penggunaan Sepeda Sepanjang Hari ---
st.subheader("Pola Sewa per Jam")
hourly_rentals = data.groupby('hr')['cnt'].mean().reset_index()
plt.figure(figsize=(12, 6))
plt.plot(hourly_rentals['hr'], hourly_rentals['cnt'], marker='o', linestyle='-')
plt.title('Rata-rata Sewa Sepeda per Jam')
plt.xlabel('Jam')
plt.ylabel('Jumlah Sewa')
plt.grid(True)
st.pyplot(plt)

st.write("Dari visualisasi di atas, terlihat bahwa penggunaan sepeda paling tinggi terjadi pada jam-jam sibuk, yaitu sekitar pukul 7-9 pagi dan pukul 17-19 sore. Hal ini menunjukkan bahwa sepeda banyak digunakan untuk keperluan berangkat dan pulang kerja.")

# --- Pertanyaan Bisnis 2: Pengaruh Cuaca terhadap Jumlah Penyewaan ---
st.subheader("Pengaruh Cuaca terhadap Jumlah Sewa")
plt.figure(figsize=(12, 6))
sns.boxplot(x='weathersit', y='cnt', data=data)
plt.title('Jumlah Sewa Sepeda berdasarkan Kondisi Cuaca')
plt.xlabel('Kondisi Cuaca (1: Cerah, 2: Berawan, 3: Ringan Hujan, 4: Hujan Lebat)')
plt.ylabel('Jumlah Sewa')
st.pyplot(plt)

st.write("Dari visualisasi di atas, terlihat bahwa kondisi cuaca berpengaruh terhadap jumlah penyewaan sepeda. Jumlah penyewaan tertinggi terjadi pada saat cuaca cerah (weathersit=1), dan menurun seiring dengan memburuknya kondisi cuaca.")

# --- Heatmap Korelasi ---
st.subheader("Heatmap Korelasi")
numeric_data = data.select_dtypes(include=['number'])
corr = numeric_data.corr()
fig, ax = plt.subplots(figsize=(10, 6))
sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)
st.pyplot(fig)

# --- Filter data berdasarkan jam ---
st.subheader("Analisis Berdasarkan Jam")
hour_filter = st.slider("Pilih Jam", min_value=0, max_value=23, value=12)
filtered_data = data[data['hr'] == hour_filter]
st.write(f"Data untuk Jam {hour_filter}:")
st.write(filtered_data)
