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
selected_months = st.sidebar.multiselect("Pilih Bulan untuk Filter:", hour_df['month'].unique(), default=hour_df['month'].unique())  # Pilih bulan
selected_weather = st.sidebar.multiselect("Pilih Kondisi Cuaca:", hour_df['weather'].unique(), default=hour_df['weather'].unique())  # Pilih kondisi cuaca

# Memfilter data berdasarkan pilihan dari sidebar
filtered_df_month = hour_df[hour_df['month'].isin(selected_months)]  # Filter berdasarkan bulan
filtered_df_weather = filtered_df_month[filtered_df_month['weather'].isin(selected_weather)]  # Filter berdasarkan cuaca

# Membuat box plot untuk distribusi jumlah penyewaan sepeda per bulan dan cuaca
plt.figure(figsize=(12, 6))

sns.boxplot(x='month', y='count', hue='weather', data=filtered_df_weather)  # Menggunakan filtered_df_weather

plt.title('Pengaruh Kondisi Cuaca terhadap Jumlah Penyewaan Sepeda pada Bulan Tertentu')
plt.xlabel('Bulan')
plt.ylabel('Jumlah Penyewaan Sepeda')
plt.legend(title='Kondisi Cuaca')

# Menampilkan plot di Streamlit
st.pyplot(plt)
