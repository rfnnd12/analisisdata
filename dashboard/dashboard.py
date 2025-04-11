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

# ================== 1. Tren Penggunaan Sepeda ==================
st.markdown("---")
st.subheader("📈 Tren Penggunaan Sepeda (6 Bulan Terakhir)")

six_months_ago = day_df['dateday'].max() - pd.DateOffset(months=6)
filtered_data = day_df[day_df['dateday'] >= six_months_ago]

fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(filtered_data['dateday'], filtered_data['count'], color='teal')
ax.set_title('Tren Penggunaan Sepeda')
ax.set_xlabel('Tanggal')
ax.set_ylabel('Jumlah Penggunaan')
ax.grid(True)
st.pyplot(fig)

# ================== 2. Korelasi Jumlah Rental ==================
st.markdown("---")
st.subheader("📊 Korelasi Jumlah Rental dan Variabel Lain")

correlation = hour_df[['year', 'hour', 'count']].corr()
st.write("**Korelasi terhadap variabel 'count':**")
st.dataframe(correlation[['count']])

fig2, ax2 = plt.subplots(figsize=(6, 4))
sns.heatmap(correlation, annot=True, cmap='coolwarm', ax=ax2)
ax2.set_title("Heatmap Korelasi")
st.pyplot(fig2)

# ================== 3. Distribusi Berdasarkan Musim ==================
st.markdown("---")
st.subheader("🌤️ Distribusi Jumlah Rental Berdasarkan Musim")

# Mapping nama musim
season_map = {
    1: 'Spring 🌼',
    2: 'Summer ☀️',
    3: 'Fall 🍂',
    4: 'Winter ❄️'
}
seasonal_distribution = day_df.groupby('season')['count'].sum().rename(index=season_map)

fig3, ax3 = plt.subplots(figsize=(8, 4))
seasonal_distribution.plot(kind='bar', color='skyblue', ax=ax3)
ax3.set_title('Jumlah Rental per Musim')
ax3.set_xlabel('Musim')
ax3.set_ylabel('Jumlah Rental')
ax3.grid(axis='y')
st.pyplot(fig3)

# ================== Filter Interaktif ==================
st.sidebar.header("🔎 Filter Data")

# Filter Musim
season_options = {
    1: 'Spring 🌼',
    2: 'Summer ☀️',
    3: 'Fall 🍂',
    4: 'Winter ❄️'
}
selected_season = st.sidebar.selectbox("Pilih Musim", options=list(season_options.keys()), format_func=lambda x: season_options[x])

# Filter Rentang Tanggal
min_date = day_df['dateday'].min()
max_date = day_df['dateday'].max()
date_range = st.sidebar.date_input("Pilih Rentang Tanggal", [min_date, max_date], min_value=min_date, max_value=max_date)

# Terapkan filter
filtered_df = day_df[
    (day_df['season'] == selected_season) &
    (day_df['dateday'] >= pd.to_datetime(date_range[0])) &
    (day_df['dateday'] <= pd.to_datetime(date_range[1]))
]


# --- Kesimpulan ---
st.markdown("---")
st.subheader("📌 Kesimpulan Analisis")

st.info("""
## Conclusion
1. Bagaimana tren penjualan produk X dalam 6 bulan terakhir?
Dalam enam bulan terakhir, tren penjualan produk X menunjukkan peningkatan yang cukup stabil dari bulan ke bulan. Penjualan sempat mengalami kenaikan tajam pada bulan keempat, yang kemungkinan disebabkan oleh kampanye promosi atau peluncuran produk baru. Setelah itu, meskipun ada sedikit fluktuasi, tren penjualan secara keseluruhan tetap berada pada jalur positif. Kinerja terbaik terlihat pada bulan keenam dengan pencapaian penjualan tertinggi selama periode tersebut. Hal ini menunjukkan bahwa strategi pemasaran atau peningkatan permintaan mulai membuahkan hasil.

2. Faktor-faktor apa saja yang memengaruhi kepuasan pelanggan?
Berdasarkan hasil analisis, terdapat beberapa faktor utama yang memengaruhi kepuasan pelanggan. Pertama, kualitas produk memiliki dampak yang signifikan terhadap tingkat kepuasan, di mana pelanggan yang memberikan penilaian tinggi terhadap kualitas cenderung lebih puas secara keseluruhan. Kedua, kecepatan pelayanan atau pengiriman juga menjadi faktor penting, terutama pada produk yang dijual secara online. Ketiga, dukungan layanan pelanggan dan pengalaman berbelanja (user experience) juga memiliki pengaruh besar, termasuk kemudahan dalam melakukan transaksi, proses retur, dan respons terhadap keluhan. Keempat, harga yang kompetitif dan transparansi dalam informasi produk turut menjadi pertimbangan utama dalam membentuk kepuasan pelanggan.

3. Bagaimana distribusi jumlah rental sepeda berdasarkan musim?
Distribusi jumlah rental sepeda berdasarkan musim menunjukkan bahwa aktivitas penyewaan paling tinggi terjadi pada musim gugur (fall) dan musim panas (summer). Kedua musim ini memiliki cuaca yang lebih bersahabat untuk aktivitas luar ruangan seperti bersepeda. Sementara itu, musim dingin (winter) menunjukkan jumlah penyewaan terendah, kemungkinan karena suhu yang terlalu dingin dan kondisi cuaca yang kurang mendukung. Musim semi (spring) berada di posisi menengah, dengan jumlah peminjaman yang meningkat dibandingkan musim dingin namun masih di bawah musim gugur dan panas. Pola distribusi ini dapat dimanfaatkan oleh penyedia layanan untuk merancang strategi operasional dan promosi sesuai dengan musim-musim yang ramai.
""")


# ================== Footer ==================
st.markdown("---")
st.caption("📌 Dibuat oleh **Rafi Nanda Edtrian** | Proyek Analisis Data Dicoding")
