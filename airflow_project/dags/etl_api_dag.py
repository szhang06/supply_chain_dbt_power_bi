from airflow import DAG
from airflow.decorators import task
from datetime import datetime, timedelta 
import requests
import pandas as pd
from airflow.providers.sqlite.hooks.sqlite import SqliteHook
from airflow.operators.python import get_current_context


with DAG(
    dag_id="market_etl",
    start_date=datetime(year=2025, month=5, day=15, hour=9, minute=0),
    schedule="@daily",
    catchup=False,
    max_active_runs=1,
    default_args={
        "retries": 1,
        "retry_delay": timedelta(minutes=2),  # timedelta represnts a duration
        "email_on_failure": False,
        "email_on_retry": False,
    }
) as dag:
    @task()
    def hit_polygon_api():
        # Print message, return a response
        print("Extracting data from the polygon ai")
        stock_ticker = "AMZN"
        polygon_api_key = "rOciMHVfcdealNRnGEMlQLM5MrDKN0k8"
        context = get_current_context()
        ds = context.get("ds")
        # url/ my api key does not have the authorization to access the data
        url = f"https://api.polygon.io/v2/aggs/ticker/{stock_ticker}/range/1/day/{ds}/{ds}?adjusted=true&apiKey={polygon_api_key}"
        response = requests.get(url)
        print(response.status_code)
        print(response.text)
        return response.json()
    @task()
    def flatten_market_data(polygon_response):
        # Access Airflow context
        context = get_current_context()
        # create a list of headers and a list to store the normalized data
        columns = {
            "status": None,
            "from": context.get("ds"),  # context often contains the runtime information, and "ds" stands for "data string" (the execution date of a DAG run)
            "symbol": "AMZN",
            "open": None,
            "high": None,
            "low": None,
            "close": None,
            "volume": None
        }
        # Flatten the response
        flattened_record = [] 
        for header_name, default_value in columns.items():
            flattened_record.append(polygon_response.get(header_name, default_value))
        flattened_dataframe = pd.DataFrame([flattened_record], columns=columns.keys())
        return flattened_dataframe
    @task
    def load_market_data(flattened_dataframe):
        # Pull the connection string from the Airflow connection
        market_database_hook = SqliteHook("market_database_conn")
        market_database_conn = market_database_hook.get_sqlalchemy_engine()
        # Load the table to SQLite, append if it exists
        flattened_dataframe.to_sql(
            name="market_data",
            con=market_database_conn,
            if_exists="append",
            index=False
        )
    # set dependencies using function calls
    raw_market_data = hit_polygon_api()
    transformed_market_data = flatten_market_data(raw_market_data)
    load_market_data(transformed_market_data)

    


        
        