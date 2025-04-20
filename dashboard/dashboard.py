import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Membaca data
hour_df = pd.read_csv('dashboard/hour_clean.csv')  # Pastikan file CSV berada dalam folder yang sama

# Business Question 1: Apa pengaruh Cuaca Terhadap Jumlah Penyewaan Sepeda?
st.write("### Apakah hari dengan cuaca buruk seperti “Light Snow/Rain” atau “Severe Weather” menunjukkan penurunan signifikan pada jumlah penyewaan?")
hour_df_grouped_weather = hour_df.groupby('weather')['count'].sum().reset_index()

plt.figure(figsize=(10, 6))
sns.barplot(x='weather', y='count', data=hour_df_grouped_weather)
plt.title('Pengaruh Cuaca Terhadap Jumlah Penyewaan Sepeda')
plt.xlabel('Kondisi Cuaca')
plt.ylabel('Jumlah Penyewaan')
st.pyplot(plt)

# Business Question 2: Bagaimana tren penyewaan sepeda berbeda antara hari kerja (workingday) dan akhir pekan/hari libur?
st.write("### Bagaimana tren penyewaan sepeda berbeda antara hari kerja (workingday) dan akhir pekan/hari libur?")
hourly_rental_counts = hour_df.groupby('hour')['count'].sum().reset_index()

plt.figure(figsize=(12, 6))
sns.barplot(x='hour', y='count', data=hourly_rental_counts)
plt.title('Pola Penyewaan Sepeda Berdasarkan Jam')
plt.xlabel('Jam')
plt.ylabel('Jumlah Penyewaan')
st.pyplot(plt)

# Business Question 3: Bagaimana pengaruh musim terhadap jumlah penyewaan sepeda?
st.write("### Bagaimana pengaruh musim terhadap jumlah penyewaan sepeda?")
rata_rata_penyewaan_per_musim = hour_df.groupby('season')['count'].mean().reset_index()

plt.figure(figsize=(10, 6))
sns.barplot(x='season', y='count', data=rata_rata_penyewaan_per_musim)
plt.title('Rata-rata Jumlah Penyewaan Sepeda per Musim')
plt.xlabel('Musim')
plt.ylabel('Rata-rata Jumlah Penyewaan')
st.pyplot(plt)
