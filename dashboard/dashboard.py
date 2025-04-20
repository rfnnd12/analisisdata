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
selected_day_type = st.sidebar.multiselect("Pilih Tipe Hari:", ['Hari Kerja', 'Hari Libur'])  # Pilih Hari Kerja atau Hari Libur

# Filter data berdasarkan pilihan dari sidebar
filtered_df_season = hour_df[hour_df['season'].isin(selected_season)]  # Menggunakan .isin untuk beberapa musim

# Memastikan hanya mengambil data untuk Hari Kerja atau Hari Libur yang dipilih
if selected_day_type == 'Hari Kerja':
    filtered_df_day = filtered_df_season[filtered_df_season['holiday'] == 0]  # Ambil data hari kerja (Senin-Jumat)
else:
    filtered_df_day = filtered_df_season[filtered_df_season['holiday'] == 1]  # Ambil data hari libur (Sabtu-Minggu)

# Mengelompokkan data dan menghitung rata-rata 'cnt'
rata_rata_penyewaan = filtered_df_day.groupby(['season', 'holiday', 'workingday'])['count'].mean().reset_index()

# Membuat bar chart
plt.figure(figsize=(12, 6))
sns.barplot(x='season', y='count', hue='workingday', data=rata_rata_penyewaan)
plt.title(f'Rata-rata Jumlah Penyewaan Sepeda per Musim ({selected_day_type})')
plt.xlabel('Musim')
plt.ylabel('Rata-rata Jumlah Penyewaan')
plt.legend(title='Tipe Hari', labels=['Hari Kerja', 'Hari Libur'])

# Menampilkan plot di Streamlit
st.pyplot(plt)

# Mengelompokkan data dan menghitung jumlah penyewaan per jam untuk hari kerja dan akhir pekan
hourly_rental_counts = hour_df.groupby(['hour', 'weekday'], observed=False)['count'].sum().reset_index()

# Memfilter data untuk hari kerja (Senin-Jumat)
weekday_data = hourly_rental_counts[hourly_rental_counts['weekday'].isin(['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat'])]

# Memfilter data untuk akhir pekan (Sabtu-Minggu)
weekend_data = hourly_rental_counts[hourly_rental_counts['weekday'].isin(['Sabtu', 'Minggu'])]

# Memilih data sesuai dengan pilihan pengguna di sidebar
if selected_day_type == 'Hari Kerja':
    plot_data = weekday_data
else:
    plot_data = weekend_data

# Membuat line chart untuk distribusi penyewaan sepeda berdasarkan jam
plt.figure(figsize=(12, 6))
sns.lineplot(x='hour', y='count', data=plot_data, label=selected_day_type)

plt.title(f'Distribusi Jumlah Penyewaan Sepeda Berdasarkan Jam ({selected_day_type})')
plt.xlabel('Jam')
plt.ylabel('Jumlah Penyewaan')
plt.legend(title='Tipe Hari', labels=[selected_day_type])
plt.grid(True)

# Menampilkan plot di Streamlit
st.pyplot(plt)
