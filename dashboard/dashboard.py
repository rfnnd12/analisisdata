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

# ================== Footer ==================
st.markdown("---")
st.caption("📌 Dibuat oleh **Rafi Nanda Edtrian** | Proyek Analisis Data Dicoding")
