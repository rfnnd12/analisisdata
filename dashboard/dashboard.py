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

