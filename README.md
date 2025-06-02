# 🏭 Supply Chain Optimization using Airflow, DBT & Power BI

## 🚀 Purpose of the Project

This project addresses a real-world business problem: **inefficient supply chain operations** in a manufacturing company. By combining modern data engineering (with DBT) and dynamic business intelligence (via Power BI), the goal is to:

- Identify inefficiencies in inventory and logistics as well as customer behaviors.
- Deliver actionable insights for cost reduction and improved operations.
- Showcase how data transformation and visualization can drive smarter decisions.

---

## 🔧 Tech Stack

- **Airflow**: - Data pipeline ochestration.
- **BigQuery**: – Cloud-based data warehouse.     
- **DBT (Data Build Tool)** – Data transformation, testing, and documentation.
- **Power BI** – Interactive dashboards for business insights.
- **SQL** – Core logic for data modeling.
- **Git & GitHub** – Version control and collaboration.
- **GitHub Actions** – CI/CD pipelines for DBT models.

---

## 🧠 Business Problem: Supply Chain Inefficiency

A global manufacturer faced rising costs and inconsistent supply chain performance. Key challenges included:

- **Supplier delays and variability** disrupting production
- **High logistics costs** without clear visibility into causes

---

## 🧩 The Solution

### Airflow Pipeline: Kaggle to BigQuery

This project contains an Apache Airflow DAG that automates the workflow of downloading a dataset from [Kaggle](https://www.kaggle.com/datasets/ziya07/smart-logistics-supply-chain-dataset), uploading it to Google Cloud Storage (GCS), and then loading it into a BigQuery table.

---

## ⚙️ Prerequisites

1. **Python 3.8+**
2. **Apache Airflow**
   - Install with GCP extras:
     ```bash
     pip install apache-airflow[gcp]
     ```
3. **Kaggle API**
   - Install:
     ```bash
     pip install kaggle kagglehub
     ```
   - Place your `kaggle.json` file in `~/.kaggle/`:
     ```bash
     mkdir -p ~/.kaggle
     cp /path/to/kaggle.json ~/.kaggle/
     chmod 600 ~/.kaggle/kaggle.json
     ```

4. **Google Cloud Credentials**
   - Place your GCP service account JSON (with BigQuery & GCS permissions) in a safe location.
   - Set the environment variable:
     ```bash
     export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your-service-account.json"
     ```

---

## 🚀 DAG Overview

| Task Name          | Description |
|--------------------|-------------|
| `download_dataset` | Uses `kagglehub` to download dataset locally |
| `create_gcs_bucket`| Creates a GCS bucket if it doesn't exist |
| `upload_to_gcs`    | Uploads the CSV file to GCS |
| `load_to_bigquery` | Loads the file from GCS into a BigQuery table |

---

## 🧠 How It Works

1. The DAG is triggered manually or scheduled.
2. Downloads `smart_logistics_dataset.csv` from Kaggle.
3. Saves it as `/tmp/schain.csv`.
4. Creates a GCS bucket (`schain_bucket_airflow`) if it doesn't exist.
5. Uploads the CSV to `gs://schain_bucket_airflow/schain_dataset/schain_data.csv`.
6. Loads the data into a BigQuery table (`schain_dataset_airflow.schain_data_table`).

---

## 📅 Running the DAG

1. Start Airflow:
   ```bash
   airflow standalone

### DBT Pipeline

Using DBT, raw supply chain data was transformed into clean, analytics-ready datasets:

- **Staging Models** – Standardized raw data into consistent formats
- **Intermediate Models** – Normalized data into dimensional and facual tables.
- **Mart Models** – Provided high-level summaries for Power BI consumption

#### ✅ DBT Highlights

| Skill | Description |
|-------|-------------|
| **Data Modeling** | Built layered architecture (staging → intermediate → marts) |
| **Data Testing** | Implemented freshness, uniqueness, and null checks |
| **CI/CD** | Configured **GitHub Actions** to run `dbt run` and `dbt test` on every pull request |
| **Documentation** | Auto-generated model documentation and lineage graphs |
| **Jinja & Macros** | Wrote reusable logic for dynamic modeling and filters |

---

### Power BI Dashboard 

The Power BI report visualizes key supply chain metrics, enabling decision-makers to quickly identify bottlenecks and improvement areas.

---

## 📈 Key Business Insights

- **Logistics**: 65.60% shipments delayed; top causes in order: weather (39.53%), mechanical (34.88%), and traffic (25.58%). The waiting times for different delay reasons are quite similar, with traffic causing the longest delay of ~35 min.
- **Customers**: Peak spending on days 6/24/31; the median of purchase frequency is 6.
- **Inventory**: Current stock aligns with demand, but the demand is higher than the stock in January and is very little in May.
---

## 💡 Recommendations

1. Better demand forecasting and inventory syncing to prevent urgent or partial shipments.
2. Diversify supplier base to reduce dependency and improve lead time.
3. Optimize routing plans to balance cost and delivery speed across regions

---


