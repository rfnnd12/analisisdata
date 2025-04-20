import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Menampilkan header
st.title("Dashboard Analisis Data Bike Sharing")
st.write("Analisis data Bike Sharing untuk memahami pola penggunaan sepeda.")

# Membaca data
hour_df = pd.read_csv('dashboard/hour_clean.csv')

# Mengelompokkan data dan menghitung jumlah penyewaan per jam untuk hari kerja dan akhir pekan
hourly_rental_counts = hour_df.groupby(['hour', 'weekday'], observed=False)['count'].sum().reset_index()

# Memfilter data untuk hari kerja (Senin-Jumat)
weekday_data = hourly_rental_counts[hourly_rental_counts['weekday'].isin(['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat'])]

# Memfilter data untuk akhir pekan (Sabtu-Minggu)
weekend_data = hourly_rental_counts[hourly_rental_counts['weekday'].isin(['Sabtu', 'Minggu'])]


# Membuat line chart untuk distribusi penyewaan sepeda berdasarkan jam
plt.figure(figsize=(12, 6))
sns.lineplot(x='hour', y='count', data=weekday_data, label='Hari Kerja')

# Membuat line chart untuk akhir pekan
sns.lineplot(x='hour', y='count', data=weekend_data, label='Akhir Pekan')
plt.title(f'Distribusi Jumlah Penyewaan Sepeda Berdasarkan Jam )')
plt.xlabel('Jam')
plt.ylabel('Jumlah Penyewaan')
plt.legend()
plt.grid(True)

# Menampilkan plot di Streamlit
st.pyplot(plt)
