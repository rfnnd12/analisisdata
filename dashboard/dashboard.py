import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Konfigurasi halaman
st.set_page_config(page_title="Dashboard Bike Sharing", layout="centered")
st.title("🚲 Dashboard Analisis Data Bike Sharing")
st.markdown("Analisis data *Bike Sharing* untuk memahami pola penggunaan sepeda dan faktor-faktor yang memengaruhinya.")

# Load data
@st.cache_data
def load_data():
    day_df = pd.read_csv("dashboard/day_cleaned.csv")
    hour_df = pd.read_csv("dashboard/hour_cleaned.csv")
    day_df['dateday'] = pd.to_datetime(day_df['dateday'])
    return day_df, hour_df

day_df, hour_df = load_data()

# ================== SIDEBAR ==================
st.sidebar.title("🔧 Filter")
# Filter tanggal
min_date = day_df['dateday'].min()
max_date = day_df['dateday'].max()

selected_date_range = st.sidebar.date_input(
    "Pilih Rentang Tanggal",
    value=[max_date - pd.DateOffset(months=6), max_date],
    min_value=min_date,
    max_value=max_date
)

# Filter korelasi
correlation_cols = st.sidebar.multiselect(
    "Pilih Kolom untuk Korelasi",
    ['year', 'hour', 'holiday', 'workingday', 'weather', 'temp', 'humidity', 'windspeed', 'count'],
    default=['year', 'hour', 'count']
)

# Filter musim
season_filter = st.sidebar.multiselect(
    "Pilih Musim untuk Distribusi",
    options=[1, 2, 3, 4],
    format_func=lambda x: {1: 'Spring 🌼', 2: 'Summer ☀️', 3: 'Fall 🍂', 4: 'Winter ❄️'}[x],
    default=[1, 2, 3, 4]
)

# ================== 1. Tren Penggunaan Sepeda ==================
st.markdown("---")
st.subheader("📈 Tren Penggunaan Sepeda")

start_date, end_date = selected_date_range
filtered_trend = day_df[(day_df['dateday'] >= pd.to_datetime(start_date)) & (day_df['dateday'] <= pd.to_datetime(end_date))]

fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(filtered_trend['dateday'], filtered_trend['count'], color='teal')
ax.set_title(f'Tren Penggunaan Sepeda ({start_date} s.d. {end_date})')
ax.set_xlabel('Tanggal')
ax.set_ylabel('Jumlah Penggunaan')
ax.grid(True)
st.pyplot(fig)

# ================== 2. Korelasi ==================
st.markdown("---")
st.subheader("📊 Korelasi Jumlah Rental dan Variabel Lain")

if len(correlation_cols) >= 2:
    corr = hour_df[correlation_cols].corr()
    st.write("**Korelasi terhadap 'count':**")
    st.dataframe(corr[['count']])

    fig2, ax2 = plt.subplots(figsize=(6, 4))
    sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax2)
    ax2.set_title("Heatmap Korelasi")
    st.pyplot(fig2)
else:
    st.warning("Pilih minimal 2 kolom di sidebar untuk melihat korelasi.")

# ================== 3. Distribusi Rental Berdasarkan Musim ==================
st.markdown("---")
st.subheader("🌤️ Distribusi Jumlah Rental Berdasarkan Musim")

season_map = {
    1: 'Spring 🌼',
    2: 'Summer ☀️',
    3: 'Fall 🍂',
    4: 'Winter ❄️'
}

# Filter berdasarkan musim dan rentang tanggal
filtered_season_df = day_df[
    (day_df['season'].isin(season_filter)) &
    (day_df['dateday'] >= pd.to_datetime(start_date)) &
    (day_df['dateday'] <= pd.to_datetime(end_date))
]

if filtered_season_df.empty:
    st.warning("Tidak ada data untuk musim dan rentang tanggal yang dipilih.")
else:
    seasonal_distribution = filtered_season_df.groupby('season')['count'].sum().rename(index=season_map)
    
    fig3, ax3 = plt.subplots(figsize=(8, 4))
    seasonal_distribution.plot(kind='bar', color='skyblue', ax=ax3)
    ax3.set_title('Jumlah Rental per Musim (Terseleksi)')
    ax3.set_xlabel('Musim')
    ax3.set_ylabel('Jumlah Rental')
    ax3.grid(axis='y')
    st.pyplot(fig3)

# ================== Footer ==================
st.markdown("---")
st.caption("📌 Dibuat oleh **Rafi Nanda Edtrian** | Proyek Analisis Data Dicoding")
