import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Judul aplikasi
st.title("Dashboard Analisis Data")

# Membaca data
data = pd.read_csv('data/data_1.csv')

# Menampilkan header
st.title("Dashboard Analisis Data Bike Sharing")
st.write("Analisis data Bike Sharing untuk memahami pola penggunaan sepeda.")

# Menampilkan data yang dibaca
st.subheader("Data Head")
st.write(data.head())
# Footer
st.caption("Dibuat oleh [Nama Kamu] - Proyek Analisis Data Dicoding")
