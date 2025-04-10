import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Dashboard Analisis Data Bike Sharing")
st.write("Analisis data Bike Sharing untuk memahami pola penggunaan sepeda.")

# Load dataset
day_df = pd.read_csv("dashboard/day_cleaned.csv")
hour_df = pd.read_csv("dashboard/hour_cleaned.csv")


# Footer
st.caption("Dibuat oleh [Nama Kamu] - Proyek Analisis Data Dicoding")
