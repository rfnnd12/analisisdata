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


# **Plot Pertama**: Bar Chart Rata-rata Jumlah Penyewaan
rata_rata_penyewaan = filtered_df_holiday.groupby(['season', 'holiday', 'workingday'])['count'].mean().reset_index()

# Menambahkan judul per plot
st.write("### Rata-rata Jumlah Penyewaan Sepeda per Musim (Hari Kerja vs. Hari Libur)")

# Membuat bar chart dengan penyesuaian warna dan menonaktifkan error bars
plt.figure(figsize=(12, 6))
sns.barplot(x='season', y='count', hue='workingday', data=rata_rata_penyewaan, palette={0: "blue", 1: "orange"}, ci=None)  
plt.xlabel('Musim')
plt.ylabel('Rata-rata Jumlah Penyewaan')
plt.legend(title='Tipe Hari', labels=['Hari Kerja', 'Hari Libur'])

# Menampilkan plot di Streamlit
st.pyplot(plt)


# **Plot Kedua**: Line Chart Distribusi Penyewaan per Jam
# Memfilter data untuk distribusi musim menggunakan satu multiselect
filtered_df_season_for_distribution = hour_df[hour_df['season'].isin(selected_season)]  # Menggunakan .isin untuk beberapa musim

# Mengelompokkan data dan menghitung jumlah penyewaan per jam per musim
hourly_rental_counts_for_distribution = filtered_df_season_for_distribution.groupby(['hour', 'season'])['count'].sum().reset_index()

# Menambahkan judul per plot
st.write("### Distribusi Jumlah Penyewaan Sepeda per Musim Berdasarkan Jam")

# Membuat line chart untuk distribusi jumlah penyewaan berdasarkan jam untuk musim tertentu dengan warna yang sesuai
plt.figure(figsize=(12, 6))
sns.lineplot(x='hour', y='count', hue='season', data=hourly_rental_counts_for_distribution, palette={"spring": "lightblue", "summer": "orange", "fall": "green", "winter": "red"})

plt.xlabel('Jam')
plt.ylabel('Jumlah Penyewaan')
plt.legend(title='Musim')
plt.grid(True)

# Menampilkan plot di Streamlit
st.pyplot(plt)


# **Plot Ketiga**: Box Plot Pengaruh Cuaca terhadap Jumlah Penyewaan
# Sidebar untuk filter interaktif
selected_months = st.sidebar.multiselect("Pilih Bulan untuk Filter:", hour_df['month'].unique(), default=hour_df['month'].unique())  # Pilih bulan
selected_weather = st.sidebar.multiselect("Pilih Kondisi Cuaca:", hour_df['weather'].unique(), default=hour_df['weather'].unique())  # Pilih kondisi cuaca

# Memfilter data berdasarkan pilihan dari sidebar
filtered_df_month = hour_df[hour_df['month'].isin(selected_months)]  # Filter berdasarkan bulan
filtered_df_weather = filtered_df_month[filtered_df_month['weather'].isin(selected_weather)]  # Filter berdasarkan cuaca

# Menambahkan judul per plot
st.write("### Pengaruh Kondisi Cuaca terhadap Jumlah Penyewaan Sepeda pada Bulan Tertentu")

# Membuat box plot untuk distribusi jumlah penyewaan sepeda per bulan dan cuaca
plt.figure(figsize=(12, 6))
sns.boxplot(x='month', y='count', hue='weather', data=filtered_df_weather)  # Menggunakan filtered_df_weather

plt.xlabel('Bulan')
plt.ylabel('Jumlah Penyewaan Sepeda')
plt.legend(title='Kondisi Cuaca')

# Menampilkan plot di Streamlit
st.pyplot(plt)
