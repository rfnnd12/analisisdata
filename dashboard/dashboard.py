import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Judul aplikasi
st.title("Dashboard Analisis Data")

# Memuat dataset
@st.cache_data
def load_data():
    df = pd.read_csv("data/data_1.csv")  # Ganti dengan nama file yang kamu pakai
    return df

df = load_data()

# Tampilkan data awal
st.subheader("Preview Dataset")
st.write(df.head())

# Ringkasan statistik
st.subheader("Ringkasan Statistik")
st.write(df.describe())

# Filter kolom
st.sidebar.subheader("Filter Data")
selected_column = st.sidebar.selectbox("Pilih Kolom untuk Visualisasi", df.columns)

# Visualisasi Distribusi
st.subheader(f"Distribusi Data: {selected_column}")
fig, ax = plt.subplots()
sns.histplot(df[selected_column].dropna(), kde=True, ax=ax)
st.pyplot(fig)

# Korelasi antar variabel numerik
if st.checkbox("Tampilkan Korelasi Variabel Numerik"):
    st.subheader("Matriks Korelasi")
    corr = df.corr(numeric_only=True)
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)
    st.pyplot(fig)

# Footer
st.caption("Dibuat oleh [Nama Kamu] - Proyek Analisis Data Dicoding")
