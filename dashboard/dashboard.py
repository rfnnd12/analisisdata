import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Menampilkan header
st.title("Dashboard Analisis Data Bike Sharing")
st.write("Analisis data Bike Sharing untuk memahami pola penggunaan sepeda.")

# Membaca data
hour_df = pd.read_csv('dashboard/hour_clean.csv')  # Pastikan file CSV berada dalam folder yang sama

# Sidebar untuk filter interaktif
selected_season = st.sidebar.multiselect("Pilih Musim untuk Filter:", hour_df['season'].unique(), default=hour_df['season'].unique())  # Pilih musim
selected_holiday = st.sidebar.multiselect("Pilih Hari Libur atau Hari Kerja:", ['Hari Libur', 'Hari Kerja'])  # Pilih hari libur atau kerja

# Filter data berdasarkan pilihan dari sidebar
filtered_df_season = hour_df[hour_df['season'].isin(selected_season)]  # Menggunakan .isin untuk beberapa musim

# Memastikan hanya mengambil data untuk Hari Libur atau Hari Kerja yang dipilih
if 'Hari Libur' in selected_holiday and 'Hari Kerja' in selected_holiday:
    filtered_df_holiday = filtered_df_season
elif 'Hari Libur' in selected_holiday:
    filtered_df_holiday = filtered_df_season[filtered_df_season['holiday'] == 1]  # Ambil data hari libur
else:
    filtered_df_holiday = filtered_df_season[filtered_df_season['holiday'] == 0]  # Ambil data hari kerja

# Mengelompokkan data dan menghitung rata-rata 'cnt'
rata_rata_penyewaan = filtered_df_holiday.groupby(['season', 'holiday', 'workingday'])['count'].mean().reset_index()

# Membuat bar chart dengan penyesuaian warna dan menonaktifkan error bars
plt.figure(figsize=(12, 6))
sns.barplot(x='season', y='count', hue='workingday', data=rata_rata_penyewaan, palette={0: "blue", 1: "orange"}, ci=None)  # Menetapkan warna manual untuk Hari Kerja dan Hari Libur
plt.title(f'Rata-rata Jumlah Penyewaan Sepeda per Musim (Hari Kerja vs. Hari Libur) untuk Musim {", ".join(map(str, selected_season))}')
plt.xlabel('Musim')
plt.ylabel('Rata-rata Jumlah Penyewaan')

# Mengatur legenda agar lebih informatif
plt.legend(title='Tipe Hari', labels=['Hari Kerja', 'Hari Libur'])

# Menampilkan plot di Streamlit
st.pyplot(plt)


# **Bagian untuk plot distribusi jumlah penyewaan berdasarkan jam per musim**

# Memfilter data berdasarkan musim yang dipilih di multiselect
filtered_df_season_for_distribution = hour_df[hour_df['season'].isin(selected_season)]  # Menggunakan .isin untuk beberapa musim

# Mengelompokkan data dan menghitung jumlah penyewaan per jam per musim
hourly_rental_counts_for_distribution = filtered_df_season_for_distribution.groupby(['hour', 'season'])['count'].sum().reset_index()

# Membuat line chart untuk distribusi jumlah penyewaan berdasarkan jam untuk musim tertentu
plt.figure(figsize=(12, 6))
sns.lineplot(x='hour', y='count', hue='season', data=hourly_rental_counts_for_distribution)

plt.title('Distribusi Jumlah Penyewaan Sepeda per Musim Berdasarkan Jam')
plt.xlabel('Jam')
plt.ylabel('Jumlah Penyewaan')
plt.legend(title='Musim')
plt.grid(True)

# Menampilkan plot di Streamlit
st.pyplot(plt)
