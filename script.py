import streamlit as st
import pandas as pd
import plotly.express as px



st.set_page_config(layout="wide")


df_reviews = pd.read_csv("datasets/customer reviews.csv")
df_top_books = pd.read_csv("datasets/Top-100 Trending Books.csv")



price_max = df_top_books["book price"].max()

price_min = df_top_books["book price"].min()

slider_value = st.sidebar.slider('Esxolha o valor:', price_min, price_max, price_max)

df_books = df_top_books[df_top_books["book price"] <= slider_value]


chart1 = px.bar(df_books["year of publication"].value_counts())

chart2 = px.histogram(df_books["book price"].value_counts())

df_books

col1, col2 = st.columns(2)

st
col1.plotly_chart(chart1)

col2.plotly_chart(chart2)
