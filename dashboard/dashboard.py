import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Konfigurasi halaman
st.set_page_config(
    page_title="Analisis Penyewaan Sepeda",
    page_icon="🚴",
    layout="wide"
)

# Load data
data_sepeda = pd.read_csv('dashboard/data_sepeda_cleaned.csv')
data_sepeda['dteday'] = pd.to_datetime(data_sepeda['dteday'])

# ======================
# SIDEBAR FILTER
# ======================
with st.sidebar:
    st.title("🔍 Filter Data")
    
    # Filter tanggal
    min_date = data_sepeda['dteday'].min().date()
    max_date = data_sepeda['dteday'].max().date()
    date_range = st.date_input(
        "Rentang Tanggal",
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date
    )
    
    # Filter musim
    selected_seasons = st.multiselect(
        "Pilih Musim",
        options=data_sepeda['season'].unique(),
        default=data_sepeda['season'].unique()
    )
    
    # Filter tipe hari
    day_type = st.multiselect(
        "Tipe Hari",
        options=['Hari Kerja', 'Hari Libur'],
        default=['Hari Kerja', 'Hari Libur']
    )

