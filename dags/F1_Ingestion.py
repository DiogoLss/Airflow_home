import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

def get_from_api_func():
    print('test')

dag = DAG(
     dag_id="F1_Ingestion",
     start_date=datetime.datetime(2021, 1, 1),
     schedule="@daily",
     catchup=False
)

get_from_api = PythonOperator(
    task_id='get_from_api',
    python_callable=get_from_api_func
)

