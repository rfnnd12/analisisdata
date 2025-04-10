import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- Konfigurasi halaman ---
st.set_page_config(
    page_title="Dashboard Bike Sharing",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- Judul utama ---
st.title("🚲 Dashboard Analisis Data Bike Sharing")
st.caption("Dibuat oleh Rafi Nanda Edtrian | Proyek Analisis Data Dicoding")

# --- Load data ---
day_df = pd.read_csv("dashboard/day_cleaned.csv")
hour_df = pd.read_csv("dashboard/hour_cleaned.csv")
day_df['dateday'] = pd.to_datetime(day_df['dateday'])

# --- Sidebar filter tanggal ---
with st.sidebar:
    st.sidebar.title("🛠️ Filter")
    min_date = day_df['dateday'].min()
    max_date = day_df['dateday'].max()
    start_date, end_date = st.date_input(
        "Pilih Rentang Tanggal",
        [min_date, max_date],
        min_value=min_date,
        max_value=max_date
    )

# --- Filter data berdasarkan tanggal ---
filtered_day_df = day_df[
    (day_df['dateday'] >= pd.to_datetime(start_date)) &
    (day_df['dateday'] <= pd.to_datetime(end_date))
]

# --- 1. Tren Penggunaan Sepeda ---
st.markdown("---")
st.subheader("📈 Tren Penggunaan Sepeda")

if filtered_day_df.empty:
    st.warning("Tidak ada data pada rentang tanggal yang dipilih.")
else:
    fig1, ax1 = plt.subplots(figsize=(12, 4))
    ax1.plot(filtered_day_df['dateday'], filtered_day_df['count'], marker='o', linestyle='-')
    ax1.set_title("Jumlah Penggunaan Sepeda dari Waktu ke Waktu")
    ax1.set_xlabel("Tanggal")
    ax1.set_ylabel("Jumlah Rental")
    ax1.grid(True)
    st.pyplot(fig1)

# --- 2. Korelasi Jumlah Rental dan Variabel Lain ---
st.markdown("---")
st.subheader("🔗 Korelasi Jumlah Rental dan Variabel Lain")

correlation = hour_df[['temp', 'atemp', 'humidity', 'windspeed', 'count']].corr()

fig2, ax2 = plt.subplots(figsize=(6, 4))
sns.heatmap(correlation, annot=True, cmap='YlGnBu', ax=ax2)
ax2.set_title("Matriks Korelasi")
st.pyplot(fig2)

# --- 3. Distribusi Jumlah Rental Berdasarkan Musim ---
st.markdown("---")
st.subheader("🌤️ Distribusi Jumlah Rental Berdasarkan Musim")

season_map = {
    1: 'Spring 🌼',
    2: 'Summer ☀️',
    3: 'Fall 🍂',
    4: 'Winter ❄️'
}

seasonal_distribution = filtered_day_df.groupby('season')['count'].sum().rename(index=season_map)

if seasonal_distribution.empty:
    st.warning("Tidak ada data musim untuk rentang tanggal yang dipilih.")
else:
    fig3, ax3 = plt.subplots(figsize=(6, 4))
    seasonal_distribution.plot(kind='bar', color='skyblue', ax=ax3)
    ax3.set_title('Jumlah Rental per Musim')
    ax3.set_xlabel('Musim')
    ax3.set_ylabel('Total Rental')
    ax3.grid(axis='y')
    st.pyplot(fig3)
