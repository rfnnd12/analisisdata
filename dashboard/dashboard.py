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
selected_day_type = st.sidebar.multiselect("Pilih Hari Kerja atau Hari Libur:", ['Hari Kerja', 'Hari Libur'])  # Pilih hari kerja atau libur

# Filter data berdasarkan pilihan dari sidebar
filtered_df_season = hour_df[hour_df['season'].isin(selected_season)]  # Menggunakan .isin untuk beberapa musim

# Memastikan hanya mengambil data untuk Hari Kerja atau Hari Libur yang dipilih
if 'Hari Kerja' in selected_day_type and 'Hari Libur' in selected_day_type:
    filtered_df_day = filtered_df_season
elif 'Hari Kerja' in selected_day_type:
    filtered_df_day = filtered_df_season[filtered_df_season['holiday'] == 0]  # Ambil data hari kerja (Senin-Jumat)
else:
    filtered_df_day = filtered_df_season[filtered_df_season['holiday'] == 1]  # Ambil data hari libur (Sabtu-Minggu)

# Mengelompokkan data dan menghitung rata-rata 'cnt'
rata_rata_penyewaan = filtered_df_day.groupby(['season', 'holiday', 'workingday'])['count'].mean().reset_index()

# Membuat bar chart dengan penyesuaian warna dan menonaktifkan error bars
plt.figure(figsize=(12, 6))
sns.barplot(x='season', y='count', hue='workingday', data=rata_rata_penyewaan, palette={0: "blue", 1: "orange"}, ci=None)  # Menetapkan warna manual untuk Hari Kerja dan Hari Libur
plt.title(f'Rata-rata Jumlah Penyewaan Sepeda per Musim (Hari Kerja vs. Hari Libur) untuk Musim {", ".join(map(str, selected_season))}')
plt.xlabel('Musim')
plt.ylabel('Rata-rata Jumlah Penyewaan')

# Menampilkan plot di Streamlit
st.pyplot(plt)

# Mengelompokkan data dan menghitung jumlah penyewaan per jam untuk hari kerja dan akhir pekan
hourly_rental_counts = hour_df.groupby(['hour', 'weekday'], observed=False)['count'].sum().reset_index()

# Memfilter data untuk hari kerja (Senin-Jumat)
weekday_data = hourly_rental_counts[hourly_rental_counts['weekday'].isin(['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat'])]

# Memfilter data untuk akhir pekan (Sabtu-Minggu)
weekend_data = hourly_rental_counts[hourly_rental_counts['weekday'].isin(['Sabtu', 'Minggu'])]

# Memilih data sesuai dengan pilihan pengguna di sidebar
if 'Hari Kerja' in selected_day_type and 'Hari Libur' not in selected_day_type:
    plot_data = weekday_data
elif 'Hari Libur' in selected_day_type and 'Hari Kerja' not in selected_day_type:
    plot_data = weekend_data
else:
    plot_data = pd.concat([weekday_data, weekend_data])  # Gabungkan keduanya jika keduanya dipilih

# Membuat line chart untuk distribusi penyewaan sepeda berdasarkan jam
plt.figure(figsize=(12, 6))
sns.lineplot(x='hour', y='count', data=plot_data, label=", ".join(selected_day_type))

plt.title(f'Distribusi Jumlah Penyewaan Sepeda Berdasarkan Jam ({", ".join(selected_day_type)})')
plt.xlabel('Jam')
plt.ylabel('Jumlah Penyewaan')
plt.legend(title='Tipe Hari', labels=[", ".join(selected_day_type)])
plt.grid(True)

# Menampilkan plot di Streamlit
st.pyplot(plt)
