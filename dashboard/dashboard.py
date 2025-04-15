import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Fungsi untuk memuat data dengan caching agar tidak membebani setiap kali interaksi
@st.cache_data
def load_data():
    # Sesuaikan path dan nama file dataset sesuai struktur proyek
    df = pd.read_csv('data/main_data.csv')
    
    # Pastikan kolom tanggal dikonversi ke format datetime
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'])
    return df

# Memuat data
data = load_data()

st.title("Dashboard Analisis Data")
st.write("Dashboard ini menyajikan hasil analisis data secara interaktif.")

# Sidebar: Filter berdasarkan rentang tanggal
if 'date' in data.columns:
    st.sidebar.header("Filter Berdasarkan Tanggal")
    min_date = data['date'].min()
    max_date = data['date'].max()

    # Menggunakan st.date_input untuk memilih rentang tanggal
    date_range = st.sidebar.date_input("Pilih rentang tanggal", [min_date, max_date])
    if len(date_range) == 2:
        start_date, end_date = date_range
        start_date = pd.to_datetime(start_date)
        end_date = pd.to_datetime(end_date)
        # Filter data berdasarkan rentang tanggal
        data = data[(data['date'] >= start_date) & (data['date'] <= end_date)]
    st.write(f"Jumlah data setelah filter tanggal: {data.shape[0]}")

# Sidebar: Contoh fitur filter tambahan (misalnya filtering berdasarkan kategori)
if 'kategori' in data.columns:
    st.sidebar.header("Filter Berdasarkan Kategori")
    kategori_list = st.sidebar.multiselect("Pilih Kategori", options=data['kategori'].unique())
    if kategori_list:
        data = data[data['kategori'].isin(kategori_list)]
    st.write(f"Jumlah data setelah filter kategori: {data.shape[0]}")

# Visualisasi 1: Contoh visualisasi data berdasarkan tanggal (misalnya total transaksi per hari)
if 'transaksi' in data.columns and 'date' in data.columns:
    st.subheader("Jumlah Transaksi Harian")
    # Mengelompokkan data berdasarkan tanggal
    daily_sum = data.groupby(data['date'].dt.date)['transaksi'].sum().reset_index()
    
    # Membuat plot
    fig, ax = plt.subplots()
    ax.plot(daily_sum['date'], daily_sum['transaksi'], marker='o')
    ax.set_title("Jumlah Transaksi per Hari")
    ax.set_xlabel("Tanggal")
    ax.set_ylabel("Total Transaksi")
    plt.xticks(rotation=45)
    st.pyplot(fig)
else:
    st.write("Data tidak menyediakan informasi transaksi untuk divisualisasikan.")

# Visualisasi 2: Contoh visualisasi distribusi kategori (jika kolom 'kategori' tersedia)
if 'kategori' in data.columns:
    st.subheader("Distribusi Kategori")
    fig2, ax2 = plt.subplots()
    sns.countplot(x='kategori', data=data, ax=ax2, palette="viridis")
    ax2.set_title("Frekuensi Kategori")
    st.pyplot(fig2)

st.write("Dashboard ini menyediakan filter interaktif yang memungkinkan pengguna melihat data yang relevan berdasarkan tanggal atau kategori.")
