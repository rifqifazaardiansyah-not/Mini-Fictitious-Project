import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Baca data
df = pd.read_csv("penjualan_umkm_fiktif.csv")
df['Tanggal'] = pd.to_datetime(df['Tanggal'])  # Konversi ke tipe datetime

# Sidebar menu
st.sidebar.title("Dashboard Penjualan UMKM")
menu = st.sidebar.radio("Pilih Visualisasi", [
    "Produk Terlaris",
    "Pendapatan Harian",
    "Harga Satuan per Produk",
    "Pendapatan per Kota"
])

st.title("📊 Dashboard Penjualan UMKM Fiktif")

# 1. Produk Terlaris
if menu == "Produk Terlaris":
    st.subheader("Produk Terlaris Berdasarkan Jumlah Terjual")
    produk_terlaris = df.groupby('Produk')['Jumlah Terjual'].sum().sort_values(ascending=False)
    fig, ax = plt.subplots()
    bars = produk_terlaris.plot(kind='bar', color='skyblue', ax=ax)
    for i, val in enumerate(produk_terlaris):
        ax.text(i, val - 1, str(val), ha='center', va='top', color='white', fontweight='bold')
    plt.ylabel("Jumlah Terjual")
    plt.xticks(rotation=45)
    st.pyplot(fig)

# 2. Pendapatan Harian
elif menu == "Pendapatan Harian":
    st.subheader("Tren Pendapatan Harian")
    pendapatan_harian = df.groupby('Tanggal')['Total'].sum().sort_index()
    fig, ax = plt.subplots()
    pendapatan_harian.plot(ax=ax, marker='o', color='orange')
    plt.ylabel("Total Pendapatan (Rp)")
    plt.grid(True)
    st.pyplot(fig)

# 3. Harga Satuan per Produk
elif menu == "Harga Satuan per Produk":
    st.subheader("Harga Satuan Rata-rata per Produk")
    harga_satuan = df.groupby('Produk')['Harga Satuan'].mean().sort_values()
    fig, ax = plt.subplots()
    harga_satuan.plot(kind='barh', ax=ax, color='green')
    for i, val in enumerate(harga_satuan):
        ax.text(val - (val * 0.05), i, f'{val:.0f}', va='center', ha='right', color='white', fontweight='bold')

    plt.xlabel("Harga Satuan (Rp)")
    st.pyplot(fig)

# 4. Pendapatan per Kota
elif menu == "Pendapatan per Kota":
    st.subheader("Total Pendapatan per Kota")
    kota_terbaik = df.groupby('Kota')['Total'].sum().sort_values(ascending=True)
    fig, ax = plt.subplots()
    kota_terbaik.plot(kind='barh', ax=ax, color='purple')
    for i, val in enumerate(kota_terbaik):
        ax.text(val - (val * 0.02), i, f'{val:,.0f}', va='center', ha='right', color='white', fontweight='bold')
    plt.ylabel("Kota")
    plt.xlabel("Pendapatan")
    st.pyplot(fig)
