from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.google.cloud.transfers.gcs_to_bigquery import GCSToBigQueryOperator
from airflow.providers.google.cloud.operators.gcs import GCSCreateBucketOperator
from airflow.providers.google.cloud.transfers.local_to_gcs import LocalFilesystemToGCSOperator
from airflow.utils.dates import days_ago
from airflow.utils.email import send_email

import os
import kagglehub
from datetime import timedelta

# Constants
GCS_BUCKET = 'schain_bucket_airflow'
GCS_OBJECT = 'schain_dataset/schain_data.csv'
LOCAL_FILE = '/tmp/schain.csv'
BQ_DATASET = 'schain_dataset_airflow'
BQ_TABLE = 'schain_data_table'

def download_dataset():
    path = kagglehub.dataset_download("ziya07/smart-logistics-supply-chain-dataset")
    csv_path = os.path.join(path, "smart_logistics_dataset.csv")
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"Expected CSV not found at {csv_path}")
    os.rename(csv_path, LOCAL_FILE)

default_args = {
    'owner': 'airflow',
    'retries': 2,
    'retry_delay': timedelta(minutes=5),
    'email_on_failure': False,  
    'email': ['myemail@gmail.com'],  # Optional: for alerts
}

with DAG(
    dag_id='download_and_upload_to_bigquery',
    default_args=default_args,
    start_date=days_ago(1),
    schedule_interval='@daily',  
    catchup=False,
    description='Download Kaggle dataset, upload to GCS and load into BigQuery',
    tags=['kaggle', 'gcs', 'bigquery'],
) as dag:

    download = PythonOperator(
        task_id='download_dataset',
        python_callable=download_dataset,
    )

    create_bucket = GCSCreateBucketOperator(
        task_id='create_gcs_bucket',
        bucket_name=GCS_BUCKET,
        storage_class='STANDARD',
        location='EU',
    )

    upload_to_gcs = LocalFilesystemToGCSOperator(
        task_id='upload_to_gcs',
        src=LOCAL_FILE,
        dst=GCS_OBJECT,
        bucket=GCS_BUCKET,
    )

    load_to_bq = GCSToBigQueryOperator(
        task_id='load_to_bigquery',
        bucket=GCS_BUCKET,
        source_objects=[GCS_OBJECT],
        destination_project_dataset_table=f'{BQ_DATASET}.{BQ_TABLE}',
        source_format='CSV',
        skip_leading_rows=1,
        write_disposition='WRITE_TRUNCATE',
        autodetect=True,
        max_bad_records=10,  
    )

    download >> create_bucket >> upload_to_gcs >> load_to_bq
