import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Membaca data
data = pd.read_csv('C:/Users/ASUS/Downloads/Bike-sharing-dataset/hour.csv')  # Pastikan file CSV berada dalam folder yang sama

# Menampilkan header
st.title("Dashboard Analisis Data Bike Sharing")
st.write("Analisis data Bike Sharing untuk memahami pola penggunaan sepeda.")

# Menampilkan data yang dibaca
st.subheader("Data Head")
st.write(data.head())

# Menampilkan analisis deskriptif
st.subheader("Statistik Deskriptif")
st.write(data.describe())

# Visualisasi Korelasi
st.subheader("Heatmap Korelasi")
# Select only numeric columns for calculating the correlation
numeric_data = data.select_dtypes(include=['number'])
corr = numeric_data.corr()  # Menghitung korelasi antara kolom numerik
fig, ax = plt.subplots(figsize=(10, 6))
sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)
st.pyplot(fig)

# Visualisasi lainnya (contoh: scatter plot)
st.subheader("Scatter Plot: Temperature vs Count")
fig2, ax2 = plt.subplots(figsize=(10, 6))
sns.scatterplot(data=data, x='temp', y='cnt', hue='season', palette='viridis', ax=ax2)
st.pyplot(fig2)

# Analisis tambahan: menambahkan filter waktu (misalnya filter berdasarkan 'hour')
st.subheader("Analisis Berdasarkan Jam")
hour_filter = st.slider("Pilih Jam", min_value=0, max_value=23, value=12)
filtered_data = data[data['hr'] == hour_filter]
st.write(f"Data untuk Jam {hour_filter}:")
st.write(filtered_data)


