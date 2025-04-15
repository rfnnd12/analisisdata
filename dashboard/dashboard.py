import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Konfigurasi halaman
st.set_page_config(page_title="Dashboard Bike Sharing", layout="centered")

# Judul utama
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

# ================== Sidebar: Filter Interaktif ==================
st.sidebar.header("🔎 Filter Data")

# Filter berdasarkan musim
season_options = {
    1: 'Spring 🌼',
    2: 'Summer ☀️',
    3: 'Fall 🍂',
    4: 'Winter ❄️'
}
selected_season = st.sidebar.selectbox("Pilih Musim", options=list(season_options.keys()), 
                                         format_func=lambda x: season_options[x])

# Filter berdasarkan rentang tanggal
min_date = day_df['dateday'].min()
max_date = day_df['dateday'].max()
date_range = st.sidebar.date_input("Pilih Rentang Tanggal", [min_date, max_date],
                                   min_value=min_date, max_value=max_date)

# Terapkan filter ke day_df untuk seluruh dashboard
filtered_day_df = day_df[
    (day_df['season'] == selected_season) &
    (day_df['dateday'] >= pd.to_datetime(date_range[0])) &
    (day_df['dateday'] <= pd.to_datetime(date_range[1]))
]

# Berikan umpan balik jumlah data yang tersisa
st.sidebar.markdown(f"Data tersisa: **{filtered_day_df.shape[0]}** baris")

# ================== 1. Tren Penggunaan Sepeda ==================
st.markdown("---")
st.subheader("📈 Tren Penggunaan Sepeda (6 Bulan Terakhir)")

# Gunakan data yang telah difilter
if not filtered_day_df.empty:
    six_months_ago = filtered_day_df['dateday'].max() - pd.DateOffset(months=6)
    filtered_trend = filtered_day_df[filtered_day_df['dateday'] >= six_months_ago]
    
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(filtered_trend['dateday'], filtered_trend['count'], color='teal')
    ax.set_title('Tren Penggunaan Sepeda')
    ax.set_xlabel('Tanggal')
    ax.set_ylabel('Jumlah Penggunaan')
    ax.grid(True)
    st.pyplot(fig)
else:
    st.warning("Tidak ada data untuk ditampilkan dengan filter yang dipilih.")

# ================== 2. Korelasi Jumlah Rental ==================
st.markdown("---")
st.subheader("📊 Korelasi Jumlah Rental dan Variabel Lain")

# Kita bisa mengambil sample dari hour_df jika ada kolom 'year', 'hour', 'count'
# Jika perlu, filter data hour_df sesuai kebutuhan (misalnya berdasarkan musim/tanggal)
# Di sini misalnya kita menggunakan hour_df secara langsung atau sesuaikan jika ada informasi filter yang relevan
hour_correlation = hour_df[['year', 'hour', 'count']].corr()
st.write("**Korelasi terhadap variabel 'count':**")
st.dataframe(hour_correlation[['count']])

fig2, ax2 = plt.subplots(figsize=(6, 4))
sns.heatmap(hour_correlation, annot=True, cmap='coolwarm', ax=ax2)
ax2.set_title("Heatmap Korelasi")
st.pyplot(fig2)

# ================== 3. Distribusi Berdasarkan Musim ==================
st.markdown("---")
st.subheader("🌤️ Distribusi Jumlah Rental Berdasarkan Musim")

# Mapping nama musim dan hitung jumlah rental menggunakan filtered_day_df
season_map = {
    1: 'Spring 🌼',
    2: 'Summer ☀️',
    3: 'Fall 🍂',
    4: 'Winter ❄️'
}
seasonal_distribution = filtered_day_df.groupby('season')['count'].sum().rename(index=season_map)

fig3, ax3 = plt.subplots(figsize=(8, 4))
seasonal_distribution.plot(kind='bar', color='skyblue', ax=ax3)
ax3.set_title('Jumlah Rental per Musim')
ax3.set_xlabel('Musim')
ax3.set_ylabel('Jumlah Rental')
ax3.grid(axis='y')
st.pyplot(fig3)

# ================== Kesimpulan ==================
st.markdown("---")
st.subheader("📌 Kesimpulan Analisis")

st.info("""
## Conclusion
1. Tren penggunaan sepeda menunjukkan variasi sesuai dengan filter yang dipilih. Dengan memilih filter tertentu, kita dapat melihat tren dalam periode yang spesifik.
2. Korelasi antara variabel pada dataset hour menunjukkan hubungan antar variabel seperti ‘year’, ‘hour’, dan ‘count’ yang penting untuk pemahaman lebih lanjut.
3. Distribusi jumlah rental berdasarkan musim membantu mengidentifikasi periode dengan aktivitas tinggi dan rendah, sehingga dapat dijadikan acuan dalam strategi operasional.
""")

# ================== Footer ==================
st.markdown("---")
st.caption("📌 Dibuat oleh **Rafi Nanda Edtrian** | Proyek Analisis Data Dicoding")
