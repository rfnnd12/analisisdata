import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Menampilkan header
st.title("Dashboard Analisis Data Bike Sharing")
st.write("Analisis data Bike Sharing untuk memahami pola penggunaan sepeda.")

# Membaca data
hour_df = pd.read_csv('dashboard/hour_clean.csv')  

# Asumsikan `hour_df` sudah ada dan 'dateday' bertipe datetime
hour_df['dateday'] = pd.to_datetime(hour_df['dateday'])
hour_df['year'] = hour_df['dateday'].dt.year
hour_df['month'] = hour_df['dateday'].dt.month

# Agregasi bulanan
monthly_rentals = hour_df.groupby(['year', 'month'])['count'].sum().reset_index()
monthly_rentals = monthly_rentals.sort_values(by=['year', 'month'])

# Buat kolom datetime untuk plotting
monthly_rentals['month_date'] = pd.to_datetime(monthly_rentals[['year', 'month']].assign(day=1))

# ==================== STREAMLIT PLOTTING ====================

st.title("📊 Monthly Bike Rentals Trend (2011–2012)")

# Buat figure dan axis
fig, ax = plt.subplots(figsize=(12, 6))

# Line plot
ax.plot(monthly_rentals['month_date'], monthly_rentals['count'], marker='o', linestyle='-', color='tab:blue')

# Set judul dan label
ax.set_title('📈 Monthly Bike Rentals (2011–2012)', fontsize=14)
ax.set_xlabel('Month', fontsize=12)
ax.set_ylabel('Total Rentals', fontsize=12)

# Format tanggal di sumbu-x
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=1))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
plt.setp(ax.get_xticklabels(), rotation=45)

# Grid dan layout
ax.grid(True, linestyle='--', alpha=0.6)
fig.tight_layout()

# Tampilkan di Streamlit
st.pyplot(fig)


# ========================================================================================
# Tampilkan judul di Streamlit
st.header("📊 Distribusi Penyewaan Sepeda: Hari Kerja vs Hari Libur")

# Agregasi statistik mean, median, dan standar deviasi
holiday_weekday_agg = hour_df.groupby(['workingday', 'holiday'])['count'].agg(['mean', 'median', 'std']).reset_index()

# Visualisasi histogram dengan seaborn
fig, ax = plt.subplots(figsize=(10, 6))
sns.histplot(
    data=hour_df,
    x='count',
    hue='workingday',
    bins=30,
    kde=False,
    palette=['#FF9999', '#66B3FF'],
    ax=ax
)

# Judul dan label
ax.set_title('Distribusi Penyewaan Sepeda: Hari Kerja vs Hari Libur', fontsize=14)
ax.set_xlabel('Jumlah Penyewaan')
ax.set_ylabel('Frekuensi')
ax.legend(title='Hari Kerja', labels=['Hari Libur', 'Hari Kerja'])

# Tampilkan ke Streamlit
st.pyplot(fig)


# ========================================================================================
# Pastikan kolom tanggal sudah dalam format datetime
hour_df['dateday'] = pd.to_datetime(hour_df['dateday'])

# Ekstrak tahun dari kolom tanggal
hour_df['year'] = hour_df['dateday'].dt.year

# Agregasi jumlah penyewaan per tahun
yearly_rentals = hour_df.groupby('year')['count'].sum()

# ======================= STREAMLIT PLOTTING =======================

# Judul halaman Streamlit
st.header("📊 Total Bike Rentals per Year")

# Buat bar chart
fig, ax = plt.subplots(figsize=(8, 6))
sns.barplot(x=yearly_rentals.index, y=yearly_rentals.values, ax=ax)

# Judul dan label sumbu
ax.set_title('Total Bike Rentals per Year')
ax.set_xlabel('Year')
ax.set_ylabel('Total Rentals')

# Tampilkan plot di Streamlit
st.pyplot(fig)


# ========================================================================================

# Judul untuk bagian visualisasi
st.header("📦 Distribusi Penyewaan Sepeda: Hari Libur Nasional vs Hari Biasa")

# Buat figure dan axis
fig, ax = plt.subplots(figsize=(10, 6))

# Boxplot dengan seaborn
sns.boxplot(x='holiday', y='count', data=hour_df, palette='Set3', ax=ax)

# Judul dan label sumbu
ax.set_title('Distribusi Penyewaan Sepeda: Hari Libur Nasional vs Hari Biasa', fontsize=14)
ax.set_xlabel('Hari Libur (1: Ya, 0: Tidak)')
ax.set_ylabel('Jumlah Penyewaan')

# Tampilkan plot ke Streamlit
st.pyplot(fig)
