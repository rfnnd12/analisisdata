import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Membaca data
hour_df = pd.read_csv('dashboard/hour_clean.csv')  # Pastikan file CSV berada dalam folder yang sama

# Sidebar untuk filter interaktif
selected_season = st.sidebar.multiselect("Pilih Musim untuk Filter:", hour_df['season'].unique())
selected_holiday = st.sidebar.selectbox("Pilih Hari Libur atau Hari Kerja:", ['Libur', 'Bukan Libur'])

# Filter data berdasarkan pilihan dari sidebar
filtered_df_season = hour_df[hour_df['season'].isin(selected_season)]  # Menggunakan .isin untuk beberapa musim
filtered_df_holiday = filtered_df_season[filtered_df_season['holiday'] == (0 if selected_holiday == 'Bukan Libur' else 1)]

# Mengelompokkan data dan menghitung rata-rata 'cnt'
rata_rata_penyewaan = filtered_df_holiday.groupby(['season', 'holiday', 'workingday'])['count'].mean().reset_index()

# Membuat bar chart
plt.figure(figsize=(12, 6))
sns.barplot(x='season', y='count', hue='workingday', data=rata_rata_penyewaan)  # Tidak perlu filter lebih lanjut karena sudah dilakukan
plt.title('Rata-rata Jumlah Penyewaan Sepeda per Musim (Hari Kerja vs. Hari Libur)')
plt.xlabel('Musim')
plt.ylabel('Rata-rata Jumlah Penyewaan')
plt.legend(title='Tipe Hari', labels=['Hari Kerja', 'Hari Libur'])

# Menampilkan plot di Streamlit
st.pyplot(plt)
