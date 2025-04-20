import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Membaca data
data = pd.read_csv('dashboard/hour_cleaned.csv')  # Pastikan file CSV berada dalam folder yang sama

# Menampilkan header
st.title("Dashboard Analisis Data Bike Sharing")
st.write("Analisis data Bike Sharing untuk memahami pola penggunaan sepeda.")


plt.figure(figsize=(10,6))
sns.boxplot(x='weather', y='count', data=hour_df)
plt.title("Pengaruh Kondisi Cuaca Terhadap Jumlah Penyewaan Sepeda")
plt.xlabel("Kondisi Cuaca")
plt.ylabel("Jumlah Penyewaan")
plt.show()


