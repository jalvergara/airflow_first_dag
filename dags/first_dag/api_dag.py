from datetime import timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import requests
import pandas as pd

def extract():
    url = 'https://api-colombia.com/api/v1/Region'
    params = {
    }
    try:
        response = requests.get(url)
        data = response.json()
        regions = [region["name"] for region in data ]
        print(data[1]['name'])
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"
    data = {
            'region': regions,
    }

    df = pd.DataFrame(data)
    print("df is", df)
    df.to_csv('./data.csv')

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 4, 3),  # Update the start date to today or an appropriate date
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

with DAG(
    'api_dag',
    default_args=default_args,
    description='Our first DAG with ETL process!',
    schedule_interval='@daily',  # Set the schedule interval as per your requirements
) as dag:

    run_etl = PythonOperator(
        task_id='complete_api_etl',
        python_callable=extract,
        dag=dag,
    )

    run_etl