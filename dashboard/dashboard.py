import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Membaca data
hour_df = pd.read_csv('dashboard/hour_clean.csv')  # Pastikan file CSV berada dalam folder yang sama

# Sidebar untuk filter interaktif
selected_season = st.sidebar.multiselect("Pilih Musim untuk Filter:", hour_df['season'].unique())
selected_weather = st.sidebar.multiselect("Pilih Kondisi Cuaca untuk Filter:", hour_df['weather'].unique())

# Mengelompokkan data dan menghitung rata-rata 'cnt'
rata_rata_penyewaan = hour_df.groupby(['season', 'holiday', 'workingday'])['count'].mean().reset_index()
# Membuat bar chart
plt.figure(figsize=(12, 6))
sns.barplot(x='season', y='count', hue='workingday', data=rata_rata_penyewaan[rata_rata_penyewaan['holiday'] == 0])  # Filter untuk hari bukan liburan
plt.title('Rata-rata Jumlah Penyewaan Sepeda per Musim (Hari Kerja vs. Hari Libur)')
plt.xlabel('Musim')
plt.ylabel('Rata-rata Jumlah Penyewaan')
plt.legend(title='Tipe Hari', labels=['Hari Libur', 'Hari Kerja'])
plt.show()
