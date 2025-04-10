import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Dashboard Analisis Data Bike Sharing")
st.write("Analisis data Bike Sharing untuk memahami pola penggunaan sepeda.")

# Load dataset
day_df = pd.read_csv("dashboard/day_cleaned.csv")
hour_df = pd.read_csv("dashboard/hour_cleaned.csv")
# Format tanggal
day_df['dateday'] = pd.to_datetime(day_df['dateday'])

# --- Tren Penjualan Produk X (6 Bulan Terakhir) ---
st.subheader("Tren Penggunaan Sepeda (6 Bulan Terakhir)")
six_months_ago = day_df['dateday'].max() - pd.DateOffset(months=6)
filtered_data = day_df[day_df['dateday'] >= six_months_ago]

fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(filtered_data['dateday'], filtered_data['count'])
ax.set_title('Tren Penggunaan Sepeda')
ax.set_xlabel('Tanggal')
ax.set_ylabel('Jumlah Penggunaan')
ax.grid(True)
st.pyplot(fig)

# --- Korelasi Jumlah Rental ---
st.subheader("Korelasi Jumlah Rental dan Variabel Lain")
correlation = hour_df[['year', 'hour', 'count']].corr()
st.write(correlation['count'])

fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(correlation, annot=True, cmap='coolwarm', ax=ax)
st.pyplot(fig)

# --- Distribusi Jumlah Rental Berdasarkan Musim ---
st.subheader("Distribusi Rental Berdasarkan Musim")
seasonal_distribution = day_df.groupby('season')['count'].sum()

fig, ax = plt.subplots(figsize=(8, 6))
seasonal_distribution.plot(kind='bar', color=['skyblue', 'lightgreen', 'orange', 'lightcoral'], ax=ax)
ax.set_title('Distribusi Jumlah Rental Berdasarkan Musim')
ax.set_xlabel('Musim')
ax.set_ylabel('Jumlah Rental')
st.pyplot(fig)

# Footer
st.caption("Dibuat oleh [Rafi Nanda Edtrian] - Proyek Analisis Data Dicoding")
