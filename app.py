import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Sales Forecasting Dashboard",
    layout="wide"
)

st.title("Sales Forecasting Dashboard")

page = st.sidebar.selectbox(
    "Select Page",
    [
        "Sales Overview",
        "Forecast Explorer",
        "Anomaly Report",
        "Demand Segments"
    ]
)

train = pd.read_csv("train.csv")

train["Order Date"] = pd.to_datetime(
    train["Order Date"],
    dayfirst=True
)

##########################################################

if page=="Sales Overview":

    st.header("Sales Overview")

    yearly=train.groupby(
        train["Order Date"].dt.year
    )["Sales"].sum()

    st.subheader("Total Sales by Year")

    fig,ax=plt.subplots()

    yearly.plot(
        kind="bar",
        ax=ax
    )

    st.pyplot(fig) 

    
    monthly=train.groupby(
        train["Order Date"].dt.to_period("M")
    )["Sales"].sum()

    monthly.index=monthly.index.astype(str)

    st.subheader("Monthly Sales Trend")

    fig,ax=plt.subplots(figsize=(12,5))

    ax.plot(monthly.index,monthly.values)

    plt.xticks(rotation=90)

    st.pyplot(fig)
    plt.close(fig)

    # ==============================
    # Sales by Region and Category
    # ==============================

    st.subheader("Sales by Region and Category")

    selected_region = st.selectbox(
        "Select Region",
        sorted(train["Region"].unique())
    )

    selected_category = st.selectbox(
        "Select Category",
        sorted(train["Category"].unique())
    )

    filtered_data = train[
        (train["Region"] == selected_region) &
        (train["Category"] == selected_category)
    ]

    filtered_sales = filtered_data.groupby(
        filtered_data["Order Date"].dt.to_period("M")
    )["Sales"].sum()

    filtered_sales.index = filtered_sales.index.astype(str)

    fig, ax = plt.subplots(figsize=(12,5))

    ax.plot(
        filtered_sales.index,
        filtered_sales.values,
        marker="o"
    )

    plt.xticks(rotation=90)

    plt.title(f"{selected_region} - {selected_category}")

    plt.xlabel("Month")

    plt.ylabel("Sales")

    plt.grid(True)

    st.pyplot(fig)
    

##########################################################

elif page=="Forecast Explorer":

    st.header("Forecast Explorer")

    forecast_type = st.selectbox(
    "Forecast Type",
    ["Category", "Region"]
    )
    
    if forecast_type == "Category":
        option = st.selectbox(
        "Select Category",
        ["Furniture", "Technology", "Office Supplies"]
        )
    else:
        option = st.selectbox(
        "Select Region",
        ["West", "East"]
        )

    months=st.slider(
        "Forecast Horizon",
        1,
        3,
        3
    )

    forecast={

        "Furniture":[9916.41,5963.93,17375.02],

        "Technology":[18585.18,23754.98,23300.44],

        "Office Supplies":[26613.11,26656.37,29828.88],

        "West":[11280.68,15253.10,21521.44],

        "East":[25542.20,26061.84,28927.07]

    }

    future=forecast[option][:months]

    st.write(f"Showing {months}-month forecast for **{option}**")

    df=pd.DataFrame({

        "Month":[
            "Jan 2019",
            "Feb 2019",
            "Mar 2019"
        ][:months],

        "Forecast":future

    })

    st.dataframe(df)

    fig, ax = plt.subplots(figsize=(8,4))
    
    ax.plot(
        df["Month"],
        df["Forecast"],
        marker="o",
        linewidth=2
    )

    ax.set_title(f"{option} Sales Forecast")
    ax.set_xlabel("Month")
    ax.set_ylabel("Forecasted Sales")
    ax.grid(True)

    st.pyplot(fig)

    st.subheader("Model Performance")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric("MAE", "9485.10")
    
    with col2:
        st.metric("RMSE", "13625.26")

##########################################################

elif page=="Anomaly Report":

    st.header("Anomaly Detection")

    st.image(
        "charts/isolation_forest_anomalies.png",
        use_container_width=True
    )

    anomaly_dates=[

        "2015-01-04",
        "2015-02-08",
        "2015-02-22",
        "2015-03-22",
        "2015-07-19",
        "2015-09-13",
        "2016-01-24",
        "2017-12-17",
        "2018-11-04",
        "2018-11-18",
        "2018-12-02"

    ]

    sales=[

        304.50,
        968.53,
        224.91,
        37703.66,
        1387.69,
        29959.14,
        358.52,
        25449.80,
        29017.47,
        30572.45,
        35998.90

    ]

    table=pd.DataFrame({

        "Date":anomaly_dates,
        "Sales":sales

    })

    st.dataframe(table)

##########################################################

else:

    st.header("Demand Segmentation")

    st.image(
        "charts/kmeans_clusters.png",
        use_container_width=True
    )

    clusters=pd.DataFrame({

        "Sub Category":[

            "Accessories",
            "Appliances",
            "Art",
            "Binders",
            "Bookcases",
            "Chairs",
            "Copiers",
            "Machines",
            "Phones",
            "Storage",
            "Tables"

        ],

        "Cluster":[

            1,
            1,
            1,
            2,
            1,
            2,
            0,
            2,
            2,
            2,
            2

        ]

    })

    st.dataframe(clusters)
