import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Menampilkan header
st.title("Dashboard Analisis Data Bike Sharing")
st.write("Analisis data Bike Sharing untuk memahami pola penggunaan sepeda.")

# Membaca data
hour_df = pd.read_csv('dashboard/hour_clean.csv')  # Pastikan file CSV berada dalam folder yang sama

# Mengelompokkan data dan menghitung jumlah penyewaan per jam
hourly_rental_counts = hour_df.groupby(['hour', 'weekday'], observed=False)['count'].sum().reset_index()

# Membuat line chart untuk distribusi penyewaan sepeda berdasarkan jam
plt.figure(figsize=(12, 6))
sns.lineplot(x='hour', y='count', data=weekday_data, label='Hari Kerja')

# Membuat line chart untuk akhir pekan
sns.lineplot(x='hour', y='count', data=weekend_data, label='Akhir Pekan')
plt.title(f'Distribusi Jumlah Penyewaan Sepeda Berdasarkan Jam ({selected_day_type})')
plt.xlabel('Jam')
plt.ylabel('Jumlah Penyewaan')
plt.legend(title='Tipe Hari', labels=[selected_day_type])
plt.grid(True)

# Menampilkan plot di Streamlit
st.pyplot(plt)
