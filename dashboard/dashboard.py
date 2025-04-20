import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Membaca data
hour_df = pd.read_csv('dashboard/hour_clean.csv')  # Pastikan file CSV berada dalam folder yang sama

# Filter by Season (interactive)
seasons = hour_df['season'].unique()  # Get unique seasons
selected_season = st.selectbox("Pilih Musim untuk Filter:", seasons)

# Filter data based on selected season
filtered_df_season = hour_df[hour_df['season'] == selected_season]

# Business Question 1: Apa pengaruh Cuaca Terhadap Jumlah Penyewaan Sepeda?
st.write("### Apakah hari dengan cuaca buruk seperti “Light Snow/Rain” atau “Severe Weather” menunjukkan penurunan signifikan pada jumlah penyewaan?")
weather_conditions = hour_df['weather'].unique()  # Get unique weather conditions
selected_weather = st.selectbox("Pilih Kondisi Cuaca untuk Filter:", weather_conditions)

# Filter data based on selected weather
filtered_df_weather = filtered_df_season[filtered_df_season['weather'] == selected_weather]

hour_df_grouped_weather = filtered_df_weather.groupby('weather')['count'].sum().reset_index()

plt.figure(figsize=(10, 6))
sns.barplot(x='weather', y='count', data=hour_df_grouped_weather)
plt.title(f'Pengaruh Cuaca {selected_weather} Terhadap Jumlah Penyewaan Sepeda')
plt.xlabel('Kondisi Cuaca')
plt.ylabel('Jumlah Penyewaan')
st.pyplot(plt)

# Business Question 2: Bagaimana tren penyewaan sepeda berbeda antara hari kerja (workingday) dan akhir pekan/hari libur?
st.write("### Bagaimana tren penyewaan sepeda berbeda antara hari kerja (workingday) dan akhir pekan/hari libur?")
workingday_options = ['Workingday', 'Weekend']  # Options for filtering
selected_workingday = st.selectbox("Pilih Hari Kerja atau Akhir Pekan:", workingday_options)

# Filter data based on workingday selection
if selected_workingday == 'Workingday':
    filtered_df_workingday = filtered_df_season[filtered_df_season['workingday'] == 1]
else:
    filtered_df_workingday = filtered_df_season[filtered_df_season['workingday'] == 0]

hourly_rental_counts = filtered_df_workingday.groupby('hour')['count'].sum().reset_index()

plt.figure(figsize=(12, 6))
sns.barplot(x='hour', y='count', data=hourly_rental_counts)
plt.title(f'Pola Penyewaan Sepeda Berdasarkan Jam ({selected_workingday})')
plt.xlabel('Jam')
plt.ylabel('Jumlah Penyewaan')
st.pyplot(plt)

# Business Question 3: Bagaimana pengaruh musim terhadap jumlah penyewaan sepeda?
st.write("### Bagaimana pengaruh musim terhadap jumlah penyewaan sepeda?")
rata_rata_penyewaan_per_musim = filtered_df_season.groupby('season')['count'].mean().reset_index()

plt.figure(figsize=(10, 6))
sns.barplot(x='season', y='count', data=rata_rata_penyewaan_per_musim)
plt.title(f'Rata-rata Jumlah Penyewaan Sepeda per Musim ({selected_season})')
plt.xlabel('Musim')
plt.ylabel('Rata-rata Jumlah Penyewaan')
st.pyplot(plt)
