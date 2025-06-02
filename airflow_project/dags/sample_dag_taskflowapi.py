from airflow.decorators import dag, task
from datetime import datetime
import pandas as pd


@dag(
    start_date=datetime(year=2024, month=5, day=18, hour=9, minute=0),
    schedule="@daily",
    catchup=True,
    max_active_runs=1
)
def weather_etl_taskflowapi():
    @task()
    def extract_data():
        # Print message, return a response
        print("Extracting data from an weather API")
        return {
            "date": "2023-01-01",
            "location": "NYC",
            "weather": {
                "temp": 33,
                "conditions": "Light snow and wind"
            }
        }

    @task()
    def transform_data(raw_data):
        # Transform response to a list
        transformed_data = [
            [
                raw_data.get("date"),
                raw_data.get("location"),
                raw_data.get("weather").get("temp"),
                raw_data.get("weather").get("conditions")
            ]
        ]
        return transformed_data

    @task()
    def load_data(transformed_data):
        # Load the data to a DataFrame, set the columns
        loaded_data = pd.DataFrame(transformed_data)
        loaded_data.columns = [
            "date",
            "location",
            "weather_temp",
            "weather_conditions"
        ]
        print(loaded_data)

    # Set dependencies using function calls
    raw_dataset = extract_data()
    transformed_dataset = transform_data(raw_dataset)
    load_data(transformed_dataset)


# Allow the DAG to be run
weather_etl_taskflowapi()
