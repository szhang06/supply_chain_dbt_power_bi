# Airflow Pipeline: Kaggle to BigQuery

This project contains an Apache Airflow DAG that automates the workflow of downloading a dataset from [Kaggle](https://www.kaggle.com/datasets/ziya07/smart-logistics-supply-chain-dataset), uploading it to Google Cloud Storage (GCS), and then loading it into a BigQuery table.

---

## 📁 Project Structure

airflow_project/
├── dags/
│   └── data_download.py         # Main DAG definition
├── airflow.cfg                  # Airflow configuration
├── airflow.db                   # Airflow metadata DB (SQLite for local use)
├── logs/                        # Airflow logs
├── webserver_config.py          # Airflow webserver config
├── .gitignore                   # Excludes secrets and environment files
└── README.md                    # Project documentation

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
