# ELT Project with Snowflake, dbt, Airflow, and Power BI

## 📌 Project Overview

This project demonstrates a complete **ELT (Extract, Load, Transform)** data pipeline:

- **Extract & Load** using Python and Airflow
- **Transform** with dbt and Snowflake
- **Visualize** using Power BI

This project was implemented under the guidance of **Eng. Asnam Ali**, based on her YouTube tutorial.

---

## 🧰 Technologies Used

- **Snowflake** – Cloud Data Warehouse  
- **dbt (data build tool)** – SQL-based transformation  
- **Apache Airflow (via Docker)** – Workflow orchestration  
- **Power BI** – Dashboard & reporting  
- **Python** – Scripting for extraction and orchestration  
- **Docker** – For managing Airflow environment

---

## 🔄 Workflow

1. **Data Extraction & Loading**  
   Using Airflow DAGs to load CSV files into Snowflake (via stages & tables).

2. **Data Transformation**  
   Using dbt to create modular SQL models:
   - `staging/` models: raw cleaned data
   - `marts/` models: business-ready tables

3. **Data Visualization**  
   Connecting Power BI to Snowflake using Direct Query and building dynamic dashboards.

---

## 📊 Power BI Dashboard

The dashboard includes:
- KPIs: Total Sales, Customer Count, etc.
- Time Series Analysis
- Top Products / Customers / Countries
- Status Distribution

---



