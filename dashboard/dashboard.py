import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.dates as mdates

# Konfigurasi dasar
st.set_page_config(layout="wide")
st.title("🚲 Dashboard Analisis Data Bike Sharing")

# Load data
hour_df = pd.read_csv('dashboard/hour_clean.csv')
hour_df['dateday'] = pd.to_datetime(hour_df['dateday'])
hour_df['year'] = hour_df['dateday'].dt.year
hour_df['month'] = hour_df['dateday'].dt.month
hour_df['day_name'] = hour_df['dateday'].dt.day_name()

# ========================== SIDEBAR ==========================

st.sidebar.header("🔎 Filter Data")

# Tahun dan bulan unik
available_years = sorted(hour_df['year'].unique())
available_months = sorted(hour_df['month'].unique())

selected_years = st.sidebar.multiselect("Pilih Tahun", available_years, default=available_years)
selected_months = st.sidebar.multiselect("Pilih Bulan", available_months, default=available_months)

# Filter data sesuai pilihan sidebar
filtered_df = hour_df[
    hour_df['year'].isin(selected_years) &
    hour_df['month'].isin(selected_months)
]

# ==================== Monthly Trend Plot ====================

st.subheader("📊 Tren Penyewaan Sepeda Bulanan")

monthly_rentals = filtered_df.groupby(['year', 'month'])['count'].sum().reset_index()
monthly_rentals = monthly_rentals.sort_values(by=['year', 'month'])
monthly_rentals['month_date'] = pd.to_datetime(monthly_rentals[['year', 'month']].assign(day=1))

fig, ax = plt.subplots(figsize=(12, 5))
ax.plot(monthly_rentals['month_date'], monthly_rentals['count'], marker='o', linestyle='-', color='tab:blue')
ax.set_title('📈 Monthly Bike Rentals', fontsize=14)
ax.set_xlabel('Month')
ax.set_ylabel('Total Rentals')
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=1))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
plt.setp(ax.get_xticklabels(), rotation=45)
ax.grid(True, linestyle='--', alpha=0.6)
fig.tight_layout()
st.pyplot(fig)

# ==================== Histogram Hari Kerja vs Libur ====================

st.subheader("📊 Distribusi Penyewaan: Hari Kerja vs Hari Libur")

fig, ax = plt.subplots(figsize=(10, 5))
sns.histplot(data=filtered_df, x='count', hue='workingday', bins=30,
             palette=['#FF9999', '#66B3FF'], ax=ax)
ax.set_title('Distribusi Penyewaan: Hari Kerja vs Hari Libur', fontsize=14)
ax.set_xlabel('Jumlah Penyewaan')
ax.set_ylabel('Frekuensi')
ax.legend(title='Hari Kerja', labels=['Hari Libur', 'Hari Kerja'])
st.pyplot(fig)

# ==================== Bar Chart Tahunan ====================

st.subheader("📊 Total Penyewaan Sepeda per Tahun")

yearly_rentals = filtered_df.groupby('year')['count'].sum()
fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(x=yearly_rentals.index, y=yearly_rentals.values, ax=ax)
ax.set_title('Total Penyewaan Sepeda per Tahun')
ax.set_xlabel('Tahun')
ax.set_ylabel('Jumlah Penyewaan')
st.pyplot(fig)

# ==================== Boxplot Hari Libur Nasional ====================

st.subheader("📦 Distribusi Penyewaan: Hari Libur Nasional vs Hari Biasa")

fig, ax = plt.subplots(figsize=(10, 5))
sns.boxplot(x='holiday', y='count', data=filtered_df, palette='Set3', ax=ax)
ax.set_title('Distribusi Penyewaan: Hari Libur Nasional vs Hari Biasa', fontsize=14)
ax.set_xlabel('Hari Libur (1: Ya, 0: Tidak)')
ax.set_ylabel('Jumlah Penyewaan')
st.pyplot(fig)
