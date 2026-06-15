import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Automated Reporting Workbook", layout="wide")

st.title("📊 Automated Reporting Dashboard")

df = pd.read_csv("data/sales_data.csv")

total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_orders = len(df)

col1, col2, col3 = st.columns(3)

col1.metric("Total Sales", f"₹{total_sales:,}")
col2.metric("Total Profit", f"₹{total_profit:,}")
col3.metric("Total Orders", total_orders)

st.subheader("Dataset Preview")
st.dataframe(df)

region_sales = df.groupby("Region")["Sales"].sum().reset_index()

fig1 = px.bar(region_sales, x="Region", y="Sales",
              title="Sales by Region")
st.plotly_chart(fig1, use_container_width=True)

category_sales = df.groupby("Category")["Sales"].sum().reset_index()

fig2 = px.pie(category_sales, names="Category",
              values="Sales",
              title="Category-wise Sales")
st.plotly_chart(fig2, use_container_width=True)

fig3 = px.line(df, x="Date", y="Sales",
               title="Sales Trend")
st.plotly_chart(fig3, use_container_width=True)