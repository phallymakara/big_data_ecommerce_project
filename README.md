# **big_data_ecomerce_project**

---

## 🎯 **Objective**

The primary objective of this project is to demonstrate practical skills in big data processing and analytics through three key phases:

1. **Data Extraction:** Utilize **PySpark** to efficiently extract and preprocess data from a semi-structured database **PostgreSQL**
2. **Data Analysis:** Apply appropriate **machine learning** techniques to analyze patterns or make predictions based on the extracted data.
3. **Data Visualization:** Present findings through meaningful and visually appealing representations using tools such as **Matplotlib**, **Seaborn**, and **Power BI**.

---

## 📊 **Dataset Overview**

This project is based on the **Brazilian E-Commerce Public Dataset by Olist**, sourced from [Kaggle](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce). The dataset offers a comprehensive view of customer behavior and logistics performance in Brazil’s online retail space.

---

### 🗂️ **Files and Structure**

The dataset includes multiple interlinked CSV files representing customers, orders, payments, reviews, products, and sellers:

| **File Name**                           | **Description**                                                        |
| --------------------------------------- | ---------------------------------------------------------------------- |
| `olist_customers_dataset.csv`           | Customer information such as location and unique customer ID           |
| `olist_orders_dataset.csv`              | Order details including status, timestamps, and relationships          |
| `olist_order_items_dataset.csv`         | Product-level data for each order                                      |
| `olist_order_payments_dataset.csv`      | Payment method and transaction values                                  |
| `olist_order_reviews_dataset.csv`       | Review scores and textual feedback from customers                      |
| `olist_products_dataset.csv`            | Product metadata such as category, name length, and description length |
| `olist_sellers_dataset.csv`             | Seller ID and their geographic location                                |
| `product_category_name_translation.csv` | English translations of product categories                             |
|  |

---

### 🔍 **Why This Dataset?**

- Simulates **real-world e-commerce operations** from an actual marketplace.
- Contains **relational data** suitable for ETL and analysis using **PySpark**.
- Enables meaningful **machine learning applications** like review prediction or sales forecasting.
- Allows for **interactive visualizations** related to geography, delivery performance, and product trends.
- Offers diverse analytical paths including customer segmentation, logistics optimization, and business intelligence.

### 📌 **Example Use Cases**

- 📦 Predict review ratings based on product and shipping data
- 🗺️ Analyze delivery performance by region or seller
- 📊 Identify sales trends by product category
- 💳 Explore customer payment preferences
- 🛍️ Cluster customers by order frequency and spending patterns
