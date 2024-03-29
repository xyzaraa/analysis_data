# -*- coding: utf-8 -*-
"""strstreamlit_dashboard.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WwEeSJcA8-Aepd3Nmyh7VOPE826jyYz_
"""

import streamlit as st
import pandas as pd
import plotly.express as px

#Title dashboard
st.header('Bike Sharing Rentals')

#Load dataset
day_df = pd.read_csv('C:/Users/kiara/Docs/Kuliah/Campus Activity/Bangkit/bike_rentals_by_zara/bike-sharing-dataset/day.csv')
hour_df = pd.read_csv('C:/Users/kiara/Docs/Kuliah/Campus Activity/Bangkit/bike_rentals_by_zara/bike-sharing-dataset/hour.csv')

#Sidebar
with st.sidebar:
    #logo company
    st.image("bike rentals.png")
   

# Plot 1: Bar Plot with Plotly Express
fig1 = px.bar(data_frame=day_df, x='weekday', y='cnt', title='Jumlah Pelanggan Berdasarkan Hari')
st.plotly_chart(fig1)

# Plot 2: Scatter Plot with Plotly Express
fig2 = px.scatter(data_frame=day_df, x='windspeed', y='cnt',
                  title='Hubungan Antara Kecepatan Angin dan Jumlah Penyewaan Sepeda',
                  labels={'windspeed': 'Kecepatan Angin', 'cnt': 'Jumlah Penyewaan'})
st.plotly_chart(fig2)

# Plot 3: Bar Plot with Plotly Express
fig3 = px.bar(data_frame=day_df, x='weathersit', y='cnt',
              title='Jumlah Pengguna Sepeda berdasarkan Kondisi Cuaca',
              labels={'weathersit': 'Kondisi Cuaca', 'cnt': 'Jumlah Pengguna Sepeda'})
st.plotly_chart(fig3)
 
st.caption('Created by Kiara Azzahra')

#!streamlit run bike_sharing_rentals.py & npx localtunnel --port 8501
#Untuk mengakses dashboard menggunakan colab, run ulang kode diatas agar mendapatkan URL baru dan masukkan external URL sebagai passwordnya
