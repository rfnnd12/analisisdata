import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Judul aplikasi
st.title("Dashboard Analisis Data")

# Muat dataset day_df dan hour_df
day_df = pd.read_csv("Dashboard/day_clean.csv")
hour_df = pd.read_csv("Dashboard/hour_clean.csv")

# Menampilkan header
st.title("Dashboard Analisis Data Bike Sharing")
st.write("Analisis data Bike Sharing untuk memahami pola penggunaan sepeda.")

# Menampilkan data yang dibaca
st.subheader("Data Head")
st.write(data.head())
# Footer
st.caption("Dibuat oleh [Nama Kamu] - Proyek Analisis Data Dicoding")
