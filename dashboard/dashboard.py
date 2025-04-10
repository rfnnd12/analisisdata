import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Konfigurasi awal tampilan
st.set_page_config(page_title="Dashboard Bike Sharing", layout="wide")
st.markdown("<style>h1, h2, h3 { color: #0D3B66; }</style>", unsafe_allow_html=True)

# Judul
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

# Layout kolom untuk konten
col1, col2 = st.columns(2)

# ========== Bagian 1 ==========
with col1:
    st.subheader("📈 Tren Penggunaan Sepeda (6 Bulan Terakhir)")
    six_months_ago = day_df['dateday'].max() - pd.DateOffset(months=6)
    filtered_data = day_df[day_df['dateday'] >= six_months_ago]

    fig1, ax1 = plt.subplots(figsize=(10, 4))
    ax1.plot(filtered_data['dateday'], filtered_data['count'], color='#1f77b4')
    ax1.set_title('Tren Penggunaan Sepeda', fontsize=12)
    ax1.set_xlabel('Tanggal')
    ax1.set_ylabel('Jumlah Penggunaan')
    ax1.grid(True)
    st.pyplot(fig1)

# ========== Bagian 2 ==========
with col2:
    st.subheader("📊 Korelasi Jumlah Rental dan Variabel Lain")
    selected_cols = st.multiselect(
        "Pilih kolom untuk korelasi", 
        ['year', 'hour', 'count'], 
        default=['year', 'hour', 'count']
    )
    if len(selected_cols) >= 2:
        corr = hour_df[selected_cols].corr()
        st.write("**Korelasi terhadap 'count':**")
        st.write(corr['count'])

        fig2, ax2 = plt.subplots(figsize=(6, 4))
        sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax2)
        st.pyplot(fig2)
    else:
        st.warning("Pilih minimal 2 kolom untuk melihat korelasi.")

# ========== Bagian 3 ==========
st.markdown("---")
st.subheader("🌤️ Distribusi Rental Berdasarkan Musim")
season_map = {
    1: 'Spring 🌼',
    2: 'Summer ☀️',
    3: 'Fall 🍂',
    4: 'Winter ❄️'
}
seasonal_distribution = day_df.groupby('season')['count'].sum().rename(index=season_map)

fig3, ax3 = plt.subplots(figsize=(8, 4))
seasonal_distribution.plot(kind='bar', color=['skyblue', 'lightgreen', 'orange', 'lightcoral'], ax=ax3)
ax3.set_title('Jumlah Rental per Musim', fontsize=12)
ax3.set_xlabel('Musim')
ax3.set_ylabel('Jumlah Rental')
ax3.grid(axis='y')
st.pyplot(fig3)

# Footer
st.markdown("---")
st.caption("📌 Dibuat oleh **Rafi Nanda Edtrian** | Proyek Analisis Data Dicoding")
