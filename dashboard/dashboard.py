import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Konfigurasi halaman
st.set_page_config(page_title="Dashboard Bike Sharing", layout="centered")

# Judul utama
st.title("🚲 Dashboard Analisis Data Bike Sharing")
st.markdown("Analisis data *Bike Sharing* untuk memahami pola penggunaan sepeda dan faktor-faktor yang memengaruhinya.")

# Load the cleaned dataset
hour_df = pd.read_csv('/hour_cleaned.csv')

# Grouping data by season
seasonal_distribution = hour_df.groupby('season')['count'].sum()

# Create a bar chart
st.subheader("Distribusi Jumlah Rental Sepeda Berdasarkan Musim")
plt.bar(seasonal_distribution.index, seasonal_distribution.values, color=['#FF9999', '#66B3FF', '#99FF99', '#FFCC99'])
plt.xlabel('Musim')
plt.ylabel('Jumlah Rental')
plt.title('Jumlah Rental Sepeda per Musim')
st.pyplot(plt)

# Grouping data by hour
hourly_distribution = hour_df.groupby('hour')['count'].sum()

# Create a line chart
st.subheader("Hubungan Antara Jam dan Jumlah Rental Sepeda")
plt.plot(hourly_distribution.index, hourly_distribution.values, marker='o', color='purple')
plt.xlabel('Jam')
plt.ylabel('Jumlah Rental')
plt.title('Jumlah Rental Sepeda per Jam')
st.pyplot(plt)

# Calculate correlation
correlation = hour_df[['year', 'hour', 'count']].corr()

# Create a heatmap
st.subheader("Faktor-Faktor yang Mempengaruhi Jumlah Rental Sepeda")
plt.figure(figsize=(8, 6))
sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Korelasi antara Tahun, Jam, dan Jumlah Rental')
st.pyplot(plt)
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
