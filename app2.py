import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Sales Dashboard", layout="wide")
st.title("📊 Sales Dashboard for Commercial Store")

df = pd.read_csv("Supermart Grocery Sales - Retail Analytics Dataset.csv", parse_dates=['Order Date'], dayfirst=True)

with st.sidebar:
    st.header("🔍 Filter Data")
    selected_region = st.multiselect("Select Region", options=df['Region'].unique(), default=df['Region'].unique())
    selected_category = st.multiselect("Select Category", options=df['Category'].unique(), default=df['Category'].unique())

df_filtered = df[(df['Region'].isin(selected_region)) & (df['Category'].isin(selected_category))]

st.subheader("📈 Daily Sales Trend")
sales_trend = df_filtered.groupby('Order Date')['Sales'].sum().reset_index()
fig1 = px.line(sales_trend, x='Order Date', y='Sales', title="Sales Over Time", markers=True)
st.plotly_chart(fig1, use_container_width=True)

st.subheader("📍 Sales Distribution by Region")
region_sales = df_filtered.groupby('Region')['Sales'].sum().reset_index()
fig2 = px.pie(region_sales, names='Region', values='Sales', title='Region-wise Sales', hole=0.3)
st.plotly_chart(fig2, use_container_width=True)

st.subheader("📦 Sales by Category")
category_sales = df_filtered.groupby('Category')['Sales'].sum().reset_index()
fig3 = px.bar(category_sales, x='Category', y='Sales', color='Category', title="Category-wise Sales")
st.plotly_chart(fig3, use_container_width=True)

st.subheader("💸 Discount vs Profit")
fig4 = px.scatter(df_filtered, x='Discount', y='Profit', color='Category', title="Discount vs Profit")
st.plotly_chart(fig4, use_container_width=True)

with st.expander("📄 View Raw Data"):
    st.dataframe(df_filtered)
