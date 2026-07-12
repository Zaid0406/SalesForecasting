# Sales Forecasting and Demand Analysis using Machine Learning

## Overview

This project analyzes historical retail sales data to identify sales trends, forecast future demand, detect anomalies, segment products based on demand patterns, and provide interactive business insights through a Streamlit dashboard.

The project was developed as part of a Sales Forecasting and Demand Analysis assignment and demonstrates the application of machine learning, time series forecasting, clustering, and data visualization techniques for business decision-making.

---

## Features

- Exploratory Data Analysis (EDA)
- Time Series Analysis
- Sales Forecasting using:
  - SARIMA
  - Facebook Prophet
  - XGBoost
- Model Performance Comparison
- Product Category & Region-wise Forecasting
- Anomaly Detection using:
  - Isolation Forest
  - Z-Score Method
- Product Demand Segmentation using K-Means Clustering
- Interactive Streamlit Dashboard

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Statsmodels
- Prophet
- XGBoost
- Streamlit

---

## Project Structure

```
SalesForecasting_ZaidAhmedShaikh/
│
├── analysis.ipynb
├── app.py
├── train.csv
├── requirements.txt
├── summary.pdf
├── charts/
└── README.md
```

---

## Running the Streamlit App

1. Install the required libraries:

```bash
pip install -r requirements.txt
```

2. Run the application:

```bash
streamlit run app.py
```

---

## Dashboard Pages

- Sales Overview
- Forecast Explorer
- Anomaly Report
- Product Demand Segments

---

## Author

**Zaid Ahmed Shaikh**

B.Tech Information Technology
