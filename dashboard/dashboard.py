import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Membaca data
hour_df = pd.read_csv('dashboard/hour_clean.csv')  

# Menampilkan header
st.title("Dashboard Analisis Data Bike Sharing")
st.write("Analisis data Bike Sharing untuk memahami pola penggunaan sepeda.")

# Group by weather and aggregate
hour_df.groupby('weather').agg({
    'count': ['max', 'min', 'mean', 'sum']
})

# Plot
plt.figure(figsize=(10, 6))
sns.boxplot(x='weather', y='count', data=hour_df)
plt.title("Pengaruh Kondisi Cuaca Terhadap Jumlah Penyewaan Sepeda")
plt.xlabel("Kondisi Cuaca")
plt.ylabel("Jumlah Penyewaan")
st.pyplot(plt)



# Membuat visualisasi tren penyewaan sepeda berdasarkan jam
hourly_rental_counts = hour_df.groupby('hour')['count'].sum().reset_index()

plt.figure(figsize=(12, 6))
sns.barplot(x='hour', y='count', data=hourly_rental_counts)
plt.title('Pola Penyewaan Sepeda Berdasarkan Jam')
plt.xlabel('Jam')
plt.ylabel('Jumlah Penyewaan')
st.pyplot(plt)  # Use st.pyplot instead of plt.show()

# Menghitung rata-rata jumlah penyewaan sepeda per musim
rata_rata_penyewaan_per_musim = hour_df.groupby('season')['count'].mean().reset_index()

# Membuat visualisasi perbandingan jumlah penyewaan sepeda di setiap musim
plt.figure(figsize=(10, 6))
sns.barplot(x='season', y='count', data=rata_rata_penyewaan_per_musim)
plt.title('Rata-rata Jumlah Penyewaan Sepeda per Musim')
plt.xlabel('Musim')
plt.ylabel('Rata-rata Jumlah Penyewaan')
st.pyplot(plt)  # Use st.pyplot instead of plt.show()
