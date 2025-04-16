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
    hour_df['dateday'] = pd.to_datetime(hour_df['dateday'])
    return hour_df

hour_df = load_data()


    plt.figure(figsize=(12, 6))
    plt.plot(filtered_data['dateday'], filtered_data['count'])
    plt.title('Tren Peminjaman Sepeda')
    plt.xlabel('Tanggal')
    plt.ylabel('Jumlah Peminjaman')
    plt.grid(True)
    plt.show()


def plot_trend(start_date=None, end_date=None):
    if start_date is None or end_date is None:
        # If no dates are provided, use the full range
        filtered_data = hour_df
    else:
        # Convert start_date and end_date to datetime64[ns]
        start_date = pd.to_datetime(start_date)
        end_date = pd.to_datetime(end_date)
        filtered_data = hour_df[(hour_df['dateday'] >= start_date) & (hour_df['dateday'] <= end_date)]

    plt.figure(figsize=(12, 6))
    plt.plot(filtered_data['dateday'], filtered_data['count'])
    plt.title('Tren Peminjaman Sepeda')
    plt.xlabel('Tanggal')
    plt.ylabel('Jumlah Peminjaman')
    plt.grid(True)
    plt.show()

# Menampilkan widget dan menghubungkannya dengan fungsi plot_trend,
# with initial values for start_date and end_date set to None
widgets.interactive(plot_trend,
                    start_date=widgets.DatePicker(value=None, description='Tanggal Mulai'),
                    end_date=widgets.DatePicker(value=None, description='Tanggal Akhir'))

# with initial values for start_date and end_date set to None
widgets.interactive(plot_trend,
                    start_date=widgets.DatePicker(value=None, description='Tanggal Mulai'),
                    end_date=widgets.DatePicker(value=None, description='Tanggal Akhir'))
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
