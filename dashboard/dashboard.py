import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import ipywidgets as widgets
from IPython.display import display

# Konfigurasi halaman
st.set_page_config(page_title="Dashboard Bike Sharing", layout="centered")

# Judul utama
st.title("🚲 Dashboard Analisis Data Bike Sharing")
st.markdown("Analisis data *Bike Sharing* untuk memahami pola penggunaan sepeda dan faktor-faktor yang memengaruhinya.")

# Load data
@st.cache_data
def load_data():
    hour_df = pd.read_csv("dashboard/hour_cleaned.csv")
    day_df['dateday'] = pd.to_datetime(day_df['dateday'])
    return day_df, hour_df

hour_df = load_data()


     # Widget untuk memilih filter
     filter_type_widget = widgets.Dropdown(options=['hour', 'dayofweek', 'month'], description='Filter Berdasarkan')
     filter_value_widget = widgets.IntSlider(min=1, max=24, description='Nilai Filter')

     # Fungsi untuk menampilkan histogram
     def plot_distribution(filter_type, filter_value):
         filtered_data = hour_df[hour_df[filter_type] == filter_value]['count']
         plt.figure(figsize=(8, 6))
         plt.hist(filtered_data, bins=10)
         plt.title(f'Distribusi Peminjaman Sepeda ({filter_type} = {filter_value})')
         plt.xlabel('Jumlah Peminjaman')
         plt.ylabel('Frekuensi')
         plt.show()

     # Menampilkan widget dan menghubungkannya dengan fungsi plot_distribution
     widgets.interactive(plot_distribution, filter_type=filter_type_widget, filter_value=filter_value_widget)

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
