import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.amazon.aws.operators.s3 import S3CreateObjectOperator

bucket_name = 'data'

dag = DAG(
     dag_id="F1_Ingestion",
     start_date=datetime.datetime(2021, 1, 1),
     schedule=None,
     catchup=False
)

create_object = S3CreateObjectOperator(
    task_id="create_object",
    s3_bucket=bucket_name,
    s3_key='test',
    data='opt/airflow/dags/include/data/f1_project/drivers/24-08-03-19-17-49.json',
    replace=True,
    aws_conn_id='minio',
    dag=dag
)

create_object