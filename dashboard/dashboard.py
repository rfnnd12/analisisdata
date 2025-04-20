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
selected_day_type = st.sidebar.selectbox("Pilih Tipe Hari:", ['Hari Kerja', 'Akhir Pekan'])  # Pilih tipe hari

# Mengelompokkan data dan menghitung jumlah penyewaan per jam
hourly_rental_counts = hour_df.groupby(['hour', 'weekday'], observed=False)['count'].sum().reset_index()

# Memfilter data berdasarkan pilihan dari sidebar
if selected_day_type == 'Hari Kerja':
    # Memfilter data untuk hari kerja (Senin-Jumat)
    plot_data = hourly_rental_counts[hourly_rental_counts['weekday'].isin(['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat'])]
else:
    # Memfilter data untuk akhir pekan (Sabtu-Minggu)
    plot_data = hourly_rental_counts[hourly_rental_counts['weekday'].isin(['Sabtu', 'Minggu'])]

# Membuat line chart untuk distribusi penyewaan sepeda berdasarkan jam
plt.figure(figsize=(12, 6))
sns.lineplot(x='hour', y='count', data=plot_data, label=selected_day_type, color='blue')

plt.title(f'Distribusi Jumlah Penyewaan Sepeda Berdasarkan Jam ({selected_day_type})')
plt.xlabel('Jam')
plt.ylabel('Jumlah Penyewaan')
plt.legend(title='Tipe Hari', labels=[selected_day_type])
plt.grid(True)

# Menampilkan plot di Streamlit
st.pyplot(plt)
