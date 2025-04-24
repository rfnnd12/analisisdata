import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

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
