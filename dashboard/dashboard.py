import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Membaca data
hour_df = pd.read_csv('dashboard/hour_clean.csv')  # Pastikan file CSV berada dalam folder yang sama

# Sidebar untuk filter interaktif
selected_season = st.sidebar.multiselect("Pilih Musim untuk Filter:", hour_df['season'].unique())
selected_weather = st.sidebar.selectbox("Pilih Kondisi Cuaca untuk Filter:", hour_df['weather'].unique())
selected_workingday = st.sidebar.selectbox("Pilih Hari Kerja atau Akhir Pekan:", ['Workingday', 'Weekend'])

# Filter data berdasarkan pilihan dari sidebar
filtered_df_season = hour_df[hour_df['season'].isin(selected_season)]  # Menggunakan .isin untuk beberapa musim
filtered_df_weather = filtered_df_season[filtered_df_season['weather'] == selected_weather]

# Filter berdasarkan workingday (hari kerja atau akhir pekan)
if selected_workingday == 'Workingday':
    filtered_df_workingday = filtered_df_weather[filtered_df_weather['workingday'] == 1]
else:
    filtered_df_workingday = filtered_df_weather[filtered_df_weather['workingday'] == 0]

# Business Question 1: Apa pengaruh Cuaca Terhadap Jumlah Penyewaan Sepeda?
st.write("### Apakah hari dengan cuaca buruk seperti “Light Snow/Rain” atau “Severe Weather” menunjukkan penurunan signifikan pada jumlah penyewaan?")
hour_df_grouped_weather = filtered_df_weather.groupby(['season', 'weather'])['count'].sum().reset_index()

# Plot untuk perbandingan antara musim dan cuaca
plt.figure(figsize=(12, 6))
sns.barplot(x='season', y='count', hue='weather', data=hour_df_grouped_weather)
plt.title(f'Perbandingan Jumlah Penyewaan Sepeda Berdasarkan Musim dan Cuaca')
plt.xlabel('Musim')
plt.ylabel('Jumlah Penyewaan')
st.pyplot(plt)

# Business Question 2: Bagaimana tren penyewaan sepeda berbeda antara hari kerja (workingday) dan akhir pekan/hari libur?
st.write("### Bagaimana tren penyewaan sepeda berbeda antara hari kerja (workingday) dan akhir pekan/hari libur?")
hourly_rental_counts = filtered_df_workingday.groupby('hour')['count'].sum().reset_index()

# Plot
plt.figure(figsize=(12, 6))
sns.barplot(x='hour', y='count', data=hourly_rental_counts)
plt.title(f'Pola Penyewaan Sepeda Berdasarkan Jam ({", ".join(selected_season)})')
plt.xlabel('Jam')
plt.ylabel('Jumlah Penyewaan')
st.pyplot(plt)

# Business Question 3: Bagaimana pengaruh musim terhadap jumlah penyewaan sepeda?
st.write("### Bagaimana pengaruh musim terhadap jumlah penyewaan sepeda?")
rata_rata_penyewaan_per_musim = filtered_df_season.groupby('season')['count'].mean().reset_index()

# Plot
plt.figure(figsize=(10, 6))
sns.barplot(x='season', y='count', data=rata_rata_penyewaan_per_musim)
plt.title(f'Rata-rata Jumlah Penyewaan Sepeda per Musim ({", ".join(selected_season)})')
plt.xlabel('Musim')
plt.ylabel('Rata-rata Jumlah Penyewaan')
st.pyplot(plt)
